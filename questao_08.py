# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 08                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_08.py                                   *
***************************************************************************/
"""
from validation import Validate

class Questao_08():
    """ Docstring """

    def __init__(self):
        """ Constructor. """

        self.data = []
        self.title = ' Digite o {}º lado do triângulo: '
        self.type = ('do tipo Equilátero', 'do tipo Escaleno', 'do tipo Isóceles')
        self.validate = (' Esses valores formam um triângulo',\
                         ' Esses valores não formam um triângulo')
        self.result = []

    def init_class(self):
        """ This function receives the input data from users. """

        _data = []

        for i in range(3):
            _data.append(Validate().validate_values(self.title.format(i + 1), False))
        
        self.data.append((_data[0], _data[1] + _data[2]))
        self.data.append((_data[1], _data[0] + _data[2]))
        self.data.append((_data[2], _data[0] + _data[1]))
        self.data = tuple(self.data)

    def process_data(self):
        """ This function process the input data from init_class. """

        self.init_class()
        print(self.data)

        for i in range(3):
            if not self.data[0][0] < self.data[0][1] and self.data[1][0] < self.data[1][1] and self.data[2][0] < self.data[2][1]:
                self.result.append(self.validate[1])
                break
            else:
                self.result.append(self.validate[0])
        
        
        if self.data[0][0] == self.data[1][0] and self.data[0][0] == self.data[2][0]:
            self.result.append(self.type[0])
        elif self.data[0][0] == self.data[1][0] and self.data[0][0] != self.data[2][0] or self.data[0][0] != self.data[1][0] and self.data[0][0] == self.data[2][0]:
            self.result.append(self.type[2])
        elif self.data[0][0] != self.data[1][0] and self.data[0][0] != self.data[2][0] and self.data[1][0] != self.data[2][0]:
            self.result.append(self.type[1])
        else:
            pass

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 08'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25, '{0} {1}'.format(self.result[0], self.result[1]),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_08().print_result()
