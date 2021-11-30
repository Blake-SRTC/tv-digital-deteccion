from tkinter import *
from tkinter.font import BOLD
from algoritmos.checksum import *
from algoritmos.noise_1_bits import *

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
    lbl2_bits_codificados = Label(pagina4, text='Checksum: ',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl2_bits_codificados.place(x=100, y=175)

    # Label bits originales
    txt1 = 'Bits: '
    for i in bit_n:
        txt1 = txt1 + i + ' : '
    lbl2_bits_normales['text']=txt1
    
    cs = checksum(bits_p, 2)

    # Label bits condificados
    cs_codificado = [] 
    for i in cs:
        y = "".join(i)        
        cs_codificado.append(y)

    # Label bits condificados
    txt2 = 'Checksum: '
    for i in cs_codificado:
        txt2 = txt2 + i + ' : '
    lbl2_bits_codificados['text']=txt2

    # cs_ruido = noise(cs_codificado, 'cs')
    # checksum_comprobacion(cs_ruido, 3)

    def transmitir():
        # Etapa de ruido
        cs_ruido = noise(cs_codificado, 'cs')
    
        ruido_1 = []
        for i in cs_ruido:
            z = "".join(i)        
            ruido_1.append(z)

        txt3 = 'Transmitidos: '
        for i in ruido_1:
            txt3 = txt3 + i + ' : '
        lbl2_errados['text']=txt3

        # Etapa de comprobacion
        ruido_codificado, validez = checksum_comprobacion(cs_ruido, 3)
        cs_comprobacion = []
        for i in ruido_codificado:
            l = "".join(i)        
            cs_comprobacion.append(l)

        txt3 = 'Recepcion: '
        for i in cs_comprobacion:
            txt3 = txt3 + i + ' : '
        lbl2_comprobado['text']=txt3

        txt4 = 'Comprobacion: '
        for i in validez:
            txt4 = txt4 + i + ' : '
        lbl3_cs_comprobado['text'] = txt4


    # BOTON DE TRANSMITIR
    btn2_transmitir = Button(pagina4, text='Transmitir', font=('Times_New_Roman',17, BOLD), command=transmitir,image=common_img, compound='c', height=50, width=200)
    btn2_transmitir.place(x=500, y=250)
    # Label del Ruido
    lbl2_errados = Label(pagina4, text='Posible trama errada',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl2_errados.place(x=100, y=325)
    # Label Comprobacion LRC
    lbl2_comprobado = Label(pagina4, text='Recepcion',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl2_comprobado.place(x=100, y=400)
    # Label Comprobacion Checksum
    lbl3_cs_comprobado = Label(pagina4, text='Comprobacion',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl3_cs_comprobado.place(x=100, y=500)
