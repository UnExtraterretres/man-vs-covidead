import pygame
from .vaccine import Vaccine
from .tools.animation import AnimateSprite


class Player(AnimateSprite):

    def __init__(self, game, name="player", size=(50, 50)):
        super().__init__(name=name, size=size)

        # init the game
        self.game = game
        # init size
        self.size = size

        # init the rect
        self.rect = self.image.get_rect()
        # rect x y
        self.rect.x = 85
        self.rect.y = 296

        # health
        self.max_health = 50
        self.health = self.max_health

        # velocity
        self.velocity = 5

        # vaccines
        self.vaccines = pygame.sprite.Group()

    def damage(self, amount: int):
        # the player is alive ?
        if self.health - amount > 0:
            self.health -= amount
        else:
            # remove/reset entities
            self.game.current_scene.mobs = pygame.sprite.Group()
            self.game.current_scene.player = Player(self.game)

            # game over
            self.game.sounds.play("covidead")
            self.game.current_scene = self.game.scenes["game over"]
            self.game.run()

    def launch_vaccines(self):
        # add a new vaccine
        self.vaccines.add(Vaccine(player=self))
        # play the sound
        self.game.sounds.play("vaccine")

    def move_right(self):
        # check the: no collision with mobs
        if not pygame.sprite.spritecollide(self, self.game.current_scene.mobs, False):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self):
        # draw health bar
        pygame.draw.rect(self.game.screen, (60, 63, 60),
                         [self.rect.x-(self.max_health-self.size[0])/2, self.rect.y, self.max_health, 5])
        pygame.draw.rect(self.game.screen, (65, 243, 20),
                         [self.rect.x-(self.max_health-self.size[0])/2, self.rect.y, self.health, 5])
