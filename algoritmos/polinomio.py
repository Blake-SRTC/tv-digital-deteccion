######################################################################################################
# POLINOMIO CRC
def polinomio_crc(entrada):
    
    # Residuo = 0 
    condicion_1 = ['1','1']
    # Residuo = 1
    condicion_2 = ['1','0']

    cond_1 = condiciones(entrada, condicion_1)
    cond_2 = condiciones(entrada, condicion_2)

    if cond_1 == '0' and cond_2 == '1':
        return True
    else:
        return False
        
def condiciones(polinomio, condicion):
    # Vacio
    vacio = ['0','0']
    temporal = []

    for i in range(len(polinomio)-1):

        # Vida de variables temporal y temp
        if temporal == []:
            temporal.append(polinomio[i])
            temporal.append(polinomio[i+1])
        else:
            del temp[0]
            temporal = temp.copy()
            temporal.append(polinomio[i+1])

        temp = []

        # Comprobar si usar [0][0] o condicion_1
        if temporal[0] == '1':
            # Armado de temp
            for j in range(len(temporal)):
                if condicion[j] == temporal[j]:
                    temp.append('0')
                elif condicion[j] != temporal[j]:
                    temp.append('1')
        elif temporal[0] == '0':
            # Armado de temp
            for j in range(len(temporal)):
                if vacio[j] == temporal[j]:
                    temp.append('0')
                elif vacio[j] != temporal[j]:
                    temp.append('1')

        # print('ciclo: ' + str(i))
        # print('temporal')
        # print(temporal)
        # print('temp')
        # print(temp)
    
    del temp[0]
    return temp[0]
        
