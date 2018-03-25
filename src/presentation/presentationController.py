import Tkinter as tk
import mainView
from src.domain.CtrlDomain import CtrlDomain

class PresentationController(tk.Tk):
    def __init__(self):
      tk.Tk.__init__(self)
      tk.Tk.minsize(self, 800, 600)
      tk.Tk.maxsize(self, 800, 600)
      self.container = tk.Frame(self)
      self.container.pack(side="top", fill="both", expand=1)
      self._frame = mainView.MainView(master=self.container, controller=self)
      self.ctrlDomain = CtrlDomain()

    def switch_frame(self, frame_class):
      new_frame = frame_class(master=self.container, controller=self)
      self._frame.destroy()
      self._frame = new_frame

    def main_node_thread(self):
        return self.ctrlDomain.detectPressEvents()

if __name__ == "__main__":
    app = PresentationController()
    app.mainloop()
