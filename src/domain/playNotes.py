import pygame
import time
class PlayNotes:
    def __init__(self):
        self.canales = []
        self.sounds = {}

    def inicializar(self):
        pygame.init()
        canales = [0 for i in range(8)]
        for i in range(8):
            canales[i] = pygame.mixer.Channel(i)

        sounds = {}
        sounds['do'] = pygame.mixer.Sound("./sonidos/do.wav")
        sounds['re'] = pygame.mixer.Sound("./sonidos/re.wav")
        sounds['mi'] = pygame.mixer.Sound("./sonidos/mi.wav")
        sounds['fa'] = pygame.mixer.Sound("./sonidos/fa.wav")
        sounds['sol']= pygame.mixer.Sound("./sonidos/sol.wav")
        sounds['la'] = pygame.mixer.Sound("./sonidos/la.wav")
        sounds['si'] = pygame.mixer.Sound("./sonidos/si.wav")
        sounds['do*'] = pygame.mixer.Sound("./sonidos/do'.wav")
        self.canales = canales
        self.sounds = sounds


    def tocar(self, notas):
        j = 0
        for i in range(len(notas)):
            if notas[i] in self.sounds:
                self.canales[j].queue(self.sounds[notas[i]])
                j = j+1
        time.sleep(0.3)
