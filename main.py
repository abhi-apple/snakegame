from ast import Str
from email import header
from operator import ge
from random import random
from time import clock_getres
import random
from tkinter import font
from tokenize import String
from xxlimited import foo
from matplotlib.pyplot import get
from pandas import array
import pygame
import os
pygame.mixer.init()

from scipy import rand
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screenwid = 900
screenheig = 600
gamewin = pygame.display.set_mode((screenwid, screenwid))
pygame.display.set_caption("snake with harry")
pygame.display.update()
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)
bgimg=pygame.image.load("snake2bg.jpg")
bgimg=pygame.transform.scale(bgimg,(screenwid,screenheig)).convert_alpha()

def textscreen(text,color,x,y):
    screentxt=font.render(text,True,color)
    gamewin.blit(screentxt,[x,y])

def plotsnk(gamewin,color,snklst,snksize):
    for x,y in snklst:
        pygame.draw.rect(gamewin,color,[x,y,snksize,snksize])

def welcome():
    exgame=False
    while not exgame:
        gamewin.blit(pygame.transform.scale(pygame.image.load(os.path.join('img','snake3bg.png')),(screenwid,screenheig)),(0,0)) 
        textscreen("Welcome to snake game ",black,230,200)
        textscreen("Press Space Bar to play ",black,230,290)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exgame=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('gamed.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    exitgame = False
    gameover = False
    snakex = 45
    snakey = 55
    velocx = 0
    velocy = 0
    fps = 60
    initval=5
    foodx=random.randint(0,screenwid/2)
    foody=random.randint(0,(screenheig/2)-30)
    score =0
    snakesize = 40
    snklst=[]
    snklen=1
    with open("highscore.txt","r") as f:
        highscore=f.read()

    while not exitgame:


        if gameover:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))

            gamewin.blit(pygame.transform.scale(pygame.image.load(os.path.join('img','snake4bc.jpg')),(screenwid,screenheig)),(0,0))
            
            textscreen("Game over! Enter to Continue",red,100,250)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exitgame = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()

        else:
            crx=random.randint(0,255)
            cry=random.randint(0,255)
            crz=random.randint(0,255)
            unkc=(crx,cry,crz)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exitgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocx = initval
                        velocy = 0
                    if event.key == pygame.K_LEFT:
                        velocx = -initval
                        velocy = 0
                    if event.key == pygame.K_UP:
                        velocy = -initval 
                        velocx = 0
                    if event.key == pygame.K_DOWN:
                        velocy = initval
                        velocx = 0

            snakex = snakex+velocx
            snakey = snakey+velocy

            if (abs(snakex-foodx)<30 and abs(snakey-foody)<30):
                score+=10
                
                foodx=random.randint(0,screenwid)
                foody=random.randint(0,screenheig)
                snklen+=5
                if score>int(highscore):
                    highscore=score
                
                
            gamewin.blit(pygame.transform.scale(pygame.image.load(os.path.join('img','high.jpg')),(screenwid,screenheig)),(0,0))
            gamewin.blit(bgimg,(0,0))
            textscreen("Score : "+str(score)+"       High score : " +str(highscore),(0,255,255),5,5)
            head=[]
            head.append(snakex)
            head.append(snakey)
            snklst.append(head)
            
            if len(snklst)>snklen:
                del snklst[0]

            if head in snklst[:-1]:
                gameover=True
                pygame.mixer.music.load('gover.wav')
                pygame.mixer.music.play()

            if snakex<0 or snakex>screenwid or snakey<0 or snakey>screenheig:
                gameover=True
                pygame.mixer.music.load('gover.wav')
                pygame.mixer.music.play()
            plotsnk(gamewin,unkc,snklst,snakesize)
            gamewin.blit(pygame.transform.scale(pygame.image.load(os.path.join('img','apple.png')),(50,50)),(foodx,foody))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

