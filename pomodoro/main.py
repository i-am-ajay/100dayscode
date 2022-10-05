import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reset = False
work_cycle = True
tick = ""


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reset
    reset = True


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_function(time):
    global reset
    global work_cycle
    timer_count = 0
    if time > 0:
        if reset:
            canvas.itemconfig(text, text=f"00:00")
            return
        time = time - 1
        min = time // 60
        sec = time % 60
        canvas.itemconfig(text, text=f"{min:02d}:{sec:02d}")
        window.after(1000,timer_function,time)
    else:
        if work_cycle:
            work_cycle = False
            if timer_count == 4:
                tick = ""
                timer_count = 0
                time = LONG_BREAK_MIN * 60

            else:
                global tick
                tick = tick+"✓\n"
                time = SHORT_BREAK_MIN * 60
            rightLabel.config(text=tick)
        else:
            work_cycle = True
            timer_count += 1
            time = WORK_MIN * 60
        window.after(1000,timer_function,time)

def call_timer_function():
    global reset
    reset = False
    timer_function(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(width=450,height=300,bg=YELLOW, padx=20, pady=20)
# Title
label = tkinter.Label(text="Pomodoro",font=("Arial",22,"bold"),bg=YELLOW,fg=GREEN)
label.grid(row=0, column=1)

# Canvas
canvas = tkinter.Canvas()
canvas.config(width=350,height=250,bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(175,100,image=image)
text = canvas.create_text(175,100,text="00:00",font=("Arial",20,"bold"), fill="White")
canvas.grid(row=1, column=1)

rightLabel = tkinter.Label(text="", font=("Arial", 10, "bold"),fg=GREEN, bg=YELLOW)
rightLabel.grid(row=3,column=1)

# Buttons
startButton = tkinter.Button(text="Start",command=call_timer_function)
startButton.grid(row=3,column=0 )

resetButton = tkinter.Button(text="Reset", command=timer_reset)
resetButton.grid(row=3,column=2)



window.mainloop()