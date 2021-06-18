import sys
import FHEpy
from Pyfhel import Pyfhel
import pickle


def indexToRemove(id):  #id:{0,1} where 0 is the id (substracted data) and 1 arrNum (positions)
    sk = FHEpy.restorePrivateKey()
    indexremove = []
    for x in range(len(id[0])): #From the substraction results:
        ar = FHEpy.decryption(id[0][x], sk) #Decrypt the substraction results
        sv = FHEpy.sameValue(ar) ##aa-aa = 0 
        if sv == True: #if the result is equal to 0 
            indexremove.append(id[1][x][1]) #Save the index of the decrypted result (if 0) to the indexRemove list.  #aa-aa = 0 is in position 0-3. We save 0-3 position
    return indexremove #Array of positions that we want to remove 
#

if __name__ == "__main__":

    with open('operations.pickle', 'rb') as input:
        finalarr = pickle.load(input)
    
    dniId = []
    concId = []
    
    dniId.append(finalarr["DNIRES"][0])
    dniId.append(finalarr["DNIPOS"][0])
    concId.append(finalarr["CONCRES"][0])
    concId.append(finalarr["CONCPOS"][0])

    indextoremove = indexToRemove(dniId) #listDNI 
    indextoremoveC= indexToRemove(concId) #listConc
    listIndexToRemove = list(dict.fromkeys(indextoremove + indextoremoveC)) #Remove duplicates 
    finalIndexToRemove = sorted(listIndexToRemove) #Sort (just in case)

    with open('positionsToRemove.pickle', 'wb') as output:
        pickle.dump(finalIndexToRemove, output, -1)
    
