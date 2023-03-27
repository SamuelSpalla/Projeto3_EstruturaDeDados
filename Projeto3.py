import time
import matplotlib.pyplot as plt


def p1():
    elementos = [
        ['a', 'b', 'c', 'd'],
        ['q', 'i', 'n', 'm'],
        ['f', 'e', 'h', 'j'],
        ['p', 'o', 'l', 'g']
    ]
    final = list()
    for x in range(len(elementos)):
        final += elementos[x]
    print(f'Crescente:   {sorted(final)}\n'
          f'Decrescente: {sorted(final, reverse=True)}')


def BigO():
    ns = list()
    tempos = list()
    for c in range(1, 31):
        inicio = time.perf_counter()
        p1()
        final_time = time.perf_counter()
        ms = (final_time - inicio) * 10 ** 6
        ns.append(c)
        tempos.append(ms)

    plt.plot(ns, tempos)
    plt.xlabel('Valor de n')
    plt.ylabel('Tempo de execução (ms)')
    plt.show()


while True:
    esc = input('\n\n0 - Sair\n\n1 - Exercício\n2 - Gerar BigO\n- ')
    if esc == '1':
        p1()
    elif esc == '2':
        BigO()
    elif esc == '0':
        break
    else:
        print('Valor incorreto')
