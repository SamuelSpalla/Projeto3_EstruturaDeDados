import time
import matplotlib.pyplot as plt


def p1():
    elementos = [['a', 'b', 'c', 'd'], ['q', 'i', 'n', 'm'], ['f', 'e', 'h', 'j'], ['p', 'o', 'l', 'g']]
    final = list()
    for x in range(len(elementos)):
        for y in range(len(elementos[x])):
            final.append(elementos[x][y])

    print(f'Crescente:   {sorted(final)}\nDecrescente: {sorted(final, reverse=True)}')


ns = []
tempos = []

for c in range(1, 31):
    inicio = time.perf_counter()
    p1()
    final = time.perf_counter()
    ms = (final-inicio) * 10 ** 6
    ns.append(c)
    tempos.append(ms)

plt.plot(ns, tempos)
plt.xlabel('Valor de n')
plt.ylabel('Tempo de execução (ms)')
plt.show()