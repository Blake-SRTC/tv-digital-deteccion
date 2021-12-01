from tkinter import *
from tkinter.font import BOLD
from algoritmos.polinomio import *
from algoritmos.crc import *
from algoritmos.noise_1_bits import *
######################################################################################################
# Pagina 3

bit_crc = []
polinomio = []

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

    lbl5_bits_codificados = Label(pagina3, text='CRC: ',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl5_bits_codificados.place(x=100, y=250)

    # Label bits originales
    txt1 = 'Bits: '
    for i in bits_n:
        txt1 = txt1 + i + ' : '
    lbl2_bits_normales['text']=txt1

    def comprobar_polinomio(entrada):
        global polinomio
        polinomio = entrada.get()
       
        #a = ["1","0","1","1"]
        # Envio de polinomio a comprobar
        validez_polinomio = polinomio_crc(polinomio)

        if validez_polinomio:
            lbl4_estado['bg']='green'
            lbl4_estado['text']='True'         
            #print(validez_polinomio)

            # Codificacion CRC
            global bit_crc
            bit_crc, colas = crc(polinomio,bits_p)

            # Para representacion grafica
            crc_codificado = []
            txt2 = 'CRC: '
            for i in bit_crc:
                x = "".join(i)
                crc_codificado.append(x)
            print(crc_codificado)

            for i in crc_codificado:
                txt2 = txt2 + i + ' : '
            lbl5_bits_codificados['text'] = txt2

        else:
            lbl4_estado['bg']='red'
            lbl4_estado['text']='False'
            lbl5_bits_codificados['text'] = 'CRC: Fail'
            print(validez_polinomio)

    def transmitir():

        bits_ruido = noise(bit_crc, 'crc')

        # Para representacion grafica
        crc_ruido = []
        txt3 = 'Transmitido: '
        for i in bits_ruido:
            x = "".join(i)
            crc_ruido.append(x)

        for i in crc_ruido:
            txt3 = txt3 + i + ' : '
        lbl2_crc_errados['text'] = txt3

        # Comprobacion CRC
        print('bits comprobados')
        bits_analizados, validez =comprobacion_crc(polinomio,bits_ruido)

        # Para representacion grafica
        crc_analizado = []
        txt4 = 'Comprobado: '
        for i in bits_analizados:
            x = "".join(i)
            crc_analizado.append(x)

        for i in crc_analizado:
            txt4 = txt4 + i + ' : '
        lbl2_crc_comprobado['text'] = txt4
        # Para representacion grafica
        txt5 = 'Comprobado: '
        for i in validez:
            txt5 = txt5 + i + ' : '
        lbl3_crc_comprobado['text'] = txt5

    # BOTON DE TRANSMITIR
    btn_transmitir = Button(pagina3, text='Transmitir', font=('Times_New_Roman',20, BOLD), command=transmitir,image=common_img, compound='c', height=50, width=200)
    btn_transmitir.place(x=500, y=325)
    # Label del Ruido
    lbl2_crc_errados = Label(pagina3, text='Posible trama errada',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl2_crc_errados.place(x=100, y=400)
    # Label Comprobacion CRC
    lbl2_crc_comprobado = Label(pagina3, text='Comprobacion',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl2_crc_comprobado.place(x=100, y=475)
     # Label Comprobacion CRC
    lbl3_crc_comprobado = Label(pagina3, text='Comprobacion',font=('Times_New_Roman',17, BOLD), image=common_img, compound='c', height=50)
    lbl3_crc_comprobado.place(x=100, y=550)

