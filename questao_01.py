# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 01                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_01.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_01():
    """
    This program takes a number from user and return the sum of all prime
    numbers from one to user input.
    """

    def __init__(self):
        """
        Constructor
        """
        self.input = int
        self.data = []
        self.num = int

    def init_class(self):
        """
        This function receives the input data from users.
        """

        self.input = Validate().validate_values(' Digite um número: ')

    def process_data(self):
        """ This function process the input data from init_class. """

        self.init_class()

        for i in range(1, self.input):
            if i % 2 == 0:
                pass
            else:
                self.data.append(i)
        self.num = sum(self.data)

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 01'.center(75), '===' * 25, sep='\n')
        self.process_data()
        print('---' * 25,
              '  A soma dos números ímpares de 1 a {} é: {}'.format(
                  self.input, self.num),
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_01().print_result()
