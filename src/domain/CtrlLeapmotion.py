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
        res = self.initializeStructure()
        for hand in self.hands:
            i = 1
            if hand.height < OCTAVE_LIMIT_1:
                i = 0
            elif hand.height > OCTAVE_LIMIT_2:
                i = 2
            if not hand.hand_type:
                res[i][0] = (hand.finger_states[Leap.Finger.TYPE_PINKY] == Hand.finger_state.TRIGGER)
                res[i][1] = (hand.finger_states[Leap.Finger.TYPE_RING] == Hand.finger_state.TRIGGER)
                res[i][2] = (hand.finger_states[Leap.Finger.TYPE_MIDDLE] == Hand.finger_state.TRIGGER)
                res[i][3] = (hand.finger_states[Leap.Finger.TYPE_INDEX] == Hand.finger_state.TRIGGER)
            else:
                res[i][4] = (hand.finger_states[Leap.Finger.TYPE_INDEX] == Hand.finger_state.TRIGGER)
                res[i][5] = (hand.finger_states[Leap.Finger.TYPE_MIDDLE] == Hand.finger_state.TRIGGER)
                res[i][6] = (hand.finger_states[Leap.Finger.TYPE_RING] == Hand.finger_state.TRIGGER)
                res[i][7] = (hand.finger_states[Leap.Finger.TYPE_RING] == Hand.finger_state.TRIGGER)

    def getTriggeredAndHeldFingers(self):
        pass

    def degToRad(self, deg):
        return deg * math.pi / 180.0

    def radToDeg(self, rad):
        return rad * 180.0 / math.pi

    def initializeStructure(self):
        aux = []
        for i in range(3):
            aux[i] = [False for j in range(8)]
        return aux

def main():
    c = CtrlLeapmotion()
    while 1:
        c.updateState()
        time.sleep(2)


if __name__ == "__main__":
    main()