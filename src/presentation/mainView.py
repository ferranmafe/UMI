import Tkinter as tk
import configView

class MainView(tk.Frame):
  def __init__(self, master, controller):
    tk.Frame.__init__(self, master)
    self.controller = controller

    # Title frame
    titleFrame = tk.Frame(self, width=1350, height=50)
    titleFrame.pack(side=tk.TOP, fill=tk.X, expand=1, anchor=tk.N)

    # Buttons frame
    buttonsFrame = tk.Frame(self, width=100, height=50, bd=4, relief="raised")
    buttonsFrame.pack(side=tk.BOTTOM, padx=20, pady=20)

    start_label = tk.Label(titleFrame,
                           text="UMI - Universal Music Instrument")
    start_button = tk.Button(buttonsFrame,
                             text="Start playing music!",
                             command=lambda: controller.switch_frame(configView.ConfigView),
                             height=2,
                             width=50)
    exit_button = tk.Button(buttonsFrame,
                            text="Exit",
                            command=self.controller.destroy,
                            height=2,
                            width=50)

    start_label.pack(side=tk.TOP)
    start_button.grid(row=1, column=0, padx=10, pady=30)
    exit_button.grid(row=2, column=0, padx=10, pady=15)
    self.pack(fill="none", expand=True)