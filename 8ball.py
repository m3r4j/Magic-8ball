from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Setup the screen
root = Tk()
root.title('8Ball')
root.configure(bg='white')
root.geometry('300x300')

# Make the screen unresizable
root.resizable(0,0)

# Setup the icon

# All the outcomes
_8ball_cmds = [
'As I see it, yes.',
'Ask again later.',
'Better not tell you now.',
'Cannot predict now.',
'Concentrate and ask again.',
'Don\’t count on it.',
'It is certain.',
'It is decidedly so.',
'Most likely.',
'My reply is no.',
'My sources say no.',
'Outlook not so good.',
'Outlook good.',
'Reply hazy, try again.',
'Signs point to yes.',
'Very doubtful.',
'Without a doubt.',
'Yes.',
'Yes – definitely.',
'You may rely on it.'
]


def choose_random():
    # Choose a random outcome for the ball
    return random.choice(_8ball_cmds)

# When the user clicks the answer button
def click():
    outcome = choose_random()
    messagebox.showinfo('Outcome', outcome)

# Create the ball
ball_img = Image.open('ball.png')
ball_img = ball_img.resize((170,170), Image.ANTIALIAS)
ball_img = ImageTk.PhotoImage(ball_img)

# Display the ball
ball_img_label = Label(image=ball_img)
ball_img_label.pack()


# Make the user ask the question / create the entry:
    # Create the label which asks the user to "enter"
enter_question = Label(root, text='Question: ', font=(None, 20), fg='blue')
enter_question.pack()
    
    # Create the entry
question_entry = Entry(root, width=100, fg='blue', font=(None, 20))
question_entry.pack()

    # Create the button
button_answer = Button(root, text='Answer', command=click, padx=300, bg='black', fg='blue', font=(None,15))
button_answer.pack()


# Run the mainloop
root.mainloop()
