import sys

from client.subsystems import subsystem, configuration, resource, state
from client.objects import layer
from client.utils import singleton
import pygame

@singleton.Singleton
class Renderer(subsystem.Subsystem):
    def __init__(self):
        super().__init__()

    def on_active(self):
        pygame.init()
        pygame.font.init()
        self.display = pygame.display
        self.screen = None
        self.layers = {}
        self.active = True
        self.worker.start()

    def create_screen(self):
        resolution = configuration.Configuration.instance().resolution
        screen_type = configuration.Configuration.instance().screen_type
        caption = configuration.Configuration.instance().caption
        icon = resource.Resource.instance().icon
        self.tick_rate = configuration.Configuration.instance.max_fps
        self.clock = pygame.Clock
        self.display.set_caption(caption)
        self.display.set_icon(icon)
        self.screen = self.display.set_mode(size=resolution, flags= screen_type | pygame.HWSURFACE | pygame.GL_DOUBLEBUFFER | pygame.HWACCEL )

    def create_layers(self) -> dict:
        lyrs = configuration.Configuration.instance().layers
        for lyr in lyrs:
            self.layers[lyr] = layer.Layer(name=lyr)

    def do_work(self):
        while self.active:
            self.screen.fill((0,0,0))

            events = []
            update = {}
            delta = self.clock.tick(self.tick_rate)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.shutdown()
                elif event.type == pygame.VIDEORESIZE:
                    resolution = scrW, scrH =  event.dict['size']
                    screen_type = configuration.Configuration.instance.screen_type
                    configuration.Configuration.instance().set_var({'resolution': resolution,
                                                                    'scrW': scrW,
                                                                    'scrH': scrH})
                    self.display.set_mode(size=resolution, flags= screen_type | pygame.HWSURFACE | pygame.GL_DOUBLEBUFFER | pygame.HWACCEL )
                events.append(event)

            # potentially we should be getting these values every N frame, instead of loading the render loop with shit.
            update['fps'] = self.clock.get_fps()
            update['delta'] = delta
            update['mouse_pos'] = pygame.mouse.get_pos()
            update['mouse_press'] = pygame.mouse.get_pressed()
            update['keys'] = keys
            update['events'] = events
            state.State.instance().put({'render_target': update})

            for name, lyr in self.layers.items():
                while lyr.queue.qsize() != 0:
                    ent = lyr.queue.get()
                    lyr.entities.append(ent)

                for ent in lyr.entities:
                    if ent.should_be_drawn:
                        self.screen.blit(ent.image, ent.rect)

            self.display.update()

    def shutdown(self):
        self.active = False
        pygame.quit()
        sys.exit()
