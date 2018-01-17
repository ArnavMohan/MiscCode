from tkinter import *
import random

class MineCell(Label):
    '''Represents a cell'''

    def __init__(self,master):
        '''MineCell(master) -> MineCell
        creates a new MineCell
        master is the frame'''
        Label.__init__(self,master,width=2,height=1,relief=RAISED,font=('Arial',18))
        #set status attributes
        self.isBomb = False
        self.isExposed = False
        self.isFlagged = False
        #colormap for numbers
        self.colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','gray']
        #set listeners
        self.bind('<Button-1>',self.expose)
        self.bind('<Button-2>',self.flag)
        self.bind('<Button-3>',self.flag)

    # accesors and mutators
    
    def get_exposed(self):
        '''MineCell.get_exposed -> boolean
        returns True if cell is exposed'''
        return self.isExposed

    def get_bomb(self):
        '''MineCell.get_bomb -> boolean
        returns True if cell is a bomb'''
        return self.isBomb

    def get_flagged(self):
        '''MineCell.get_flagged -> boolean
        returns True if cell is flagged'''
        return self.isFlagged

    def set_bomb(self):
        '''MineCell.set_bomb()
        makes cell a bomb'''
        self.isBomb = True

    def set_exposed(self):
        '''MineCell.set_exposed()
        makes cell exposed'''
        self.isExposed = True

    # display changes
    def expose_bomb(self):
        self['relief'] = SUNKEN
        self['text'] = '*'
        self['bg'] = 'red'

    def expose_cell(self,number):
        self.set_exposed()
        self['relief'] = SUNKEN
        self['bg'] = 'gray'
        if number == 0:
            self['text'] = ''
        else:
            self['text'] = str(number)
            self['fg'] = self.colormap[number]
        self.master.increase_exposed()
    
    def expose_value(self,is_gameover):
        '''MineCell.expose_cell(is_gameover)
        exposes cell and sets value to MineFrame.get_bombcount(MineCell)'''
        if not self.get_exposed() and not self.get_flagged():
            
            if self.get_bomb():
                self.expose_bomb()
                if not is_gameover:
                    self.master.end(False)
                    
            elif not is_gameover:
                bombCount = self.master.get_bombcount(self)
                self.expose_cell(bombCount)
                
    def expose(self,event):
        '''MineCell.expose()
        handler for MineCell left click'''
        self.expose_value(False)
        

    def flag(self,event):
        '''MineCell.flag()
        handler for MineCell right click'''
        if not self.get_exposed():
            if self.get_flagged():
                self.master.add_bombcount()
                self['text'] = ''
            else:
                self.master.sub_bombcount()
                self['text'] = '*'
        self.isFlagged = not self.isFlagged

class MineGrid(Frame):
    '''represents the Minesweeper frame'''
    def __init__(self,master,numBombs,length,width):
        # initialize frame
        Frame.__init__(self,master,bg='black')
        self.grid()
        # init game data
        self.height = length
        self.width = width
        self.numBombs = numBombs
        self.numExposed = 0
        #set up bomblabel
        self.bombLabel = Label(self,text=str(numBombs),font=('Arial',20))
        self.bombLabel.grid(row=self.height,column=0,columnspan=self.width)
        #set up cells
        self.cells = {}
        bombs = []
        for row in range(self.height):
            for col in range(self.width):
                self.cells[(row,col)] = MineCell(self)
                self.cells[(row,col)].grid(row=row,column=col)
                bombs.append(self.cells[(row,col)])
        #set up bombs
        for i in range(self.numBombs):
            bomb = random.choice(bombs)
            bomb.set_bomb()
            bombs.remove(bomb)
        

    def add_bombcount(self):
        self.numBombs += 1
        self.bombLabel['text'] = str(self.numBombs)

    def sub_bombcount(self):
        self.numBombs -= 1
        self.bombLabel['text'] = str(self.numBombs)

    def increase_exposed(self):
        self.numExposed += 1
        if self.numExposed == self.height * self.width - self.numBombs:
            self.master.end(True)

    def get_bombcount(self,cell):
        if cell.get_exposed():
            return
        bombcount = 0
        coord = []
        for (x,y) in self.cells.keys():
            if self.cells[(x,y)] == cell:
                coord = [x,y]
        for row in range(coord[0]-1,coord[0]+2):
            for col in range(coord[1]-1,coord[1]+2):
                if row in range(0,self.height) and col in range(self.width) and self.cells[(row,col)].get_bomb():
                    bombcount +=1
        if bombcount == 0:
            cell.set_exposed()
            for row in range(coord[0]-1,coord[0]+2):
                for col in range(coord[1]-1,coord[1]+2):
                    if row in range(0,self.height) and col in range(0,self.width):
                        self.cells[(row,col)].expose_value(False)
        return bombcount

    def end(self,won):
        for cell in self.cells:
            self.cells[cell].unbind('<Button-1>')
            self.cells[cell].unbind('<Button-2>')
            self.cells[cell].unbind('<Button-3>')
        if won:
            messagebox.showinfo('Minesweeper','You Won!',parent=self)
        else:
            messagebox.showerror('Minesweeper','You Lose!',parent=self)
            for coord in self.cells:
                if self.cells[coord].get_bomb():
                    self.cells[coord].expose_value(True)

def play_minesweeper(numBombs, height, width):
    root = Tk()
    root.title('Minesweeper')
    MineGrid(root,numBombs,width,height)
    root.mainloop()
            
play_minesweeper(20,20,20)           

            

