import pygame
from pygame.locals import *
import math as M
from Numeric import *

def main ():
    def plasma (x,y):
        return 127+127*sin(x/(50+10*cos(y/78.))) \
               *cos(y/(60+10*sin(x/60.)))
    
screen_array=fromfunction(plasma, (1520, 1800)).astype(Int)

pygame.init()
screen=pygame.display.set_mode((320, 200), 0, 8)

clock=pygame.time.Clock()

aika = 1
done = 0

while not done:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            done=1

    tiheys = (M.sin(aika/55) + 1.04) * 60
    palett = []
    for k in range(256):
