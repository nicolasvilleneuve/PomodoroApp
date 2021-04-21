from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    REPS = 0
    window.after_cancel(timer)
    timer_label.config(text='Timer', bg=YELLOW, foreground=GREEN)
    background.itemconfig(timer_text, text='00:00')
    checkmark.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        countdown(60 * LONG_BREAK_MIN)
        timer_label.config(text='Long Break', bg=YELLOW, foreground=RED)
    elif REPS % 2 == 0:
        countdown(60 * SHORT_BREAK_MIN)
        timer_label.config(text='Short Break', bg=YELLOW, foreground=PINK)
    else:
        countdown(60 * WORK_MIN)
        timer_label.config(text='Work', bg=YELLOW, foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f'0{secs}'

    background.itemconfig(timer_text, text=f'{mins}:{secs}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            mark += '✔'
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

background = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
background.create_image(100, 112, image=tomato)
timer_text = background.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
background.grid(column=1, row=2)

timer_label = Label(text='Timer', font=(FONT_NAME, 45), bg=YELLOW, foreground=GREEN)
timer_label.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text='Reset', highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark = Label(foreground=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=4)

window.mainloop()
