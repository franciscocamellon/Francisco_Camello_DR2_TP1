# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 13                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_13.py                                   *
***************************************************************************/
"""
import turtle
from validation import Validate

class Questao_13():
    """ This function draws squares side by side. """

    def __init__(self):
        """ Constructor. """
        turtle.title('Questão 13')
        self.squirtle = turtle.Turtle()
        self.squirtle.penup()
        self.side_size, self.x, self.y = 0, 0, 0
        self.distance_txt = ' Digite o tamanho do lado do primeiro quadrado: '
        self.quantity_txt = ' Digite a quantidade de quadrados a serem desenhados: '
        self.data = {self.quantity_txt: 0, self.distance_txt: 4}

    def init_class(self):
        """ This function receives the input data from users. """

        for k, v in self.data.items():
            self.data[k] = Validate().validate_values(k, False)

        self.x = self.y = (self.data.get(self.distance_txt) // 2) * (-1)

    def process_data(self):
        """ This function process the input data from init_class. """

        self.init_class()
        self.squirtle.setpos(self.x, self.y)

        _range = self.data.get(self.quantity_txt)
        _distance = self.data.get(self.distance_txt)

        for i in range(1, _range):
            self.squirtle.pendown()
            for sides in range(1, 5):
                self.squirtle.forward(_distance * i*3)
                self.squirtle.setheading(sides * 90)
            self.squirtle.penup()
            self.squirtle.goto(self.x * i*2.5, self.y * i*2.5)
        
        self.squirtle.goto(self.x, self.y)

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 13'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, ' Desenho finalizado com sucesso!', '---' *
              25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")

        turtle.done()


Questao_13().print_result()
