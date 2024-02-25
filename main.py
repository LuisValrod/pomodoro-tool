from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

#Create Label
label = Label()
label.config(text='Timer', font=(FONT_NAME, 35, 'italic'), bg=YELLOW, highlightthickness=0, fg=GREEN)

#Create button 'Start'
start_button = Button()
start_button.config(text='Start', font=(FONT_NAME, 10), fg='Blue', width=5)

# Create button 'Reset
reset_button = Button()
reset_button.config(text='Reset', font=(FONT_NAME, 10), fg='Blue', width=5, bg=YELLOW, highlightthickness=0)

# Create check mark
check = Label()
check.config(text='✔', font=(FONT_NAME, 10), fg=GREEN)

# Positions
label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check.grid(column=1, row=3)








window.mainloop()