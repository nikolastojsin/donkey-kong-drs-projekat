from PyQt5.QtGui import QPixmap
from client.constants import IMAGES_DIR
from client.models.abstract.playable_character import PlayableCharacter


class FirstPlayer(PlayableCharacter):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_frame_index = 0
        self.movement_frames_left = [
            QPixmap(IMAGES_DIR + "first_player/move/move_left_1.png"),
            QPixmap(IMAGES_DIR + "first_player/move/move_left_2.png")
        ]
        self.movement_frames_right = [
            QPixmap(IMAGES_DIR + "first_player/move/move_right_1.png"),
            QPixmap(IMAGES_DIR + "first_player/move/move_right_2.png")
        ]
        self.climb_frames = [
            QPixmap(IMAGES_DIR + "first_player/climb/climb_1.png"),
            QPixmap(IMAGES_DIR + "first_player/climb/climb_2.png")
        ]
        self.climb_finish_frames = [
            QPixmap(IMAGES_DIR + "first_player/climb/climb_finish_1.png"),
            QPixmap(IMAGES_DIR + "first_player/climb/climb_finish_2.png")
        ]
        self.default_frame_left = QPixmap(IMAGES_DIR + "first_player/idle/idle_left.png")
        self.default_frame_right = QPixmap(IMAGES_DIR + "first_player/idle/idle_right.png")
        self.default_frame_up = QPixmap(IMAGES_DIR + "first_player/climb/climb_finish_3.png")
        self.item.setPixmap(self.default_frame_right)
        self.item.setZValue(3)
        self.lives.setPos(0, 0)
        self.__parent__.addItem(self.lives)
