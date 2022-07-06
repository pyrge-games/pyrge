import os

import pygame.surface, pygame.image
import pygame.mixer # todo just import sound object
from client.utils import singleton
from client.subsystems import subsystem, configuration


@singleton.Singleton
class Resource(subsystem.Subsystem):

    def __init__(self):
        super().__init__()
        self.datastore = None
        self.icon = None
        self.resource_store = None

    def on_active(self):
        self.datastore = os.path.join(configuration.Configuration.instance().install_path, 'resources')
        self.icon = pygame.image.load(os.path.join(self.datastore, 'image', 'pyrge_logo.png'))
        self.active = True
        self.worker.start()

    def load_local_resource(self):
        pass

    def load_remote_resource(self):
        pass

    def do_work(self):
        pass

    def shutdown(self):
        pass