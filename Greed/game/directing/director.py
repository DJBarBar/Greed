<<<<<<< HEAD:Greed/game/directing/director.py
=======
from game.services.video_service import VideoService
from game.casting.artifact import Artifact
from game.casting.actor import Actor


>>>>>>> 7cd9b2465c232089094eca25dcb7ef0a0e293592:Greed/game/directory/director.py
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
<<<<<<< HEAD:Greed/game/directing/director.py
        self._points = 500
=======
        self._game_score = 500
>>>>>>> 7cd9b2465c232089094eca25dcb7ef0a0e293592:Greed/game/directory/director.py
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
<<<<<<< HEAD:Greed/game/directing/director.py
        player.set_velocity(velocity)        
=======
        robot.set_velocity(velocity)   
>>>>>>> 7cd9b2465c232089094eca25dcb7ef0a0e293592:Greed/game/directory/director.py

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("points")
        player = cast.get_first_actor("player")
        gems = cast.get_actors("gems")
<<<<<<< HEAD:Greed/game/directing/director.py
        stones = cast.get_actors("stones")
        points = self._points

        banner.set_text("Points %s" % (points))
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        if points == 0:
            self._video_service.game_over()
            self._points = 500
=======
        score = self._game_score
        banner.set_text(f"Score: {score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for artifact in gems:
            artifact.move_next(max_x, max_y)
            if robot.get_position().equals(artifact.get_position()):
                if artifact == "*":
                    self._game_score += 10 
                    banner.set_text(f"Score:{self._game_score}")
                    artifact.remove_actor()
                else:
                    self._game_score -= 50
                    banner.set_text(f"Score:{self._game_score}")
                    artifact.remove_actor()
            if gems.get_position().equals(max_y):
                artifact.remove_actor
>>>>>>> 7cd9b2465c232089094eca25dcb7ef0a0e293592:Greed/game/directory/director.py

        for gem in gems:
            gem.fall(max_y)
            if player.get_position().equals(gem.get_position()):
                self._points += 10

        for stone in stones:
            stone.fall(max_y)
            if player.get_position().equals(stone.get_position()):
                self._points -= 50

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
<<<<<<< HEAD:Greed/game/directing/director.py
        self._video_service.flush_buffer()
=======
        self._video_service.flush_buffer()
        if self._game_score <= 0:
            VideoService.close_window()
            VideoService._game_over()
            self.start_game()
>>>>>>> 7cd9b2465c232089094eca25dcb7ef0a0e293592:Greed/game/directory/director.py
