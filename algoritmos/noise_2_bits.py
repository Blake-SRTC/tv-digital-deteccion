######################################################################################################
# Elemento de ruido de 2 bit por trama
import random

def noise(bits_originales):
    bits_corrompidos = [['0' for col in range(8)] for row in range(len(bits_originales))]

    for i in range(len(bits_originales)):

        probabilidad = random.randint(0,1)
        print('probabilidad Trama ' + str(i) + ': ' + str(probabilidad))
        if probabilidad == 0:
            for j in range(8):
                bits_corrompidos[i][j] = bits_originales[i][j]
        else:
            aleatorio = random.randint(0,7)
            print('aleatorio bit: ' + str(aleatorio))
            
            for j in range(8):
                bits_corrompidos[i][j] = bits_originales[i][j]    
                if j == aleatorio:
                    if bits_corrompidos[i][j] == '0':
                        bits_corrompidos[i][j] = '1'
                    else:
                        bits_corrompidos[i][j] = '0'

    return(bits_corrompidos)
