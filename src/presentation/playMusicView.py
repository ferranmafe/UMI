# Multi-frame tkinter application v1.3
import Tkinter as tk
import mainView
from threading import Thread

class PlayMusicView(tk.Frame):
  def __init__(self, master, controller):
    tk.Frame.__init__(self, master)
    self._notes = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
    self.controller = controller

    # ---------- Frames -------------------------------------------------------
    titleFrame = tk.Frame(self, width=100, height=50)
    titleFrame.pack(side=tk.TOP, padx=20, pady=20)

    notesFrame = tk.Frame(self, width=100, height=50)
    notesFrame.pack(side=tk.TOP, padx=20, pady=20)

    leftHandFrame = tk.Frame(notesFrame, width=100, height=50, bd=2, relief="solid")
    leftHandFrame.pack(side=tk.LEFT, padx=20, pady=20)

    leftHandTitleFrame = tk.Frame(leftHandFrame, width=100, height=50)
    leftHandTitleFrame.pack(side=tk.TOP, padx=20, pady=20)

    upperNotesLH = tk.Frame(leftHandFrame, width=100, height=50, bd=4)
    upperNotesLH.pack(side=tk.TOP, padx=20, pady=20)

    middleNotesLH = tk.Frame(leftHandFrame, width=100, height=50, bd=4)
    middleNotesLH.pack(side=tk.TOP, padx=20, pady=20)

    bottomNotesLH = tk.Frame(leftHandFrame, width=100, height=50, bd=4)
    bottomNotesLH.pack(side=tk.TOP, padx=20, pady=20)

    rightHandFrame = tk.Frame(notesFrame, width=100, height=50, bd=2, relief="solid")
    rightHandFrame.pack(side=tk.RIGHT, padx=20, pady=20)

    rightHandTitleFrame = tk.Frame(rightHandFrame, width=100, height=50)
    rightHandTitleFrame.pack(side=tk.TOP, padx=20, pady=20)

    upperNotesRH = tk.Frame(rightHandFrame, width=100, height=50, bd=4)
    upperNotesRH.pack(side=tk.TOP, padx=20, pady=20)

    middleNotesRH = tk.Frame(rightHandFrame, width=100, height=50, bd=4)
    middleNotesRH.pack(side=tk.TOP, padx=20, pady=20)

    bottomNotesRH = tk.Frame(rightHandFrame, width=100, height=50, bd=4)
    bottomNotesRH.pack(side=tk.TOP, padx=20, pady=20)

    buttonsFrame = tk.Frame(self, width=100, height=50)
    buttonsFrame.pack(side=tk.BOTTOM, padx=20, pady=20)
    # -------------------------------------------------------------------------

    # ---------- Widgets ------------------------------------------------------
    title_label = tk.Label(
      titleFrame,
      text="Play Music View",
      font=("Rototo", 24, "bold"))
    return_button = tk.Button(
      buttonsFrame,
      text="Return main screen",
      command=lambda:controller.switch_frame(mainView.MainView),
      font=("Rototo", 14, "bold"))

    left_hand_title = tk.Label(
      leftHandTitleFrame,
      text="Left Hand",
      font=("Rototo", 14, "bold"))

    right_hand_title = tk.Label(
      rightHandTitleFrame,
      text="Rigth Hand",
      font=("Rototo", 14, "bold"))

    self._buttons = []
    for i in range(0, 3):
      buttons_hand = []
      for j in range(0, 2):
        buttons_note = []
        for k in range(0, 4):
          if i == 0 and j == 0:
            buttons_note.append(tk.Button(
              upperNotesLH, bg="white", width=2, height=2, state=tk.DISABLED, text=self._notes[k]
            ))
          elif i == 1 and j == 0:
            buttons_note.append(tk.Button(
              middleNotesLH, bg="white", width=2, height=2, state=tk.DISABLED, text=self._notes[k]
            ))
          elif i == 2 and j == 0:
            buttons_note.append(tk.Button(
              bottomNotesLH, bg="white", width=2, height=2, state=tk.DISABLED, text=self._notes[k]
            ))
          elif i == 0 and j == 1:
            buttons_note.append(tk.Button(
              upperNotesRH, bg="white", width=2, height=2, state=tk.DISABLED, text=self._notes[k + 4]
            ))
          elif i == 1 and j == 1:
            buttons_note.append(tk.Button(
              middleNotesRH, bg="white", width=2, height=2, state=tk.DISABLED, text=self._notes[k + 4]
            ))
          else:
            buttons_note.append(tk.Button(
              bottomNotesRH, bg="white", width=2, height=2, state=tk.DISABLED, text=self._notes[k + 4]
            ))
        buttons_hand.append(buttons_note)
      self._buttons.append(buttons_hand)
    # -------------------------------------------------------------------------

    # ------------ Pack -------------------------------------------------------
    title_label.pack()
    for i in range(0, len(self._buttons)):
      for j in range(0, len(self._buttons[i])):
        for k in range(0, len(self._buttons[i][j])):
          self._buttons[i][j][k].pack(side=tk.LEFT, padx=10)
    return_button.pack()
    left_hand_title.pack()
    right_hand_title.pack()
    self.pack()

    self.controller.ctrlDomain.initializeAction()
    thread = Thread(target=self.controller.main_node_thread, args=())
    thread.daemon = True #Run along the main
    thread.start() #Resume thread execution
    self.pooling_for_notes()
    # -------------------------------------------------------------------------

  def pooling_for_notes(self):
    print('Pooling for notes!')

    self.change_button_colors()
    self.after(0, self.pooling_for_notes)

  def change_button_colors(self):
    pressed_notes = self.controller.res
    for i in range(0, len(pressed_notes)):
      for j in range(0, len(pressed_notes[i])):
        k = 0
        if j >= 4:
          k = 1

        if pressed_notes [i][j] == 0:
          self._buttons[i][k][j%4].configure(bg="white")
        elif pressed_notes [i][j] == 1:
          self._buttons[i][k][j%4].configure(bg="red")
        elif pressed_notes [i][j] == 2:
          self._buttons[i][k][j%4].configure(bg="cyan")

