from datetime import datetime

def validateDNI(dni_user):
    if dni_user == None or not isinstance(dni_user, str):
        return False
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    nif = dni_user
    result = False
    if (len(nif) == 9):
        letraControl = nif[8].upper()
        dni = nif[:8]
        if (len(dni) == len( [n for n in dni if n in numeros])):
            if tabla[int(dni)%23] == letraControl:
                result=True
    #print("resultado: ", result)
    return result

def validateDate(date_string): #Receives a string
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        #print("Incorrect format date")
        return False


def FalseDNI(count, entity): #Create a FalseDNI. It receives the counter(1,2,...,N), and the value of the entity identifier (X). 
    num = str(count)
    res = 7 - len(num) 
    string_val = "0" * res 
    dni = ''.join((entity,string_val,num,"I")) #"X"00000"1"I
    return dni
    