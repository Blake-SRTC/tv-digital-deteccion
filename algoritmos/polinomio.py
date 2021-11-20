######################################################################################################
# POLINOMIO CRC

def polinomio_crc(polinomio):
    
    prueba = polinomio.copy()
    # Residuo = 0 
    condicion_1 = ['1','1']
    # Residuo = 1
    condicion_2 = ['1','0']
    # Vacio
    vacio = ['0','0']

    temporal = []
    # temporal.append(prueba[0])
    # temporal.append(prueba[1])
    for i in range(len(prueba)-1):

        if temporal == []:
            temporal.append(prueba[i])
            temporal.append(prueba[i+1])
        else:
            del temp[0]
            temporal = temp.copy()
            temporal.append(prueba[i+1])

        temp = []
        # Comprobar si usar [0][0] o condicion
        if temporal[0] == '1':
            # Armado de temp
            for j in range(len(temporal)):
                if condicion_1[j] == temporal[j]:
                    temp.append('0')
                elif condicion_1[j] != temporal[j]:
                    temp.append('1')
        elif temporal[0] == '0':
            # Armado de temp
            for j in range(len(temporal)):
                if vacio[j] == temporal[j]:
                    temp.append('0')
                elif vacio[j] != temporal[j]:
                    temp.append('1')

        print('temporal')
        print(temporal)
        print('temp')
        print(temp)
        print('ciclo' + str(i))



    # def condicion_1():
    #     print("x+1 = residuo 0")
    
    # def condicion_2():
    #     print("x = residuo 1")
