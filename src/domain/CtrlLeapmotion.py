import sys, Leap

class CtrlLeapmotion:
    ctrlLeapmotion = None
    hands = []
    actFrame = None

    def __init__(self):
        self.ctrlLeapmotion = Leap.Controller()
        self.initState()

    def initState(self):
        if (self.ctrlLeapmotion.is_connected):
            actFrame = self.ctrlLeapmotion.frame()
            handlist = actFrame.hands
            for hand in handlist:
                id = hand.id
                height = getHandHeight(hand)



def main():
    c = CtrlLeapmotion()


if __name__ == "__main__":
    main()