from tkinter import Tk, simpledialog, messagebox
from easygui import *

if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    q1 = choicebox("Are you happy?","Are You Happy",["Yes","No"])
    if q1 == "Yes":
        messagebox.showinfo("Are You Happy","Keep doing whatever your doing.")
    elif q1 == "No":
        q2 = choicebox("Do you want to be happy?","Are You Happy",["Yes","No"])
        if q2 == "Yes":
            messagebox.showinfo("Are You Happy","Change something.")
        elif q2 == "No":
            messagebox.showinfo("Are You Happy","Keep doing whatever your doing.")
    pass
