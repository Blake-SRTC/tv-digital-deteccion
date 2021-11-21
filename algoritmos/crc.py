######################################################################################################
# CRC

def crc(polinomio,bits):

    zeros = []
    for i in range(len(polinomio)-1):
        zeros.append('0')
    print(zeros)

    divisor = []

    for i in bits:        
        divisor.append(i+zeros)
    print(divisor)
    
