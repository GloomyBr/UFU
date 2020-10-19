import pandas as pd
import numpy as np
import mount
import time

FILE = 'input.txt'

table = mount.table()
with pd.ExcelWriter('tabela.xlsx') as writer:  # doctest: +SKIP
    table.to_excel(writer, sheet_name='Sheet_name_1')
    writer.save()
buffer = []
table.to_csv('tabela.csv')
with open(FILE,'r') as file:
    input = file
    for line in file:
        if line != '\n':
            data = line.strip().split(' ')
            for x in data:
                buffer.append(x)

fag = 0
fog = 0
count_rel=0
def check_table(letter,table,word,counter):
    global fag
    global count_rel
    global fog
    

    type_letter = mount.check_type(letter)
    get_row, get_col = mount.check_letter_on_file(letter, word) #Pega linha e coluna de cada token

    # Se nao estiver o token na coluna da tabela ja n é aceito
    if letter in table.columns:
        states = table[table[letter] == 1]
        finals = states['ES'][states['ES'] == 'S'].value_counts()
        not_finals = states['ES'][states['ES'] == 'N'].value_counts()
    else:
        return 0

    #Aceita todos que possuem 1 estado final, letra, relop, operandos e numeros
    if word.endswith(letter) and counter == len(word) and finals['S'] >= 1:
        fag = 0
        fog = 0
        return 1, type_letter,get_row,get_col

        #Verifica e começa e terminal com um relop, entao aceita
    elif type_letter == 'relop' and word.startswith(letter) or fag == 1:
        fag = 1

        if fag == 1 and letter.isdigit() or letter.isalpha():
            fag = 0
            return 0, type_letter,get_row,get_col
        elif type_letter == 'relop':
            return 2, type_letter,get_row,get_col
        else:
            return 0, type_letter,get_row,get_col

    #Rejeita ids que comecao com numeros, aceita digitos
    elif word.startswith(letter) and letter.isnumeric() or fog == 1:
        fog = 1
        if fog == 1 and letter.isnumeric():
            return 2, type_letter,get_row,get_col
        elif fog == 1 and letter.isalpha():
            return 0, type_letter,get_row,get_col

    #Verifica se possui alguma id com relop, operadores, simbolos
    elif type_letter == 'relop' and len(word) > 0 or type_letter == 'operador' and len(word) > 0 or type_letter == 'simbolo' and len(word) > 0:
        return 0, type_letter,get_row,get_col

    #Verifica se possui mais letra na string
    elif counter <= len(word) and not_finals['N'] >= 1:
        # print('Tem mais letra')
        return 2, type_letter,get_row,get_col
    
    #Caso não caia em nenhum desses casos, certamente será um erro
    else:
        return 0, type_letter,get_row,get_col


count = 1
flag = 1

for word in buffer:
    for letter in word:
        result, type_token,get_row,get_col = check_table(letter,table,word,count)
        if not result:
            print('Palavra ' + str(word) + ' nao aceito' + '\n'+'Tipo: ' + str(type_token) + ' errado')
            print('Linha: ' + str(get_row) + ' Coluna: ' + str(get_col))
            print()
            flag = 0 
            break
        elif result == 2:
            print('Token ' + letter +'\n' + 'Tipo: ' + str(type_token) )
            print('Linha: ' + str(get_row) + ' Coluna: ' + str(get_col))
            print()
        else:
            print('Palavra ' + str(word) + ' aceita' + '\n' + 'Tipo: ' + str(type_token))
            print('Linha: ' + str(get_row) + ' Coluna: ' + str(get_col))
            print()

        count+=1
        time.sleep(2)

    count = 1

    if not flag:
        break


