import uuid

import pygame


class Entity:
    def __init__(self):
        self.uid = uuid.uuid4()
        self.name = 'NewEntity'

        self.should_be_drawn = True # will the renderer blit the image to the screen
        self.active = True # should it consume during an update tick

        self.image = pygame.Surface(0,0) # todo get this from the resource manager
        self.rect = self.image.get_rect() # todo get this from the resource manager

        self.location = self.locX, self.locY = 0, 0 # world position

        self.collider_type = 'standard'

        self.health = 100
        self.can_be_killed = False

        self.can_be_used = False

        self.speed = 0
        self.acceleration = 0
        self.friction = 0
        self.gravity = 0

        # todo continue defining Entity
