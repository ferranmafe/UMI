# Multi-frame tkinter application v1.3
import Tkinter as tk
import mainView

class PlayMusicView(tk.Frame):
  def __init__(self, master, controller):
    tk.Frame.__init__(self, master)
    self.controller = controller

    page_2_label = tk.Label(self, text="Play Music View")
    start_button = tk.Button(self, text="Return main screen",
                             command=lambda: controller.switch_frame(mainView.MainView))
    page_2_label.pack(side="top", fill="x", pady=10)
    start_button.pack()
    self.pack()


