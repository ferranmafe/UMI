import Leap

class hand_types:
    LEFT_HAND   = 0
    RIGHT_HAND  = 1

class finger_state:
    IDLE    = 0
    TRIGGER = 1
    HELD    = 2

class Hand:

    #Constructor, height, whether it's right or left hand and also the state of it's fingers
    def __init__(self, hand_type, height):
        self.height     = height
        self.hand_type  = hand_type
        self.finger_states = {Leap.Finger.TYPE_THUMB : finger_state.IDLE,
                              Leap.Finger.TYPE_INDEX : finger_state.IDLE,
                              Leap.Finger.TYPE_MIDDLE : finger_state.IDLE,
                              Leap.Finger.TYPE_RING : finger_state.IDLE,
                              Leap.Finger.TYPE_PINKY : finger_state.IDLE}

    def setFingerState(self, fingerType, fingerState):
        self.finger_states[fingerType] = fingerState

    def getFingerState(self, fingerType):
        return self.finger_states[fingerType]

    def printHandStatus(self):
        print("Hand height: " + str(self.height) + "\n")
        if self.hand_type :
            print("Hand type: Right\n")
        else:
            print("Hand type: Left\n")
        for f in self.finger_states:
            print("\t" + str(f) + " -> " + str(self.finger_states[f]) + "\n")


def main():
    x = Hand(1, 234.3)
    print("HI!")

if __name__ == "__main__":
    main()