import pygame, time

class SoundPlayer:
    sounds = []

    def __init__(self):
        pygame.init()
        sounds = [0 for i in range(7)]
        for i in range(7):
            sounds[i] = pygame.mixer.Sound("./sonidos/" + str(i) + ".wav")
        self.sounds = sounds

    def playSounds(self, key):
        print key
        for i in range(0, 7): #Should be len(key)
            if key[i]:
                channel = pygame.mixer.find_channel(True)
                print(channel)
                channel.play(self.sounds[i])

        while 1:
            pass
