from Pyfhel import Pyfhel, PyPtxt, PyCtxt
import numpy as np
import pandas as pd

#Encryption function. 
def encryption(data, HE):
    arr = np.array(list(map(ord,data))) #Inits
    arr2 = np.empty(len(arr),dtype=PyCtxt)
    for i in np.arange(len(arr)): #Encrypts char by char
        arr2[i] = HE.encryptInt(arr[i]) #Pyfhel function 
    return arr2

#Decryption function
def decryption(data, HE2):
    return [HE2.decryptInt(data[i]) for i in np.arange(len(data))]
    #return HE2.decryptInt(data)

def sameValue(arr):
    same = True
    for i in range(len(arr)):
        if arr[i] != 0: 
            same = False
    return same

def saveKeys(HE):
    HE.saveContext("keys/context")
    HE.savepublicKey("keys/pub.key")
    HE.savesecretKey("keys/sec.key")

def restorePublicKey(): #Generates Pyfhel object HE2 and restore context and public keys. 
    HE2 = Pyfhel()
    HE2.restoreContext("keys/context") #From the folder /keys
    HE2.restorepublicKey("keys/pub.key")
    return HE2

def restorePrivateKey():
    HE2 = Pyfhel()
    HE2.restoreContext("keys/context")
    HE2.restorepublicKey("keys/pub.key")
    HE2.restoresecretKey("keys/sec.key")
    return HE2
