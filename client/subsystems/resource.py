import os

import pygame.surface, pygame.image
import pygame.mixer # todo just import sound object
from client.utils import singleton
from client.subsystems import subsystem, configuration


@singleton.Singleton
class Resource(subsystem.Subsystem):
    """ Resource Subsystem stores resources for use by the entire system.

     images, the frame offsets for that image
     sounds, music

     objects, entities are able to reference the name of the sound or image for use in processing, and the object
     stores how to use the resource (sound level, frame of the animation to render at the time.)

     """
    def __init__(self):
        super().__init__()
        self.datastore = None
        self.icon = None
        self.resource_store = None

        self.image = {
            "image_name": {"image": "Surface",
                           "frames": {0: "Frame"}}
        }

        self.sound = {
            "sound_name": "Sound"
        }

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