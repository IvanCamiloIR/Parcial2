#1algoritmo que determine si en un lista no existen elementos repetidos 
#2programa que determine si en una lista se encuentra una cadena de caracteres
#programa que dada dos listas determine que elemento tiene la primera lista que no tenga la segunda.
#algoristo que calcule promedio de un arreglo de reales
#algoritmo que determine la mediana de un arreglo de enteros
def repetidos(lista):
    for i in lista:
        n = lista.count(i)
    if lista.count(i) == 1:
            return "No repite"
    return "Si repite"

def str_in_lista(lista, strr):
    for i in lista: 
        if strr == i:
            return "si"
    return "No"

def diferencias_de_listas(lista1, lista2):
    lista3 = lista1 + lista2
    lista3 = lista1 + lista2
    for i in lista1:
        if 2 > lista3.count(i):
             return print("la segunda lista no tiene este elemento:", i)

def promedio_arreglo(arreglo):
    s = 0
    for i in arreglo:
        s += i
    prom = s/len(arreglo)
    return prom

def mediana(arreglo):
     mediana = len(arreglo)/2
     return mediana