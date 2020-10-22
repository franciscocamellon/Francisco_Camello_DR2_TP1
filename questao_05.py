# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 05                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_05.py                                   *
***************************************************************************/
"""


class Questao_05():
    """
    Docstring
    """

    def __init__(self):
        """
        Constructor
        """
        self.tuple = ('Segunda', True, '15', {1: "maçã"}, [0, 1, 2], 3.1416)
        self.idx = int
        self.input = str

    def init_class(self):
        """
        Docstring
        """
        self.input = input("Digite um elemento pertencente ou não à tupla: ")
        for item in range(len(self.tuple)):
            if self.tuple[item] == self.input:
                self.idx = item
                string = 'pertence'
                return item, string

    def divide(self):
        half = len(self.tuple)//2
        another_half = len(self.tuple)-half
        common_order_1 = self.tuple[:half]
        common_order_2 = self.tuple[another_half:]
        return common_order_1, common_order_2

    def rem(self):
        pop = list(self.tuple)
        pop.remove(self.input)
        return tuple(pop)

    def reverse(self):
        rev = list(self.tuple)
        rev.reverse()
        return tuple(rev)

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, '{:^75}'.format('Questão 05'),
              '===' * 25, 'Dada a seguinte tupla: {}'.format(self.tuple), sep='\n')
        self.init_class()
        print(
            '---' * 25,
            'O elemento digitado pertence à tupla e seu índice é: {}.'.format(
                self.idx),
            "Dividindo-se a tupla obtém-se: \n   tupla 1 {} e \n   tupla 2 {}.".format(
                self.divide()[0], self.divide()[1]),
            "Eliminando-se o elemento digitado: \n   {}.".format(self.rem()),
            "Invertendo a tupla obtém-se: \n   {}.".format(self.reverse()),
            '---' * 25, '{:>75}'.format('Aluno: Francisco Camello'), sep="\n"
        )


Questao_05().print_result()
