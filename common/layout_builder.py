import numpy as np
from common.constants import SCENE_HEIGHT, SCENE_GRID_BLOCK_HEIGHT, SCENE_WIDTH, SCENE_GRID_BLOCK_WIDTH
from common.enums.layout_block import LayoutBlock


def get_level_layout(level: str):
    layout = np.full(300, None).reshape(int(SCENE_HEIGHT / SCENE_GRID_BLOCK_HEIGHT),
                                        int(SCENE_WIDTH / SCENE_GRID_BLOCK_WIDTH))

    with open(level) as file:
        line = file.readline()
        row = 0
        while line:
            for column in range(int(SCENE_WIDTH / SCENE_GRID_BLOCK_WIDTH)):
                if line[column] == "P":
                    layout[row][column] = LayoutBlock.Platform
                elif line[column] == "L":
                    layout[row][column] = LayoutBlock.Ladder
                elif line[column] == "1":
                    layout[row][column] = LayoutBlock.Player_1
                elif line[column] == "2":
                    layout[row][column] = LayoutBlock.Player_2
                elif line[column] == "p":
                    layout[row][column] = LayoutBlock.Princess
                elif line[column] == "G":
                    layout[row][column] = LayoutBlock.Gorilla
            row += 1
            line = file.readline()

    return layout
