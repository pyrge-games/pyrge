from client.utils import singleton
from client.subsystems import subsystem
import pygame

@singleton.Singleton
class State(subsystem.Subsystem):

    def __init__(self):
        super().__init__()
        self.clock = None
        # todo Need to abstract out different ticks, so we can schedule different things at different times.

    def on_active(self):
        #self.clock = pygame.Clock
        self.active = True

    def do_work(self):
        pass

    def shutdown(self):
        pass