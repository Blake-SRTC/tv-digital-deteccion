######################################################################################################
# CHECKSUM

def checksum(bits):

    temporal = []
    temp = []
    contador = 0
    
    checksum_final = []
    for i in bits:
        checksum_final.append(i)

    tramas = int(len(bits)/2)
    print(bits)
    y = 2
    z = 2
    for x in range(tramas):
        # Accion de conteo por derecha
        for j in range(7, -1, -1):
            # Suma vertical del contador
            for i in range(z-2,z,1):
                if bits[i][j] == '1':
                    contador += 1
            # Reglas de Checksum
            if contador == 1:
                temporal.append('1')
                contador = 0
            elif contador == 0:
                temporal.append('0')
                contador = 0
            elif contador == 2:
                temporal.append('0')
                contador = 1
            elif contador == 3:
                temporal.append('1')
                contador = 1

        # # Acarreo al final 
        # print(j)
        # if j == 0 and contador == 1:
        #     tempo = []
        #     cont = 0
        #     print('Toco')
        #     for t in range(temporal):
        #         if t == '1':
        #             tempo.append('0')
        #             cont += 1
        #         elif t == '0':
        #             tempo.append('1')
        #             cont +=0

        z += 2

        # Invierte la suma total para que tenga coherencia
        temporal.reverse()
        complemento = []
        
        for i in temporal:
            if i == '0':
                complemento.append('1')
            elif i == '1':
                complemento.append('0')
        # Grupo de bits complemento
        checksum_final.insert(x+y,complemento)
        y += 2
        #temp.append(complemento)
        temporal = []

    #print(temp)
    print(checksum_final)

