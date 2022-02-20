from random import randint
from .tools.animation import AnimateSprite


class Mob(AnimateSprite):

    def __init__(self, game, name: str, spawn_point: int, max_health: int, velocity: int, attack: float, size=(60, 60)):
        super().__init__(name=name, size=size)

        # init of Game
        self.game = game
        # name
        self.name = name
        # spawn point
        self.spawn_point = spawn_point
        # size
        self.size = size

        # init the rect
        self.rect = self.image.get_rect()
        # rect x y
        self.rect.x = 900 + randint(0, spawn_point)
        self.rect.y = 290

        # health
        self.max_health = max_health
        self.health = self.max_health

        # velocity
        self.velocity = velocity

        # attack
        self.attack = attack

    def damage(self, amount: int):
        # do damage
        self.health -= amount

        # the mob is alive ?
        if self.health <= 0:
            self.game.current_scene.mobs.remove(self)

    def forward(self):
        # cough randomly
        if randint(0, 1000) == 0:
            self.game.sounds.play("cough")

        # check collision to forward/attack
        if self.rect.colliderect(self.game.current_scene.player.rect):
            self.is_animated = False
            self.game.current_scene.player.damage(amount=self.attack)
        else:
            self.is_animated = True
            self.rect.x -= self.velocity


class Covidead(Mob):

    def __init__(self, game):
        super().__init__(game, "covidead", 300, 9, randint(1, 4), 0.05)


class CommunistCovidead(Mob):

    def __init__(self, game):
        super().__init__(game, "communist covidead", 300, 18, randint(1, 4), 0.05)


class Kamikaze(Mob):

    def __init__(self, game):
        super().__init__(game, "kamikaze", 300, 21, 3, 0.5)

    def forward(self):
        super().forward()
        if not self.is_animated:
            self.game.current_scene.mobs.remove(self)
