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

    def init_class(self, number):
        """
        This function receives the input data from users.
        """
        
        self.input = int(input('Digite um número inteiro e positivo: '))
        for i in range(1, self.input):
            if i % 2 == 0:
                pass
            else:
                self.data.append(i)
        self.num = sum(self.data)
        return self.num

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, '{:^75}'.format('Questão 01'), '===' * 25, sep='\n')
        self.init_class(self.input)
        print('---' * 25,
              'A soma dos números ímpares de 1 a {} é: {}'.format(
                  self.input, self.num),
              '---' * 25,
              '{:>75}'.format('Aluno: Francisco Camello'), sep="\n")


Questao_01().print_result()
