# CI1238/CI7056 Otimização/Tópicos em Algoritmos
> 26 de junho de 2021

## Introdução

O trabalho consiste em modelar e implementar, por Branch & Bound, o
problema Caminhada Máxima, descrito na Seção "O problema".
A resolução do problema, ou seja, a descrição do problema, da modelagem
e da implementação, deve estar em um texto claro em formato de um artigo
em pdf. Além disso, deve ser feita uma análise com sua função limitante
(bound ).
O texto deve conter o nome do autor (aluno), uma introdução com o
problema, a modelagem e sua explicação (de por que essa modelagem resolve o problema), detalhes da implementação (com exemplos de uso), e uma
análise do uso da função limitante. Nesta análise devem ser feitas contagens
de número de nós da árvore e tempo de execução (com relatório gerado pelo
programa). Outras métricas também podem ser usadas.
Todas as referências que forem usadas devem estar citadas corretamente
no texto.
Você pode usar bibliotecas para estruturas de dados (como listas, conjuntos etc), mas não para o algoritmo de resolução principal do problema. O
seu programa deve compilar e executar nas servidoras do DINF.
O trabalho deve ser entregue com um makefile de forma que ao digitar o
comando make o executável caminhada seja construı́do.
Resumindo, o texto deve ter:
- identificação;
- explicação do problema;
- modelagem;
- análise da função limitante;
- detalhes da implementação.

A implementação:
- deve ter executável de nome caminhada;
- deve gerar relatório (na saı́da de erro padrão, stderr) com número de
nós da árvore e tempo gasto (sem contar o tempo de entrada e saı́da).

Você deve entregar um arquivo compactado (tar.gz) com os seguintes
- arquivos no diretório corrente:
- texto (em pdf);
- os fontes (podem estar em subdiretórios);
- makefile;
- exemplos usados na análise (podem estar em subdiretórios).

## O problema
Caminhada máxima
Toda manhã Sr. Gump sai para caminhar por sua cidade. Ele não gosta
de passar mais de uma vez por cada lugar. Mas ele gosta de demorar em seu
passeio. Dado um conjunto de lugares (vértices), as ligações entre estes lugares (arestas) e os custos (tempo) de percorrer cada uma destas ligações, devemos encontrar um trajeto para o Sr. Gump que seja o mais longo possı́vel,
sem repetir lugares.

### Formato de entrada e saı́da

Os formatos de entrada e saı́da, são descritos a seguir e devem ser usados
a entrada e a saı́da padrão (stdin e stdout).
A entrada é formada de um conjunto de números inteiros. Os números
podem estar separados por um ou mais espaços, tabs ou fim de linha.
A saı́da também é um conjunto de números inteiros. Nas linhas com
mais de número, estes números devem estar separados por apenas um espaço
e sem espaço no começo nem no fim da linha.

Entrada: Inicia com o número de lugares, n. Em seguida temos n−1 linhas,
representando uma matriz simétrica n × n, A = [aij ], com as ligações e
os pesos. Essa matriz está representada somente pelos valores aij com
i < j. Ou seja, a primeira linha tem n−1 números, representando os valores de a12 , a13 , . . . , a1n ; a segunda linha tem os valores de a23 , . . . , a2n ;
a linha i tem os valores ai(i+1) , . . . , ain . Os valores da diagonal principal
são 0 (ou seja, aii = 0, para todo 1 ≤ i ≤ n). Se aij = 0, com i 6= j
(fora da diagonal principal) então não existe a ligação entre o lugar i
e o lugar j. O tempo de percorrer uma ligação entre os lugares i e j é
dado por aij . O lugar inicial é o lugar 1.
Saı́da: Uma linha com o valor do tempo total da caminhada máxima. Em
seguida uma linha com a sequência de lugares percorridos. O lugar 1
deve ser o primeiro e o último.

### Exemplos de entrada e saı́da

Os relatórios com o número de nós e o tempo foram omitidos nestes exemplos, já que podem variar com a modelagem e a função limitante escolhida.
#### Exemplo simples com n = 4

![image](https://github.com/felipeymn/t2-otimizacao/assets/34167982/22bf0f68-bf32-426e-9d1f-d87933c2769f)

Figura 1: Desenho do exemplo

Entrada:  
> 3  
> 110  
> 51  
> 1

Saı́da:  
> 7  
> 1231  
> 3  

#### Exemplo com n = 6 com partes inacessı́veis (pois não tem
caminho de volta)

![image](https://github.com/felipeymn/t2-otimizacao/assets/34167982/0acf0986-c477-463f-9674-5a79b3d7fc2b)

Figura 2: Desenho do exemplo

Entrada:
> 6  
> 11000  
> 0100  
> 100  
> 10  
> 1  

Saı́da:
> 4  
> 12431  

