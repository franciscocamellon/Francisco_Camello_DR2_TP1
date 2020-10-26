# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 11                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_11.py                                   *
***************************************************************************/
"""
import turtle
from validation import Validate

class Questao_11():
    """ This function draws a triangle with side size given by the user. """

    def __init__(self):
        """ Constructor. """
        turtle.title('Questão 11')
        self.squirtle = turtle.Turtle()
        self.squirtle.penup()
        self.side_size, self.x, self.y = 0, 0, 0
        self.input_txt = ' Digite o tamanho do lado do triângulo: '
        self.data = {self.input_txt: 4}
        self.points = []

    def init_class(self):
        """ This function receives the input data from users. """

        for k, v in self.data.items():
            self.data[k] = Validate().validate_values(k, False)

        self.side_size = self.data.get(self.input_txt)
        self.x = self.y = (self.data.get(self.input_txt) // 2) * (-1)

    def process_data(self):
        """ This function process the input data from init_class. """

        self.init_class()
        self.squirtle.setpos( self.x, self.y)
        self.squirtle.pendown()

        for sides in range(1, 4):
            self.squirtle.forward(self.side_size)
            self.squirtle.setheading(sides * 120)

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 11'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, 
            ' Triângulo de lado {} desenhado com sucesso!'.format(self.side_size), 
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")

        turtle.done()


Questao_11().print_result()
