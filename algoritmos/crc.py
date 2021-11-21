######################################################################################################
# CRC

def crc(polinomio,bits):

    zeros = []
    for i in range(len(polinomio)-1):
        zeros.append('0')
    #print(zeros)

    divisor = []
    for i in bits:        
        divisor.append(i+zeros)
    #print(divisor)

    vacio = []
    for i in range(len(polinomio)):
        vacio.append('0')

    # Ciclos de grupos de bits grandes
    for i in divisor:

        print(i)
        # ciclos de operaciones necesarias
        temporal = []
        temp = []
        for x in range(len(i)-len(zeros)):

            if temporal == []:  
                for j in range(len(polinomio)):
                    temporal.append(i[j])
                # Primer temporal creado
            else:
                # Descartando el bit no util y recorriendo al siguiente
                del temp[0]
                temporal = temp.copy()
                temporal.append(i[x+len(polinomio)-1])

            temp = []
            # Comprobar si usar [0][0] o condicion_1
            if temporal[0] == '1':
                # Armado de temp de resutlados
                for t in range(len(temporal)):
                    if polinomio[t] == temporal[t]:
                        temp.append('0')
                    elif polinomio[t] != temporal[t]:
                        temp.append('1')
            elif temporal[0] == '0':
                # Armado de temp
                for k in range(len(temporal)):
                    if vacio[k] == temporal[k]:
                        temp.append('0')
                    elif vacio[k] != temporal[k]:
                        temp.append('1')

            print('ciclos' + str(x))
            print('temporal')
            print(temporal)
            print('Temp')        
            print(temp)
        