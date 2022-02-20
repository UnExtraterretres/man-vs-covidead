from .scene import *
from .tools.sounds import SoundManager


class Game:

    def __init__(self):
        # creation of the screen
        self.screen = pygame.display.set_mode((1080, 360))
        # title
        pygame.display.set_caption("One man vs covidead")
        # icon
        pygame.display.set_icon(pygame.image.load("assets/entities/player/player0.png"))

        # the font
        self.font = pygame.font.Font("assets/pixel.ttf", 35)

        # FPS
        self.clock = pygame.time.Clock()
        self.default_FPS = 60

        # default state of the game
        self.is_running = True

        # key pressed
        self.pressed = {}

        # sounds
        self.sounds = SoundManager()

        # scenes, current
        self.scenes = {
            "main menu": Menu(game=self),
            "level 1": Level(game=self),
            "game over": GameOver(game=self)
        }
        self.current_scene = self.scenes["main menu"]

    def check_events(self):
        # checking of events
        for event in pygame.event.get():
            # quit event
            if event.type == pygame.QUIT:
                # check the closing
                self.is_running = False
            # get key pressed
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            # get key release
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

                # trying to launch a vaccine
                try:
                    if event.key == pygame.K_SPACE and self.current_scene == self.scenes["level 1"]:
                        self.current_scene.player.launch_vaccines()
                except AttributeError:
                    pass

    def run(self):
        # the game loop
        while self.is_running:
            # first a checking of the events
            self.check_events()
            # updating by applying the logic of the current scene
            self.current_scene.update()
            # displays of the current scenes
            self.current_scene.display()
            # do the tick of the clock
            self.clock.tick(self.default_FPS)

    def pin_up(self, text: str, coordinate: tuple, color=(0, 0, 0)):
        """
        this function show on the pygame window the text
        """
        txt = self.font.render(text, True, color)
        self.screen.blit(txt, coordinate)
