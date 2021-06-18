import sys
import FHEpy
import readFile
import formatFile
import numpy as np
import pandas as pd
import pickle

if __name__ == "__main__":    
# 1. formatted File with format validations
# 2. readFile -> read formatted file
# 3. Encrypt data from Excel and export it to another excel
    # Python program showing
# a use of input()

    print("Enter your entity number below.")
    print("1) Down Tarragona")
    print("2) Fundació Cromo suma")
    print("3) Aura Fundació")
    print("4) Associació Lleidatana per a la síndrome de down")
    print("5) Andi Sabadell")
    print("6) Associació familiaamic")
    print("7) Fundació Astrid-21 Girona")
    user_input = input("Number:")

    #1
    if int(user_input) <= 7 and int(user_input) > 0:
        formatFile.formatFile(user_input) #Format data 
    else:
        sys.exit("Incorrect number") 
    
    #2
    df = pd.DataFrame() #Create new DataFrame object 
    id_dni = readFile.readDNIId()
    id_conc = readFile.readConcId()
    gender = readFile.readGender()
    otherDisability = readFile.readOtherDisability()
    sdown = readFile.readSD()
    partners = readFile.readPartner()
    location = readFile.readLocation()
    programs = readFile.readPrograms()
    birth = readFile.readBirth()
    for i in range(len(birth)): 
        age = list(map(str, birth)) 

    #3 
    initObj = FHEpy.restorePublicKey() #Restore public key
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
        } #Create dictionaire. 

    for i in range(len(id_conc)): #Save on the respective columns, each encrypted (or not) data. 
        arrData["ID_DNI"].append(FHEpy.encryption(str(id_dni[i]), initObj))
        arrData["ID-CONC"].append(FHEpy.encryption(str(id_conc[i]), initObj))
        arrData["AGE"].append(str(age[i]))
        arrData["GENDER"].append(str(gender[i]))
        arrData["OD"].append(str(otherDisability[i]))
        arrData["SD"].append(str(sdown[i]))
        arrData["PARTNERS"].append(str(partners[i]))
        arrData["LOCATION"].append(str(location[i]))
        arrData["PROGRAMS"].append(str(programs[i]))

with open("dataEnc2.pickle", 'wb') as output: #Generate .pickle with dictionaire encrypted (or not) data. 
    pickle.dump(arrData, output, -1)
