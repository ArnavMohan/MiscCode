
from tkinter import *

class HelloWorldFrame(Frame):
    '''creates a hello world window'''

    def __init__(self,master):
        '''HelloWorldFrame()
        creates a new HelloWorldFrame'''
        Frame.__init__(self,master)  # set up as a Tk frame
        self.grid()  # place the frame in the root window
        # create a button
        self.hwButton = Button(self,text='Click me!',command=self.print_message)
        self.hwButton.grid(row=0,column=0)
        # create a text display
        self.hwMessageBox = Label(self,text="I'm waiting...")
        self.hwMessageBox.grid(row=1,column=0)

    def print_message(self):
        '''prints hello world message'''
        self.hwMessageBox['text'] = 'Hello, World!'

root = Tk()
hwf = HelloWorldFrame(root)
hwf.mainloop()
