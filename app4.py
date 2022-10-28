from tkinter import *


#----------------------------------------------------
# Widgets

class FrameNome(Frame):
    def __init__(self, meumaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text = 'Nome: ')
        text_nome = Entry(self)
        label_nome.grid(row = 0, column= 0)
        text_nome.grid(row = 0, column=1)

#----------------------------------------------------
# GUI

root = Tk()
root.title('Título')
                        #substitui 'meumaster'
frame_nome1 = FrameNome(root)
frame_nome2 = FrameNome(root)
frame_nome3 = FrameNome(root)


frame_nome1.grid()
frame_nome2.grid()
frame_nome3.grid()



root.mainloop()