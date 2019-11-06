def obtenerMatriz(listaDatos,listaDominio):
    matriz = []
    numero_filas = len(listaDatos)
    numero_columnas = len(listaDatos)+1

    for i in range(numero_filas):
        matriz.append([])
        for j in range(numero_columnas):
            matriz[i].append(None)

    for i in range(numero_filas):
        for j in range(numero_columnas):
            matriz[i][j] = (0,1,1)

    for i in range(numero_filas): #datos iniciales
            matriz[i][0] = listaDominio[i]
            matriz[i][1] = listaDatos[i]


    for i in range(1,numero_filas):
        matriz[i-1][2] = ( (matriz[i][1] - matriz[i-1][1] )/ ( matriz[i][0]-matriz[i-1][0] ),matriz[i][0],matriz[i-1][0] )

    contador = 1
    for j in range(3,numero_columnas):
        #contador+=1
        for i in range(1,numero_filas-contador):
            matriz[i-1][j] = ( (matriz[i][j-1][0]- matriz[i-1][j-1][0])/(matriz[i][j-1][1]-matriz[i-1][j-1][2]) ,matriz[i][j-1][1],matriz[i-1][j-1][2])
        contador += 1

    for h in range(numero_filas):
        matriz[h].pop(0)

    matriz = darFormato(matriz,numero_filas)

#    for i in range (len(listaDatos)):
#        print(matriz[i])

    return matriz

def obtenerPasosCalculo(listaDatos,listaDominio):
    pasos = []
    matriz = []
    numero_filas = len(listaDatos)
    numero_columnas = len(listaDatos)+1

    for i in range(numero_filas):
        matriz.append([])
        for j in range(numero_columnas):
            matriz[i].append(None)

    for i in range(numero_filas):
        for j in range(numero_columnas):
            matriz[i][j] = (0,1,1)

    for i in range(numero_filas): #datos iniciales
            matriz[i][0] = listaDominio[i]
            matriz[i][1] = listaDatos[i]


    for i in range(1,numero_filas): #Calcula las primeras divisiones finitas en la matriz
        matriz[i-1][2] = ( (matriz[i][1] - matriz[i-1][1] )/ ( matriz[i][0]-matriz[i-1][0] ),matriz[i][0],matriz[i-1][0] )
    #    if(i==1):
        paso= "f[X"+str(i-1)+",X"+str(i)+"] = " +"("+ str(matriz[i][1])+" - "+str(matriz[i-1][1])+")/ ("+str(matriz[i][0])+" - "+str(matriz[i-1][0])+") = "+str(matriz[i-1][2][0])
        pasos.append(paso)
    contador = 1
    for j in range(3,numero_columnas):
        for i in range(1,numero_filas-contador):
            paso = agregarXveces(i,j)
    #        paso = "f[X"+str(i-1)+",X"+str(i)+",X"+str(i+1)+"] = "
            matriz[i-1][j] = ( (matriz[i][j-1][0]- matriz[i-1][j-1][0])/(matriz[i][j-1][1]-matriz[i-1][j-1][2]) ,matriz[i][j-1][1],matriz[i-1][j-1][2])
            #if(i==1):
            paso+= "("+str(matriz[i][j-1][0])+" - "+str(matriz[i-1][j-1][0])+")/ ("+str(matriz[i][j-1][1])+" - "+str(matriz[i-1][j-1][2])+") = "+str(matriz[i-1][j][0])
            pasos.append(paso)
        contador += 1


    return pasos

def darFormato(matriz,numero_filas):
    for i in range(numero_filas):
        for c in range(1,numero_filas):
            matriz[i][c] = matriz[i][c][0]
    return matriz

def agregarXveces(nro,orden):
    cadena = "f["
    primero = True
    for j in range(nro-1,nro+orden-1):
        if (primero):
            cadena += "X"+str(j)
            primero = False
        else:
            cadena += ",X"+str(j)
    cadena+="] = "
    return cadena
