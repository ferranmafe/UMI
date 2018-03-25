import SoundPlayer

class CtrlSound:
    soundPlayer = None

    def __init__(self):
        self.soundPlayer = SoundPlayer.SoundPlayer()

    def reproduceSoundEvents(self, soundEventsDetected):

        self.soundPlayer.playSounds(soundEventsDetected)

def main():
    ctrl = CtrlSound()
    ctrl.reproduceSoundEvents()

if __name__ == "__main__":
    main()
