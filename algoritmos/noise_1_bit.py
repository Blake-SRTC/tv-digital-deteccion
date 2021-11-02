######################################################################################################
# Elemento de ruido de 1 bit por trama
import random

def noise(vrc_puro):
    for i in range(len(vrc_puro)):

        probabilidad = random.randint(0,1)
        print('probabilidad Trama ' + str(i) + ': ' + str(probabilidad))
        if probabilidad == 0:
            continue
        else:
            aleatorio = random.randint(0,6)
            print('aleatorio bit: ' + str(aleatorio))
            #print(i)
            for j in range(8):
                #print(j)
                if j == aleatorio:
                    if vrc_puro[i][j] == '0':
                        vrc_puro[i][j] = '1'
                    else:
                        vrc_puro[i][j] = '0'
    return(vrc_puro) 
