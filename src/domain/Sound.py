import SoundPlayer

class CtrlSound:

    def __init__(self):
        pass

    def reproduceSoundEvents(self, soundEventsDetected):
        for row in soundEventsDetected:
            for sound in soundEventsDetected[row]:
                if sound == 1:
                    #Play sound



def main():
    ctrl = CtrlSound()
    ctrl.reproduceSoundEvents()

if __name__ == "__main__":
    main()
