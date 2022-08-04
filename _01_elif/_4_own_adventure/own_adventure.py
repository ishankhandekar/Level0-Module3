from email import message
from tkinter import simpledialog, messagebox, Tk
from easygui import *

if __name__ == '__main__':
    # TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story

    window = Tk()
    window.withdraw()
    q1 = choicebox("Your on a roof, do you jump down, or try to get somebody's attention?","Own Adventure",["Jump down","Stay up there and yell loudly"])
    if q1 == "Jump down":
        messagebox.showinfo("Own Adventure","You break your legs and have to get a cast.")
    elif q1 == "Stay up there and yell loudly":
        q2 = choicebox("Somebody hears you and comes quickly. They ask for you to climb down the ladder. Do you do it, or ask for them to call the police because the ladder is unstable.","Own Adventure",["climb down the ladder","ask for them to call the police"])
        if q2 == "climb down the ladder":
            messagebox.showinfo("Own Adventure","You fall on the ladder because it is unstable.")
        elif q2 == "ask for them to call the police":
            messagebox.showinfo("Own Adventure","You get down safely")
            
    pass

