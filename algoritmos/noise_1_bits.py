######################################################################################################
# Elemento de ruido de 2 bit por trama
import random

def noise(bits_originales, metodo):
    # Meto que Requiere la funcion ruido
    print('Ruido de unico bit')
    if metodo == 'lrc':
        n = 7
        x = 8
    elif metodo == 'vrc':
        #n = 6
        n = 7
        #x = 8
        x = len(bits_originales[0])
    elif metodo == 'crc':
        n = 7
        x = len(bits_originales[0])
    elif metodo == 'cs':
        n = 7
        x = len(bits_originales[0])
    
    # Lista vacia de 0 con la longitud de la trama original
    bits_corrompidos = [['0' for col in range(x)] for row in range(len(bits_originales))]

    # Analisis del ruido
    for i in range(len(bits_originales)):

        # Probabilidad de corromper una trama de 8 bits
        probabilidad = random.randint(0,1)
        print('probabilidad Trama ' + str(i) + ': ' + str(probabilidad))

        # x Longitud constante de 8 bits
        if probabilidad == 0:
            for j in range(x):
                bits_corrompidos[i][j] = bits_originales[i][j]
        else:
            # Bit que sera afectados en la trama afectada
            aleatorio = random.randint(0,n)
            print('aleatorio bit: ' + str(aleatorio))
            
            for j in range(x):
                # Copio la trama de bits al grupo de ceros vacio
                bits_corrompidos[i][j] = bits_originales[i][j]    
                if j == aleatorio:
                    if bits_corrompidos[i][j] == '0':
                        bits_corrompidos[i][j] = '1'
                    else:
                        bits_corrompidos[i][j] = '0'

    return(bits_corrompidos)
