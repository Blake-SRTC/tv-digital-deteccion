from tkinter import *
from tkinter.font import BOLD

from paginas.p1_vrc import *
from paginas.p2_lrc import *
from paginas.p3_crc import *
from paginas.p4_chsu import *

from algoritmos.bits import *

root=Tk()
root.title('Verificacion de Errores')
root.geometry("1200x800")

######################################################################################################
# Resultados 1
def resultados1(entrada):
    global lbl_alfabeto
    global lbl_ascii
    global lbl_binario
    global bits_puros
    global bits_normales

    x, y ,z, q = bits(entrada)
    bits_normales = z
    bits_puros = q

    txt1 = 'Alfabeto : '
    for i in x:
        txt1 = txt1 + i + ' : '
    lbl_alfabeto['text'] = txt1

    txt2 = 'ASCII :    '
    for i in y:
        t = str(i)
        txt2 = txt2 + t + ' : '
    lbl_ascii['text'] = txt2

    txt3 = 'Binario :  '
    for i in z:
        txt3 = txt3 + i + ' : '
    lbl_binario['text'] = txt3

######################################################################################################
# Paginas
def paginas(num):
    # llamar de nuevo al metodo resultados1 arregla un bug de continuidad de los bits originales
    resultados1(entry1)
    if num == '1':
        tab1(root, common_img, bits_normales, bits_puros)
    elif num == '2':
        tab2(root, common_img, bits_normales, bits_puros)
    elif num == '3':
        tab3(root, common_img, bits_normales, bits_puros)
    elif num == '4':
        tab4(root, common_img, bits_normales, bits_puros)
    else:
        print('Algo paso y solo Dios sabe que paso :(')
        
######################################################################################################
# Menu Pirncipal

# Variable global que almacena los bits
bits_normales=[]
# Variable global que almacena los bits desglosados detalladamente
bits_puros=()

# CONFIG BTN Y LBL
common_img = PhotoImage(width=1, height=1)

# TITULO
label1=Label(root,text='Menu Principal', font=('Times_New_Roman',20, BOLD), width=800 , height=50, image=common_img, compound='c')
label1.place(x=200, y=10)

# ENTRADA DE DATOS
entry1 = Entry(root, font=('Times_New_Roman',25))
entry1.place(x=100, y=100, width=1000, height=50)
# BOTON ENVIO DE DATOS
enviar = Button(root, text='Enviar',font=('Times_New_Roman',15, BOLD), image=common_img, compound='c', width=200, height=50, command=lambda: resultados1(entry1))
enviar.place(x=500, y=175)

# ETIQUETAS DE RESULTADO
lbl_alfabeto = Label(root, text='Alfabeto : ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
lbl_alfabeto.place(x=100, y=250)
lbl_ascii = Label(root, text='ASCII :    ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
lbl_ascii.place(x=100, y=325)
lbl_binario = Label(root, text='Binario :  ',font=('Times_New_Roman',15, BOLD), image=common_img, compound='c', height=50)
lbl_binario.place(x=100, y=400)

# BOTONOES DE METODOS
button1=Button(root,text='VRC',font=('Times_New_Roman',15, BOLD), image=common_img, command=lambda: paginas('1'), activebackground='white', padx=1, pady=10, width=150, height=50, compound='c')
button1.place(x=400, y=500)
button2=Button(root,text='LRC',font=('Times_New_Roman',15, BOLD), image=common_img, command=lambda: paginas('2'), activebackground='white', padx=1, pady=10, width=150, height=50, compound='c')
button2.place(x=650, y=500)
button3=Button(root,text='CRC',font=('Times_New_Roman',15, BOLD), image=common_img, command=lambda: paginas('3'), activebackground='white', padx=1, pady=10, width=150, height=50, compound='c')
button3.place(x=400, y=650)
button4=Button(root,text='CHECKSUM',font=('Times_New_Roman',15, BOLD), image=common_img, command=lambda: paginas('4'), activebackground='white', padx=1, pady=10, width=150, height=50, compound='c')
button4.place(x=650, y=650)

root.mainloop()