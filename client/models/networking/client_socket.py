import json
from socket import *
from threading import Thread
from common.enums.client_message import ClientMessage
from common.enums.info_scenes import InfoScenes


class ClientSocket:
    def __init__(self, parent, ip_address, port):
        self.__parent__ = parent
        self.socket = None
        self.ip_address = ip_address
        self.port = port
        self.kill_thread = False
        self.thread = Thread(target=self.__do_work)
        self.establish_connection()
        self.thread.start()

    """ Connects to the server """
    def establish_connection(self):
        self.socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        self.socket.connect((self.ip_address, self.port))
        self.socket.settimeout(2)
        message = json.dumps({ "command": ClientMessage.CONNECTION_ESTABLISHED.value })
        self.send_to_server(message)

    """ Sends a message to the server """
    def send_to_server(self, msg):
        try:
            self.socket.send(bytes(msg, 'utf-8'))
        except ConnectionResetError:
            print("lost connection to server")
            self.__parent__.load_info_scene_signal.emit(InfoScenes.MAIN_MENU.value)
            self.__parent__.socket = None

    """ Closes the connection """
    def close(self):
        self.socket.close()
        self.kill_thread = True

    """ Receives server messages """
    def __do_work(self):
        while True:
            try:
                if self.kill_thread:
                    break
                msg = self.socket.recv(1024)
            except error as e:
                if e.args[0] != "timed out":
                    break
            else:
                if len(msg) > 0:
                    self.__parent__.process_socket_message(msg.decode('utf-8'))
