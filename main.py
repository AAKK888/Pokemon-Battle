import pygame

logo = "                                  ,'\ \n" \
       "    _.----.        ____         ,'  _\   ___    ___     ____\n" \
       "_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n" \
       "\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n" \
       " \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n" \
       "   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n" \
       "    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n" \
       "     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n" \
       "      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n" \
       "       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n" \
       "        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n" \
       "                                `'                            '-._|\n"
print(logo)

TITLE = "Pokemon Battle"
WIDTH = 1520
HEIGHT = 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BG_COLOR = WHITE
FONT_NAME = "arial"


class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(FONT_NAME)

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BG_COLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Battle with Pokemon", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Controls are", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, 15)
        pygame.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BG_COLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("The Battle is over", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
