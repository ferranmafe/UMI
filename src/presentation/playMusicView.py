# Multi-frame tkinter application v1.3
import Tkinter as tk
import mainView

class PlayMusicView(tk.Frame):
  def __init__(self, master, controller):
    tk.Frame.__init__(self, master)
    self.controller = controller

    # ---------- Frames -------------------------------------------------------
    titleFrame = tk.Frame(self, width=100, height=50, bd=4, relief="raised")
    titleFrame.pack(side=tk.TOP, padx=20, pady=20)

    notesFrame = tk.Frame(self, width=100, height=50, bd=4, relief="raised")
    notesFrame.pack(side=tk.TOP, padx=20, pady=20)

    leftHandFrame = tk.Frame(notesFrame, width=100, height=50, bd=4, relief="raised")
    leftHandFrame.pack(side=tk.LEFT, padx=20, pady=20)

    upperNotesLH = tk.Frame(leftHandFrame, width=100, height=50, bd=4)
    upperNotesLH.pack(side=tk.TOP, padx=20, pady=20)

    middleNotesLH = tk.Frame(leftHandFrame, width=100, height=50, bd=4)
    middleNotesLH.pack(side=tk.TOP, padx=20, pady=20)

    bottomNotesLH = tk.Frame(leftHandFrame, width=100, height=50, bd=4)
    bottomNotesLH.pack(side=tk.TOP, padx=20, pady=20)

    rightHandFrame = tk.Frame(notesFrame, width=100, height=50, bd=4, relief="raised")
    rightHandFrame.pack(side=tk.RIGHT, padx=20, pady=20)

    upperNotesRH = tk.Frame(rightHandFrame, width=100, height=50, bd=4)
    upperNotesRH.pack(side=tk.TOP, padx=20, pady=20)

    middleNotesRH = tk.Frame(rightHandFrame, width=100, height=50, bd=4)
    middleNotesRH.pack(side=tk.TOP, padx=20, pady=20)

    bottomNotesRH = tk.Frame(rightHandFrame, width=100, height=50, bd=4)
    bottomNotesRH.pack(side=tk.TOP, padx=20, pady=20)

    buttonsFrame = tk.Frame(self, width=100, height=50, bd=4, relief="raised")
    buttonsFrame.pack(side=tk.BOTTOM, padx=20, pady=20)
    # -------------------------------------------------------------------------

    # ---------- Widgets ------------------------------------------------------
    title_label = tk.Label(titleFrame, text="Play Music View")
    return_button = tk.Button(
      buttonsFrame,
      text="Return main screen",
      command=lambda:controller.switch_frame(mainView.MainView))

    self._buttons = []
    for i in range(0, 3):
      buttons_hand = []
      for j in range(0, 2):
        buttons_note = []
        for k in range(0, 4):
          if i == 0 and j == 0:
            buttons_note.append(tk.Button(
              upperNotesLH, bg="cyan"
            ))
          elif i == 1 and j == 0:
            buttons_note.append(tk.Button(
              middleNotesLH, bg="grey"
            ))
          elif i == 2 and j == 0:
            buttons_note.append(tk.Button(
              bottomNotesLH, bg="grey"
            ))
          elif i == 0 and j == 1:
            buttons_note.append(tk.Button(
              upperNotesRH, bg="grey"
            ))
          elif i == 1 and j == 1:
            buttons_note.append(tk.Button(
              middleNotesRH, bg="grey"
            ))
          else:
            buttons_note.append(tk.Button(
              bottomNotesRH, bg="grey"
            ))
        buttons_hand.append(buttons_note)
      self._buttons.append(buttons_hand)
    # -------------------------------------------------------------------------

    # ------------ Pack -------------------------------------------------------
    title_label.pack()
    for i in range(0, len(self._buttons)):
      for j in range(0, len(self._buttons[i])):
        for k in range(0, len(self._buttons[i][j])):
          self._buttons[i][j][k].pack(side=tk.LEFT)
    return_button.pack()
    self.pack()
    self.start_pooling()
    # -------------------------------------------------------------------------

  def start_pooling(self):
    print("hello")
    self.after(2000, self.continue_pooling)

  def continue_pooling(self):
    self.controller.main_node_thread()
    self.after(1000, self.continue_pooling)