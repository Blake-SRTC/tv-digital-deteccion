from tkinter import *
from tkinter.font import BOLD
from algoritmos.checksum import *

######################################################################################################
# Pagina 4
def tab4(root, common_img, bit_n, bits_p):
    pagina4 = Toplevel(root)
    pagina4.geometry("1200x800")
    pagina4.title('CHECKSUM')
    label1=Label(pagina4,text='CHECKSUM', font=('Times_New_Roman',20), width=800 , height=50, image=common_img, compound='c')
    label1.place(x=200, y=10)

    lbl2_bits_normales = Label(pagina4, text='Bits: ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl2_bits_normales.place(x=100, y=100)
    lbl2_bits_codificados = Label(pagina4, text='CS: ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl2_bits_codificados.place(x=100, y=175)

    # Label bits originales
    txt1 = 'Bits: '
    for i in bit_n:
        txt1 = txt1 + i + ' : '
    lbl2_bits_normales['text']=txt1

    
    b = [['1','1','0','1','1','0','1','0'], ['1','0','0','0','1','0','1','0']]
    c = [['1','1','0','1','1','0','1','0'], ['1','0','0','0','1','0','1','0'], ['1','0','0','1','1','0','1','0']]
    
    cs = checksum(bits_p, 2)

    # Label bits condificados
    cs_codificado = [] 
    for i in cs:
        y = "".join(i)        
        cs_codificado.append(y)

    # Label bits condificados
    txt2 = 'CS: '
    for i in cs_codificado:
        txt2 = txt2 + i + ' : '
    lbl2_bits_codificados['text']=txt2

    checksum_comprobacion(cs, 3)

