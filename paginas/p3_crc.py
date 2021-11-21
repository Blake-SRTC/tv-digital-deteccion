from tkinter import *
from tkinter.font import BOLD
from algoritmos.polinomio import *
from algoritmos.crc import *
######################################################################################################
# Pagina 3
def tab3(root, common_img, bits_n, bits_p):
    pagina3 = Toplevel(root)
    pagina3.geometry("1200x800")
    pagina3.title('CRC')
    label1=Label(pagina3,text='CRC', font=('Times_New_Roman',20, BOLD), width=800 , height=50, image=common_img, compound='c')
    label1.place(x=200, y=10)

    lbl2_bits_normales = Label(pagina3, text='Bits: ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl2_bits_normales.place(x=100, y=100)

    lbl3_poli = Label(pagina3, text='Polinomio: ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50, width=150)
    lbl3_poli.place(x=100, y=175)
    # ENTRADA DE DATOS
    entry1 = Entry(pagina3, font=('Times_New_Roman',25))
    entry1.place(x=300, y=175, width=400, height=50)
    # BOTON COMPROBAR POLINOMIO
    comprobar = Button(pagina3, text='Comprobar',font=('Times_New_Roman',15, BOLD), image=common_img, compound='c', width=200, height=50, command=lambda: comprobar_polinomio(entry1))
    comprobar.place(x=750, y=175)
    # ESTADO DE LA COMPROBACION
    lbl4_estado = Label(pagina3, text='ESTADO',font=('Times_New_Roman',15, BOLD), image=common_img, compound='c', width=100,height=50, bg='gray', foreground='white')
    lbl4_estado.place(x=1000, y=175)

    lbl5_bits_codificados = Label(pagina3, text='CRC: ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl5_bits_codificados.place(x=100, y=250)

    # Label bits originales
    txt1 = 'Bits: '
    for i in bits_n:
        txt1 = txt1 + i + ' : '
    lbl2_bits_normales['text']=txt1

    def comprobar_polinomio(entrada):
        polinomio = entrada.get()
       
        #a = ["1","0","1","1"]
        # Envio de polinomio a comprobar
        validez_polinomio = polinomio_crc(polinomio)
        if validez_polinomio:
            lbl4_estado['bg']='green'
            lbl4_estado['text']='True'         
            #print(validez_polinomio)
            crc(polinomio,bits_p)
        else:
            lbl4_estado['bg']='red'
            lbl4_estado['text']='False'
            print(validez_polinomio)