import pygame as pg
from pygame.locals import *
import sys
import random
import time
#ballon animation for window..
def ballon_animation():
    global ballon,screen_width,screen_height
    if ballon.top <= 0:
        ballon.top= 0
    if ballon.bottom >= screen_height:
        ballon.bottom = screen_height
    if ballon.left <= 0:
        ballon.left = 0
    if ballon.right >=screen_width:
        ballon.right = screen_width
#score board
def always_message_display(text):
    global ballon_color,screen
    scoretext = pg.font.Font("freesansbold.ttf",20)
    textsurface = scoretext.render(text,True,ballon_color)
    textrect = textsurface.get_rect()
    #textrect.center = ((int(screen_width/2)),(int(screen_height/2)))
    textrect.center = (130,30)
    screen.blit(textsurface,textrect)
    pg.display.update()
def message_display(text):
    global ballon_color,screen
    scoretext = pg.font.Font("freesansbold.ttf",30)
    textsurface = scoretext.render(text,True,ballon_color)
    textrect = textsurface.get_rect()
    textrect.center = ((int(screen_width/2)),(int(screen_height/2)))
    screen.blit(textsurface,textrect)
    pg.display.update()
    time.sleep(3)
    run_game()
#init of the window
def run_game():
    global ballon,screen_width,screen_height,ballon_color,screen
    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()
    pg.mixer.music.load("song.mp3")
    pg.mixer.music.play(-1,0.0)
    #bullet needs
    enemies = []
    bullet = pg.Surface((10,50))
    bullet.fill((255,255,255))
    collision = 10
    bullet_y = 5
    score = 0
    #window setup
    screen_width = 1100
    screen_height = 600
    screen = pg.display.set_mode((screen_width,screen_height))
    pg.display.set_caption("Ballon game")
    #colors
    ballon_color = (190,60,50)
    bg_color = pg.Color("grey12")

    #ballon
    ballon = pg.Rect(int(screen_width/2-10),screen_height-70,50,50)
    #ballon1 = pg.image.load("ball.png")
    #sticks



    #infinite loop for running the run_game
    while True:
        #handling the input
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    ballon.x -= 80
                elif event.key == pg.K_RIGHT:
                    ballon.x += 80
                elif event.key == pg.K_UP:
                    ballon.y -= 80
                elif event.key == pg.K_DOWN:
                    ballon.y += 80
            if event.type == pg.QUIT:
                sys.exit()
        #ballon animation
        ballon_animation()
        #window update
        screen.fill(bg_color)
        pg.draw.ellipse(screen,ballon_color,ballon)
        #randnum = random.randint(1,500)
        #andnum = random.randint(500,1100)
        #pg.draw.rect(screen,ballon_color,Rect(randnum,0,10,50))
        #pg.draw.rect(screen,ballon_color,Rect(andnum,0,10,50))
        #stick animation
        if collision == 50:
            enemies.append(bullet.get_rect(topleft=(random.randrange(0,1200,80),0)))
            enemies.append(bullet.get_rect(topleft=(random.randrange(0,1200,80),0)))
            collision -= 50
        else:
            collision += 1
        for enemy in enemies:
            if score <= 100:
                enemy.y += bullet_y
            elif score <= 200:
                enemy.y += bullet_y+1
            elif score <= 300:
                enemy.y += bullet_y+2
            elif score <= 400:
                    enemy.y += bullet_y+3
            elif score <= 500:
                enemy.y += bullet_y+4
            else:
                enemy.y += bullet_y + 5
            if ballon.colliderect(enemy):
                message_text = "oouch! your crashed,yours score :"+" "+str(score)
                message_display(message_text)
            if enemy.bottom >= screen_height:
                score += 1
                enemies.remove(enemy)
        for enemy in enemies:
            screen.blit(bullet,enemy)
        #stick_animation()
        always_message_display("Yours Score : {}".format(str(score)))
        #updating the display
        pg.display.flip()
        clock.tick(60)
run_game()
