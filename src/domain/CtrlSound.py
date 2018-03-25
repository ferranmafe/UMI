import SoundPlayer

class CtrlSound:
    soundPlayer = None

    def __init__(self):
        self.soundPlayer = SoundPlayer.SoundPlayer()

    def reproduceSoundEvents(self, soundEventsDetected):
        #soundEventsDetected is a 3x8 Matrix
        soundsToPlay = soundEventsDetected[0] + soundEventsDetected[1] + soundEventsDetected[2]
        self.soundPlayer.playSounds(soundsToPlay)

def main():
    ctrl = CtrlSound()
    sound = [[0,1,1,1,0,0,0,1], [0,1,1,1,0,0,0,1], [0,1,1,1,0,0,0,1]] #Input
    ctrl.reproduceSoundEvents(sound)

if __name__ == "__main__":
    main()
