import CtrlLeapmotion

class CtrlDomain:
    ctrlLeapmotion = None
    ctrlSound = None

    def __init__(self):
        pass


    def initializeAction(self):
        self.ctrlLeapmotion = CtrlLeapmotion.CtrlLeapmotion()
        self.ctrlSound = CtrlSound.CtrlSound()

    def getNextMove(self):
        self.updateLeapmotionState()
        soundEventsDetected = self.detectSoundEvents()
        self.reproduceSoundEvents(soundEventsDetected)
        return self.detectPressEvents()

    def detectSoundEvents(self):
        return self.ctrlLeapmotion.getTriggeredFingers()

    def detectPressEvents(self):
        return self.ctrlLeapmotion.getTriggeredAndHeldFingers()

    def updateLeapmotionState(self):
        self.ctrlLeapmotion.updateState()

    def reproduceSoundEvents(self, soundEventsDetected):
        self.ctrlSound.reproduceSoundEvents(soundEventsDetected)