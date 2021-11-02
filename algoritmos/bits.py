######################################################################################################
# Elemento de traduccion de datos
def bits(x):
    entrada = x.get() # Input de caja
    separador=[]
    to_ascii=[]
    to_binari=[]
    bits_p = []
    y=[]

    separador[:0]=entrada  
    for i in separador:
        to_ascii.append(ord(i))

    for i in to_ascii:
        to_binari.append(format(i, "08b"))

    for i in range(len(to_binari)):
        y[:0] = to_binari[i]
        bits_p.append(y)
        y = []
    t_bit_puros = tuple(bits_p)
    return separador, to_ascii, to_binari, t_bit_puros