import Tkinter as tk
import configView

class MainView(tk.Frame):
  def __init__(self, master, controller):
    tk.Frame.__init__(self, master)
    self.controller = controller

    # Title frame
    titleFrame = tk.Frame(self, width=100, height=400)
    titleFrame.pack(side=tk.TOP, fill=tk.BOTH, anchor=tk.N)

    # Buttons frame
    buttonsFrame = tk.Frame(self, width=100, height=50, bg="#ffffff")
    buttonsFrame.pack(side=tk.TOP, padx=20, pady=20)

    start_label = tk.Label(
      titleFrame,
      text="UMI - Universal Music Instrument",
      font=("Rototo", 26, "bold"))

    start_button = tk.Button(
      buttonsFrame,
      text="Start playing music!",
      command=lambda: controller.switch_frame(configView.ConfigView),
      relief="flat",
      height=2,
      width=50,
      font=("Rototo", 12, "bold"))

    exit_button = tk.Button(
      buttonsFrame,
      text="Exit",
      command=self.controller.destroy,
      relief="flat",
      height=2,
      width=50,
      font=("Rototo", 12, "bold"))

    start_label.grid(pady=100)
    start_button.grid(row=0, column=0, padx=30, pady=30)
    exit_button.grid(row=1, column=0, padx=30, pady=30)
    self.pack(expand=1, fill=tk.Y)