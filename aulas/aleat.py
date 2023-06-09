from tkinter import *

app = Tk()
app.title('Cilab Cursos')
app.geometry('600x600')
app.configure(background='#008')

txt1 = Label(app, text='Curso de Python', 
           background='#008', 
           foreground='#fff')
txt1.place(x=10, y=10, width=150, height=30)


vtxt = 'Módulo bibliotecas!'
vbg = '#fff'
vfg = '#000'
txt2 = Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, 
          side='top', fill=X, expand=True)

app.mainloop()