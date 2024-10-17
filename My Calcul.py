# EL BAKALI Ibtissam / AKAYAB Nadir

from sympy import *
import tkinter as tk
from math import *
from numpy import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import quad


root = tk.Tk()  # créer la fenetre principale

root.title('My Calcul')  # définir un titre

field_text = ""  # variable qui va contenir l'expression à calculer par eval
result = ''  # variable qui va contenir le résultat

bol = True
frame = tk.Frame(root, bg='#2A363B', height=440, width=700)
frame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

field_coptext = ""  # variable qui va contenir l'expression affiché a l'ecran


interface_menu = tk.Frame(root, bg='black')  # créer un frame pour le menu

interface_menu.place(x=0, y=40, height=500, width=200)


affichage = {'pi': '\u03C0'}


def supprimer(field):  # supprimer le dernier caractére
    global field_text
    global field_coptext
    field_text = field_text.rstrip(field_text[-1])
    field_coptext = field_coptext.rstrip(field_coptext[-1])

    field.delete("1.0", "end")
    field.insert("1.0", field_coptext)


def clear(field):  # effacer toute l'écran de la calculatrice
    global field_text
    global field_coptext
    field_coptext = ""
    field_text = ""
    field.delete("1.0", "end")


def calculate(field):  # calculer et afficher le résultat
    global result
    global field_text
    global field_coptext
    try:
        result = str(eval(field_text))
        field_text = ""

    except Exception as e:
        result = "Error"
    finally:
        field.delete("1.0", "end")
        field.insert(tk.INSERT, field_coptext+'\n')
        field.insert(tk.INSERT, result)
        field_text = result
        field_coptext = result


numbers = {'7': (2, 1), '8': (2, 2), '9': (2, 3), '4': (3, 1), '5': (3, 2), '6': (
    3, 3), '1': (4, 1), '2': (4, 2), '3': (4, 3),  '0': (5, 2), '.': (5, 1)}


base = {'hexadeci': (5, 1), 'decimale': (5, 2), 'binaire': (
    5, 4), 'octale': (5, 5)}

hexadeci = {'A': (2, 1), 'B': (3, 1), 'C': (
    4, 1), 'D': (2, 5), 'E': (3, 5), 'F': (4, 5)}

numbers_base_op = {'7': (2, 2), '8': (2, 3), '9': (2, 4), '4': (3, 2), '5': (3, 3), '6': (
    3, 4), '1': (4, 2), '2': (4, 3), '3': (4, 4),  '0': (5, 3)}

matrice = {'7': (6, 1), '8': (6, 2), '9': (6, 3), '4': (7, 1), '5': (7, 2), '6': (
    7, 3), '1': (8, 1), '2': (8, 2), '3': (8, 3),  '0': (9, 2), '.': (9, 1)}


def add_to_field(ajouter, field):
    global field_text

    global field_coptext

    field_text += ajouter
    field_coptext += ajouter
    if (ajouter.endswith('sqrt')):
        field_coptext = field_coptext.replace('sqrt', '√')
        field_coptext += "("
        field_text += "("
    elif (ajouter.endswith('gcd')):
        field_coptext = field_coptext.replace('gcd', 'PGCD')
        field_coptext += '('
        field_text += "("

    tup = ("cos", "sin", 'min', 'max', 'radians',
           'degrees', 'round', 'abs', 'factorial',
           'exp', 'tan', 'log10', 'log', 'log2', 'cosh', 'sinh', 'tanh', 'arccos', 'arcsin', 'arctan', 'acosh', 'asinh', 'atanh')

    for operator, symbol in affichage.items():
        field_coptext = field_coptext.replace(operator, f'{symbol}')

    if (ajouter in tup):
        field_coptext += "("
        field_text += '('

    for operator, symbol in operations.items():
        field_coptext = field_coptext.replace(operator, f'{symbol}')

    field_coptext = field_coptext.replace("binaire", '')
    field_coptext = field_coptext.replace("hexadeci", '')
    field_coptext = field_coptext.replace("octale", '')
    field_coptext = field_coptext.replace("decimale", '')
    field.delete("1.0", "end")
    field.insert(tk.INSERT, field_coptext)


