from tkinter import *
import random
import datetime
START_TIME = 0
index = 0
score = 0

# Prepare the word list for test
words_1 = "until stop far most no their even those take their line without call kind his into down look enough my ask use them animal has one change far who its same keep number men give so enough cut to country say walk him more book live by but just say long at own now we thing add her always watch will then not hear then now here family still mother before or animal may read new did she animal start different home very tell make them ask house his run"
word_list_1 = words_1.split()

# words_2 = "must red state follow both follow own leave high sound most between part far fall great second thought life list high would sometimes could if children take have eye life all page day find mother us form letter large new his this think work put which great or say almost still come are cut first after also like little then we a we look long below answer about next did live sometimes after far part both got their any where well tree put take have is us help begin give"
# word_list_2 = words_2.split()


def timer():
    global START_TIME
    if START_TIME == 0:
        START_TIME = datetime.datetime.now()

    elapsed = datetime.datetime.now() - START_TIME
    elapsed = int(str(elapsed).split(".")[0].split(":")[-1])
    countdown = 59 - elapsed
    if countdown > 0:
        timer_label.config(text=f"Time remaining:{str(countdown)} Seconds")
    else:
        timer_label.config(text="Time Up", bg="red")
        entry.config(state="disabled")


def key_pressed(event):
    global index, score
    timer()
    if event.keysym == "space":
        entered_word = entry.get().replace(" ", "")
        if entered_word == word_list_1[index]:
            score += 1
        index += 1
        entry.delete(0, END)
        score_label.config(text=f"You typed {str(score)} words per minute.")
        last_label.config(text=f"Supposed to type:{word_list_1[index-1]},You typed:{entered_word}")

# Make the UI for test
root = Tk()
root.title("Typing-Speed Test")
root.minsize(width=800, height=600)

instruction1_label = Label(root, pady=20, text="Welcome to 1 minute typing speed test. \n Please typewrite the following text. Countdown will start with first keystroke.")
instruction1_label.grid(column=1, row=0)

# Print word list in a label
for n in range(len(word_list_1)):
    words_label = Label(root, pady=10, padx=10, text=words_1, wraplength=600, justify="left", font=("default", 16), bg="white")
    words_label.grid(column=0, row=1, columnspan=2)

# Box to type
entry = Entry(root)
entry.focus()
entry.insert(END, string="")
entry.bind("<Key>", key_pressed)
entry.grid(column=1, row=2)

instruction2_label = Label(root, pady=20, text="Please type in this box ->")
instruction2_label.grid(column=0, row=2)

# Timer
timer_label = Label(root, pady=20, padx=20, text="Time remaining: 60 Seconds")
timer_label.grid(column=3, row=1)

# Score
score_label = Label(root, pady=20, padx=20, text="0")
score_label.grid(column=2, row=3)

# Last Word
last_label = Label(root, pady=20, padx=20, text="Supposed to type: ,You typed:")
last_label.grid(column=1, row=3)

root.mainloop()

