import pygame.sprite

from .player import *
from .mob import *
from .items import *


class Menu:

    def __init__(self, game):
        # loading of Game
        self.game = game

        # background
        self.background = pygame.image.load("assets/backgrounds/main menu.png")

    def update(self):
        self.game.sounds.play("theme")
        if self.game.pressed.get(pygame.K_RETURN):
            self.game.sounds.stop("theme")
            self.game.sounds.play("click")

            self.game.current_scene = self.game.scenes["level 1"]

    def display(self):
        # display the background
        self.game.screen.blit(self.background, (0, -100))

        # display texts
        self.game.pin_up(text="press <return> to start a party", coordinate=(200, 80))

        # flip pygame
        pygame.display.flip()


class Level:

    def __init__(self, game):
        # loading of Game
        self.game = game

        # background
        self.background = pygame.image.load("assets/backgrounds/main menu.png")

        # percent
        self.percent = 0
        self.percent_speed = 33

        # the current day
        self.current_day = 0

        # the player
        self.player = Player(game=self.game)

        # the  items
        self.items = pygame.sprite.Group()

        # the mobs
        self.mobs = pygame.sprite.Group()

    def update(self):
        # Day Event
        if self.percent >= 100 and len(self.mobs) == 0:
            # reset percent
            self.percent = 0
            # there is a new day
            self.current_day += 1

            # create some mobs
            for i in range(randint(1, self.current_day)):
                self.mobs.add(Covidead.__call__(self.game))

            if self.current_day % 5 == 0:
                for i in range(randint(1, self.current_day // 5)):
                    self.mobs.add(CommunistCovidead.__call__(self.game))

            if self.current_day % 7 == 0:
                for i in range(randint(1, self.current_day // 7)):
                    self.mobs.add(Kamikaze.__call__(self.game))

            # create some items
            if randint(1, 10) == 1:
                # 10% for Surgical Mask
                self.items.add(SurgicalMask.__call__(self.game))

            if randint(1, 100) == 1:
                # 1% for HydroAlcoholicGel
                self.items.add(HydroAlcoholicGel.__call__(self.game))

        # Update Items
        for item in self.items:
            item.update()

        # Update Vaccines
        for vac in self.player.vaccines:
            vac.move()

        # Update Mobs
        for mob in self.mobs:
            mob.forward()
            mob.animation()

        # Keys Event
        if self.game.pressed.get(pygame.K_d) and \
                self.player.rect.x + self.player.rect.width < self.game.screen.get_width():
            # anime the player
            self.player.is_animated = True
            self.player.animation()

            # the player goes right
            self.player.move_right()
        elif self.game.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            # anime the player
            self.player.is_animated = True
            self.player.animation()

            # the player goes left
            self.player.move_left()
        elif not (self.game.pressed.get(pygame.K_d) and self.game.pressed.get(pygame.K_q)):
            # the player isn't moving
            self.player.is_animated = False
            self.player.animation()

    def display(self):
        # display the background
        self.game.screen.blit(self.background, (0, -100))

        # pin up the current day
        self.game.pin_up(text=f"Day: {self.current_day}", coordinate=(0, 0))

        # update the loading bar
        self.update_bar()

        # draw the player
        self.game.screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar()

        # draw the items
        for item in self.items:
            self.game.screen.blit(item.image, item.rect)

        # draw the vaccines
        for vac in self.player.vaccines:
            self.game.screen.blit(vac.image, vac.rect)

        # draw the mobs
        for mob in self.mobs:
            self.game.screen.blit(mob.image, mob.rect)

        # flip pygame
        pygame.display.flip()

    def update_bar(self):
        # add percent
        self.percent += self.percent_speed/100

        # bg bar (dark)
        pygame.draw.rect(self.game.screen, (0, 0, 0),
                         [0, self.game.screen.get_height() - 10, self.game.screen.get_width(), 10])
        # fg bar
        pygame.draw.rect(self.game.screen, (187, 11, 11),
                         [0, self.game.screen.get_height() - 10,
                          (self.game.screen.get_width() / 100) * self.percent, 10])


class GameOver:

    def __init__(self, game):
        # loading the game
        self.game = game

        # background
        self.background = pygame.image.load("assets/backgrounds/main menu.png")

    def update(self):
        self.game.sounds.play("hearth")

    def display(self):
        # display the background
        self.game.screen.blit(self.background, (0, -100))

        # display texts
        self.game.pin_up(text="Game Over...", coordinate=(500, 80))

        # flip pygame
        pygame.display.flip()
