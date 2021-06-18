from Pyfhel import Pyfhel, PyPtxt, PyCtxt

#Mother entity will execute. Public keys and context will be sent to sister entities. Secret key will be kept private. 

def initialize(): 
    HE = Pyfhel()
    HE.contextGen(p=12289, m=1024, base=3, flagBatching=True)   # Generating context. --> p not prime or p-1 not multiple 2*m
    # The values of p and m are chosen to enable batching 
    HE.keyGen()
    saveKeys(HE)

def saveKeys(HE):
    HE.saveContext("keys/context")
    HE.savepublicKey("keys/pub.key")
    HE.savesecretKey("keys/sec.key")

if __name__ == "__main__":
    initialize()
