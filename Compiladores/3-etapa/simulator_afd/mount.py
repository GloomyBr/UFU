import pandas as pd
import numpy as np
import time

def table():
    tabela = pd.DataFrame(columns = ['ES','0','1','2','3','4','5','6','7','8','9',
                                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z',
                                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','(',')','[',']',
                                '/','*',';','.','"',"'",'+','-','<','>','='],
                      index = np.arange(93))
                      
    tabela['ES'][0] = 'S'
    tabela['ES'][1] = 'S'
    tabela['ES'][4] = 'S'
    tabela['ES'][13] = 'S'
    tabela['ES'][12] = 'S'
    tabela['ES'][2] = 'N'
    tabela['ES'][3] = 'N'
    tabela['ES'][5] = 'N'
    tabela['ES'][6] = 'N'
    tabela['ES'][7] = 'N'
    tabela['ES'][8] = 'N'
    tabela['ES'][9] = 'N'
    tabela['ES'][10] = 'N'
    tabela['ES'][11] = 'N'
    tabela['ES'][14] = 'N'
    tabela['ES'][15] = 'N'
    tabela['ES'][16] = 'N'
    tabela['ES'][21] = 'N'
    tabela['ES'][23] = 'N'
    tabela['ES'][27] = 'N'
    tabela['ES'][28] = 'N'
    tabela['ES'][29] = 'N'
    tabela['ES'][30] = 'N'
    tabela['ES'][31] = 'N'
    tabela['ES'][32] = 'N'
    tabela['ES'][33] = 'N'
    tabela['ES'][36] = 'N'
    tabela['ES'][39] = 'N'
    tabela['ES'][40] = 'N'
    tabela['ES'][42] = 'N'
    tabela['ES'][43] = 'N'
    tabela['ES'][44] = 'N'
    tabela['ES'][45] = 'N'
    tabela['ES'][49] = 'N'
    tabela['ES'][55] = 'N'
    tabela['ES'][51] = 'N'
    tabela['ES'][52] = 'N'
    tabela['ES'][53] = 'N'
    tabela['ES'][54] = 'N'
    tabela['ES'][56] = 'N'
    tabela['ES'][58] = 'N'
    tabela['ES'][60] = 'N'
    tabela['ES'][61] = 'N'
    tabela['ES'][62] = 'N'
    tabela['ES'][64] = 'N'
    tabela['ES'][66] = 'N'
    tabela['ES'][67] = 'N'
    tabela['ES'][68] = 'N'
    tabela['ES'][69] = 'N'
    tabela['ES'][72] = 'N'
    tabela['ES'][73] = 'N'
    tabela['ES'][74] = 'N'
    tabela['ES'][77] = 'N'
    tabela['ES'][78] = 'N'
    tabela['ES'][81] = 'N'
    tabela['ES'][82] = 'N'
    tabela['ES'][83] = 'N'
    tabela['ES'][84] = 'N'
    tabela['ES'][85] = 'N'
    tabela['ES'][86] = 'N'
    tabela['ES'][89] = 'N'
    tabela['ES'][90] = 'N'
    tabela['ES'][17] = 'N'
    tabela['ES'][41] = 'N'
    tabela['ES'][18] = 'S'
    tabela['ES'][19] = 'S'
    tabela['ES'][20] = 'S'
    tabela['ES'][24] = 'S'
    tabela['ES'][26] = 'S'
    tabela['ES'][25] = 'S'
    tabela['ES'][22] = 'S'
    tabela['ES'][35] = 'S'
    tabela['ES'][34] = 'S'
    tabela['ES'][37] = 'S'
    tabela['ES'][38] = 'S'
    tabela['ES'][46] = 'S'
    tabela['ES'][47] = 'S'
    tabela['ES'][48] = 'S'
    tabela['ES'][50] = 'S'
    tabela['ES'][57] = 'S'
    tabela['ES'][59] = 'S'
    tabela['ES'][65] = 'S'
    tabela['ES'][63] = 'S'
    tabela['ES'][70] = 'S'
    tabela['ES'][71] = 'S'
    tabela['ES'][75] = 'S'
    tabela['ES'][76] = 'S'
    tabela['ES'][79] = 'S'
    tabela['ES'][80] = 'S'
    tabela['ES'][87] = 'S'
    tabela['ES'][88] = 'S'

    tabela['*'][4] = 1    
    tabela['['][1] = 1    
    tabela[']'][18] = 1    
    tabela['/'][4] = 1    
    tabela['+'][4] = 1    
    tabela['.'][4] = 1    
    tabela[';'][20] = 1    
    tabela['('][24] = 1    
    tabela[')'][26] = 1    
    tabela["'"][25] = 1  
    tabela['s'][10] = 1       
    tabela['e'][35] = 1       
    tabela['>'][22] = 1       
    tabela['<'][13] = 1       
    tabela['='][37] = 1  
    tabela['>'][38] = 1  
    tabela['='][16] = 1  
    tabela['-'][12] = 1  
    tabela['"'][19] = 1  
    tabela['o'][9] = 1  
    tabela['r'][34] = 1  
    tabela['p'][23] = 1  
    tabela['a'][44] = 1  
    tabela['r'][60] = 1  
    tabela['a'][71] = 1  
    tabela['r'][45] = 1  
    tabela['o'][61] = 1  
    tabela['g'][72] = 1  
    tabela['r'][78] = 1  
    tabela['a'][82] = 1  
    tabela['m'][85] = 1  
    tabela['a'][88] = 1  
    tabela['a'][2] = 1  
    tabela['n'][27] = 1  
    tabela['d'][46] = 1  
    tabela['c'][7] = 1  
    tabela['h'][32] = 1  
    tabela['a'][52] = 1  
    tabela['r'][65] = 1  
    tabela['f'][21] = 1  
    tabela['i'][43] = 1  
    tabela['m'][59] = 1  
    tabela['a'][42] = 1  
    tabela['c'][58] = 1  
    tabela['a'][70] = 1  
    tabela['i'][6] = 1  
    tabela['n'][31] = 1  
    tabela['t'][50] = 1  
    tabela['n'][51] = 1  
    tabela['c'][64] = 1  
    tabela['i'][73] = 1  
    tabela['o'][79] = 1  
    tabela['n'][3] = 1  
    tabela['o'][29] = 1  
    tabela['t'][48] = 1  
    tabela['e'][15] = 1  
    tabela['n'][40] = 1  
    tabela['t'][55] = 1  
    tabela['a'][68] = 1  
    tabela['o'][76] = 1  
    tabela['q'][56] = 1  
    tabela['u'][69] = 1  
    tabela['a'][77] = 1  
    tabela['n'][81] = 1  
    tabela['t'][84] = 1  
    tabela['o'][87] = 1  
    tabela['r'][5] = 1  
    tabela['e'][30] = 1  
    tabela['a'][49] = 1  
    tabela['l'][63] = 1 

    tabela.at[91] = 1
    tabela.at[92] = 1
    tabela.at[92,'ES'] = 'N'
    tabela.at[91,'ES'] = 'S'
    return tabela

def check_type(letter):
    if letter == '>' or letter == '<' or letter == '=':
        return 'relop'
    elif letter == '/' or letter == '+' or letter == '-' or letter == '*':
        return 'operador'
    elif letter == '"' or letter == '.' or letter == "'" or letter == '[' or letter == ']' or letter == '(' or letter == ')' or letter == ';':
        return 'simbolo'
    elif letter.islower() or letter.isupper():
        return 'letra'
    elif letter.isdigit():
        return 'digito'

def check_letter_on_file(letter,word):
    count_row = 1
    count_col = 1
    col = []
    row = []
    with open(r'input.txt','r') as file:
            for line in file:
                if letter in line and word in line:
                    for i in line:
                        if letter == i:
                            col.append(count_col)
                        count_col +=1
                    break
                count_row += 1
                count_col = 1
                col = []
            return count_row,col
