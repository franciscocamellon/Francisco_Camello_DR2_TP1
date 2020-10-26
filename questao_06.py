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
from validation import Validate


class Questao_06():
    """ This fuction draws the angles by 15° from a circle. """

    def __init__(self):
        """ Constructor. """
        turtle.title('Questão 06')
        self.squirtle = turtle.Turtle()
        self.degree = ' Digite um ângulo: '
        self.distance = ' Digite uma distância: '
        self.data = {self.degree: 0, self.distance: 0}

    def init_class(self):
        """ This function receives the input data from users. """

        for k, v in self.data.items():
            self.data[k] = Validate().validate_values(k, False)

    def process_data(self):
        """ This function process the input data from init_class. """

        self.init_class()
        _range = 360 // self.data.get(self.degree)
        _distance = self.data.get(self.distance)

        for i in range(_range):
            _degree = i * self.data.get(self.degree)
            self.squirtle.setheading(_degree)
            self.squirtle.forward(_distance)
            if _degree == 90 or _degree == 270:
                self.squirtle.write('{}º'.format(
                    _degree), False, align='center')
            elif _degree in range(0, 75) or _degree in range(285, 360):
                self.squirtle.write('{}º'.format(
                    _degree), False, align='left')
            else:
                self.squirtle.write('{}º'.format(
                    _degree), False, align='right')
            self.squirtle.home()

        print('---' * 25, ' Desenho finalizado com sucesso!', '---' *
              25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")

        turtle.done()

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 06'.center(75), '===' * 25, sep='\n')
        self.process_data()


Questao_06().print_result()
