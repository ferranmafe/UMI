import Tkinter as tk
import mainView
import playMusicView

class ConfigView(tk.Frame):
  def __init__(self, master, controller):
    tk.Frame.__init__(self, master)
    self.controller = controller
    screen_title = self.define_screen_title()
    start_button = self.define_start_button()
    return_button = self.define_return_button()
    radiobuttons_title = self.define_radiobuttons_title()
    radiobuttons = self.define_radiobuttons()

    screen_title.pack()
    radiobuttons_title.pack()
    self.display_buttons(radiobuttons)
    start_button.pack()
    return_button.pack()
    self.pack()

  def define_screen_title(self):
    return tk.Label(self, text="Config View")

  def define_start_button(self):
    return tk.Button(
      self,
      text="Start!",
      command=lambda:self.controller.switch_frame(playMusicView.PlayMusicView))

  def define_return_button(self):
    return tk.Button(
      self,
      text="Return",
      command=lambda:self.controller.switch_frame(mainView.MainView))

  def define_radiobuttons_title(self):
    return tk.Label(
      self,
      text="""Choose the instruments that you want to use:""",
      justify=tk.LEFT,
      padx=20)

  def define_radiobuttons(self):
    v = tk.IntVar()
    v.set(1)

    self._instruments = [
      ("Piano", 1),
      ("Guitar", 2),
      ("Bongo", 3),
      ("Flute", 4),
      ("Trumpet", 5)
    ]

    # Function to show what option was pressed (only for debug purposes)
    def ShowChoice():
      print(v.get())

    radiobuttons = []
    for val, language in enumerate(self._instruments):
      radiobuttons.append(tk.Radiobutton(
        self,
        text=language,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val))

    return radiobuttons

  def display_buttons(self, radiobuttons):
    for i in range(0, len(radiobuttons)):
      radiobuttons[i].pack(anchor=tk.W)