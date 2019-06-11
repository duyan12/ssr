def getRowMap():
	return {} # if your db row "encrypt" means "method", write {"encrypt": "method"}

def getKeys(key_list):
	return key_list + ['plan'] # append the column name 'plan'

def isTurnOn(row):
	return row['plan'] == 'D' or row['plan'] == 'E'