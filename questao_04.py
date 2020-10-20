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


class Questao_04():
    """
    Docstring
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
        Docstring
        """
        self.input = int(input("Digite o valor de n: "))

        while self.count <= self.input:
            self.num *= self.count
            self.count += 1

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, '{:^75}'.format('Questão 03'), '===' * 25, sep='\n')
        self.init_class()
        print(
            '---' *
            25, 'O fatorial de {}! é: {}.'.format(self.input, self.num),
            '---' * 25, '{:>75}'.format('Aluno: Francisco Camello'), sep="\n"
        )


Questao_04().print_result()
