import tkinter as tk

#main window
root = tk.Tk()
root.geometry("500x500") #size of the window
root.resizable(False, False) #can't resize it, stuck at fixed size :P
root.title("DiagonalTacToe Game") #thingy that appears top left

welcome_label = tk.Label(root, text = "Welcome to DiagonalTacToe!!!")
welcome_label.pack()


root.mainloop()
