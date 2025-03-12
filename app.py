# app.py
import tkinter as tk
from gui.chat_interface import ChatInterface

def main():
    root = tk.Tk()
    app = ChatInterface(root)
    root.mainloop()

if __name__ == '__main__':
    main()
