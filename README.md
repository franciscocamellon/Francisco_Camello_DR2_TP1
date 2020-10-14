# Francisco_Camello_DR2_TP1
Teste de Performance 01 - Fundamentos do Desenvolvimento Python

1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

2. Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, meses e dias e retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.

3. Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120. Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.

4. Escreva um programa em Python que calcule o fatorial de um dado número N usando um while. Use as mesmas especificações do item anterior.

5. Trabalhar com tuplas é muito importante! Crie 4 funções nas quais:

Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
Dada uma tupla e um elemento, elimine esse elemento da tupla.
Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.
6. (Desafío) Utilizando a ferramenta turtle, desenhe os ângulos de um círculo como indicado na figura a seguir:

Utilize as funções da ferramenta turtle setheading e write, além de outras que sejam necessárias.

7. Utilizando a ferramenta turtle, desenhe uma série de quadrados um do lado do outro como indicada na figura a seguir:

8. Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores numa tupla e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, retorne qual o tipo de triângulo formado.

Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo deve ser menor do que a soma do comprimento dos outros dois lados. Além disso, o programa deve identificar o tipo de triângulo formado observando as seguintes definições:

Triângulo Equilátero: os comprimentos dos três lados são iguais.
Triângulo Isósceles: os comprimentos de dois lados são iguais.
Triângulo Escaleno: os comprimentos dos três lados são diferentes.
 9. Faça uma função que desenhe o triângulo obtido na questão 7 com a ferramenta turtle.

10. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um quadrado de lado N.

11. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um triângulo de lado N.

12. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um círculo de raio N.

13. Usando a função obtida na questão 10, desenhe n quadrados um dentro de outro como mostrado na figura:


Utilize as funções turtle.penup() e turtle.pendown() para mexer a tartaruga sem desenhar

14. Utilizando o código 10.1 da Etapa 2, onde utilizando a função onkey do turtle associamos valores às setas do teclado, para este exercício associe as funções obtidas nas questões 10, 11 e 12 às teclas ‘q’, ‘t’ e ‘c’ respectivamente.

Código 10.1:

15. Rode o código a seguir e explique com suas palavras o que acontece nele.

Código 11:

16. Altere o código da questão 15 para adicionar em outra região um novo polígono à sua escolha.

 17. Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições para a esquerda. Assuma que a string tem pelo menos x caracteres.

Isto é, utilizando como entradas a string “aeiou” e o inteiro 3, o resultado da sua função deve ser “ouaei”.

18. (desafio) Em jogos antigos era possível ver que os desenhos eram compostos por vários triângulos. Como uma maneira de treinar isso, a partir do N dado pelo usuário desenhe um polígono de lado N composto somente por triângulos como na figura:

19. Dado um valor N do usuário, desenhe com a ferramenta turtle a seguinte imagem:

Para ela, a tartaruga aumenta o passo andado em um e gira 90 graus após cada movimentação.

20. Baseando no código criado na questão anterior, crie uma função na qual dado um N obtido através do usuário, sua tartaruga gire 90 + N graus. Teste para 1, 4 e 10 para obter as figuras a seguir.

Teste quais outras figuras você pode gerar com o mesmo código, apenas alterando o ângulo.