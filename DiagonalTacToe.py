import tkinter as tk

def quit_program():
    root.destroy() #quit button

def home_frame():
    frame_home_page.pack()

def help_frame():
    #IN ORDER TO SWTICH BETWEEN "PAGES" / FRAMES, YOU FORGET CURRENT PAGE THEN LOAD NEXT PAGE :P
    frame_home_page.pack_forget()
    frame_help_page.pack()

def back_program_help():
    frame_help_page.pack_forget()
    frame_home_page.pack()

def play_frame():
    frame_home_page.pack_forget()
    frame_play_page.pack()

def back_program_play():
    frame_play_page.pack_forget()
    frame_home_page.pack()

def difficulty_frame():
    frame_play_page.pack_forget()
    frame_difficulty_page.pack()

def back_program_diff():
    frame_difficulty_page.pack_forget()
    frame_play_page.pack()

def game_frame():
    frame_difficulty_page.pack_forget()
    frame_game_screen.pack()




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

frame_help_page = tk.Frame(root, height=500, width=500)
frame_help_page.pack_propagate(False)  # keep fixed size like difficulty page

help_label = tk.Label(frame_help_page, text="HOW TO PLAY", font=("Ariel", 20, "bold"))
help_label.pack(pady=(10, 0))

# Scrollable text area using Text widget and Scrollbar 
text_frame = tk.Frame(frame_help_page, width=460, height=340)
text_frame.pack(pady=(5, 0))
text_frame.pack_propagate(False)

help_scrollbar = tk.Scrollbar(text_frame, orient="vertical", relief = "flat")
help_scrollbar.pack(side="right", fill="y")

help_text_box = tk.Text(
    text_frame,
    font=("Ariel", 12),
    wrap="word", #allows it to end lines at words instead of letters
    yscrollcommand=help_scrollbar.set, #without this scrollbar is tiny ahh
    relief="flat", #pushes it back
    bg=root.cget("bg"),  # match window background so it looks like a label 
    cursor = "arrow", #mouse looks normal or else it looks editable
    width=52,
    height=18
)
help_text_box.pack(side="left", fill="both", expand=True)
help_scrollbar.config(command=help_text_box.yview)


                    #end means "insert at the end of the current text"
help_text_box.insert("end", "Welcome to DiagonalTacToe!! This game is very similar to your regular tictactoe, ""with a slight twist... the addition of linear algebra :))\n\n""You will be given an N x N matrix and if your number is 1, then your goal is to make "
                     "the matrix diagonalizable, while 0's goal is to make sure 1 doesn't succeed and make ""a defective matrix.\n\n")

help_text_box.insert("end", "LINEAR ALGEBRA\n", ("bold_header",))
help_text_box.tag_config("bold_header", font=("Ariel", 15, "bold"))

help_text_box.insert("end","A matrix is diagonalizable if it has enough linearly independent eigenvectors to form a full eigenbasis. ""In simpler terms, if an N x N matrix has N distinct eigenvalues, it is always diagonalizable!\n\n"
    "An eigenvalue is a special number λ such that: A·v = λ·v\n""where A is your matrix and v is a non-zero eigenvector.\n\n""A defective matrix does NOT have enough eigenvectors, it cannot be diagonalized.\n\n"
)

help_text_box.insert("end", "EXAMPLE WITH A 2x2 MATRIX\n", ("bold_header",))
help_text_box.insert("end", "Suppose you have a matrix that looks like this (identity matrix):\n\n1  0\n0  1\n\nto calculate if it is diagonalizable, first you start by subtracting λ from the diagonal values\n\n1-λ 0\n0 1-λ\n\n" \
"then find the determinant of this matrix using either ad-bc or cofactor expansion and solve for λ.\nSo for this we would get:\n\n(1-λ) * (1-λ)\n1-2λ-λ^2\nλ = 1 with multiplicity of 2\n\nNow we plug it back into the formula (A-λI)x = 0" \
" to get\n\n0 0\n0 0\n\nGiving us the system:\n\n0x1 + 0x2 = 0\n0x1 + 0x2 = 0\n\nMaking both x1 and x2 free variables, giving two linearly independant eigenvectors. Since the algebraic and geometric multiplicity is the same, this matrix is diagonalizable\n\n")

