import sys, Leap, Hand

class CtrlLeapmotion:
    ctrlLeapmotion = None
    hands = {}
    actFrame = None

    def __init__(self):
        self.ctrlLeapmotion = Leap.Controller()
        self.initState()

    def initState(self):
        while (not self.ctrlLeapmotion.is_connected):
            pass
        while (not self.ctrlLeapmotion.frame().is_valid):
            pass
        actFrame = self.ctrlLeapmotion.frame()
        handlist = actFrame.hands
        for hand in handlist:
            id = hand.id
            height = self.getHandHeight(hand)
            self.hands[id] = Hand.Hand(int(hand.is_right), height)

    def getHandHeight(self, hand):
        return hand.wrist_position.y

    def printAttributes(self):
        for hand in self.hands:
            print self.hands[hand].height



def main():
    c = CtrlLeapmotion()
    c.printAttributes()


if __name__ == "__main__":
    main()