*****************************************************************************************
README.TXT
Laia Auset Rizo - TFG 
18/06/2021
Framework implementation of python program: Guide to follow 
*****************************************************************************************

The code is structured in different files to know which program should be executed by each partner. 

IMPORTANT: Entities and Down Catalunya must create a folder named "keys" at the same location where the code downloaded is allocated.

 	1. Down Catalunya: Generate Keys: First, execute generateKeys.py

	2. Entities: Format Files: Executes main.py. 
		- Main.py calls other python files such as formatFile.py, readFile.py, validator.py and FHEpy.py.
		- DadesEntitats.csv belongs to the first Entity. 
		- DadesEntitats2.csv belongs to the second Entity.
		Code should be tested with these two .csv, changing on the formatFile.py the name of the .csv.
		Code generates a dataEnc.pickle file for each entity. 

	3. UPF: Concatenate: concatEncEntitiesFiles.py 
		This program reads all .pickles and concatenates them. It generates 2 outputs (.pickle files). 
		1. First it generates dataOperate.pickle where all entities .pickle files are concatenated (without removing duplicates).
			Output: dataOperate.pickle. It contains all the data from entities concatenated.
		2. Secondly it computes operations with Fully Homomorphic Encryption,
		and then permutes data to prepare the file (operations.pickle) to be sent to Down Catalunya.
			Output: operations.pickle. This file contains ONLY the encrypted results of the operations. 
		NO PERSONAL INFORMATION ABOUT THE ENTITIES IS BEING SENT. 
	
	4.Down Catalunya: Executes positionsToRemove.py
		With the private key, the program decrypts the results received by reading the operations.pickle file and outputs a positionsToRemove.pickle. 
		This file contains the positions where the duplicates are stored. UPF will remove these poitions. 

	5.UPF: removeDuplicates.py, operations.py 
		UPF receives the file where all the duplicates positions are stored and calls a function named dropDuplicates(positionsToRemove),
		which removes the duplicates. Then, it outputs a file named dataFinal.pickle.
		In operations.py, the UPF answers to the proposal questions defined by Down Catalunya. 
		And outputs a file results.txt.  

	6.Down Catalunya: 
		It receives the final file (results.txt) with only answers to the questions. 
	
Program FINISHES 
