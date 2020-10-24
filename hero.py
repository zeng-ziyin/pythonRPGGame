import pygame


class hero(object):
    def __init__(self, hero_image_path, screen, background_size,
                 name='abc', hp=10, atk=1, defe=0, agi=1, lv=1, exp=0, prof=None):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.image = pygame.image.load(hero_image_path)
        self.rect = self.image.get_rect()
        self.width, self.height = self.background_size = background_size
        self.rect.left, self.rect.top = 50, 50
        self.speed = 50
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.agi = agi
        self.prof = prof
        self.lv = lv
        self.exp = exp

    def move_up(self):
        self.rect.top -= self.speed

    def move_down(self):
        self.rect.top += self.speed

    def move_left(self):
        self.rect.left -= self.speed

    def move_right(self):
        self.rect.left += self.speed