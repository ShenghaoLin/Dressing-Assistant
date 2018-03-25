import pygame
import time
import random

import numpy as np
import cv2
 
pygame.init()
 
display_width = 800
display_height = 600
 
text_color = (0,0,0)
bg_color = (196,235,255)

buttom_width = 150
buttom_height = 80

start_buttom_color = (193,232,129)
start_buttom_color_hover = (184,247,97)
end_buttom_color = (255,126,88)
end_buttom_color_hover = (247,94,46)



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PROJECT NAME')

def text_objects(text, font):
    textSurface = font.render(text, True, text_color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("Roboto-Light.ttf",24)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(bg_color)
        largeText = pygame.font.Font('Roboto-Regular.ttf',72)
        TextSurf, TextRect = text_objects("PROJECT NAME", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start",150,display_height/2+50,buttom_width,buttom_height,start_buttom_color,start_buttom_color_hover,game_loop)
        button("Quit",500,display_height/2+50,buttom_width,buttom_height,end_buttom_color,end_buttom_color_hover,quit_game)
                
        pygame.display.update()


def game_loop():

    cap = cv2.VideoCapture(0)
 
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def quit_game():
    pygame.quit()
    quit()

game_intro()
game_loop()
quit_game()
