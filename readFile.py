import pandas as pd
import numpy as np

#Read Format data
def readFormatted():
    df = pd.read_csv('formatted.csv', encoding='latin1')
    return df

def readName():
    df = readFormatted()
    arrName = np.array(df['Name'].to_numpy()) #Generates numpy array for this column
    return arrName

def readSurname():
    df = readFormatted()
    arrApellido = np.array(df['Surname'].to_numpy())
    return arrApellido
    
def readDNI():
    df = readFormatted()
    arrDNI = np.array(str(df['DNI']).to_numpy())
    return arrDNI

def readBirth():
    df = readFormatted()
    arrAge = np.array(df['AGE'].to_numpy())
    return arrAge

def readConcId():
    df = readFormatted()
    arrConcId = np.array(df['CONC-ID'].to_numpy())
    return arrConcId

def readDNIId():
    df = readFormatted()
    arrDNIId = np.array(df['DNI-ID'].to_numpy()) 
    return arrDNIId

def readGender():
    df = readFormatted()
    arrGender = np.array(df['Sexe'].to_numpy())
    return arrGender

def readOtherDisability():
    df = readFormatted()
    arrDisability = np.array(df['Altra discapacitat (SI / NO)'].to_numpy())
    return arrDisability

def readSD():
    df = readFormatted()
    arrSD = np.array(df['Síndrome de Down (SI / NO)'].to_numpy())
    return arrSD

def readPartner():
    df = readFormatted()
    arrPartner = np.array(df['Persona socia (SI / NO)'].to_numpy())
    return arrPartner

def readLocation():
    df = readFormatted()
    arrLocation = np.array(df['Ubicacio'].to_numpy())
    return arrLocation

def readPrograms():
    df = readFormatted()
    arrPrograms = np.array(df['Programs'].to_numpy())
    return arrPrograms


