import Tkinter as tk
import mainView
import playMusicView

class ConfigView(tk.Frame):
  def __init__(self, master, controller):
    tk.Frame.__init__(self, master)
    self.controller = controller

    topFrame = tk.Frame(self, width=350, height=50)
    topFrame.pack(side=tk.TOP, fill=tk.X, expand=1, anchor=tk.N)

    titleRadioButtonsFrame = tk.Frame(self, width=1350, height=50)
    titleRadioButtonsFrame.pack(side=tk.TOP, fill=tk.X, expand=1, anchor=tk.N)

    # Buttons frame
    buttonsFrame = tk.Frame(self, width=300, height=50, bd=4, relief="raised")
    buttonsFrame.pack(side=tk.TOP, padx=20, pady=20, expand=True, fill="both")

    leftHandFrame = tk.Frame(buttonsFrame, width=300, height=50, bd=4, relief="raised")
    leftHandFrame.pack(side=tk.LEFT, padx=20, pady=20, expand=True, fill="both")

    rightHandFrame = tk.Frame(buttonsFrame, width=300, height=50, bd=4, relief="raised")
    rightHandFrame.pack(side=tk.RIGHT, padx=20, pady=20, expand=True, fill="both")

    buttonsFrame = tk.Frame(self, width=100, height=50, bd=4)
    buttonsFrame.pack(side=tk.BOTTOM, padx=20, pady=20)

    buttonsFrame = tk.Frame(self, width=100, height=50, bd=4)
    buttonsFrame.pack(side=tk.BOTTOM, padx=20, pady=20)

    continueFrame = tk.Frame(buttonsFrame, width=100, height=50, bd=4)
    continueFrame.pack(side=tk.LEFT, padx=20, pady=20, fill="both")

    returnFrame = tk.Frame(buttonsFrame, width=100, height=50, bd=4)
    returnFrame.pack(side=tk.RIGHT, padx=20, pady=20, fill="both")

    screen_title = self.define_screen_title(topFrame)
    radiobuttons_title = self.define_radiobuttons_title(titleRadioButtonsFrame)
    radiobuttons_left_hand = self.define_radiobuttons_left(leftHandFrame)
    radiobuttons_right_hand = self.define_radiobuttons_right(rightHandFrame)
    start_button = self.define_start_button(continueFrame)
    return_button = self.define_return_button(returnFrame)

    screen_title.pack()
    radiobuttons_title.pack()
    self.display_buttons(radiobuttons_left_hand)
    self.display_buttons(radiobuttons_right_hand)
    start_button.pack()
    return_button.pack()
    self.pack()

  def define_screen_title(self, frame):
    return tk.Label(frame, text="Config View", font=("Arial", 18))

  def define_start_button(self, frame):
    return tk.Button(
      frame,
      text="Start!",
      command=lambda:self.controller.switch_frame(playMusicView.PlayMusicView))

  def define_return_button(self, frame):
    return tk.Button(
      frame,
      text="Return",
      command=lambda:self.controller.switch_frame(mainView.MainView))

  def define_radiobuttons_title(self, frame):
    return tk.Label(
      frame,
      text="""Choose the instruments that you want to use:""",
      justify=tk.LEFT,
      padx=20)

  def define_radiobuttons_left(self, frame):
    self._vl = tk.IntVar()
    self._vl.set(1)

    self._instruments = [
      ("Piano", 1),
      ("Guitar", 2),
      ("Bongo", 3),
      ("Flute", 4),
      ("Trumpet", 5)
    ]

    # Function to show what option was pressed (only for debug purposes)
    def ShowChoice():
      print(self._vl.get())

    radiobuttons = []
    for val, language in enumerate(self._instruments):
      radiobuttons.append(tk.Radiobutton(
        frame,
        text=language,
        padx=20,
        variable=self._vl,
        command=ShowChoice,
        value=val))

    return radiobuttons

  def define_radiobuttons_right(self, frame):
    self._vr = tk.IntVar()
    self._vr.set(1)

    self._instruments = [
      ("Piano", 1),
      ("Guitar", 2),
      ("Bongo", 3),
      ("Flute", 4),
      ("Trumpet", 5)
    ]

    # Function to show what option was pressed (only for debug purposes)
    def ShowChoice():
      print(self._vr.get())

    radiobuttons = []
    for val, language in enumerate(self._instruments):
      radiobuttons.append(tk.Radiobutton(
        frame,
        text=language,
        padx=20,
        variable=self._vr,
        command=ShowChoice,
        value=val))

    return radiobuttons

  def display_buttons(self, radiobuttons):
    for i in range(0, len(radiobuttons)):
      radiobuttons[i].pack(anchor=tk.W)