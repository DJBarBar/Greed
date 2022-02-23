from game.casting.actor import Actor

# This class needs to be able to handle the points.
class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        
    def get_points(self, gems):
        """Gets the artifact's point value. Gems add points, while everything else subtracts them.
        
        Returns:
            Int: The points.
        """ 
            #  Setting up the score, if robot touch a gem pass true for gems amd false for rock  
        self._points = 0  
        if gems == "*":
            self._points += 10
        else:
            self._points -= 50
           
        return int(self._points)
