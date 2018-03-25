import pygame

class SoundPlayer:
    channels = []
    sounds = []

    def initializePiano(self):
        pygame.init()
        channels = [0 for i in range(24)]
        for i in range(24):
            channels[i] = pygame.mixer.Channel(i)

        sounds = [0 for i in range(24)]
        for i in range(24):
            sounds[i] = pygame.mixer.Sound("./sonidos/" + str(i) + ".wav")
        self.channels = channels
        self.sounds = sounds

    def playSounds(self, notas):
        for i in len(notas):
            if notas[i]:
                self.channels[i].play(self.sounds[i])