def convert(field):  # convertion entre les bases binaire décimale hexadécimale et octale
    global field_text
    global result
    if field_text.startswith("binaire"):
        field_text = field_text.lstrip("binaire")
        if field_text.endswith("decimale"):
            field_text = field_text.rstrip("decimale")
            existe = True
            for x in field_text:
                if x not in ["0", "1"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0B"+field_text
                result = str(eval(field_text))
            else:
                result = "ERROR"

        elif field_text.endswith("octale"):
            field_text = field_text.rstrip("octale")
            existe = True
            for x in field_text:
                if x not in ["0", "1"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0B"+field_text
                result = str(format(eval(field_text), 'o'))
            else:
                result = "ERROR"

        elif field_text.endswith("hexadeci"):
            field_text = field_text.rstrip("hexadeci")

            existe = True
            for x in field_text:
                if x not in ["0", "1"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0B"+field_text
                result = str(format(eval(field_text), 'x'))
                result = result.swapcase()
            else:
                result = "ERROR"

        elif field_text.endswith("binaire"):
            field_text = field_text.strip("binaire")
            result = field_text

        else:
            result = "ERROR"

    elif field_text.startswith("octale"):
        field_text = field_text.lstrip("octale")
        if field_text.endswith("decimale"):

            field_text = field_text.rstrip("decimale")
            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0o"+field_text
                result = str(eval(field_text))
            else:
                result = "ERROR"

        elif field_text.endswith("binaire"):

            field_text = field_text.rstrip("binaire")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0o"+field_text
                result = str(format(eval(field_text), 'b'))
            else:
                result = "ERROR"

        elif field_text.endswith("hexadeci"):

            field_text = field_text.rstrip("hexadeci")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0O"+field_text
                result = str(format(eval(field_text), 'x'))
                result = result.swapcase()
            else:
                result = "ERROR"
        elif field_text.endswith("octale"):
            field_text = field_text.strip("octale")
            result = field_text

        else:
            result = "ERROR"

    elif field_text.startswith("hexadeci"):
        field_text = field_text.lstrip("hexadeci")
        if field_text.endswith("decimale"):

            field_text = field_text.rstrip("decimale")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0X"+field_text
                result = str(eval(field_text))
            else:
                result = "ERROR"

        elif field_text.endswith("binaire"):

            field_text = field_text.rstrip("binaire")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0X"+field_text
                result = str(format(eval(field_text), 'b'))
            else:
                result = "ERROR"

        elif field_text.endswith("octale"):

            field_text = field_text.rstrip("octale")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
                    existe = False
                    break
            if existe == True:
                field_text = "0x"+field_text
                result = str(format(eval(field_text), 'o'))
            else:
                result = "ERROR"

        elif field_text.endswith("hexadeci"):
            field_text = field_text.strip("hexadeci")
            result = field_text

        else:
            result = "ERROR"

    elif field_text.startswith("decimale"):
        field_text = field_text.lstrip("decimale")
        if field_text.endswith("binaire"):

            field_text = field_text.rstrip("binaire")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    existe = False
                    break
            if existe == True:
                result = str(format(eval(field_text), 'b'))
            else:
                result = "ERROR"

        elif field_text.endswith("hexadeci"):

            field_text = field_text.rstrip("hexadeci")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    existe = False
                    break
            if existe == True:
                result = str(format(eval(field_text), 'x'))
                result = result.swapcase()
            else:
                result = "ERROR"

        elif field_text.endswith("octale"):

            field_text = field_text.rstrip("octale")

            existe = True
            for x in field_text:
                if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    existe = False
                    break
            if existe == True:
                result = str(format(eval(field_text), 'o'))
            else:
                result = "ERROR"

        elif field_text.endswith("decimale"):
            field_text = field_text.strip("decimale")
            result = field_text

        else:
            result = "ERROR"

    field.delete("1.0", "end")
    field.insert(tk.INSERT, field_coptext+'\n')
    field.insert(tk.INSERT, result)


# créer les boutons en utilisant les dictionnaires
def create_dictio_buttons(field, dictio, wid):
    global frame

    for c, v in dictio.items():

        btn = tk.Button(frame, text=c, fg="#343434", bg='#f5f5f5',  width=wid, font=(
            "Times New Roman", 14), command=lambda x=c:  add_to_field(x, field))
        if (c == "gcd"):
            btn['text'] = "pgcd"
        elif (c == "pi"):
            btn['text'] = "\u03C0"

        btn.grid(row=v[0], column=v[1])


logique = {' and ': (2, 5), ' or ': (3, 5), ' not ': (
    4, 5), '<': (2, 1), ">": (3, 1), '!': (4, 1), '=': (5, 1), '(': (5, 2), ')': (5, 4), '-': (5, 5), '.': (6, 3)}


fonction = {'factorial': (9, 2), 'e': (9, 3), 'pi': (
    9, 4), 'log': (10, 1), 'log10': (10, 2), 'log2': (10, 3), 'exp': (10, 4),  'abs': (11, 1), 'degrees': (11, 2),  'radians': (11, 3),  'max': (11, 4), 'min': (12, 1),   'gcd': (12, 2), ',': (12, 3)}

fonction_1 = {'cos': (9, 2), 'sin': (9, 3), 'tan': (
    9, 4), 'arccos': (10, 1), 'arcsin': (10, 2), 'arctan': (10, 3), 'cosh': (10, 4), 'sinh': (11, 1), 'tanh': (11, 2), 'acosh': (11, 3), 'asinh': (11, 4), 'atanh': (12, 1),  'round': (12, 2), ',': (12, 3)}


simpleop = {'//': (5, 3), '%': (6, 3), '(': (
    6, 1), ')': (6, 2)}


operations = {"**": "^",  "/": "\u00F7", "*": "\u00D7", "-": "-",
              "+": "+", "sqrt": "√", "\u00F7\u00F7": "//"}


def create_buttons_operations(field):
    i = 2
    global frame
    for operator, symbol in operations.items():
        button = tk.Button(frame, text=symbol, bg="#FF9F0A", width=13,  font=(
            "Times New Roman", 14),
            command=lambda x=operator: add_to_field(x, field))
        button.grid(row=i, column=4)
        i += 1


def create_button(field, l, c, cs, wid, fun, signe):  # créer le bouton égal
    global frame
    button_equal = tk.Button(frame, text=signe, bg="#FF9F0A", width=wid, font=(
        "Times New Roman", 14),
        command=lambda: fun(field))
    button_equal.grid(row=l, column=c, columnspan=cs)


def changer(field, fonction, fonction_1, wid):  # créer le bouton changer
    global bol
    global frame
    if bol == True:
        create_dictio_buttons(field, fonction, wid)
    else:
        create_dictio_buttons(field, fonction_1, wid)
    bol = not bol


def delete_pages():  # suprimer tous les widgets enfants dans un frame
    global frame
    for i in frame.winfo_children():
        i.destroy()


def calsimple_page():

    delete_pages()
    global interface_menu
    interface_menu.place_forget()
    global frame
    field = tk.Text(frame, height=2, width=40, font=(
        "Times New Roman", 20), fg='#f5f5f5', bg="#343434")
    field.grid(row=1, column=1, columnspan=5)

    field.focus()
    root.geometry("540x380")
    create_dictio_buttons(field, numbers, 13)
    create_buttons_operations(field)
    create_dictio_buttons(field, simpleop, 13)
    create_button(field, 8, 1, 4, 55, calculate, "=")
    create_button(field, 7, 1, 2, 27, clear, "clear")
    create_button(field, 7, 3, 1, 13, supprimer, "supp")


def fonction_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()
    global bol
    field = tk.Text(frame, height=2, width=40, font=(
        "Times New Roman", 20), fg='#f5f5f5', bg="#343434")
    field.grid(row=1, column=1, columnspan=5)
    field.focus()

    root.geometry("540x500")
    create_dictio_buttons(field, numbers, 13)
    create_buttons_operations(field)
    create_dictio_buttons(field, simpleop, 13)
    create_button(field, 8, 1, 4, 55, calculate, "=")
    create_button(field, 7, 1, 2, 27, clear, "clear")
    create_dictio_buttons(field, fonction, 13)
    bol = not bol
    changer_btn = tk.Button(frame, text='change',
                            font=('Bold', 15), fg='black', activebackground='#FF9F0A', bg='#FF9F0A', width=12, command=lambda: changer(field, fonction, fonction_1, 13))
    changer_btn.grid(row=9, column=1)
    create_button(field, 7, 3, 1, 13, supprimer, "sup")


def base_page():
    delete_pages()

    global frame
    global interface_menu
    interface_menu.place_forget()

    field = tk.Text(frame, height=2, width=40, font=(
        "Times New Roman", 20), fg='#f5f5f5', bg="#343434")
    field.grid(row=1, column=1, columnspan=5)
    field.focus()
    root.geometry("540x340")
    create_dictio_buttons(field, numbers_base_op, 10)
    create_dictio_buttons(field, hexadeci, 10)
    create_dictio_buttons(field, base, 10)
    create_button(field, 6, 3, 3, 25, supprimer, "sup")
    create_button(field, 6, 1, 2, 20, clear, "clear")
    create_button(field, 7, 1, 5, 35, convert, "=")


def logique_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()
    root.geometry("540x350")

    field = tk.Text(frame, height=2, width=40, font=(
        "Times New Roman", 20), fg='#f5f5f5', bg="#343434")
    field.grid(row=1, column=1, columnspan=5)
    field.focus()

    create_dictio_buttons(field, numbers_base_op, 10)
    create_button(field, 7, 1, 5, 32, calculate, "=")
    create_button(field, 6, 4, 2, 16, clear, "clear")
    create_button(field, 6, 1, 2, 16, supprimer, "sup")
    create_dictio_buttons(field, logique, 10)


def plot():  # tracer les représentations graphiques des équations
    global field_text
    global frame
    x = linspace(-10, 10, 1000)
    y = eval(field_text)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    canvas = FigureCanvasTkAgg(fig, master=frame)

    canvas.get_tk_widget().grid()
    canvas.get_tk_widget().place(x=600, y=0)
    root.geometry("1200x550")


reso = {'(': (8, 3), ')': (8, 4)}

fonction_reso = {'cos': (6, 2), 'sin': (6, 3), 'tan': (
    7, 1), 'x': (7, 2), 'exp': (7, 3), 'arccos': (8, 1), 'arcsin': (8, 2)}
fonction_reso_1 = {'cosh': (6, 2), 'sinh': (6, 3), 'tanh': (
    7, 1), 'x': (7, 2), 'pi': (7, 3), 'log': (8, 1), 'arctan': (8, 2)}

resoudre_trigo = {'arccos': 'acos', 'arcsin': 'asin', 'arctan': 'atan',
                  'arccosh': 'acosh', 'arcsinh': 'asinh', 'arctanh': 'atanh', '√': 'sqrt', "\u00F7": "/", "\u00D7": "*", "\u03C0": "pi"}


def resoudreequa(field):  # résoudre des équations
    global field_text
    global field_coptext

    for operator, symbol in resoudre_trigo.items():
        field_coptext = field_coptext.replace(operator, f'{symbol}')
    x = Symbol('x')
    equation = sympify(field_coptext)
    solutions = str(solve(equation))

    field.delete("1.0", "end")
    field.insert("1.0", solutions)


def resolution_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()
    global bol
    root.geometry("540x410")

    field = tk.Text(frame, height=2, width=40, font=(
        "Times New Roman", 20), fg='#f5f5f5', bg="#343434")
    field.grid(row=1, column=1, columnspan=5)
    field.focus()

    create_buttons_operations(field)
    create_dictio_buttons(field, numbers, 13)
    create_dictio_buttons(field, fonction_reso, 13)
    bol = not bol
    changer_btn = tk.Button(frame, text='change', font=(
        'Times New Roman', 14), fg='black', activebackground='#FF9F0A', bg='#FF9F0A', width=13, command=lambda: changer(field, fonction_reso, fonction_reso_1, 13))
    changer_btn.grid(row=6, column=1)
    create_dictio_buttons(field, reso, 13)
    create_button(field, 9, 3, 1, 13, clear, "clear")
    create_button(field, 5, 3,
                  1, 13, resoudreequa, "resoudre")
    create_button(field, 9, 4, 1, 13, supprimer, "sup")
    plot_button = tk.Button(frame, font=(
        "Times New Roman", 14),
        command=lambda: plot(),
        width=27,
        text="Plot", fg='black', bg='#FF9F0A')
    plot_button.grid(row=9, column=1, columnspan=2)


def createMatrix(entries, rows, columns, fram, frame):  # créer une matrice
    try:

        matrix = array(entries).reshape(rows, columns)
    except:
        for i in frame.winfo_children():
            i.destroy()
        for i in fram.winfo_children():
            i.destroy()
        result = tk.Label(
            fram, bg='#2A363B', font=('Aial', 13), fg='red', text="Entrée des valeurs non valide! ")
        result.grid(row=3, column=0)
    return matrix


def PDP(matrix):  # le PDP d'une matrice
    eVals, eVecs = linalg.eig(matrix)
    invVecs = linalg.inv(eVecs)
    D = diag(eVals)
    D = D.round(5).real
    P = eVecs.round(5).real
    Pinv = invVecs.round(5).real
    return P, D, Pinv


def LU(matrix):  # le Lu d'une matrice

    P, L, U = scipy.linalg.lu(matrix)
    L = L.round(4).real
    U = U.round(4).real
    return P, L, U


def addMat(m1, m2):  # addition de 2 matrices
    m3 = m1 + m2
    return m3


def soustrMat(m1, m2):  # soustraction de 2 matrices
    m3 = m1 - m2
    return m3


def determinat(matrix):  # déterminant d'une matrice
    return linalg.det(matrix)


def inverse(matrix):  # inverse d'une matrice
    return linalg.inv(matrix)


def mul(m1, m2):  # multiplication de deux matrice
    m3 = matmul(m1, m2)
    m3 = m3.round(5).real
    return m3


def QR(matrix):
    q, r = scipy.linalg.qr(matrix)

    q = q.round(4).real
    r = r.round(4).real
    return q, r


def update(Matrix_fram, fram, fram_result):
    global answ
    try:
        for i in fram.winfo_children():
            i.destroy()
        for i in fram_result.winfo_children():
            i.destroy()
        Rows = testRows.get()
        Cols = testCols.get()
        answ = tk.Entry(Matrix_fram, text="")
        answ.grid(column=1, row=2, columnspan=3)
    except:
        for i in fram.winfo_children():
            i.destroy()
        for i in fram_result.winfo_children():
            i.destroy()

        result = tk.Label(
            fram, bg='#2A363B', font=('Aial', 13), fg='red', text="Entrée de lignes et de colonnes non valide! ")
        result.grid(row=3, column=0)


def calculatematrice(selection, Matrix1_frame, Matrix2_frame, Matrix_result_frame):
    global frame
    global answ1

    rows = testRows.get()
    columns = testCols.get()

    read = answ.get()
    try:
        entries = list(map(float, read.split()))
    except:
        for i in Matrix2_frame.winfo_children():
            i.destroy()
        result = tk.Label(
            Matrix2_frame, bg='#2A363B', font=('Aial', 13), fg='red', text="les valeurs doivent etre des nombres ")
        result.grid(row=3, column=0)

    Mat1 = createMatrix(entries, rows, columns,
                        Matrix2_frame, Matrix_result_frame)
    if selection.get() == "PDP Factorization":

        P, D, Pinv = PDP(Mat1)

        for i in Matrix2_frame.winfo_children():
            i.destroy()
        for i in Matrix_result_frame.winfo_children():
            i.destroy()

        result = tk.Label(
            Matrix2_frame, bg='#2A363B', font=('Aial', 13), fg='white', text="Matrice P, Matrice Diagonal D, et matrice P^-1:")
        result.grid(row=0, column=0)
        resultP = tk.Label(Matrix2_frame, bg='#2A363B',
                           font=('Aial', 13), fg='white', text=P)
        resultP.grid(row=1, column=0)
        resultD = tk.Label(Matrix2_frame, bg='#2A363B',
                           font=('Aial', 13), fg='white', text=D)
        resultD.grid(row=1, column=1)
        resultPinv = tk.Label(Matrix2_frame, bg='#2A363B',
                              font=('Aial', 13), fg='white', text=Pinv)
        resultPinv.grid(row=1, column=3)

    elif selection.get() == "Matrix Determinant":
        for i in Matrix2_frame.winfo_children():
            i.destroy()
        for i in Matrix_result_frame.winfo_children():
            i.destroy()
        try:
            det = determinat(Mat1)

            result = tk.Label(
                Matrix2_frame, bg='#2A363B', font=('Aial', 16), fg='white', text="determinant  est :")
            result.grid(row=0, column=0)
            resultDet = tk.Label(Matrix2_frame, bg='#2A363B',
                                 font=('Aial', 16), fg='white', text=det)
            resultDet.grid(row=1, column=0)
        except:
            eror = tk.Label(Matrix2_frame, bg='#2A363B',
                            font=('Aial', 16), fg='red', text="matrice n'est pas carrée")
            eror.grid(row=1, column=0)
    elif selection.get() == "Matrix Inverse":

        for i in Matrix2_frame.winfo_children():
            i.destroy()
        for i in Matrix_result_frame.winfo_children():
            i.destroy()
        try:
            Inv = inverse(Mat1)

            result = tk.Label(
                Matrix2_frame, bg='#2A363B', font=('Aial', 16), fg='white', text=" Inverse Matrice:")
            result.grid(row=0, column=0)
            resultInv = tk.Label(Matrix2_frame, font=(
                'Aial', 16), fg='white', bg='#2A363B', text=Inv)
            resultInv.grid(row=1, column=0)

        except:
            eror = tk.Label(Matrix2_frame, bg='#2A363B',
                            font=('Aial', 16), fg='red', text="matrice n'est pas carrée")
            eror.grid(row=1, column=0)

    elif selection.get() == "LU Factorization":

        P, L, U = LU(Mat1)

        for i in Matrix2_frame.winfo_children():
            i.destroy()
        for i in Matrix_result_frame.winfo_children():
            i.destroy()
        result = tk.Label(Matrix2_frame, font=('Aial', 16), fg='white', bg='#2A363B',
                          text="Matrice P, Matrice L, et matrice U:")
        result.grid(row=0, column=0)
        resultP = tk.Label(Matrix2_frame, bg='#2A363B',
                           font=('Aial', 16), fg='white', text=P)
        resultP.grid(row=1, column=0)
        resultL = tk.Label(Matrix2_frame, bg='#2A363B',
                           font=('Aial', 16), fg='white', text=L)
        resultL.grid(row=1, column=1)
        resultU = tk.Label(Matrix2_frame, bg='#2A363B',
                           font=('Aial', 16), fg='white', text=U)
        resultU.grid(row=1, column=3)
    elif selection.get() == "QR Factorization":

        Q, R = QR(Mat1)
        for i in Matrix2_frame.winfo_children():
            i.destroy()
        for i in Matrix_result_frame.winfo_children():
            i.destroy()

        result = tk.Label(Matrix2_frame, font=('Aial', 16), fg='white', bg='#2A363B',
                          text="matrice orthogonal Q, et R:")
        result.grid(row=0, column=0)
        resultQ = tk.Label(Matrix2_frame, bg='#2A363B',
                           font=('Aial', 16), fg='white', text=Q)
        resultQ.grid(row=1, column=0)
        resultR = tk.Label(Matrix2_frame, bg='#2A363B',
                           font=('Aial', 16), fg='white', text=R)
        resultR.grid(row=1, column=1)
    elif selection.get() == "Matrix Addition" or selection.get() == "Matrix Multiplication" or selection.get() == "Matrix Soustraction":

        for i in Matrix2_frame.winfo_children():
            i.destroy()
        for i in Matrix_result_frame.winfo_children():
            i.destroy()
        Info = tk.Label(Matrix2_frame, font=('Aial', 13), fg='white',
                        bg='#2A363B', text="entrer les valeurs de la deuxiéme matrice séparé d'un espcace: ")
        Info.grid(row=0, column=0)
        answ1 = tk.Entry(Matrix2_frame, text="")
        answ1.grid(column=0, row=2, columnspan=2)

        Done = tk.Button(Matrix2_frame, text="Solve", command=lambda: Solve(
            Mat1, selection, Matrix_result_frame, Matrix2_frame))

        Done.grid(row=3, column=0)

    return


def Solve(Mat1, selection, Matrix_result_frame, Matrix2_frame):
    global frame
    rows = testRows.get()
    columns = testCols.get()

    read = answ1.get()
    try:
        entries1 = list(map(float, read.split()))
    except:
        for i in Matrix2_frame.winfo_children():
            i.destroy()
        result = tk.Label(
            Matrix2_frame, bg='#2A363B', font=('Aial', 13), fg='red', text="les valeurs doivent etre des nombres ")
        result.grid(row=3, column=0)
    Mat3 = createMatrix(entries1, rows, columns,
                        Matrix2_frame, Matrix_result_frame)
    if selection.get() == "Matrix Addition":

        Mat4 = addMat(Mat1, Mat3)

    elif selection.get() == "Matrix Soustraction":

        Mat4 = soustrMat(Mat1, Mat3)

    elif selection.get() == "Matrix Multiplication":

        Mat4 = mul(Mat1, Mat3)
    for i in Matrix_result_frame.winfo_children():
        i.destroy()

    result1 = tk.Label(Matrix_result_frame, fg='white', bg='#2A363B', font=('Aial', 16),
                       text="Matrice 1, Matrice 2, et le résultat: ")

    result1.grid(row=0, column=0)
    result = tk.Label(Matrix_result_frame, bg='#2A363B',
                      font=('Aial', 16), fg='white', text=Mat1)

    result.grid(row=1, column=0)
    result = tk.Label(Matrix_result_frame, bg='#2A363B',
                      font=('Aial', 16), fg='white', text=Mat3)

    result.grid(row=1, column=1)
    result = tk.Label(Matrix_result_frame, bg='#2A363B',
                      fg='white', font=('Aial', 16), text=Mat4)

    result.grid(row=1, column=2)


bouttons_matrice = {'7': (2, 2), '8': (2, 3), '9': (2, 4), '4': (3, 2), '5': (3, 3), '6': (
    3, 4), '1': (4, 2), '2': (4, 3), '3': (4, 4),  '0': (5, 3)}


def matrice_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()
    global testRows
    global testCols
    root.geometry("800x500")
    Matrix1_frame = tk.Frame(frame, bg='#2A363B')

    Matrix2_frame = tk.Frame(frame, bg='#2A363B')
    Matrix_result_frame = tk.Frame(frame, bg='#2A363B')

    Matrix1_frame.pack(pady=0)
    Matrix2_frame.pack(pady=10)
    Matrix_result_frame.pack(pady=20)

    Instructions = tk.Label(
        Matrix1_frame, bg='#2A363B', fg='white', font=('Aial', 10), text="Entrer le nombre des lignes aprés les nombres de colonnes. Ensuite entrer les valeurs des lignes de votre matrice séparé d'un espace: ")
    Instructions.grid(row=0, column=0, columnspan=6)

    testRows = tk.IntVar(Matrix1_frame)
    sizeRows = tk.Entry(Matrix1_frame, width=15, textvariable=testRows)
    sizeRows.grid(column=1, row=1)

    testCols = tk.IntVar(Matrix1_frame)
    sizeRows = tk.Entry(Matrix1_frame, width=15, textvariable=testCols)
    sizeRows.grid(column=3, row=1)

    updatE = tk.Button(Matrix1_frame, text="Entrer valeurs",
                       command=lambda: update(Matrix1_frame, Matrix2_frame, Matrix_result_frame))
    updatE.grid(row=1, column=5)

    Options_List = ["Matrix Multiplication", "Matrix Addition", "PDP Factorization", "LU Factorization",
                    "QR Factorization",
                    "Matrix Soustraction", "Matrix Determinant", "Matrix Inverse"]

    selection = tk.StringVar(Matrix1_frame)
    selection.set(Options_List[0])

    drop_down = tk.OptionMenu(Matrix1_frame, selection, *Options_List)
    drop_down.grid(row=1, column=0)

    calc = tk.Button(Matrix1_frame, text="Solve", command=lambda: calculatematrice(
        selection, Matrix1_frame, Matrix2_frame, Matrix_result_frame))

    calc.grid(row=2, column=0)


def lagrange_polynomial(x_points, y_points):
    x = Symbol('x')
    lagrange_poly = 0
    for i in range(len(x_points)):
        xi = x_points[i]
        yi = y_points[i]
        term = yi
        for j in range(len(x_points)):
            if i == j:
                continue
            xj = x_points[j]
            yj = y_points[j]
            term *= (x - xj) / (xi - xj)
        lagrange_poly += term

    return simplify(lagrange_poly)


def calcul_polynome(image, pts, frame2):  # Vérifiez que les entrées x et y sont valides
    data = pts.get()
    mesures = image.get()
    try:
        x = list(map(float, data.split()))
        y = list(map(float, mesures.split()))
    except ValueError:
        for i in frame2.winfo_children():
            i.destroy()
        result = tk.Label(frame2, bg='#2A363B', font=(
            'Arial', 16), fg='red', text="Entrée de données non valide.")
        result.grid(row=0, column=0)
        return  # Vérifiez que x et y ont la même longueur
    if len(x) != len(y):
        for i in frame2.winfo_children():
            i.destroy()
        result = tk.Label(frame2, bg='#2A363B', font=(
            'Arial', 16), fg='red', text="Les entrées x et y doivent avoir la même longueur.")
        result.grid(row=0, column=0)
        return  # Calculez le polynôme d'interpolation

    p = str(lagrange_polynomial(x, y))
    p = p.replace('**', '^')

    p = p.replace('*', '')
    for i in frame2.winfo_children():
        i.destroy()
    result = tk.Label(frame2, bg='#2A363B', font=('Arial', 16),
                      fg='white', text="Le polynôme d'interpolation est :")
    result.grid(row=0, column=0)
    resultP = tk.Label(frame2, font=('Arial', 16),
                       fg='white', bg='#2A363B', text=p)
    resultP.grid(row=1, column=0)


def interpolation():
    delete_pages()

    global frame
    global interface_menu
    interface_menu.place_forget()
    root.geometry("800x500")
    frame1 = tk.Frame(frame, bg='#2A363B')

    frame2 = tk.Frame(frame, bg='#2A363B')

    frame1.pack(pady=0)
    frame2.pack(pady=30)
    Instruction1 = tk.Label(
        frame1, bg='#2A363B', fg='white', font=('Aial', 13), text="Entrer les points d'interpolations séparé d'un espace aprés entrer leurs images  : ")
    Instruction1.grid(row=1, column=0, columnspan=4)
    pts = tk.StringVar(frame1)
    pts_size = tk.Entry(frame1, width=15, textvariable=pts)
    pts_size.grid(column=2, row=2)

    image = tk.StringVar(frame1)
    images = tk.Entry(frame1, width=15, textvariable=image)
    images.grid(column=4, row=2)

    calc = tk.Button(frame1, text="Solve",
                     command=lambda: calcul_polynome(image, pts, frame2))

    calc.grid(row=4, column=3)


def calcul_integral(interval, f, frame3):
    x = Symbol('x')
    bornes = interval.get()

    try:
        function = lambdify(x, parse_expr(f.get()))
    except SyntaxError:
        for i in frame3.winfo_children():
            i.destroy()
        result = tk.Label(frame3, bg='#2A363B', font=(
            'Arial', 16), fg='red', text="Entrée de données non valide.")
        result.grid(row=0, column=0)
        return
    try:
        l = list(map(float, bornes.split()))
    except ValueError:
        for i in frame3.winfo_children():
            i.destroy()
        result = tk.Label(frame3, bg='#2A363B', font=(
            'Arial', 16), fg='red', text="Entrée de données non valide.")
        result.grid(row=0, column=0)
        return
    if len(l) != 2:
        for i in frame3.winfo_children():
            i.destroy()
        result = tk.Label(frame3, bg='#2A363B', font=(
            'Arial', 16), fg='red', text="vous devez entrer deux chiffres.")
        result.grid(row=0, column=0)
        return
    resultI, error = quad(function, l[0], l[1])
    for i in frame3.winfo_children():
        i.destroy()
    result = tk.Label(frame3, bg='#2A363B', font=(
        'Arial', 16), fg='white', text="Le résultat  est :")
    result.grid(row=0, column=0)
    resultP = tk.Label(frame3, font=('Arial', 16),
                       fg='white', bg='#2A363B', text=resultI)
    resultP.grid(row=1, column=0)


def integration():
    delete_pages()

    global frame
    global interface_menu
    interface_menu.place_forget()
    root.geometry("800x500")
    frame1 = tk.Frame(frame, bg='#2A363B')

    frame2 = tk.Frame(frame, bg='#2A363B')
    frame3 = tk.Frame(frame, bg='#2A363B')

    frame1.pack(pady=0)
    frame2.pack(pady=50)
    frame3.pack(pady=70)

    Instruction1 = tk.Label(
        frame1, bg='#2A363B', fg='#FF9F0A', font=('Aial', 12), text="Guide d'utilisation : ")
    Instruction1.grid(row=0, column=0)
    Instruction1 = tk.Label(
        frame1, bg='#2A363B', fg='white', font=('Aial', 12), text=" multiplication : *       valeur absolue: abs()       racine : sqrt()")
    Instruction1.grid(row=1, column=0)

    Instruction2 = tk.Label(
        frame1, bg='#2A363B', fg='white', font=('Aial', 12), text=" exposant : **      division: /       expononciel : exp()")
    Instruction2.grid(row=2, column=0)

    Instruction3 = tk.Label(
        frame1, bg='#2A363B', fg='white', font=('Aial', 12), text=" logarithme : log()      variable: x       fonction tigonométrique : cos()")
    Instruction3.grid(row=3, column=0)

    Instruction1 = tk.Label(
        frame2, bg='#2A363B', fg='white', font=('Aial', 12), text="Entrer les bornes de l'intervalle a et b séparé d'un espace  : ")
    Instruction1.grid(row=0, column=0)  # , columnspan=4)
    bornes = tk.StringVar(frame2)
    bornes_size = tk.Entry(frame2, width=15, textvariable=bornes)
    bornes_size.grid(column=2, row=1)

    Instruction2 = tk.Label(
        frame2, bg='#2A363B', fg='white', font=('Aial', 12), text="   Entrer la fonction  : ")
    Instruction2.grid(row=0, column=4)  # , columnspan=4)

    f = tk.StringVar(frame2)
    function = tk.Entry(frame2, width=15, textvariable=f)
    function.grid(column=5, row=1)

    calc = tk.Button(frame2, text="Solve",
                     command=lambda: calcul_integral(bornes, f, frame3))

    calc.grid(row=5, column=4)  # , columnspan =3)


calsimple_page()


def menu_selection():
    global interface_menu
    interface_menu.place(x=0, y=10, height=600, width=200)
    calsimple_btn = tk.Button(interface_menu, text='Cal. Simple',
                              font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda: calsimple_page())
    calsimple_btn.place(x=10, y=40)
    fonction_btn = tk.Button(interface_menu, text='Fonctions',
                             font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda: fonction_page())
    fonction_btn.place(x=10, y=70)
    base_btn = tk.Button(interface_menu, text='Bases',
                         font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda:  base_page())
    base_btn.place(x=10, y=100)
    logique_btn = tk.Button(interface_menu, text='Opé. Logique',
                            font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda:  logique_page())
    logique_btn.place(x=10, y=130)
    resolution_btn = tk.Button(interface_menu, text='Resolution',
                               font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda: resolution_page())
    resolution_btn.place(x=10, y=160)
    matrice_btn = tk.Button(interface_menu, text='Matrices',
                            font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda:     matrice_page())
    matrice_btn.place(x=10, y=190)
    interpolation_btn = tk.Button(interface_menu, text='interpolation',
                                  font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda:    interpolation())
    interpolation_btn.place(x=10, y=220)
    integration_btn = tk.Button(interface_menu, text='integration',
                                font=('Bold', 15), fg='#FF9F0A', bg='black', bd=0, command=lambda:    integration())
    integration_btn.place(x=10, y=250)


head_frame = tk.Frame(root, bg='BLACK', highlightbackground='white')

menu_btn = tk.Button(head_frame, text='☰', bg='BLACK',
                     fg='white', command=menu_selection)
title_btn_menu = tk.Label(head_frame, text='Menu', bg='BLACK', fg='white')
menu_btn.pack(side=tk.LEFT)
title_btn_menu.pack(side=tk.LEFT)
head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)


root.mainloop()
