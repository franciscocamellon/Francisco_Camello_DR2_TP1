# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 07                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_07.py                                   *
***************************************************************************/
"""
import turtle

class Questao_07():
    """
    Docstring
    """

    def __init__(self):
        """
        Constructor
        """
        # turtle.shape('turtle')
        turtle.title('Questão 07')
        self.squirtle = turtle.Turtle()
        self.squirtle.penup()
        self.squirtle.setpos(-150,0)
        self.distance = int

    def draw(self):
        """
        Docstring
        """
        count = 0
        self.squirtle.pendown()
        while count < 4:
        # for i in range(4):

            distance = 100
            # self.squirtle.setheading(0)
            self.squirtle.forward(distance)
            self.squirtle.setheading(90)
            self.squirtle.forward(distance)
            self.squirtle.setheading(180)
            self.squirtle.forward(distance)
            self.squirtle.setheading(270)
            self.squirtle.forward(distance)
            self.squirtle.penup()
            self.squirtle.setheading(0)
            self.squirtle.forward(distance)
            self.squirtle.pendown()
            count += 1
        # to keep turtle screen open
        turtle.done()
        return

    def print_result(self):
        """
        This is a printer! It prints.
        """
        self.draw()


Questao_07().print_result()
