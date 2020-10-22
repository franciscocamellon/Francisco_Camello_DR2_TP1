# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 06                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_06.py                                   *
***************************************************************************/
"""
import turtle


class Questao_06():
    """
    Docstring
    """

    def __init__(self):
        """
        Constructor
        """
        turtle.shape('turtle')
        self.squirtle = turtle.Turtle()
        self.degree = int

    def draw(self, distance):
        """
        Docstring
        """
        for i in range(24):
            self.degree = i*15
            self.squirtle.setheading(self.degree)
            self.squirtle.forward(distance)
            if self.degree == 90 or self.degree == 270:
                self.squirtle.write('{}º'.format(
                    self.degree), False, align='center')
            elif self.degree in range(0, 75) or self.degree in range(285, 360):
                self.squirtle.write('{}º'.format(
                    self.degree), False, align='left')
            else:
                self.squirtle.write('{}º'.format(
                    self.degree), False, align='right')
            self.squirtle.home()
        # to keep turtle screen open when using vscode
        turtle.done()


    def print_result(self):
        """
        This is a printer! It prints.
        """
        self.draw(150)


Questao_06().print_result()

