import tkinter as tk

def quit_program():
    root.destroy() #quit button

def home_frame():
    frame_home_page.pack()

def help_frame():
    #IN ORDER TO SWTICH BETWEEN "PAGES" / FRAMES, YOU FORGET CURRENT PAGE THEN LOAD NEXT PAGE :P
    frame_home_page.pack_forget()
    frame_help_page.pack()

def play_frame():
    frame_home_page.pack_forget()
    frame_play_page.pack()

def back_program_play():
    frame_play_page.pack_forget()
    frame_home_page.pack()

def difficulty_frame(x):
    frame_play_page.pack_forget()
    frame_difficulty_page.pack()
    against_who = x
    print(against_who)

def back_program_diff():
    frame_difficulty_page.pack_forget()
    frame_play_page.pack()




#main window
root = tk.Tk()
root.geometry("500x500") #size of the window
root.resizable(False, False) #can't resize it, stuck at fixed size :P
root.title("DiagonalTacToe Game") #thingy that appears top left

frame_home_page = tk.Frame(root, height=500, width=500)
frame_home_page.pack()

welcome_label = tk.Label(frame_home_page, text = "Welcome to DiagonalTacToe!!!", font = ("Ariel", 20, "bold"))
welcome_label.pack(pady = (20,0))

play_button = tk.Button(frame_home_page, text = "PLAY", font = ("ariel", 20, "bold"), width=8, height=2, background="green", command = play_frame)
htp_button = tk.Button(frame_home_page, text = "HOW TO PLAY", font = ("ariel", 15, "bold"), width = 12, height = 3, background="gray", command = help_frame)
quit_button = tk.Button(frame_home_page, text = "QUIT", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = quit_program)

play_button.pack(pady = (50,50)) #pady is spacing between buttons(up, down)
htp_button.pack(pady = (0,50)) #additional note, padding is only done in packs or grids, not in actual element
quit_button.pack(pady = (0,10))

#above is all beginning screen
#_____________________________________________________________________________________________________________________________________________________________________________________
#below will be help screen

frame_help_page = tk.Frame(root, height = 500, width = 500)

help_label = tk.Label(frame_help_page, text = "HOW TO PLAY", font = ("Ariel", 20, "bold"))
help_label.pack()
help_scrollbar = tk.Scrollbar(frame_help_page, orient = "vertical")
help_scrollbar.pack(padx=(450,0)) #sent fully to the right

htp_text = tk.Label(frame_help_page, text = "Welcome to DiagonalTacToe!! This game is very similar to your regular tictactoe, with a slight twist... the addition of linear algebra :)) \n\n" \
"You will be given an N x N matrix and if your number is 1, then your goal is to make the matrix diagonalizable, while 0's goal is to make sure 1 doesn't succeed and make a defective matrix.", font = ("Ariel", 12), wraplength = 450, justify = "left")
lin_alg_label = tk.Label(frame_help_page, text = "LINEAR ALGEBRA", font = ("Ariel", 15, "bold"))




htp_text.pack()
lin_alg_label.pack(pady = (9))


#above is help screen
#_____________________________________________________________________________________________________________________________________________________________________________________
#below is play screen
frame_play_page = tk.Frame(root, height = 500, width = 500)
against_who = ""
play_label = tk.Label(frame_play_page, text = "PICK GAMEMODE", font = ("Ariel", 20, "bold"))
pvp_button = tk.Button(frame_play_page, text = "P V P", font = ("ariel", 20, "bold"), width=9, height=2, background="light blue", command = lambda: difficulty_frame("pvp"))
pvai_button = tk.Button(frame_play_page, text = "P V AI", font = ("ariel", 20, "bold"), width=9, height=2, background="blue", command = lambda: difficulty_frame("pvai"))
quit_button = tk.Button(frame_play_page, text = "QUIT", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = quit_program)
back_button_play = tk.Button(frame_play_page, text = "BACK", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = back_program_play)


play_label.pack(pady = 15)
pvp_button.pack(pady = 40)
pvai_button.pack()
#note for the two below... if it aint broke dont fix it
quit_button.pack(pady = (70,0), padx = (325,0)) #Gojo button (Saachi's request)
back_button_play.place(x = 0, y = 400)


#above is play screen
#_____________________________________________________________________________________________________________________________________________________________________________________
#below is difficulty screen

frame_difficulty_page = tk.Frame(root, height = 500, width = 500)
frame_difficulty_page.pack_propagate(False) #doesn't let the frame "shrink"
dd = tk.Label(frame_difficulty_page, text = "HI")
quit_button_diff = tk.Button(frame_difficulty_page, text = "QUIT", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = quit_program)
back_button_diff = tk.Button(frame_difficulty_page, text = "BACK", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = back_program_diff)


dd.pack()
back_button_diff.place(x = 10, y = 400)
quit_button_diff.place(x = 340, y = 400)












root.mainloop()
