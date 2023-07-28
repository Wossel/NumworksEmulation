from kandinsky import *
from time import *

class Game():
    def __init__(self):
        #Variables for stabilizing fps
        self.targetFps = fps
        self.currentFps = fps
        self.breakDuration = 1/(fps*2)
        self.startTime = monotonic()
        #Starts the gameloop
        self.run()

    def update(self):
        pass
    
    def draw(self):
        pass