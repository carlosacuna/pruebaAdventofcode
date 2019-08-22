import re
#obtenemos el archivo
text = './day1.txt'
#iniciamos lectura del archivo
with open(text, 'r') as input_file:
     #recorremos el archivo archivo
    for line in input_file:
        ope_paren = re.findall(r'\(', line)
        close_paren = re.findall(r'\)',line)
        floor = len(ope_paren) - len(close_paren)
        print("Result: floor # " + str(floor))
input_file.close()