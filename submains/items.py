import pygame
from random import randint


class Item(pygame.sprite.Sprite):

    def __init__(self, game, name: str, size=(25, 25)):
        super().__init__()

        # args
        self.game = game
        self.name = name
        self.size = size

        # init the image, rect
        self.image = pygame.image.load(f"assets/entities/items/{self.name}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        # rect x y
        self.rect.x = randint(10, 300)
        self.rect.y = 0

        # is used
        self.is_used = False

    def update(self):
        # the item fall from the sky
        if self.rect.y < 320:
            self.rect.y += 2

        # check a collision with the player
        if self.rect.colliderect(self.game.current_scene.player.rect):
            self.game.current_scene.items.remove(self)
            self.is_used = True


class SurgicalMask(Item):

    def __init__(self, game):
        super().__init__(game, "surgical mask")

    def update(self):
        super().update()

        if self.is_used:
            self.game.current_scene.player.max_health += 2


class HydroAlcoholicGel(Item):

    def __init__(self, game):
        super().__init__(game, "hydro alcoholic gel")

    def update(self):
        super().update()

        if self.is_used:
            self.game.current_scene.player.health = self.game.current_scene.player.max_health
