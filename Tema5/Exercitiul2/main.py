import pygame
from pygame.locals import *
import sysv_ipc


class App:
    X = 'X'
    O = 'O'

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

        self._was_blocked = False
        self._block = False
        key = 777
        try:
            self._message_queue = sysv_ipc.MessageQueue(key)
            self._msg_send_type = 1
            self._msg_recv_type = 2
            self._current_player = self.O
        except sysv_ipc.ExistentialError:
            self._message_queue = sysv_ipc.MessageQueue(key, flags=sysv_ipc.IPC_CREAT)
            self._msg_send_type = 2
            self._msg_recv_type = 1
            self._current_player = self.X

    def _winner(self):
        gm = self._game_matrix

        if (gm[0] == gm[4] == gm[8] or gm[2] == gm[4] == gm[6]) and gm[4] != 0:
            return f'{gm[4]} has won!'

        if gm[0] == gm[1] == gm[2] and gm[0] != 0:
            return f'{gm[0]} has won!'

        if gm[3] == gm[4] == gm[5] and gm[3] != 0:
            return f'{gm[3]} has won!'

        if gm[6] == gm[7] == gm[8] and gm[6] != 0:
            return f'{gm[6]} has won!'

        if gm[0] == gm[3] == gm[6] and gm[0] != 0:
            return f'{gm[0]} has won!'

        if gm[1] == gm[4] == gm[6] and gm[1] != 0:
            return f'{gm[1]} has won!'

        if gm[2] == gm[5] == gm[8] and gm[8] != 0:
            return f'{gm[8]} has won!'

        return None

    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._font = pygame.font.SysFont("Fira Code", 20)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if self._was_blocked:
                return

            x, y = event.pos[0], event.pos[1]
            self._block = True

            for idx, square in enumerate(self._game_rects):
                if square.collidepoint(x, y):
                    self._message_queue.send(f'{self._current_player}: {idx}', type=self._msg_send_type)
                    self._game_matrix[idx] = self._current_player

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

        winner = self._winner()
        if winner is not None:
            text = self._font.render(winner, True, "black")
            self._display_surface.blit(text, (330, 100))

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self._was_blocked = False

            self.on_render()

            try:
                msg = self._message_queue.receive(block=self._block, type=self._msg_recv_type)
                data = msg[0]
                split = data.split(b':')
                player = split[0].decode('utf-8')
                idx = int(split[1].decode('utf-8').strip())
                self._game_matrix[idx] = player
                self._block = False
                self._was_blocked = True
            except sysv_ipc.BusyError:
                pass

        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
