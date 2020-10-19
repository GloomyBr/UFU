from scipy.stats import expon
import matplotlib.pyplot as pt
from scipy.stats import chisquare


f = open("dados.txt", "r")

data = []
for x in f.read().split():
    data.append(int(x))

# Outlier, remover para exemplificar no arquivo pdf
data.remove(728)

# Teste de Qui-quadrado
Pk = [0.5022, 0.2500, 0.1244, 0.0620, 0.0308, 0.0154, 0.0076, 0.0038, 0.0038]
tk = []
# Calculo do TK
for x in Pk:
    tk.append(round(199*x))

aux = 0
for x in range(5, 9):
    aux += tk[x]

tk.insert(4, tk[4]+aux)
del tk[5:]

ok = [0]*5
for x in data:
    if x < 4.8:
        ok[0] += 1
    elif x >= 4.8 and x < 9.6:
        ok[1] += 1
    elif x >= 9.6 and x < 14.3:
        ok[2] += 1
    elif x >= 14.3 and x < 19.1:
        ok[3] += 1
    elif x >= 19.1:
        ok[4] += 1

(t,p) = chisquare(ok, tk)

print('Teste de Qui-Square')
print('Ok = ', ok)
print('Tk = ', tk)
print('E = ', t)
print('P-value = ', p)
