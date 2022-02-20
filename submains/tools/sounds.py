import pygame


class SoundManager:

    def __init__(self):

        # load the sounds
        self.sounds = {
            "click": pygame.mixer.Sound("assets/sounds/click.ogg"),
            "cough": pygame.mixer.Sound("assets/sounds/cough.ogg"),
            "covidead": pygame.mixer.Sound("assets/sounds/covidead.ogg"),
            "hearth": pygame.mixer.Sound("assets/sounds/hearth.ogg"),
            "theme": pygame.mixer.Sound("assets/sounds/theme.ogg"),
            "vaccine": pygame.mixer.Sound("assets/sounds/vaccine.ogg")
        }

    def play(self, music: str):
        self.sounds[music].play()

    def stop(self, music: str):
        self.sounds[music].stop()
