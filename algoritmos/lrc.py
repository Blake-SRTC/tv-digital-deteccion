######################################################################################################
# LRC Devuelve la trama de bits codificada
def lrc(bits_originales):
    contador = 0
    bloque_lrc = []
    for j in range(8):
        #print('columna ' + str(j))
        for i in range(len(bits_originales)):
            #print(bits_originales[i][j])
            if bits_originales[i][j] == '1':
                contador += 1
        if contador%2 == 0:
            bloque_lrc.append('0')
        else:
            bloque_lrc.append('1')
        contador = 0

    return bloque_lrc

def comprobacion_lrc(t_origen, t_ruido):
    mensaje = ''
    print('lrc test')
    print(t_origen)
    print(t_ruido)
    if t_origen == t_ruido:
        mensaje = 'Bloque Aceptado'
    else:
        mensaje = 'Bloque Rechazado'
    print(mensaje)
    return mensaje