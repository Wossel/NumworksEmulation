from settings import *

from kandinsky import *
from time import *


class GameEngine():
    def __init__(self):
        #Variables for stabilizing fps
        self.targetFps = fps
        self.currentFps = fps
        self.breakDuration = 1/(fps*2)
        self.startTime = monotonic()
        #Starts the gameloop
        self.running = True
        self.run()

    def optimizeFps(self):
        sleep(self.breakTime)
        self.currentFps = 1/(monotonic()-self.startTime)
        if self.currentFps > self.targetFps:
            self.breakDuration += self.breakDuration/10
        elif self.currentFps < self.targetFps:
            self.breakDuration -= self.breakDuration/10
        else:
            pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def run(self):
        while True:
            while running:
                self.startTime = monotonic()
                self.update()
                self.draw()
                self.optimizeFps()


game = GameEngine()






