import pygame
from random import randint


def load_images(name: str):
    # future list
    images = []

    # path
    path = f"assets/entities/{name}/{name}"

    # load images
    for i in range(5):
        images.append(pygame.image.load(f"{path}{i}.png"))

    return images


entities = ["communist covidead", "covidead", "kamikaze", "player"]
animations = {}
for entity in entities:
    animations[entity] = load_images(entity)


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name: str, size=(50, 50)):
        super().__init__()

        # name
        self.name = name
        # size
        self.size = size

        # current image index
        self.current_img_idx = 0
        # is animated
        self.is_animated = True

        # load images
        self.images = animations.get(self.name)
        # init the first image
        self.image = self.images[self.current_img_idx]
        self.image = pygame.transform.scale(self.image, self.size)

    def animation(self):
        if self.is_animated:
            # increase the current image index
            self.current_img_idx += randint(0, 1)
            if self.current_img_idx >= len(self.images):
                self.current_img_idx = 0

            # change the current image
            self.image = self.images[self.current_img_idx]
            self.image = pygame.transform.scale(self.image, self.size)
        else:
            # reset the current image index
            self.current_img_idx = 0

            # change the current image
            self.image = self.images[self.current_img_idx]
            self.image = pygame.transform.scale(self.image, self.size)
