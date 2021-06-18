import sys
import pickle
import numpy as np
import pandas as pd
import FHEpy
from Pyfhel import Pyfhel

with open('dataFinal.pickle', 'rb') as input:
    arrData = pickle.load(input)

key = FHEpy.restorePublicKey()
#sk = FHEpy.restorePrivateKey()

for i in range(len(arrData["ID_DNI"][0])):
    for ctxt in arrData["ID_DNI"][0][i]:
        ctxt._pyfhel = key

for i in range(len(arrData["ID-CONC"][0])):
    for ctxt in arrData["ID-CONC"][0][i]:
        ctxt._pyfhel = key


sys.stdout = open("results.txt", "w")

print("0. Total persones", len(arrData["ID_DNI"][0]))
print("===========================================")
numpplD = 0
for i in range(len(arrData["ID_DNI"][0])):
    if arrData["OD"][0][i] == "SI" or arrData["SD"][0][i] == "SI":
        numpplD = numpplD +1
print("1. Amb quanta gent amb discapacitat intelectual treballem?", numpplD)

print("===========================================")
numpplOD = 0
for i in range(len(arrData["ID_DNI"][0])):
    if arrData["OD"][0][i] == "NO" and arrData["SD"][0][i] == "NO":
        numpplOD = numpplOD +1
print("2. Amb quantes persones sense discapacitat intelectual treballem?", numpplOD)

print("===========================================")

numpplPOD = 0
for i in range(len(arrData["ID_DNI"][0])):
    if arrData["PARTNERS"][0][i] == "SI" and (arrData["OD"][0][i] == "SI" or arrData["SD"][0][i] == "SI"):
        numpplPOD= numpplPOD +1

print("3. De les persones amb discapacitat intel·lectual amb les que treballem, quantes són sòcies d’alguna entitat?", numpplPOD)
print("===========================================")

numpplPNOD = 0
for i in range(len(arrData["ID_DNI"][0])):
    if arrData["PARTNERS"][0][i] == "SI" and arrData["OD"][0][i] == "NO" and arrData["SD"][0][i] == "NO":
        numpplPNOD= numpplPNOD +1

print("4. De les persones sense discapacitat intel·lectual amb les que treballem, quantes són sòcies d’alguna entitat?", numpplPNOD)
print("===========================================")
print("5. Quantes persones de cada edat participen a alguna entitat sòcia?")
numpplAGE = 0
age = []
text =''
age2 = []
age10 = 0
age20 = 0
age30 = 0
age40 = 0
age50 = 0
age60 = 0
age70 = 0

for i in range(len(arrData["AGE"][0])):
    if int(arrData["AGE"][0][i]) >= 10 and int(arrData["AGE"][0][i]) <= 19:
        age10 = age10+1
    elif int(arrData["AGE"][0][i]) >= 20 and int(arrData["AGE"][0][i]) <= 29:
        age20 = age20+1
    elif int(arrData["AGE"][0][i]) >= 30 and int(arrData["AGE"][0][i]) <= 39:
        age30 = age30+1
    elif int(arrData["AGE"][0][i]) >= 40 and int(arrData["AGE"][0][i]) <= 49:
        age40 = age40+1
    elif int(arrData["AGE"][0][i]) >= 50 and int(arrData["AGE"][0][i]) <= 59:
        age50 = age50+1
    elif int(arrData["AGE"][0][i]) >= 60 and int(arrData["AGE"][0][i]) <= 69:
        age60 = age60+1
    elif int(arrData["AGE"][0][i]) >= 70 and int(arrData["AGE"][0][i]) <= 80:
        age70 = age70+1

print("Rang de 10 a 19 anys:", age10)
print("Rang de 20 a 29 anys:", age20)
print("Rang de 30 a 39 anys:", age30)
print("Rang de 40 a 49 anys:", age40)
print("Rang de 50 a 59 anys:", age50)
print("Rang de 60 a 69 anys:", age60)
print("Rang de 70 a 80 anys:", age70)

print("===========================================")
numMale = 0
numFemale = 0
for i in range(len(arrData["ID_DNI"][0])):
    if arrData["GENDER"][0][i] == "M":
        numMale= numMale +1
    elif arrData["GENDER"][0][i] == "F":
        numFemale= numFemale +1

print("6. Quin és el nombre d’homes i de dones que participen a alguna entitat sòcia?")
print("Hombres:", numMale)
print("Mujeres:", numFemale)

print("===========================================")
print("7. Quanta gent participa a cada programa?")
programs = []
programs.append(list(dict.fromkeys(arrData["PROGRAMS"][0])))

for i in range(len(programs[0])):
    prog = 0
    for x in range(len(arrData["PROGRAMS"][0])):
        if programs[0][i] == arrData["PROGRAMS"][0][x]:
            prog = prog +1
    print("Al programa", programs[0][i], "hi han", prog, "persones.")

print("===========================================")
numpplESD = 0
for i in range(len(arrData["ID_DNI"][0])):
    if arrData["SD"][0][i] == "SI":
        numpplESD= numpplESD +1

print("8. Quin és el nombre total de persones que participen a alguna entitat sòcia amb Síndrome de Down?", numpplESD)
print("===========================================")
numpplEOD = 0
for i in range(len(arrData["ID_DNI"][0])):
    if arrData["OD"][0][i] == "SI":
        numpplEOD= numpplEOD +1

print("9. Quin és el nombre total de persones que participen a alguna entitat sòcia amb altra discapacitat intel·lectual (diferent a SD)?", numpplEOD)
print("===========================================")
print("10. Quin és el nombre total de persones que participen a alguna entitat sòcia per província de residència?")
city = []
city.append(list(dict.fromkeys(arrData["LOCATION"][0])))

for i in range(len(city[0])):
    cit = 0
    for x in range(len(arrData["LOCATION"][0])):
        if city[0][i] == arrData["LOCATION"][0][x]:
            cit = cit +1
    print("A la provincia", city[0][i], "hi ha", cit, "participants.")

sys.stdout.close()
