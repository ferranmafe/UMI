import pygame

class SoundPlayer:
    sounds = []

    def __init__(self):
        pygame.init()
        sounds = [0 for i in range(24)]
        for i in range(24):
            sounds[i] = pygame.mixer.Sound("./sonidos/" + str(i) + ".wav")
        self.sounds = sounds

    def playSounds(self, notas):
        for i in len(notas):
            if notas[i]:
                channel = pygame.mixer.find_channel(True)
                channel.play(self.sounds[i])