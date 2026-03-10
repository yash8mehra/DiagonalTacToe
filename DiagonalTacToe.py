import tkinter as tk

def quit_program():
    root.destroy()

def home_frame():
    frame_home_page.pack()

def help_frame():
    frame_home_page.pack_forget()
    frame_help_page.pack()


#main window
root = tk.Tk()
root.geometry("500x500") #size of the window
root.resizable(False, False) #can't resize it, stuck at fixed size :P
root.title("DiagonalTacToe Game") #thingy that appears top left

frame_home_page = tk.Frame(root, height=500, width=500)
frame_home_page.pack()

welcome_label = tk.Label(frame_home_page, text = "Welcome to DiagonalTacToe!!!", font = ("Ariel", 20, "bold"))
welcome_label.pack(pady = (20,0))

play_button = tk.Button(frame_home_page, text = "PLAY", font = ("ariel", 20, "bold"), width=8, height=2, background="green")
htp_button = tk.Button(frame_home_page, text = "HOW TO PLAY", font = ("ariel", 15, "bold"), width = 12, height = 3, background="gray", command = help_frame)
quit_button = tk.Button(frame_home_page, text = "QUIT", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = quit_program)

play_button.pack(pady = (50,50)) #pady is spacing between buttons(up, down)
htp_button.pack(pady = (0,50))
quit_button.pack(pady = (0,10))

#above is all beginning screen
#below will be help screen

frame_help_page = tk.Frame(root, height = 500, width = 500)

test_label = tk.Label(frame_help_page, text = "HOW TO PLAY", font = ("Ariel", 20, "bold"))
test_label.pack()





root.mainloop()
