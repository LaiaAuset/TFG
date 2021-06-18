import sys
import pandas as pd
import numpy as np
import re
from unicodedata import normalize
import validator
import hashlib  # Se importa hashlib
from datetime import date
from pathlib import Path
PATH = Path(__file__).parent

def toUpperCase(data, df):
    list1 = []
    np_arr = np.array(df[data].to_numpy())
    for i in range(len(np_arr)):
        arr = np.array(df[data][i].upper())
        sur = quitarAcentos(arr.tolist())
        list1.append(sur)
    return list1

def quitarAcentos(surname):
    surname = re.sub(
    	r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
    	normalize( "NFD", surname), 0, re.I
    )
    surname = normalize('NFC', surname)
    return surname

#Read TEST Excel


def formatFile(user_input):
    df = pd.read_csv(PATH/'DadesEntitats2.csv', encoding='latin1')
    df.to_json()
    listaDNI = []
    listaId = []
    ageList = []
    count = 0
    arrSurname = toUpperCase("Cognoms", df)
    arrName = toUpperCase("Nom", df)
    arrProgram = toUpperCase("Programes", df)

    for i in range(len(arrSurname)):
        df["Surname"] = arrSurname
    
    for i in range(len(arrName)):
        df["Name"] = arrName

    for i in range(len(arrProgram)):
        df["Programs"] = arrProgram

    for i in range(len(df["DNI"])):
        if df["Altra discapacitat (SI / NO)"][i] == "SI" and df["Síndrome de Down (SI / NO)"][i] == "SI":
            print("ERROR: Les columnes Síndrome de Down i Altra discapacitat no poden contenir el mateix valor per una mateixa persona.")
            exit()

    for i in range(len(df)):
        if validator.validateDate(str(df["Data de naixement"][i])) == False: #If its not a string, it does not work. If data is not valid, ERROR
            print("ERROR. El formato de la fecha de nacimiento:", df["Data de naixement"][i], "no es correcto correspondiente al usuario:", df["Nom"][i])
            exit()
        else:
            today = date.today() #Date of the local computer/device
            year = today.year
            birth = str(df["Data de naixement"][i]) 
            age = year - int(birth[-4:]) #Substract both years (today - the lasts 4 digits (int) of date variable)
            ageList.append(age) #Save on a list
    df["AGE"] = np.array(ageList) #Create new colum AGE, add values from list when for loop has finished. 

    for i in range(len(df)):
        if validator.validateDNI(df["DNI"][i]) == True: #Validates DNI. If it is OK, then: 
            unique_id = str(df["Data de naixement"][i]) + "-" + df["Surname"][i] + "-" + df["Name"][i] + "-" + df["Sexe"][i] #Concat different values to create a new identifier 
            listaDNI.append(df["DNI"][i]) #Add TRUE dni to listaDNI
            hashedId = hashlib.sha512(unique_id.encode()) #Hash the new identifier
            listaId.append(hashedId.hexdigest()) #Add the hashedIdentifier to the listaId. 
        else:
            df["DNI"][i] = "-1" #If DNI is False, then: 
            count=count+1 
            falseDNI = validator.FalseDNI(count,user_input) 
            unique_id = str(df["Data de naixement"][i]) + "-" + df["Surname"][i] + "-" + df["Name"][i] + "-" + df["Sexe"][i]
            hashedId = hashlib.sha512(unique_id.encode())
            listaDNI.append(falseDNI) #Add False DNI generated to listaDNI
            listaId.append(hashedId.hexdigest())
            
    df["CONC-ID"] = np.array(listaId) #Create new colum for the new ID (concat values)
    df["DNI-ID"] = np.array(listaDNI) #Create new column for the DNIs

    #Sort and Drop duplicates
    sort = df.sort_values(by=['DNI-ID']) 
    drop_duplicates = sort.drop_duplicates(subset=['DNI-ID']) #First drop
    drop_duplicates_Id = drop_duplicates.drop_duplicates(subset=['CONC-ID']) #Second drop from first drop 
    drop_duplicates_Id.to_csv("formatted.csv", encoding='latin1') #Save to Formatted. 

#formatFile()