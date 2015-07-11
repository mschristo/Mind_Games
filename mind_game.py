__author__ = 'christos'

# Python/Pygame 05C
#
# ΠΑΙΧΝΙΔΙ 'ΜΠΑΛΑ - ΡΑΚΕΤΑ' ΜΕ ΣΚΟΡ ΣΤΗΝ ΟΘΟΝΗ
#
# @sdemetri - 2015
#=====================================================

# (1) ΣΥΝΔΕΣΗ & ΑΡΧΙΚΟΠΟΙΗΣΗ της pygame
from MyLibrary import *
from random import *




pygame.init()

# -- MAIN ------------------------
my_clock = pygame.time.Clock()

# (2) ΕΝΑΡΞΗ - SETUP
# Ανάλυση
HORIZ=800
VERT=600

# Οθόνη
my_screen = pygame.display.set_mode((HORIZ, VERT), 0, 32)
pygame.display.set_caption('Mind Games - ')

# Άλλες ρυθμίσεις
# Χρώματα
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (135,206,250)
background = LIGHT_BLUE
my_screen.fill(background)

# Δημιουργία αντικειμένου my_ball --> Ball type
my_ball = Lamp(1,50,50,30,30,"ball.png","basketball.png")


# Δημιουργία αντικειμένου my_game --> Game type
my_game = Game()

pygame.display.update()
balls = []
y=1
for i in range(6):
    if i>2 : y=2
    balls.append(Lamp(i,50*i,50*y,30,30,"ball.png","basketball.png",False))

pattern = [randint(0,10) for i in range(5)]
#=========================================================
# (3) ΒΡΟΧΟΣ ΠΑΙΧΝΙΔΙΟΥ

while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()

        if ev.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and balls[0].rect.collidepoint(pygame.mouse.get_pos()):
                print("Me patises!",balls[0].id)
                balls[0].simple(my_screen)
                pygame.display.update()
            if pygame.mouse.get_pressed()[0] and balls[1].rect.collidepoint(pygame.mouse.get_pos()):
                print("Me patises!",balls[1].id)
            if pygame.mouse.get_pressed()[0] and balls[2].rect.collidepoint(pygame.mouse.get_pos()):
                print("Me patises!",balls[2].id)
            if pygame.mouse.get_pressed()[0] and balls[3].rect.collidepoint(pygame.mouse.get_pos()):
                print("Me patises!",balls[3].id)
            if pygame.mouse.get_pressed()[0] and balls[4].rect.collidepoint(pygame.mouse.get_pos()):
                print("Me patises!",balls[4].id)
            if pygame.mouse.get_pressed()[0] and balls[5].rect.collidepoint(pygame.mouse.get_pos()):
                print("Me patises!",balls[5].id)


        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                my_screen.fill(background)
                for i in range(6): balls[i].highlighted(my_screen)
                pygame.display.update()

            if ev.key == K_CAPSLOCK:
                my_screen.fill(WHITE)
                balls[0].simple(my_screen)
                pygame.display.update()

            if ev.key == K_ESCAPE:
                pygame.quit()
                sys.exit()










