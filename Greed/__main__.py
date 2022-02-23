import os
import random
import time

from game.casting.actor import Actor
from game.casting.gems import Gem
from game.casting.stones import Stone
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 20
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
GREEN = Color(0,255,0)
RED = Color(255,0,0)
GEM_COUNT = 25
STONE_COUNT = 20


def main():
    
    # create the cast
    cast = Cast()
    
    # create the points
    points = Actor()
    points.set_text("")
    points.set_font_size(FONT_SIZE)
    points.set_color(WHITE)
    points.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("points", points)
    
    # create the robot
    x = int(MAX_X / 2)
<<<<<<< HEAD
    y = 570
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)


    for n in range(GEM_COUNT):
=======
    y = int(MAX_Y - 30)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    for n in range(DEFAULT_ARTIFACTS):
        text = (random.randint(1, 100))
        if text > 40:
            text = "*"
        else:
            text = chr(random.randint(33, 126))
>>>>>>> 7cd9b2465c232089094eca25dcb7ef0a0e293592

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

<<<<<<< HEAD
        gems = Gem()
        gems.set_text('*')
        gems.set_font_size(FONT_SIZE)
        gems.set_color(GREEN)
        gems.set_position(position)
        cast.add_actor("gems", gems)
    
    for n in range(STONE_COUNT):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        stones = Stone()
        stones.set_text('D')
        stones.set_font_size(FONT_SIZE)
        stones.set_color(RED)
        stones.set_position(position)
        cast.add_actor("stones", stones)
=======
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)
>>>>>>> 7cd9b2465c232089094eca25dcb7ef0a0e293592
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()