import os.path
import threading
import pygame.constants
from typing import Union
from client.subsystems import subsystem
from client.utils import singleton


@singleton.Singleton
class Configuration(subsystem.Subsystem):

    def __init__(self):
        super().__init__()
        self.lock = threading.Lock

        self.resolution = self.scrW, self.scrH = 2560, 1440
        self.screen_type = pygame.constants.FULLSCREEN
        self.caption = self.game_title = 'NewGame'
        self.install_path = "C:/Users/rich/pyrge/client"
        self.tick_rate = 10
        self.max_fps = 144
        self.layers = ['far_background',
                       'background',
                       'foreground',
                       'close_foreground',
                       'ui']

    def set_var(self, new_value: Union[tuple, dict] ):
        """ Acquire the lock and set new parameters."""
        with self.lock:
            if isinstance(new_value, tuple):
                self.__dict__[new_value[0]] = new_value[1]
            else:
                for k,v in new_value.items():
                    self.__dict__[k] = v