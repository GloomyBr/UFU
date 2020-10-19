from scipy.stats import expon
import matplotlib.pyplot as pt
from scipy.stats import chisquare



f = open("dados.txt", "r")

data = []
for x in f.read().split():
    data.append(int(x))

# Outlier, remover para exemplificar no arquivo pdf
data.remove(728)
# Outlier
pt.boxplot(data)
pt.show()
