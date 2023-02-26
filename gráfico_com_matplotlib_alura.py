import matplotlib.pyplot as plt
from random import randrange, seed

notas_matematica = []
seed(11)

for notas in range(8):
    notas_matematica.append([randrange(0,11)])

notas_matematica
#chama a lista já editada, criada com o range
x = list(range(1,9))
y = notas_matematica
plt.plot(x, y,marker='x')
plt.title('Notas de matemática')
plt.xlabel('provas')
plt.ylabel('notas')
plt.show()
