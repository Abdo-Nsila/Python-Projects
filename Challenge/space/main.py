import pygame
import math
from pygame import mixer
import time

start_time = time.time()
users_active = False
WIDTH = 800
HEIGHT = 600
# intialize the pygame
pygame.init()

Tab_bullet = []


class Bullet:
    p_Hielth: int = 29
    e_Hielth: int = 29

    def __init__(self, x, y, change, img):
        self.__X = x
        self.__Y = y
        self.__Ch = change
        self.__Img = img
        self.__score = 0

    def move(self):
        self.__Y += self.__Ch
        screen.blit(self.__Img, (self.__X, self.__Y))

    def free_memory(self):
        if self.__Ch < 0:
            if self.__Y < 0:
                return True
        if self.__Ch > 0:
            if self.__Y > WIDTH:
                return True
        return False

    def isShout(self, px, py, ex, ey):

        if self.__Ch < 0:
            distance = math.sqrt(math.pow(ex - self.__X, 2) + math.pow(ey - self.__Y, 2))
            if distance <= 30:
                mixer.Sound("./sounds/laser_explosion.mp3").play()
                Bullet.e_Hielth -= 1
                return True
        if self.__Ch > 0:
            distance = math.sqrt(math.pow(px - self.__X, 2) + math.pow(py - self.__Y, 2))
            if distance <= 30:
                mixer.Sound("./sounds/explosion1.mp3").play()
                Bullet.p_Hielth -= 1
                return True
        return False

    @classmethod
    def score(cls):
        return [Bullet.p_Hielth, Bullet.e_Hielth]


# create a scree
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title abd Icon
pygame.display.set_caption("Space")
icon = pygame.image.load('./images/player.png')
pygame.display.set_icon(icon)

# backgound
bg_load = pygame.image.load('./images/bg.jpg')
bg_Img = pygame.transform.scale(bg_load, (800, 600))
# backgorund sound
mixer.music.load("./sounds/background.mp3")
mixer.music.play(-1)
# player
img_player = pygame.image.load('./images/player.png')
P_SIZE = 60
playerImg = pygame.transform.scale(img_player, (60, 60))
playerX = 370
playerY = 500
playerCh = 5 #speed
X_L = X_R = Y_U = Y_D = 0
player_score = 0


def player(x: float, y: float) -> None:
    screen.blit(playerImg, (x, y))


# player bullet
img_player_bullet = pygame.image.load('./images/bullet_player.png')
player_bulletImg = pygame.transform.scale(img_player_bullet, (10, 10))
# enemy bullet
img_enemy_bullet = pygame.image.load('./images/bullet_enemy.png')
enemy_bulletImg = pygame.transform.scale(img_enemy_bullet, (10, 10))

# enemy
img_enemy = pygame.image.load('./images/enemy.png')
E_SIZE = 60
enemyImg = pygame.transform.scale(img_enemy, (E_SIZE, E_SIZE))
enemyX = 370
enemyY = 60
enemyCh = 5 # speed
EX_L = EX_R = EY_U = EY_D = 0
enemy_score = 0


def enemy(x, y) -> None:
    screen.blit(enemyImg, (x, y))


font = pygame.font.Font('./fonts/ARCADECLASSIC.TTF', 32)


def setScore():
    scoreP = font.render("Score  " + str(player_score), True, (255, 255, 255))
    scoreE = font.render("Score  " + str(enemy_score), True, (255, 255, 255))
    screen.blit(scoreP, (WIDTH - 180, HEIGHT - 40))
    screen.blit(scoreE, (10, 10))
    pass


# game over
def game_over():
    run1 = True
    while run1:
        # backround

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False

# for loop
over_font = pygame.font.Font('./fonts/ARCADECLASSIC.TTF', 64)
already_played = False
WINNER = ""
show_game_info = True
controles = pygame.image.load('./images/Controles_menu.png')
# create a clock object to control the frame rate
clock = pygame.time.Clock()
# game loop D
run = True
while run:
    if show_game_info:
        screen.fill((80, 80, 80))
        screen.blit(controles, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # set show_game_info = false when click on space
            # that will start game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_game_info = False
        continue


    player_score = Bullet.score()[0]
    enemy_score = Bullet.score()[1]
    if player_score <= 0 or enemy_score <= 0:
        if player_score <= 0:
            WINNER = "MONSTER"
        else:
            WINNER = "HUMAN"
        if not already_played:
            already_played = True
            mixer.Sound("./sounds/game win over.mp3").play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # backround
        pygame.display.flip()
        screen.fill((20, 20, 20))
        text = over_font.render(f"The winner is {WINNER}", True, (0, 255, 0))
        screen.blit(text, (WIDTH // 2 - 300, HEIGHT // 2 - 30))
        mixer.music.play(0)
        continue

    # bg img
    screen.blit(bg_Img, (0, 0))
    if users_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # for player
                if event.key == pygame.K_LEFT:
                    X_L = -playerCh
                if event.key == pygame.K_RIGHT:
                    X_R = playerCh
                if event.key == pygame.K_UP:
                    Y_U = -playerCh
                if event.key == pygame.K_DOWN:
                    Y_D = playerCh
                # for enemy
                if event.key == pygame.K_a:
                    EX_L = -playerCh
                if event.key == pygame.K_d:
                    EX_R = playerCh
                if event.key == pygame.K_w:
                    EY_U = -playerCh
                if event.key == pygame.K_s:
                    EY_D = playerCh
                if event.key == pygame.K_l:
                    mixer.Sound('./sounds/laser1.mp3').play()
                    Tab_bullet.append(Bullet(playerX + 25, playerY + 25, -10, player_bulletImg))
                if event.key == pygame.K_SPACE:
                    mixer.Sound('./sounds/laser2.mp3').play()
                    Tab_bullet.append(Bullet(enemyX + 25, enemyY + 25, +10, enemy_bulletImg))
            if event.type == pygame.KEYUP:
                # for player
                if event.key == pygame.K_LEFT:
                    X_L = 0
                if event.key == pygame.K_RIGHT:
                    X_R = 0
                if event.key == pygame.K_UP:
                    Y_U = 0
                if event.key == pygame.K_DOWN:
                    Y_D = 0
                # for enemy
                if event.key == pygame.K_a:
                    EX_L = 0
                if event.key == pygame.K_d:
                    EX_R = 0
                if event.key == pygame.K_w:
                    EY_U = 0
                if event.key == pygame.K_s:
                    EY_D = 0
    try:
        for i in range(len(Tab_bullet)):
            Tab_bullet[i].move()
            if Tab_bullet[i].free_memory():
                del Tab_bullet[i]
            if Tab_bullet[i].isShout(playerX + 30, playerY + 30, enemyX + 30, enemyY + 30):
                del Tab_bullet[i]


    except:
        pass
    elapased_time = time.time()
    if not users_active:
        if  elapased_time - start_time> 5:
            pygame.event.get()
            users_active = True
    # for player
    if not playerX > WIDTH - P_SIZE:
        playerX += X_R
    if not playerX <= 0:
        playerX += X_L
    if not playerY > HEIGHT - P_SIZE:
        playerY += Y_D
    if not playerY <= 250:
        playerY += Y_U
    # for enemy
    if not enemyX > WIDTH - E_SIZE:
        enemyX += EX_R
    if not enemyX <= 0:
        enemyX += EX_L
    if not enemyY > 200:
        enemyY += EY_D
    if not enemyY <= 0:
        enemyY += EY_U

    setScore()

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
    clock.tick(60)
    