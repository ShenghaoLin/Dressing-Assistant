#import sys
#sys.path.append("/Users/xiangcui/anaconda2/lib/python2.7/site-packages/")
import pygame
import time
import random
from darkflow.net.build import TFNet
import numpy as np
import cv2
from helper_main import draw_collar,detect_person,draw_belt

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
pygame.display.set_caption('')

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
        TextSurf, TextRect = text_objects("Dressing Assistant", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start",150,display_height/2+50,buttom_width,buttom_height,start_buttom_color,start_buttom_color_hover,game_loop)
        button("Quit",500,display_height/2+50,buttom_width,buttom_height,end_buttom_color,end_buttom_color_hover,quit_game)
                
        pygame.display.update()


def game_loop():
    pygame.mixer.music.load("voice/1-hello.wav")
    pygame.mixer.music.play()
    #time.sleep(7)
    #pygame.mixer.music.stop()

    options_person = {
        "model" : "cfg/yolo.cfg",
        "load" :  "bin/yolo.weights",
        "threshold" : 0.5
    }

    options_collar = {
        "model" : "ckpt/tiny-yolo-voc-3c.cfg",
        "load" :  800,
        "threshold" : 0.01
    }

    options_belt = {
        "model" : "ckpt/tiny-yolo-voc-1c.cfg",
        "load" : 500,
        "threshold" : 0.01
    }

    tfnet_person = TFNet(options_person) #person 
    f = open("labels.txt","w")
    f.write("abnormal\n")
    f.write("normal\n")
    f.write("half-normal")
    f.close()
    tfnet_collar = TFNet(options_collar)
    f = open("labels.txt","w")
    f.write("belt")
    f.close()
    tfnet_belt = TFNet(options_belt)

    detect = True
    bool_preson, bool_collar,bool_belt= False, False, False
    done = None
 
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
       # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty('frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        result_person = tfnet_person.return_predict(frame)
        frame,bool_preson = detect_person(frame,result_person)
    
        if detect == True:
            if bool_preson==False:
                pygame.mixer.music.load("voice/comeback.wav")
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.mixer.music.stop()
            else:
                result = tfnet_collar.return_predict(frame)
                frame,bool_collar = draw_collar(frame,result)
                if bool_collar== False:
                    pygame.mixer.music.load("voice/collarError.wav")
                    pygame.mixer.music.play()
                    time.sleep(7)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("voice/adjustCollar.wav")
                    pygame.mixer.music.play()
                    time.sleep(7)
                    pygame.mixer.music.stop()
                result = tfnet_belt.return_predict(frame)
                frame,bool_belt = draw_belt(frame,result)
                if bool_collar== False:
                    pygame.mixer.music.load("voice/adjustShirtBelt.wav")
                    pygame.mixer.music.play()
                    time.sleep(7)
                    pygame.mixer.music.stop()
            if bool_preson == True and  bool_collar==True and bool_belt==True:
                print("done")
                detect = False
                cv2.imshow('frame',frame)
                pygame.mixer.music.load("voice/congrats.wav")
                pygame.mixer.music.play()
                done = frame
                time.sleep(10)
                cap.release()
                cv2.destroyAllWindows()
                break

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    try:    
        cv2.imshow("cloth",done)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
    except:
         pygame.mixer.music.load("voice/congrats.wav")
         pygame.mixer.music.play()
        


def quit_game():
    pygame.quit()
    quit()

game_intro()
