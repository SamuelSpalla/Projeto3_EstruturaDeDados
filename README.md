# Projeto 3 Estrutura De Dados

Este código Python apresenta duas funções. A primeira função (p1()) consiste em criar uma lista com quatro sub-listas, cada uma contendo quatro letras. Em seguida, essa lista é descompactada em uma nova lista e ordenada em ordem crescente e decrescente, sendo os resultados impressos na tela. A segunda função (BigO()) executa a função p1() 30 vezes para valores crescentes de n (1 a 30), medindo o tempo de execução em microssegundos (μs) e plota um gráfico de dispersão com esses dados.

# Pré-requisitos:
  1 - Python 3.x
  2 - Biblioteca matplotlib

# Como executar:
  1 - Clone o repositório ou baixe o arquivo exercicio_complexidade.py.
  2 - Abra o terminal e navegue até o diretório do arquivo.
  3 - Execute o arquivo digitando python nome_arquivo.py.
  4 - Digite o número correspondente à opção desejada:
      1: Executa a função p1() uma vez.
      2: Executa a função p1() 30 vezes para valores crescentes de n e plota um gráfico de dispersão.
      0: Sai do programa.
    
# Análise de complexidade
Função p1():
A complexidade de tempo da função sorted() é de O(n log n) no pior caso, em que n é o número de elementos a serem ordenados. No caso dessa função p1(), a lista final possui 16 elementos, portanto, a complexidade de tempo de sorted(final) é O(16 log 16) ≈ O(64), que é uma operação de tempo constante. Assim, a complexidade de tempo de p1() é O(1).

Função BigO()
A função BigO() executa a função p1() 30 vezes para valores crescentes de n, de 1 a 30. Portanto, a complexidade de tempo de BigO() é O(n), onde n é o número de vezes que a função p1() é executada. Dentro do loop for, a função p1() é executada, o que possui complexidade O(1), e o tempo de execução é medido em microssegundos. Portanto, a complexidade de tempo total de BigO() é O(n).

# Autor
Nome: Yago Guimarães, Samuel Spalla, João Espindolla, Gabriel Neves, Luis Fellipe
GitHub: https://github.com/SamuelSpalla , https://github.com/YagoTarsin
