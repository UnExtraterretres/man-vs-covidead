import pygame
from random import randint


class Vaccine(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()

        # init the player
        self.player = player

        # init the image, rect
        self.image = pygame.image.load("assets/entities/vaccine.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 10
        self.rect.y = self.player.rect.y + 10 + randint(-2, 2)

        # velocity
        self.velocity = 5
        # damage
        self.damage = 3

    def move(self):
        # move
        self.rect.x += self.velocity

        # check collision with mobs
        for mob in pygame.sprite.spritecollide(self, self.player.game.current_scene.mobs, False):
            # remove the vaccine
            self.player.vaccines.remove(self)
            # do damage
            mob.damage(self.damage)

        # remove the vaccine
        if self.rect.x > self.player.game.screen.get_size()[0]:
            self.player.vaccines.remove(self)
