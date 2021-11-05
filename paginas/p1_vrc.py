from tkinter import *
from tkinter.font import BOLD

from algoritmos.vrc import *
from algoritmos.noise_1_bits import *

#from main import *

######################################################################################################
# Pagina 1
def tab1(root, common_img, bits_normales, bits_desglosados):
    pagina1 = Toplevel(root)
    pagina1.geometry("1200x800")
    pagina1.title('VRC')
    
    
    # TITULO
    label1=Label(pagina1,text='VRC', font=('Times_New_Roman',20), width=1000 , height=50, image=common_img, compound='c')
    label1.place(x=100, y=10)

    lbl_bits_normales = Label(pagina1, text='Bits: ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl_bits_normales.place(x=100, y=100)
    lbl_bits_codificados = Label(pagina1, text='VRC: ',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl_bits_codificados.place(x=100, y=175)

    # Codificacion VRC
    b_separados = list(bits_desglosados)
    vrc_1 = vrc(b_separados)
    print('vrc')
    print(vrc_1)
    
    vrc_codificado = [] 
    for i in vrc_1:
        y = "".join(i)        
        vrc_codificado.append(y)

    # Label bits originales
    txt1 = 'Bits: '
    for i in bits_normales:
        txt1 = txt1 + i + ' : '
    lbl_bits_normales['text']=txt1

    # Label bits condificados
    txt2 = 'VRC: '
    for i in vrc_codificado:
        txt2 = txt2 + i + ' : '
    lbl_bits_codificados['text']=txt2

    # Funcion que envia los datos y posible ruido
    def transmitir():
        # Tramas con posibles errores
        trama_errada = []
        trama_errada = noise(vrc_1,'vrc')
        print('Grupo Transmitido')
        print(trama_errada)
        trama_errada2 = []
        for i in trama_errada:
            y = "".join(i)        
            trama_errada2.append(y)
        # Label bits condificados
        txt3 = 'Transmitidos: '
        for i in trama_errada2:
            txt3 = txt3 + i + ' : '
        lbl_errados['text']=txt3

        # Comprobacion VRC
        comprobado = comprobacion_vrc(trama_errada)
        print(comprobado)
        lbl_comprobado['text']='Comprobacion: ' + comprobado

        print(vrc_1)

    # BOTON DE TRANSMITIR
    btn_transmitir = Button(pagina1, text='Transmitir', font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50, width=200, command=transmitir)
    btn_transmitir.place(x=500, y=250)
    # Label del Ruido
    lbl_errados = Label(pagina1, text='Posible trama errada',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl_errados.place(x=100, y=325)
     # Label Comprobacion VRC
    lbl_comprobado = Label(pagina1, text='Comprobacion',font=('Times_New_Roman',20, BOLD), image=common_img, compound='c', height=50)
    lbl_comprobado.place(x=100, y=400)

    # def cerrar():
    #     print('Desglosados')
    #     print(bits_desglosados)
    #     resultados1()
    #     pagina1.destroy()
    
    # pagina1.protocol('WM_DELETE_WINDOW', cerrar)

    # Revisar como no alterar la variable global de bits desglosados