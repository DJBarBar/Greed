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
        self._message = ""
        
    def get_points(self, gems):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """ 
            #  Setting up the score, if robot touch a gem pass true for gems amd false for rock    
        if gems == True:
            self._points += 1
        else:
            self._points -= 1
           
        return self._points
    
    # def set_message(self, message):
    #     """Updates the message to the given one.
        
    #     Args:
    #         message (string): The given message.
    #     """
    #     self._message = message