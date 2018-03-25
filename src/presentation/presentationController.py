import Tkinter as tk
import mainView
from src.domain.CtrlDomain import CtrlDomain
import os

class PresentationController(tk.Tk):
    def __init__(self):
      tk.Tk.__init__(self)
      tk.Tk.minsize(self, 800, 600)
      tk.Tk.maxsize(self, 800, 600)
      self.container = tk.Frame(self)
      self.container.pack(side="top", fill="both", expand=1)
      self._frame = mainView.MainView(master=self.container, controller=self)
      self.ctrlDomain = CtrlDomain()
      self.res = None #Shared with the thread

      r, w = os.pipe()

      pid = os.fork()
      if pid:
          print pid
          os.close(w)
          self.r = os.fdopen(r)
      else:
          # This is the child process
          os.close(r)
          """
          os.close(0)
          os.dup2(w, 0)
          """
          os.execlp('/usr/bin/python2.7', '/usr/bin/python2.7', "/home/akuja/akuja_drive/Marc/Hackathons/HackBordeaux'18/UMI/src/domain/CtrlDomain.py")


    def switch_frame(self, frame_class):
      new_frame = frame_class(master=self.container, controller=self)
      self._frame.destroy()
      self._frame = new_frame



if __name__ == "__main__":
    app = PresentationController()
    app.mainloop()
