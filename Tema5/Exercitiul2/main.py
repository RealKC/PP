import pygame
from pygame.locals import *


class App:
    X = 1
    O = 2

    def __init__(self):
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = 640, 480  # God's resolution
        self._game_rects = [
            Rect(20, 30, 100, 100), Rect(120, 30, 100, 100), Rect(220, 30, 100, 100),
            Rect(20, 130, 100, 100), Rect(120, 130, 100, 100), Rect(220, 130, 100, 100),
            Rect(20, 230, 100, 100), Rect(120, 230, 100, 100), Rect(220, 230, 100, 100)
        ]
        self._game_matrix = [0] * 9
        print(type(self._game_matrix))
        self._current_player = self.X

    def _toggle_player(self):
        if self._current_player == self.X:
            self._current_player = self.O
        else:
            self._current_player = self.X

    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos[0], event.pos[1]

            for idx, square in enumerate(self._game_rects):
                if square.collidepoint(x, y):
                    self._game_matrix[idx] = self._current_player
                    self._toggle_player()

    def on_render(self):
        self._display_surface.fill("white")

        for idx, square in enumerate(self._game_rects):
            pygame.draw.rect(self._display_surface, "black", square, 2)
            shape = self._game_matrix[idx]
            match shape:
                case 0: pass
                case self.X:
                    pygame.draw.line(self._display_surface, "green", (square.x, square.y), (square.x + square.w, square.y + square.h), width=2)
                    pygame.draw.line(self._display_surface, "green", (square.x + square.w, square.y), (square.x, square.y + square.h), width=2)
                case self.O:
                    pygame.draw.circle(self._display_surface, "blue", (square.x + square.w / 2, square.y + square.h / 2), square.h / 2)
                    pygame.draw.circle(self._display_surface, "white", (square.x + square.w / 2, square.y + square.h / 2), square.h / 2 - 2)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
                self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
