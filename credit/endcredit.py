#!/usr/bin/python
import time
import threading
import pygame
from pygame.locals import *

# Initialise pygame + other settings
pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
pygame.display.set_caption('End credits')
screen = pygame.display.set_mode((1920, 1080))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
fontsize = 40
font = pygame.font.SysFont("Arial", fontsize)
x = 0

def main():
    global x
    credit_list = ["CREDITS - The Departed"," ","Leonardo DiCaprio - Billy","Matt Damon - Colin Sullivan", "Jack Nicholson - Frank Costello", "Mark Wahlberg - Dignam", "Martin Sheen - Queenan"]

    going = True
    while going:
        events = event_get()
        for e in events:
            if e.type in [QUIT]:
                going = False
            if e.type in [KEYDOWN] and e.key == pygame.K_ESCAPE:
                going = False

        # Loop that creates the end credits
        ypos = screen.get_height()
        while ypos > (0 - len(credit_list)*50) and x == 0: # Loop through pixel by pixel, screenheight + height of all the textlines combined
            drawText(credit_list,ypos)
            ypos = ypos - 1
        x = 1

    pygame.quit()

def drawText(text,y):
    for line in text:
        text = font.render(line, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, (textpos.x,y))
        y = y + 45

    # Blit all the text    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.sleep(0.0001) # Sleep function to adjust speed of the end credits

    # Blit white background (else all the text will stay visible)
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    pygame.display.flip()

if __name__ == '__main__': main()