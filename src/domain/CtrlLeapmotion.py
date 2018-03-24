import Leap, Hand, math, time

class CtrlLeapmotion:
    ctrlLeapmotion = None
    hands = {}
    actFrame = None
    thresholdAngle = {Leap.Finger.TYPE_THUMB : 25 * math.pi/180.0,
                      Leap.Finger.TYPE_INDEX : 25 * math.pi/180.0,
                      Leap.Finger.TYPE_MIDDLE : 25 * math.pi/180.0,
                      Leap.Finger.TYPE_RING : 20 * math.pi/180.0,
                      Leap.Finger.TYPE_PINKY : 30 * math.pi/180.0}

    OCTAVE_LIMIT_1 = 120
    OCTAVE_LIMIT_2 = 240

    def __init__(self):
        self.ctrlLeapmotion = Leap.Controller()
        self.initState()

    def initState(self):
        while (not self.ctrlLeapmotion.is_connected):
            pass
        while (not self.ctrlLeapmotion.frame().is_valid):
            pass
        self.actFrame = self.ctrlLeapmotion.frame()
        handlist = self.actFrame.hands
        for hand in handlist:
            id = hand.id
            height = self.getHandHeight(hand)
            self.hands[id] = Hand.Hand(int(hand.is_right), height)

    def getHandHeight(self, hand):
        return hand.wrist_position.y

    def printAttributes(self):
        for hand in self.hands:
            print self.hands[hand].height

    def updateState(self):
        while (not self.ctrlLeapmotion.frame().is_valid):
            pass
        if (self.actFrame.id == self.ctrlLeapmotion.frame().id):
            return
        self.actFrame = self.ctrlLeapmotion.frame()
        print("\nFrame ID: " + str(self.actFrame.id) + "\n")
        handlist = self.actFrame.hands
        for hand in handlist:
            id = hand.id
            for finger in hand.fingers:
                previousState = self.hands[id].getFingerState(finger.type)
                eventDetected = self.detectEvent(finger)
                fingerState = self.getNewState(previousState, eventDetected)
                self.hands[id].setFingerState(finger.type, fingerState)
            self.hands[id].printHandStatus()

    def detectEvent(self, finger):
        fingerMetacarpal = finger.bone(Leap.Bone.TYPE_METACARPAL).direction
        fingerPhalange = finger.bone(Leap.Bone.TYPE_PROXIMAL).direction
        detectedAngle = fingerMetacarpal.angle_to(fingerPhalange)
        return detectedAngle >= self.thresholdAngle[finger.type]

    def getNewState(self, previousState, eventDetected):
        if (eventDetected and (previousState == Hand.finger_state.HELD or previousState == Hand.finger_state.TRIGGER)):
            return Hand.finger_state.HELD
        elif (eventDetected and previousState == Hand.finger_state.IDLE):
            return Hand.finger_state.TRIGGER
        return Hand.finger_state.IDLE

    def getTriggeredFingers(self):

        for hand in self.hands


    def getTriggeredAndHeldFingers(self):


    def degToRad(self, deg):
        return deg * math.pi / 180.0

    def radToDeg(self, rad):
        return rad * 180.0 / math.pi

def main():
    c = CtrlLeapmotion()
    while 1:
        c.updateState()
        time.sleep(2)


if __name__ == "__main__":
    main()