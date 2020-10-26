# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 17                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_17.py                                   *
***************************************************************************/
"""
from validation import Validate


class Questao_17():
    """
    Docstring
    """

    def __init__(self):
        """
        Constructor
        """
        self.input = ''
        self.input_title = ' Digite uma string com no mínimo {} caracteres: '
        self.num = 0
        self.num_title = ' Digite um número: '
        self.res = ''

    def init_class(self):
        """
        This function receives the input data from users.
        """
        self.num = Validate().validate_values(self.num_title)
        self.input = Validate().validate_strings(self.input_title.format(self.num), self.num)

        aux = self.input[:self.num]
        aux2 = self.input[self.num:]
        self.res = aux2 + aux

        return self.res

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 17'.center(75), '===' * 25, sep='\n')
        self.init_class()
        print(
            '---' * 25,
            ' A string {} rotacionada {} posições corresponde a:\n  {}'.format(
                self.input, self.num, self.res),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_17().print_result()
