import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

import sqlite3

root = Tk()
root.title("Cadastro e consulta de notas")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#A8A8A8")

# ------------ VARIAVEIS --------------
materia = StringVar()
nota1 = StringVar()
nota2 = StringVar()
nota3 = StringVar()
id = None
updateWindow = None
newWindow = None

def database():
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS 'programa' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            materia TEXT, nota1 VARCHAR, nota2 VARCHAR, nota3 VARCHAR) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'programa' ORDER BY materia")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def submitData():
    if materia.get() == "" or nota1.get() == "" or nota2.get() == '' or nota3.get() == '':
        resultado = tk.showwarning("", "Por favor, digite todos os  campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("cadastro.db")
        cursor = conn.cursor()
        query = """INSERT INTO 'programa' (Materia, Nota1, Nota2, Nota3) VALUES (?, ?, ?, ?)"""
        cursor.execute(query, (str(materia.get()), str(nota1.get()), str(nota2.get()), str(nota3.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'programa' ORDER BY materia")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        materia.set("")
        nota1.set("")
        nota2.set("")
        nota3.set("")
        newWindow.destroy()


def updateData():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("cadastro.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE 'programa' SET materia = ?, nota1 = ?, nota2 = ?, nota3 = ?, WHERE id = ?""",
                   (str(materia.get()), str(nota1.get()), str(nota2.get()), str(nota3.get()),
                    int(id)))
    conn.commit()
    cursor.execute("SELECT * FROM 'programa' ORDER BY materia ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    materia.set("")
    nota1.set("")
    nota2.set("")
    nota3.set("")
    updateWindow.destroy()


def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo['values']
    id = selectedItem[0]
    materia.set("")
    nota1.set("")
    nota2.set("")
    nota3.set("")
    materia.set(selectedItem[1])
    nota1.set(selectedItem[2])
    nota2.set(selectedItem[3])
    nota3.set(selectedItem[4])

    # ----------- FRAMES - ATULIZAR ----------------
    updateWindow = Toplevel()
    updateWindow.title("Atualizando materia")
    formTitle = Frame(updateWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(updateWindow)
    formContact.pack(side=TOP, pady=10)
    width = 400
    height = 300
    screen_width = updateWindow.winfo_screenwidth()
    screen_height = updateWindow.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    # ----------- LABELS - ATULIZAR ----------------
    lbl_title = Label(formTitle, text="Atualizando cadastro", font=('arial', 18), bg='#A8A8A8', width=300)
    lbl_title.pack(fill=X)
    lbl_materia = Label(formContact, text='Materia', font=('arial', 12))
    lbl_materia.grid(row=0, sticky=W)
    lbl_nota1 = Label(formContact, text='Nota AV1', font=('arial', 12))
    lbl_nota1.grid(row=1, sticky=W)
    lbl_nota2 = Label(formContact, text='Nota AV2', font=('arial', 12))
    lbl_nota2.grid(row=2, sticky=W)
    lbl_nota3 = Label(formContact, text='Nota AVD', font=('arial', 12))
    lbl_nota3.grid(row=3, sticky=W)

    # ----------- ENTRY - ATULIZAR ----------------
    materiaEntry = Entry(formContact, textvariable=materia, font=('arial', 12))
    materiaEntry.grid(row=0, column=1)
    nota1Entry = Entry(formContact, textvariable=nota1, font=('arial', 12))
    nota1Entry.grid(row=1, column=1)
    nota2Entry = Entry(formContact, textvariable=nota2, font=('arial', 12))
    nota2Entry.grid(row=2, column=1)
    nota3Entry = Entry(formContact, textvariable=nota3, font=('arial', 12))
    nota3Entry.grid(row=3, column=1)

    # ----------- BOTÃO - ATUALIZAR ---------------
    btn_updatecom = Button(formContact, text="Atualizar",
                           width=50, command=updateData)
    btn_updatecom.grid(row=6, columnspan=2, pady=10)


def addData():
    global newWindow
    materia.set("")
    nota1.set("")
    nota2.set("")
    nota3.set("")


    # ----------- FRAMES - INCLUIR ----------------
    newWindow = Toplevel()
    newWindow.title("Incluindo Dados")
    formTitle = Frame(newWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(newWindow)
    formContact.pack(side=TOP, pady=10)
    width = 400
    height = 300
    screen_width = newWindow.winfo_screenwidth()
    screen_height = newWindow.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    # ----------- LABELS - INCLUIR ----------------
    lbl_title = Label(formTitle, text="Incluindo Dados",
                      font=('arial', 18), bg='#A8A8A8', width=300)
    lbl_title.pack(fill=X)
    lbl_materia = Label(formContact, text='Materia', font=('arial', 12))
    lbl_materia.grid(row=0, sticky=W)
    lbl_nota1 = Label(formContact, text='Nota AV1', font=('arial', 12))
    lbl_nota1.grid(row=1, sticky=W)
    lbl_nota2 = Label(formContact, text='Nota AV2', font=('arial', 12))
    lbl_nota2.grid(row=2, sticky=W)
    lbl_nota3 = Label(formContact, text='Nota AVD', font=('arial', 12))
    lbl_nota3.grid(row=3, sticky=W)

    # ----------- ENTRY - INCLUIR ----------------
    materiaEntry = Entry(formContact, textvariable=materia, font=('arial', 12))
    materiaEntry.grid(row=0, column=1)
    nota1Entry = Entry(formContact, textvariable=nota1, font=('arial', 12))
    nota1Entry.grid(row=1, column=1)
    nota2Entry = Entry(formContact, textvariable=nota2, font=('arial', 12))
    nota2Entry.grid(row=2, column=1)
    nota3Entry = Entry(formContact, textvariable=nota3, font=('arial', 12))
    nota3Entry.grid(row=3, column=1)

    # ----------- BOTÃO - INCLUIR ---------------
    btn_includecom = Button(formContact, text="Incluir",
                            width=50, command=submitData)
    btn_includecom.grid(row=6, columnspan=2, pady=10)


# ----------- FRAME PRINCIPAL -----------------

top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg="#A8A8A8")
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=10)
midleftPadding = Frame(mid, width=350, bg="#A8A8A8")
midleftPadding.pack(side=LEFT)
bottom = Frame(root, width=200)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

# ----------- LABEL PRINCIPAL -----------------

lbl_title = Label(top, text="Sistema de cadastro", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

# ----------- BUTTONS PRINCIPAL ----------------

bttn_add = Button(midleft, text="INCLUIR",
                  bg="green2", command=addData)
bttn_add.pack()

# ----------- TABELAS - TREEVIEW ----------------

scrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
scrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Materia", "Nota AV1", "Nota AV2", "Nota AVD"),
                    height=400, selectmode="extended", yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
scrollbarX.config(command=tree.xview)
scrollbarX.pack(side=BOTTOM, fill=X)
scrollbarY.config(command=tree.yview)
scrollbarY.pack(side=RIGHT, fill=Y)

tree.heading("ID", text="ID", anchor=W)
tree.heading("Materia", text="Materia", anchor=W)
tree.heading("Nota AV1", text="Nota AV1", anchor=W)
tree.heading("Nota AV2", text="Nota AV2", anchor=W)
tree.heading("Nota AVD", text="Nota AVD", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.pack()

# ---------- INICIAR -------------
if __name__ == '__main__':
    database()
    root.mainloop()
