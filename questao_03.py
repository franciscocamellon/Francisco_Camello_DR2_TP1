# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 03                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_03.py                                   *
***************************************************************************/
"""
from validation import Validate

class Questao_03():
    """
    This function calculates the factorial from a given number by the user
    """

    def __init__(self):
        """
        Constructor
        """
        self.input = int
        self.data = {}
        self.num = 1

    def init_class(self, number):
        """
        This function receives the input data from users.
        """
        self.input = Validate().validate_factorial(' Digite um número: ')

        for i in range(1, self.input + 1):
            self.num *= i

        return self.num

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 03'.center(75), '===' * 25, sep='\n')
        self.init_class(self.input)
        print(
            '---' * 25, 'O fatorial de {} é {}!'.format(self.input, self.num),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_03().print_result()
