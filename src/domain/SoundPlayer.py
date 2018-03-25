import pygame, time

class SoundPlayer:
    sounds = []
    channels = []

    def __init__(self):
        pygame.init()
        channels = [0 for i in range(8)]
        for i in range(8):
            channels[i] = pygame.mixer.Channel(i)
        sounds = [0 for i in range(24)]
        for i in range(24):
            sounds[i] = pygame.mixer.Sound("../domain/sonidos2/" + str(i) + ".wav")
        self.sounds = sounds
        self.channels = channels

    def playSounds(self, key):
        for i in range(0, len(key)):
            if key[i]:
                self.channels[i % 8].play(self.sounds[i])