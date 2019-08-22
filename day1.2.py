import operator

text = './day1.txt'
bas = False
fl = 0
contChar = 0
#iniciamos lectura del archivo
with open(text, 'r') as input_file:
    #recorremos el archivo archivo
    for lines in input_file:
        for char in lines:
            #Validamos el  caracter
            if operator.eq('(',char):
                fl += 1
            elif operator.eq(')',char):
                fl -= 1
            contChar += 1
            if(fl < 0):
                if not bas:
                    bas = True
                    print("Result: basement # " + str(contChar))

input_file.close()