help_text_box.insert("end", "HOW TO WIN\n", ("bold_header",))
help_text_box.insert("end", "Player 1 (ones): Fill in 1s to try to create a diagonalizable matrix.\n""Player 0 (zeros): Fill in 0s to block Player 1 and make the matrix defective.\n\n""Players alternate turns placing their number into any empty cell of the matrix. "
    "Once the matrix is full, the game checks if it is diagonalizable.\n\n"
    "Good luck, and hope you win! :)\n"
)

help_text_box.config(state="disabled")  #make it read only

back_button_help = tk.Button(frame_help_page, text="BACK", font=("ariel", 20, "bold"), width=8, height=2, background="red", command = back_program_help)
quit_button_help = tk.Button(frame_help_page, text="QUIT", font=("ariel", 20, "bold"), width=8, height=2, background="red", command = quit_program)

back_button_help.place(x=10, y=400)
quit_button_help.place(x=340, y=400)

#above is help screen
#_____________________________________________________________________________________________________________________________________________________________________________________
#below is play screen
frame_play_page = tk.Frame(root, height = 500, width = 500)
#lambda instead of regular so it doesn't run instantly but still sends string 
play_label = tk.Label(frame_play_page, text = "PICK GAMEMODE", font = ("Ariel", 20, "bold"))
pvp_button = tk.Button(frame_play_page, text = "P V P", font = ("ariel", 20, "bold"), width=9, height=2, background="light blue", command = difficulty_frame)
pvai_button = tk.Button(frame_play_page, text = "P V AI", font = ("ariel", 20, "bold"), width=9, height=2, background="blue", command = difficulty_frame)
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
#creating the images for the buttons
two_by_two_img = tk.PhotoImage(file = "tbt.png")
three_by_three_img = tk.PhotoImage(file = "thbth.png")
four_by_four_img = tk.PhotoImage(file = "fbf.png")
five_by_five_img = tk.PhotoImage(file = "fibfi.png")

                                            #x, y
three_by_three_img = three_by_three_img.subsample(2,2)
four_by_four_img = four_by_four_img.subsample(2,2)
five_by_five_img = five_by_five_img.subsample(2,2)

pyd_label = tk.Label(frame_difficulty_page, text = "PICK YOUR DIFFICULTY", font = ("ariel", 20, "bold"))

quit_button_diff = tk.Button(frame_difficulty_page, text = "QUIT", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = quit_program)
back_button_diff = tk.Button(frame_difficulty_page, text = "BACK", font = ("ariel", 20, "bold"), width=8, height = 2, background="red", command = back_program_diff)

two_by_two_button = tk.Button(frame_difficulty_page, image = two_by_two_img, width = 150, height = 115, command = game_frame)
three_by_three_button = tk.Button(frame_difficulty_page, image = three_by_three_img, width = 150, height = 115, command = game_frame)
four_by_four_button = tk.Button(frame_difficulty_page, image = four_by_four_img, width = 150, height = 115, command = game_frame)
five_by_five_button = tk.Button(frame_difficulty_page, image = five_by_five_img, width = 150, height = 115, command = game_frame)


pyd_label.pack(pady = 15)
back_button_diff.place(x = 10, y = 400)
quit_button_diff.place(x = 340, y = 400)

two_by_two_button.place(x = 50, y = 75)
three_by_three_button.place(x = 300, y = 75)
four_by_four_button.place(x = 50, y = 245)
five_by_five_button.place(x = 300, y = 245)






#above is difficulty screen
#_____________________________________________________________________________________________________________________________________________________________________________________
#below is actual game screen

frame_game_screen = tk.Frame(root, height = 500, width = 500)



root.mainloop()
