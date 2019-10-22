# coding:iso-8859-9 Türkçe

from winsound import Beep
for i in range (100, 4000, 100): Beep (i, 500)

input ("Ent:")
from winsound import PlaySound
PlaySound ("ses/0.wav", 0)

input ("Ent:")
import pygame
pygame.mixer.init (18000, -16, 2, 1024)
ses = pygame.mixer.Sound ("ses/0.wav")
ses.play() # Windows'ta çalışmadı...