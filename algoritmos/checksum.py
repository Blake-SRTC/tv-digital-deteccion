######################################################################################################
# CHECKSUM

def checksum(bits, f):
    
    temporal = []
    temp = []
    contador = 0
    
    checksum_final = []
    for i in bits:
        checksum_final.append(i)

    print(bits)
    y = 2
    z = f
    if f == 2:
        tramas = int(len(bits)/2)
    elif f == 3:
        tramas = int(len(bits)/f)


    for x in range(tramas):
        print(z)
        # Accion de conteo por derecha
        for j in range(7, -1, -1):
            # Suma vertical del contador
            for i in range(z-f,z,1):
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
            # Caso especial en ruido
            elif contador > 3:
                temporal.append('0')

        temporal.reverse()
        extra = []
        # Acarreo al final 
        print(j)
        if j == 0 and contador == 1:
            print('entrante acarreo extra')
            print(temporal)
            cont = 1
            # Accion de conteo por derecha
            for h in range(7, -1, -1):

                # Reglas de acarreo
                if cont == 1 and temporal[h] == '1':
                    extra.append('0')
                    cont = 1
                elif cont == 1 and temporal[h] == '0':
                    extra.append('1')
                    cont = 0
                elif cont == 0 and temporal[h] == '1':
                    extra.append('1')
                elif cont == 0 and temporal[h] == '0':
                    extra.append(temporal[h])
            extra.reverse()
            temporal = extra
        # Fin acarreo final

        # Ubicacion de la trama de checksum
        z += f

        # Invierte la suma total para que tenga coherencia
        #temporal.reverse()
        complemento = []
        
        for i in temporal:
            if i == '0':
                complemento.append('1')
            elif i == '1':
                complemento.append('0')
        # Grupo de bits complemento
        if f == 3:
            checksum_final[x+y] = complemento
        else:
            checksum_final.insert(x+y,complemento)
        y += 2
        #temp.append(complemento)
        temporal = []

    #print(temp)
    print(checksum_final)
    return checksum_final

def checksum_comprobacion(bits_cs, n):
    print('comprobando')
    comprobacion = checksum(bits_cs, n)

