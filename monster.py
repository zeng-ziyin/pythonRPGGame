import pygame


class monster(object):
    def __init__(self, monster_image_path, screen, background_size,
                 position, name='abc', hp=10, atk=1, defe=0, agi=1, exped=0):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.image = pygame.image.load(monster_image_path)
        self.rect = self.image.get_rect()
        self.width, self.height = self.background_size = background_size
        self.rect.left, self.rect.top = position
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.agi = agi
        self.__exped = exped