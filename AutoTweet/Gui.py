from Tkinter import *
x=0
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.buttonSelect = Button(frame, 
                         text="Select Tweet From File",
                         command=self.assignValueOne)
    self.buttonSelect.pack()
    self.buttonRandom = Button(frame,
                         text="Generate Random Tweet",
                         command=self.assignValueTwo)
    self.buttonRandom.pack()
    self.buttonPost = Button(frame,
                         text="Post To Twitter",
                         command=self.assignValueThree)
    self.buttonPost.pack()
    self.buttonChange = Button(frame,
                         text="Change Twitter Account",
                         command= self.assignValueFour)
    self.buttonChange.pack()
    self.buttonQuit = Button(frame,
                         text="Exit AutoTweet",
                         command=quit)
    self.buttonQuit.pack()
  def assignValueOne(self):
    global x
    x=1
    print x

  def assignValueTwo(self):
    global x
    x=2
    print x

  def assignValueThree(self):
    global x
    x=3
    print x

  def assignValueFour(self):
    global x
    x=4
    print x

root = Tk()
app = App(root)
root.mainloop()