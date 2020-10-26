# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 12                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_12.py                                   *
***************************************************************************/
"""
import turtle
from validation import Validate

class Questao_12():
    """ This function draws a circle with side size given by the user. """

    def __init__(self):
        """ Constructor. """
        turtle.title('Questão 12')
        self.squirtle = turtle.Turtle()
        self.squirtle.penup()
        self.side_size, self.x, self.y = 0, 0, 0
        self.input_txt = ' Digite o tamanho do raio do círculo: '
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

        self.squirtle.circle(self.side_size)

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 12'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, 
            ' Círculo de raio {} desenhado com sucesso!'.format(self.side_size), 
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")

        turtle.done()


Questao_12().print_result()
