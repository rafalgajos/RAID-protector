from tkinter import Tk
from gui.raid_gui import RAIDMonitorApp


if __name__ == "__main__":
    root = Tk()  # Create the main window
    app = RAIDMonitorApp(root)  # Instantiate the RAIDMonitorApp
    root.mainloop()  # Run the Tkinter main loop to start the application

