import sys
import pandas as pd
import glob
from itertools import chain
from collections import defaultdict
import pickle
from Pyfhel import Pyfhel
import FHEpy
import numpy as np


if __name__ == "__main__":
    files = glob.glob('*.pickle') #Get all .pickle files from local file
    frames = defaultdict(list) #Init dict
    for i in range(len(files)): #Default function for reading and saving .pickle files. 
        df = pd.read_pickle(files[i]) 
        frames[i].append(df) #Save data in DataFrames list for each .pickle file found. 
    
    #Concatenate data
    dict1 = defaultdict(list) #Init dict
    for i in range(len(frames)): 
        for d in frames[i]:
            for key, value in d.items():
                dict1[key].append(value) #Save in dict1 all the data from frames (.pickle files)
    
    key = FHEpy.restorePublicKey()

    arrData = {
        "ID_DNI": [],
        "ID-CONC": [],
        "AGE": [],
        "GENDER":[],
        "OD":[],
        "SD":[],
        "PARTNERS":[],
        "LOCATION":[],
        "PROGRAMS":[]
    }

    def idDNI(): 
        for i in range(len(dict1["ID_DNI"])-1): #Substract each list from each .pickle to a only list for the variable for all pickle files. 
            i=i+1
            for x in range(len(dict1["ID_DNI"][i])): 
                aux = dict1["ID_DNI"][i][x]
                idDNI = dict1["ID_DNI"][0]
                idDNI.append(aux)
        return idDNI

    def idConc():
        #print(dict1["ID-CONC"])
        for i in range(len(dict1["ID-CONC"])-1):
            i=i+1
            for x in range(len(dict1["ID-CONC"][i])):
                aux = dict1["ID-CONC"][i][x]
                idConc = dict1["ID-CONC"][0]
                idConc.append(aux)
        return idConc    

    def age():
        #print(dict1["AGE"])
        for i in range(len(dict1["AGE"])-1):
            i=i+1
            for x in range(len(dict1["AGE"][i])):
                aux = dict1["AGE"][i][x]
                age = dict1["AGE"][0]
                age.append(aux)
        #print(age)
        return age
    
    def gender():
        #print(dict1["GENDER"])
        for i in range(len(dict1["GENDER"])-1):
            i=i+1
            for x in range(len(dict1["GENDER"][i])):
                aux = dict1["GENDER"][i][x]
                gender = dict1["GENDER"][0]
                gender.append(aux)
        #print("idDNI", gender)
        return gender

    def od():
        #print(dict1["OD"])
        for i in range(len(dict1["OD"])-1):
            i=i+1
            for x in range(len(dict1["OD"][i])):
                aux = dict1["OD"][i][x]
                od = dict1["OD"][0]
                od.append(aux)
        #print("OD", od)
        return od

    def sd():
        #print(dict1["SD"])
        for i in range(len(dict1["SD"])-1):
            i=i+1
            for x in range(len(dict1["SD"][i])):
                aux = dict1["SD"][i][x]
                sd = dict1["SD"][0]
                sd.append(aux)
        #print("SD", sd)
        return sd

    def partners():
        #print(dict1["PARTNERS"])
        for i in range(len(dict1["PARTNERS"])-1):
            i=i+1
            for x in range(len(dict1["PARTNERS"][i])):
                aux = dict1["PARTNERS"][i][x]
                partners = dict1["PARTNERS"][0]
                partners.append(aux)
        #print("PARTNERS", partners)
        return partners

    def location():
        #print(dict1["LOCATION"])
        for i in range(len(dict1["LOCATION"])-1):
            i=i+1
            for x in range(len(dict1["LOCATION"][i])):
                aux = dict1["LOCATION"][i][x]
                location = dict1["LOCATION"][0]
                location.append(aux)
        #print("LOCATION", location)
        return location

    def programs():
        #print(dict1["PROGRAMS"])
        for i in range(len(dict1["PROGRAMS"])-1):
            i=i+1
            for x in range(len(dict1["PROGRAMS"][i])):
                aux = dict1["PROGRAMS"][i][x]
                programs = dict1["PROGRAMS"][0]
                programs.append(aux)
        #print("PROGRAMS", programs)
        return programs         

    #Create final dictionaire columns 
    arrData["ID_DNI"].append(idDNI())
    arrData["ID-CONC"].append(idConc())
    arrData["AGE"].append(age())
    arrData["GENDER"].append(gender())
    arrData["OD"].append(od())
    arrData["SD"].append(sd())
    arrData["PARTNERS"].append(partners())
    arrData["LOCATION"].append(location())
    arrData["PROGRAMS"].append(programs())
  
    #Save in new .pickle file
    with open("dataOperate.pickle", 'wb') as output:
        pickle.dump(arrData, output, -1)

    #For data that needs to be encrypted (ID_DNI, ID-CONC, AGE): Add public key to ciphertext object. 
    for i in range(len(arrData["ID_DNI"][0])): 
        for ctxt in arrData["ID_DNI"][0][i]:
            ctxt._pyfhel = key

    for i in range(len(arrData["ID-CONC"][0])):
        for ctxt in arrData["ID-CONC"][0][i]:
            ctxt._pyfhel = key

    def substractAndPosition(name):
        id = [] #Substraction of all possible combinations between rows
        arrNum = [] #Position 

        for x in range(len(arrData[""+name+""][0])): #
            for i in range(len(arrData[""+name+""][0])):
                while x < i:             
                    if i <= len(arrData[""+name+""][0]):
                        #print(x, i)
                        arrNum.append([x,i])  
                        id.append(arrData[""+name+""][0][x] - arrData[""+name+""][0][i])
                        break
                    i = x+1
        return id, arrNum

    #Get position of a duplicate row 
    dniId, dniPos = substractAndPosition("ID_DNI")
    concId, concPos = substractAndPosition("ID-CONC")
    
    #Permutations
    def permutations(arr):
        permutation = []
        for i in range(len(arr)):
            np.random.shuffle(arr[i])
            permutation.append(arr[i])
        return permutation
    
    dniIdPermuted = permutations(dniId)
    concIdPermuted = permutations(concId)

    finalarr = {
        "DNIRES": [],
        "DNIPOS": [],
        "CONCRES": [],
        "CONCPOS": [],
    }

    finalarr["DNIRES"].append(dniIdPermuted)
    finalarr["DNIPOS"].append(dniPos)
    finalarr["CONCRES"].append(concIdPermuted)
    finalarr["CONCPOS"].append(concPos)
    
    
    #print(finalarr["DNIPOS"][0])
    with open("operations.pickle", 'wb') as output:
        pickle.dump(finalarr, output, -1)

            