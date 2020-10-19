from scipy.stats import kstest
import math

f = open("dados.txt", "r")

data = []
for x in f.read().split():
  data.append(int(x))

# Removendo o outlier
data.remove(728)

sum = 0
for x in data:
  sum += x

# A media na distribuicao exponencial eh 1/lambda
media = sum / len(data)
la = 1/media # lambda

aux = [0]*44
for x in data:
  aux[x] += 1

frqAc, sx, fesq, fdir, desq, ddir = 0, 0, 0, 0, 0, 0
maior = -1
i = 1
for x in aux:
  frqAc += x
  sx = round(frqAc / len(data), 3)
  fesq = fdir
  fdir = round(1 - math.exp(-la * i), 3)
  desq = round(abs(fesq - sx), 3)
  ddir = round(abs(fdir - sx), 3)
  maior = max(maior, max(desq, ddir))
  i += 1
  print("| Frq.Ac: " + str(frqAc) + " | S(x): " + str(sx) + " | Fesq: " + str(fesq) + " | Fdir: " + str(fdir) + " | Desq: " + str(desq) + " | Ddir: " + str(ddir) + " | D: " + str(max(desq, ddir)))

print("Dmax: " + str(maior))
print("Dcrit: " + str(round(1.36/(math.sqrt(199)),3)))
