__author__ = 'christos'

from MyLibrary import *
from random import *

def display_start_screen():
    my_screen.blit(back,screen_rect)
    pygame.draw.rect(my_screen, YELLOW, start_rect, 0)
    pygame.draw.rect(my_screen, YELLOW, quit_rect, 0)
    my_screen.blit(title,(170,50))
    my_screen.blit(start_button,(264,200))
    my_screen.blit(quit_button,(265,280))
    pygame.display.update()

def display_instructions():
    my_screen.blit(back,screen_rect)
    my_screen.blit(choose,(114,50))
    pygame.draw.rect(my_screen, YELLOW, continue_rect, 0)
    my_screen.blit(instructions_image,instructions_rect)
    my_screen.blit(continue_button,(250,330))
    pygame.display.update()

def display_game_screen():
    my_screen.blit(back,screen_rect)
    pygame.draw.rect(my_screen, YELLOW, restart_rect, 0)
    pygame.draw.rect(my_screen, YELLOW, quit_rect_2, 0)
    my_screen.blit(restart_button,(510,15))
    my_screen.blit(quit_button_2,(520,55))
    update_score()
    for i in range(7):
        lamps[i].draw(my_screen)
    pygame.display.update()

def light_ball(i):
    lamps[i].make_highlight()
    lamps[i].draw(my_screen)
    pygame.display.update()
    pygame.time.delay(150)
    lamps[i].make_simple()
    lamps[i].draw(my_screen)
    pygame.display.update()

def update_score():
    score_text = my_font_3.render("Score: "+str(score),True,BLACK)
    my_screen.blit(pygame.image.load("score.png"),score_rect)
    my_screen.blit(score_text,(10,10))
    pygame.display.update()

def show_message(text):
    message = my_font_3.render(text, True,BLACK)
    my_screen.blit(back_message,message_rect)
    my_screen.blit(message,(160,130))
    update_score()
    pygame.display.update()


pygame.init()

# -- MAIN ------------------------
my_clock = pygame.time.Clock()

# (2) ΕΝΑΡΞΗ - SETUP
# Ανάλυση
HORIZ=600
VERT=400

# Οθόνη
my_screen = pygame.display.set_mode((HORIZ, VERT), 0, 32)
pygame.display.set_caption('Mind Games')

screen_rect = pygame.Rect(0, 0, 600, 400)
back = pygame.image.load("background.png")
back_message = pygame.image.load("back_message.png")


# Άλλες ρυθμίσεις
# Χρώματα
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 51)
ORANGE = (255, 153, 0)
BROWN = (153, 0, 0)
LIGHT_BLUE = (135,206,250)

background = LIGHT_BLUE
score = 0

# Κείμενο
my_font = pygame.font.SysFont(None,64)
my_font_2 = pygame.font.SysFont(None,46)
my_font_3 = pygame.font.SysFont(None,32)

title = my_font.render('MIND GAME',True,BLACK)
choose = my_font.render('Choose difficulty',True,BLACK)

start_button = my_font_2.render('Start',True,BLACK)
start_rect = pygame.Rect(225, 193, 150, 40)

quit_button = my_font_2.render('Quit',True,BLACK)
quit_rect = pygame.Rect(225, 273, 150, 40)

instructions_image = pygame.image.load("instructions.png")
instructions_rect = pygame.Rect(0, 0, 600, 308)

continue_button = my_font_3.render('Continue',True,BLACK)
continue_rect = pygame.Rect(225, 320, 150, 40)

score_text = my_font_3.render("Score: "+str(score),True,BLACK)
score_rect = pygame.Rect(0, 0, 202, 117)

message_rect = pygame.Rect(0,0,447,202)

restart_button = my_font_3.render('Restart',True,BLACK)
restart_rect = pygame.Rect(500, 10, 100, 30)

quit_button_2 = my_font_3.render('Quit',True,BLACK)
quit_rect_2 = pygame.Rect(500, 50, 100, 30)


# Κατάσταση Οθόνης
# 1 Αρχική οθόνη, 2 Οδηγίες , 3 Βασικη οθόνη παιχνιδιού, 4 Game over
state = 1

# Δημιουργία αντικειμένου my_game --> Game type
my_game = Game()

