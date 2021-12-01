######################################################################################################
# VRC Devuelve la trama de bits codificada
def vrc(bits_puro):
    #global bits_puros
    bits_cod = list(bits_puro)
    for i in bits_cod:
        if i.count('1')%2 == 0:
            #del i[0]
            i.append('0')
        else:
            #del i[0]
            i.append('1')
    return bits_cod

def comprobacion_vrc(trama_err):
    txt_mensaje = ''
    contador = 0
    for i in range(len(trama_err)):
        for j in range(8):
            if trama_err[i][j] == '1':
                contador = contador + 1
        #print('contador: ' + str(contador))
        if contador%2==0 and trama_err[i][8]=='1':
            #print('Grupo Errado Retransmitir')
            txt_mensaje = txt_mensaje + 'Retransmitir : '
        elif contador%2!=0 and trama_err[i][8]=='0':
            #print('Grupo Errado Retransmitir')
            txt_mensaje = txt_mensaje + 'Retransmitir : '
        else:
            #print('Grupo Aceptado')
            txt_mensaje = txt_mensaje + 'Aceptado : '
        contador = 0

    return txt_mensaje