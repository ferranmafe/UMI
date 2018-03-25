import Tkinter as tk
import mainView
import playMusicView

class ConfigView(tk.Frame):
  def __init__(self, master, controller):
    self._instruments = {
      "Piano": 1,
      "Guitar": 2
    }

    tk.Frame.__init__(self, master)
    self.controller = controller

    # ----------------------- FRAMES ------------------------------------------
    topFrame = tk.Frame(self, width=350, height=50)
    topFrame.pack(side=tk.TOP, expand=1, anchor=tk.N)

    titleRadioButtonsFrame = tk.Frame(self, width=100, height=50)
    titleRadioButtonsFrame.pack(side=tk.TOP, fill=tk.X, expand=1, anchor=tk.N)

    # Buttons frame
    radiobuttonsFrame = tk.Frame(self, width=300, height=50)
    radiobuttonsFrame.pack(side=tk.TOP, padx=20, pady=50, expand=True, fill="both")

    leftFrame = tk.Frame(radiobuttonsFrame, width=300, height=150, bd=2, relief="solid")
    leftFrame.pack(side=tk.LEFT, padx = 10, expand=1, fill="both")

    titleLeftHandFrame = tk.Frame(leftFrame, width=300, height=150)
    titleLeftHandFrame.pack(side=tk.TOP, expand=1, fill="both")

    leftHandFrame = tk.Frame(leftFrame, width=300, height=150)
    leftHandFrame.pack(side=tk.BOTTOM, expand=1, fill="both")

    rightFrame = tk.Frame(radiobuttonsFrame, width=300, height=150, bd=2, relief="solid")
    rightFrame.pack(side=tk.RIGHT, expand=1, padx = 10, fill="both")

    titleRightHandFrame = tk.Frame(rightFrame, width=300, height=150)
    titleRightHandFrame.pack(side=tk.TOP, expand=1, fill="both")

    rightHandFrame = tk.Frame(rightFrame, width=300, height=150)
    rightHandFrame.pack(side=tk.BOTTOM, expand=1, fill="both")

    buttonsFrame = tk.Frame(self, width=100, height=50)
    buttonsFrame.pack(side=tk.BOTTOM, padx=20, pady=20)

    continueFrame = tk.Frame(buttonsFrame, width=100, height=50, bd=4, )
    continueFrame.pack(side=tk.LEFT, padx=10, pady=20, fill="both")

    returnFrame = tk.Frame(buttonsFrame, width=100, height=50, bd=4)
    returnFrame.pack(side=tk.RIGHT, padx=10, pady=20, fill="both")
    #--------------------------------------------------------------------------

    #---------------------------- WIDGETS -------------------------------------
    screen_title = self.define_screen_title(topFrame)
    radiobuttons_title = self.define_radiobuttons_title(titleRadioButtonsFrame)
    radiobuttons_left_hand = self.define_radiobuttons_left(leftHandFrame)
    radiobuttons_right_hand = self.define_radiobuttons_right(rightHandFrame)
    start_button = self.define_start_button(continueFrame)
    return_button = self.define_return_button(returnFrame)
    left_hand_title = tk.Label(
      titleLeftHandFrame,
      text='Left Hand',
      justify=tk.LEFT,
      font=("Rototo", 14, "bold"),
      padx=20)
    right_hand_title = tk.Label(
      titleRightHandFrame,
      text='Right Hand',
      justify=tk.LEFT,
      font=("Rototo", 16, "bold"),
      padx=20)
    screen_title.grid(pady=20)
    radiobuttons_title.pack(pady=15)
    self.display_buttons(radiobuttons_left_hand)
    self.display_buttons(radiobuttons_right_hand)
    start_button.pack()
    return_button.pack()
    left_hand_title.pack()
    right_hand_title.pack()
    self.pack()
    #--------------------------------------------------------------------------

  def define_screen_title(self, frame):
    return tk.Label(frame, text="Configuration", font=("Rototo", 24, "bold"))

  def define_start_button(self, frame):
    return tk.Button(
      frame,
      text="Start!",
      font=("Rototo", 14, 'bold'),
      height=1,
      width=10,
      command=lambda:self.controller.switch_frame(playMusicView.PlayMusicView))

  def define_return_button(self, frame):
    return tk.Button(
      frame,
      text="Return",
      font=("Rototo", 14, 'bold'),
      height=1,
      width=10,
      command=lambda:self.controller.switch_frame(mainView.MainView))

  def define_radiobuttons_title(self, frame):
    return tk.Label(
      frame,
      text="""Choose the instruments that you want to use!""",
      justify=tk.LEFT,
      font=("Rototo", 16, "bold"),
      padx=20)

  def define_radiobuttons_left(self, frame):
    self._vl = tk.IntVar()
    self._vl.set(0)

    # Function to show what option was pressed (only for debug purposes)
    def ShowChoice():
      print(self._vl.get())

    radiobuttons = []
    for key, val in self._instruments.iteritems():
      radiobuttons.append(tk.Radiobutton(
        frame,
        text=key,
        padx=20,
        font=("Rototo", 12),
        variable=self._vl,
        command=ShowChoice,
        value=val))

    return radiobuttons

  def define_radiobuttons_right(self, frame):
    self._vr = tk.IntVar()
    self._vr.set(0)

    # Function to show what option was pressed (only for debug purposes)
    def ShowChoice():
      print(self._vr.get())

    radiobuttons = []
    for key, val in self._instruments.iteritems():
      radiobuttons.append(tk.Radiobutton(
        frame,
        text=key,
        padx=20,
        font=("Rototo", 12),
        variable=self._vr,
        command=ShowChoice,
        value=val))

    return radiobuttons

  def display_buttons(self, radiobuttons):
    for i in range(len(radiobuttons)):
      radiobuttons[i].grid(pady=20)