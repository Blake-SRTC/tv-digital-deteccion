from tkinter import *
######################################################################################################
# Pagina 3
def tab3(root, common_img, bit_n, bits_p):
    pagina1 = Toplevel(root)
    pagina1.geometry("1200x800")
    pagina1.title('CRC')
    label1=Label(pagina1,text='CRC', font=('Times_New_Roman',20), width=800 , height=50, image=common_img, compound='c')
    label1.place(x=200, y=10)