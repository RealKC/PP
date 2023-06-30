import copy

import pygame

class Carucior:
    WIDTH = 50
    HEIGHT = 30

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, color='black', rect=(self.x, self.y, self.WIDTH, self.HEIGHT))
        pygame.draw.rect(surface, color='white', rect=(self.x+7, self.y-5, self.WIDTH-14, self.HEIGHT))

    def clone(self):
        return copy.copy(self)


def make_carucior1(proto):
    new = proto.clone()
    new.set_x(15)
    new.set_y(200)
    return new


def make_carucior2(proto):
    new = proto.clone()
    new.set_x(500)
    new.set_y(15)
    return new


if __name__ == '__main__':
    pygame.init()
    #                                  AMEN
    surface = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)

    carucior_prototip = Carucior()

    carucioare = [make_carucior2(carucior_prototip), make_carucior1(carucior_prototip)]

    surface.fill('white')

    for carucior in carucioare:
        carucior.draw(surface)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        pygame.display.flip()
