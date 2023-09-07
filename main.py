import pygame
import random
import pokemon
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
BG_COLOR = RED
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
        self.screen.fill(BG_COLOR)
        self.draw_text("These are your teams", 40, WHITE, WIDTH / 2, HEIGHT / 4)
        self.Snorlax = pokemon.Pokemon("Snorlax", "Normal", 540, 160, 110, 65, 65, 110, 30)
        self.Charzard = pokemon.Pokemon("Charzard", "Fire", 534, 78, 84, 78, 109, 85, 100)
        self.Greninja = pokemon.Pokemon("Greninja", "Water", 530, 72, 123, 67, 95, 85, 95)
        self.Electivire = pokemon.Pokemon("Electivire", "Electric", 540, 75, 123, 67, 95, 85, 95)
        self.Sceptile = pokemon.Pokemon("Sceptile", "Grass", 530, 70, 85, 65, 105, 85, 120)
        self.Lapras = pokemon.Pokemon("Lapras", "Ice", 535, 130, 85, 80, 85, 95, 60)
        self.Lucario = pokemon.Pokemon("Lucario", "Fighting", 525, 70, 110, 70, 115, 70, 90)
        self.Crobat = pokemon.Pokemon("Crobat", "Poison", 535, 85, 90, 80, 70, 80, 130)
        self.Rhyperior = pokemon.Pokemon("Rhyperior", "Ground", 535, 115, 140, 130, 55, 55, 40)
        self.Gyarados = pokemon.Pokemon("Gyarados", "Flying", 540, 95, 125, 79, 60, 100, 81)
        self.Gardevoir = pokemon.Pokemon("Gardevoir", "Psychic", 528, 68, 65, 65, 125, 115, 90)
        self.Yanmega = pokemon.Pokemon("Yanmega", "Bug", 515, 86, 76, 86, 116, 56, 95)
        self.Probropass = pokemon.Pokemon("Probropass", "Rock", 525, 60, 55, 145, 75, 150, 40)
        self.Dusknoir = pokemon.Pokemon("Dusknoir", "Ghost", 525, 45, 100, 135, 65, 135, 45)
        self.Haxorus = pokemon.Pokemon("Haxorus", "Poison", 535, 85, 90, 80, 70, 80, 130)
        self.Hisuian_Samurott = pokemon.Pokemon("Hisuian Samurott", "Dark", 528, 90, 108, 80, 100, 65, 85)
        self.Aggron = pokemon.Pokemon("Aggron", "Steel", 530, 70, 110, 180, 60, 60, 50)
        self.Florges = pokemon.Pokemon("Florges", "Fairy", 552, 78, 65, 68, 112, 154, 75)

        self.Salamence = pokemon.Pokemon("Salamence", "Dragon", 600, 95, 135, 80, 110, 80, 100)
        self.Kommo_o = pokemon.Pokemon("Kommo o", "Fighting", 600, 75, 110, 125, 100, 105, 85)
        self.Dragapult = pokemon.Pokemon("Dragapult", "Ghost", 600, 88, 120, 75, 100, 75, 142)
        self.Garchomp = pokemon.Pokemon("Garchomp", "Ground", 600, 108, 130, 95, 80, 85, 102)
        self.Tyranitar = pokemon.Pokemon("Tyranitar", "Rock", 600, 100, 134, 110, 95, 100, 61)
        self.Dragonite = pokemon.Pokemon("Dragonite", "Flying", 600, 91, 134, 95, 100, 100, 80)
        self.Metagross = pokemon.Pokemon("Metagross", "Steel", 600, 80, 135, 130, 95, 90, 70)
        self.Baxcalibur = pokemon.Pokemon("Baxcalibur", "Ice", 600, 115, 145, 92, 75, 86, 87)
        self.Goodra = pokemon.Pokemon("Goodra", "Dragon", 600, 90, 100, 70, 110, 150, 80)
        self.Gods_Pikachu = pokemon.Pokemon("God's Pikachu", "Electric", 710, 30, 140, 110, 140, 110, 180)
        self.pokemon_group = (self.Goodra, self.Baxcalibur, self.Dragapult, self.Kommo_o, self.Salamence, self.Aggron, self.Probropass, self.Haxorus, self.Snorlax, self.Charzard, self.Greninja, self.Electivire, self.Sceptile, self.Lapras, self.Lucario, self.Crobat, self.Garchomp, self.Gyarados, self.Gardevoir, self.Yanmega, self.Tyranitar, self.Dusknoir, self.Dragonite, self.Hisuian_Samurott, self.Metagross, self.Florges, self.Rhyperior)
        r = random.randint(0, 60)
        if r == 12:
            self.pokemon_chosen_1 = random.sample(self.pokemon_group, 5)
            self.pokemon_chosen_1.append(self.Gods_Pikachu)
        else:
            self.pokemon_chosen_1 = random.sample(self.pokemon_group, 6)
        for i in range(len(self.pokemon_chosen_1)):
            x = self.pokemon_chosen_1[i]
            self.draw_text(x.name + "  " + x.type, 22, WHITE, WIDTH / 4, HEIGHT / 4 + i * 20 + 40)
        pygame.display.flip()
        self.wait_for_key()
        self.pokemon_chosen_2 = random.sample(self.pokemon_group, 6)
        for i in range(len(self.pokemon_chosen_2)):
            x = self.pokemon_chosen_2[i]
            self.draw_text(x.name + "  " + x.type, 22, WHITE, WIDTH * 3 / 4, HEIGHT / 4 + i * 20 + 40)
        pygame.display.flip()
        self.wait_for_key()
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
        self.pokemon_out_1 = self.pokemon_chosen_1[0]
        self.pokemon_out_2 = self.pokemon_chosen_2[0]
        if self.pokemon_out_1.speed > self.pokemon_out_2:
            pass
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

    def button(self, position, text):
        font = pygame.font.SysFont("Arial", 50)
        text_render = font.render(text, 1, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pygame.draw.line(self.screen, (150, 150, 150), (x, y), (x + w, y), 5)
        pygame.draw.line(self.screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(self.screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(self.screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(self.screen, (100, 100, 100), (x, y, w, h))
        return self.screen.blit(text_render, (x, y))


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
