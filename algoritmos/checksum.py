######################################################################################################
# CHECKSUM

def checksum(bits):

    temporal = []
    contador = 0

    for j in range(7, -1, -1):
        for i in range(len(bits)):
            if bits[i][j] == '1':
                contador += 1
        
        if contador == 1:
            temporal.append('1')
        elif contador == 0:
            temporal.append('0')
        elif contador > 1:
            b_list = []
            # Bits sumados beta
            valor = format(contador, "b")
            b_list[:0] = valor
            print(b_list)

            # Conmtinua la suma desde aca
            temporal.append(b_list.pop())

        print('bits: ' + str(contador))
        contador = 0

    # Invierte la suma total para que tenga coherencia
    temporal.reverse()
    print(temporal)