lamps = []
no_of_lamps = 4
lamps.append(Lamp(1,25,200,100,70,"lamp1.png","light1.png",False))
lamps.append(Lamp(2,175,200,100,70,"lamp2.png","light2.png",False))
lamps.append(Lamp(3,325,200,100,70,"lamp3.png","light3.png",False))
lamps.append(Lamp(4,475,200,100,70,"lamp4.png","light4.png",False))
lamps.append(Lamp(5,100,300,100,70,"lamp5.png","light5.png",False))
lamps.append(Lamp(6,250,300,100,70,"lamp6.png","light6.png",False))
lamps.append(Lamp(7,400,300,100,70,"lamp7.png","light7.png",False))

pygame.display.update()

#=========================================================
# (3) ΒΡΟΧΟΣ ΠΑΙΧΝΙΔΙΟΥ
level = 1
play = False
pygame.mixer.music.load("test.wav")
while True:
    if state == 1:
        # Arxikh katastasi
        display_start_screen()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and start_rect.collidepoint(pygame.mouse.get_pos()):
                    state=2
                    pygame.time.delay(300)
                    display_instructions()
                elif pygame.mouse.get_pressed()[0] and quit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()


    elif state == 2:
        # Othoni duskolias
        display_instructions()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and continue_rect.collidepoint(pygame.mouse.get_pos()):
                    state=3
                    pygame.time.delay(300)
                    display_game_screen()

    elif state == 3:
        if not play:
            pattern = [randint(0,6) for i in range(level)]
            pygame.time.delay(300)
            show_message("Look carefully !!!")
            pygame.time.delay(700)
            for i in range(level):
                light_ball(pattern[i])
                pygame.time.delay(150)
            pygame.time.delay(600)
            show_message("Go !")
            to_check = 0 # Elegxos an to kathe hit einai stin antistoixi thesi sto pattern
            play=True
        # Othoni paixnidiou
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and lamps[0].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==0:
                        print("Me patises!",lamps[0].id)
                        pygame.mixer.music.play()
                        score+=10
                        update_score()
                        light_ball(0)
                        to_check += 1
                    else:
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(400)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[1].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==1:
                        print("Me patises!",lamps[1].id)
                        pygame.mixer.music.play()
                        score+=10
                        update_score()
                        light_ball(1)
                        to_check += 1
                    else:
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(400)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[2].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==2:
                        print("Me patises!",lamps[2].id)
                        pygame.mixer.music.play()
                        score+=10
                        update_score()
                        light_ball(2)
                        to_check += 1
                    else:
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(400)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[3].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==3:
                        print("Me patises!",lamps[3].id)
                        pygame.mixer.music.play()
                        score+=10
                        update_score()
                        light_ball(3)
                        to_check += 1
                    else:
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(400)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[4].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==4:
                        print("Me patises!",lamps[4].id)
                        pygame.mixer.music.play()
                        score+=10
                        update_score()
                        show_message("Help")
                        light_ball(4)
                        to_check += 1
                    else:
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(400)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[5].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==5:
                        print("Me patises!",lamps[5].id)
                        pygame.mixer.music.play()
                        score+=10
                        update_score()
                        light_ball(5)
                        to_check += 1
                    else:
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(400)
                        show_message("Press restart to play again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and lamps[6].rect.collidepoint(pygame.mouse.get_pos()):
                    if pattern[to_check]==6:
                        print("Me patises!",lamps[6].id)
                        pygame.mixer.music.play()
                        score+=10
                        update_score()
                        light_ball(6)
                        to_check += 1
                    else:
                        show_message("Wrong")
                        pygame.time.delay(400)
                        show_message("Your score was: "+str(score))
                        pygame.time.delay(400)
                        show_message("Press restart to play\n again")
                        state = 4
                if pygame.mouse.get_pressed()[0] and restart_rect.collidepoint(pygame.mouse.get_pos()):
                    state = 3
                    play=0
                    level=1
                    score=0
                elif pygame.mouse.get_pressed()[0] and quit_rect_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if(to_check>=len(pattern)):
                    show_message("Great work!")
                    play=0
                    level += 1
                    pygame.time.delay(300)



            if ev.type == KEYDOWN:

                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    else:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and restart_rect.collidepoint(pygame.mouse.get_pos()):
                    print(10)
                    state = 3
                    play=0
                    level=1
                    score=0
                elif pygame.mouse.get_pressed()[0] and quit_rect_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()











