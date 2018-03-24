import Tkinter as tk
import mainView

class PresentationController(tk.Tk):
    def __init__(self):
      tk.Tk.__init__(self)
      self.container = tk.Frame(self)
      self.container.pack(side="top", fill="both", expand=True)
      self._frame = mainView.MainView(master=self.container, controller=self)
      tk.Tk.minsize(self, 800, 600)
      tk.Tk.maxsize(self, 800, 600)

    def switch_frame(self, frame_class):
      """Destroys current frame and replaces it with a new one."""
      new_frame = frame_class(master=self.container, controller=self)
      self._frame.destroy()
      self._frame = new_frame


if __name__ == "__main__":
    app = PresentationController()
    app.mainloop()
