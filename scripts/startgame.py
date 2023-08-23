import pygame
from scripts.settings import *
from scripts.scene import Scene
from scripts.menu import Menu
from scripts.gameOver import GameOver
from scripts.game import Game

class StartGame:
    def __init__(self):
        # iniciar font, som e video
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        #janela
        self.display = pygame.display.set_mode((1280, 720))

campo_img = pygame.image.load("assets/bg.png")
campo = campo_img.get_rect()

#parte - formas - player
#pos e forma em retangulo
# 0,0 pos esquerda superior
player1_img = pygame.image.load("assets/player1.png")
player1 = player1_img.get_rect()
# player1 = pygame.Rect(0, 0, 30, 150)
player1_velocidade = 6
player1_score = 0

player2_img = pygame.image.load("assets/player2.png")
player2 = player2_img.get_rect(right=1280)
player2_score = 0

ball_img=pygame.image.load("assets/ball.png")
ball = ball_img.get_rect(center=[1280/2, 720/2])
#ball = pygame.Rect(600, 350, 150, 15)
ball_dir_x = 6
ball_dir_y = 6

#parte 7 -
font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")

menu_img = pygame.image.load("assets/menu.png")
menu = menu_img.get_rect()

gameover_img = pygame.image.load("assets/gameover.png")
gameover = gameover_img.get_rect()

fade_img = pygame.Surface((1280, 720)).convert_alpha()
fade = fade_img.get_rect()
fade_img.fill("black")
fade_alpha = 255

music = pygame.mixer.Sound("assets/music.ogg")
music.play(-1)

#loop do game
cena = "menu"

fps = pygame.time.Clock()
loop = True
while loop:

    if cena == "jogo":
        #parte 2 - eventos
        for event in pygame.event.get():
            #evento do X de fechar
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player1_velocidade = 6
                if event.key == pygame.K_w:
                    player1_velocidade = -6

        if player2_score >= 3:
            cena = "gameover"
            fade_alpha = 255

        if player1_score >= 3:
            cena = "gameover"
            fade_alpha = 255

        #parte 6 - colisão e mov bola
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dir_x *= -1
            hit = pygame.mixer.Sound("assets/pong.wav")
            hit.play()

        if player1.y <= 0:
            player1.y = 0
        elif player1.y >= 720 - 150:
            player1.y = 720 - 150

        player1.y += player1_velocidade

        if ball.x <= 0:
            player2_score += 1
            placar_player2 = font.render(str(player2_score), True, "white")
            ball.x = 600
            ball_dir_x *= -1
        elif ball.x >= 1280:
            player1_score += 1
            placar_player1 = font.render(str(player1_score), True, "white")
            ball.x = 600
            ball_dir_x *= -1

        if ball.y <= 0:
            ball_dir_y *= -1
        elif ball.y >= 720 - 15:
            ball_dir_y *= -1

        ball.x += ball_dir_x
        ball.y += ball_dir_y

        player2.y = ball.y - 75

        #fica preenchendo a tela
        display.fill((0, 0, 0))

        display.blit(campo_img, campo)
        display.blit(player1_img, player1)
        display.blit(player2_img, player2)
        display.blit(ball_img, ball)

        display.blit(placar_player1, (500, 50))
        display.blit(placar_player2, (780, 50))
    elif cena == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player2_score = 0
                    player1_score = 0
                    placar_player1 = font.render(str(player1_score), True, "white")
                    placar_player2 = font.render(str(player2_score), True, "white")
                    ball.x = 640
                    ball.y = 320
                    player1.y = 0
                    player2.y = 0
                    cena = "menu"
                elif event.key == pygame.K_q:
                    loop = False
        if fade_alpha > 0:
            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)

        display.fill((0, 0, 0))
        display.blit(gameover_img, gameover)
        display.blit(fade_img,fade)
    elif cena == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "jogo"
                    fade_alpha = 255
                    start = pygame.mixer.Sound("assets/start.wav")
                    start.play()
                if event.key == pygame.K_q:
                    loop = False
        if fade_alpha > 0:
            fade_alpha -= 10
            fade_img.set_alpha(fade_alpha)
        display.fill((0, 0, 0))
        text_win = font.render("Aperte Enter", True, "white")
        display.blit(menu_img, menu)
        display.blit(fade_img, fade)

    #atualizano a tela
    fps.tick(60)
    pygame.display.flip()
