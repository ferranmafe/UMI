
class hand_types:
    LEFT_HAND   = 0
    RIGHT_HAND  = 1

class finger_state:
    IDLE    = 0
    TRIGGER = 1
    HELD    = 2

class Hand:

    #Constructor, height, whether it's right or left hand and also the state of it's fingers
    def __init__(self, hand_id, hand_type, height):
        self.hand_id    = hand_id
        self.height     = height
        self.hand_type  = hand_type
        self.finger_states = [finger_state.IDLE, finger_state.IDLE,
                              finger_state.IDLE, finger_state.IDLE,
                              finger_state.IDLE]

def main():

if __name__ == "__main__":
    main()