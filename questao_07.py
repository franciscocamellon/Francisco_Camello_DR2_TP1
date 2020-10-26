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
from validation import Validate

class Questao_07():
    """ This function draws squares side by side. """

    def __init__(self):
        """ Constructor. """
        turtle.title('Questão 07')
        self.squirtle = turtle.Turtle()
        self.squirtle.penup()
        self.position = 0
        self.distance = ' Digite o tamanho do lado do quadrado: '
        self.quantity = ' Digite a quantidade de quadrados a serem desenhados: '
        self.data = {self.quantity: 0, self.distance: 4}

    def init_class(self):
        """ This function receives the input data from users. """

        for k, v in self.data.items():
            self.data[k] = Validate().validate_values(k, False)

        self.position = self.data.get(self.distance) * (-2)

    def process_data(self):
        """ This function process the input data from init_class. """

        self.init_class()
        self.squirtle.setpos(self.position, 0)

        _range = self.data.get(self.quantity)
        _distance = self.data.get(self.distance)

        for i in range(_range):
            self.squirtle.pendown()
            for sides in range(1, 5):
                self.squirtle.forward(_distance)
                self.squirtle.setheading(sides * 90)
            self.squirtle.penup()
            self.squirtle.setheading(0)
            if i < (_range - 1):
                self.squirtle.forward(_distance)
                self.squirtle.pendown()
            else:
                self.squirtle.setpos(self.position, 0)

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 07'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, ' Desenho finalizado com sucesso!', '---' *
              25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")

        turtle.done()


Questao_07().print_result()
