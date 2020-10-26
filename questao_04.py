# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 04                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_04.py                                   *
***************************************************************************/
"""
from validation import Validate

class Questao_04():
    """
     This function uses a WHILE loop to calculate the factorial from a given number
    by the user.
    """

    def __init__(self):
        """
        Constructor
        """
        self.input = int
        self.count = 2
        self.num = 1

    def init_class(self):
        """
        This function receives the input data from users.
        """
        self.input = Validate().validate_factorial(' Digite um número: ')

        while self.count <= self.input:
            self.num *= self.count
            self.count += 1

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 04'.center(75), '===' * 25, sep='\n')
        self.init_class()
        print(
            '---' *
            25, 'O fatorial de {}! é: {}.'.format(self.input, self.num),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_04().print_result()
