from tkinter import *
######################################################################################################
# Pagina 4
def tab4(root, common_img):
    pagina1 = Toplevel(root)
    pagina1.geometry("1200x800")
    pagina1.title('CHECKSUM')
    label1=Label(pagina1,text='CHECKSUM', font=('Times_New_Roman',20), width=800 , height=50, image=common_img, compound='c')
    label1.place(x=200, y=10)