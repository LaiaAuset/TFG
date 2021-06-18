import pickle
from Pyfhel import Pyfhel

def popValues(indexremove, arrFinal):   #Remove entire row of the duplicated index 
    arrFinal["ID_DNI"][0].pop(indexremove)
    arrFinal["ID-CONC"][0].pop(indexremove)
    arrFinal["AGE"][0].pop(indexremove)
    arrFinal["GENDER"][0].pop(indexremove)
    arrFinal["OD"][0].pop(indexremove)
    arrFinal["SD"][0].pop(indexremove)
    arrFinal["PARTNERS"][0].pop(indexremove)
    arrFinal["LOCATION"][0].pop(indexremove)
    arrFinal["PROGRAMS"][0].pop(indexremove)

def dropDuplicates(index): #Recorre el listIndexToRemove sin duplicades 
    for i in range(len(index)):
        popValues(index[i]-i, arrFinal) #Posiciones que queremos eliminar (excel de tst) 3, 6 y 5. Como faltara una row (index), para eliminar el siguiente habra que ajustar el lenght array a -1

if __name__ == "__main__":
    
    with open('dataOperate.pickle', 'rb') as input: #Open final .pickle file
        arrData = pickle.load(input)

    arrFinal = arrData

    with open('positionsToRemove.pickle', 'rb') as input:
        finalIndexToRemove = pickle.load(input)

    dropDuplicates(finalIndexToRemove) #

    with open("dataFinal.pickle", 'wb') as output:
        pickle.dump(arrFinal, output, -1)
