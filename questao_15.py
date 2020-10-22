# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 15                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_15.py                                   *
***************************************************************************/
"""
import turtle

class Questao_15():
    """
    Docstring
    """


    def __init__(self):
        """
        Constructor
        """
        turtle.title('Questão 15')
        self.squirtle = turtle.Turtle()



    def geraPontos(self, i):
        """ Gera pontos para quadrados de qualquer tamanho """
        return [(i, 0), (i, i), (0, i), (0, 0)]

    def desenhaPoligono(self, inicio, pontos, corLinha="black", corRecheio="white"):
        self.squirtle.pencolor(corLinha)
        self.squirtle.fillcolor(corRecheio)

        self.squirtle.penup()

        self.squirtle.goto(inicio)

        self.squirtle.pendown()
        self.squirtle.begin_fill()

        x, y = inicio

        for ponto in pontos:
            dx, dy = ponto
            self.squirtle.goto(x + dx, y + dy)
        self.squirtle.goto(inicio)

        self.squirtle.end_fill()
        self.squirtle.penup()



    def teste(self):
        # Primeiro quadrado
        self.quadrado = [(50, 0), (50, 50), (0, 50), (0, 0)]
        self.desenhaPoligono((200, 200), self.quadrado)

        # Segundo quadrado
        self.quadrado_maior = self.geraPontos(100)
        self.desenhaPoligono((-200, 200), self.quadrado_maior, corRecheio="green")

        # Triangulo
        self.triangulo = [(200, 0), (100, 100), (0, 0)]
        self.desenhaPoligono((100, -100), self.triangulo, corRecheio="green")


    def main(self):
        self.teste()
        turtle.done()




Questao_15().main()
