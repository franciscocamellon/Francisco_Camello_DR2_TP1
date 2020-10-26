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

from validation import Validate


class Questao_05():
    """
    This function search in the tuple for a string given by the user, divides
    the tuple, removes an item from the tuple and reverses the tuple.
    """

    def __init__(self):
        """
        Constructor
        """
        self.tuple = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')
        self.idx = 0
        self.input = ''

    def init_class(self):
        """
        This function receives the input data from users.
        """
        self.input = Validate().validate_value_tuple(
            "Digite um elemento pertencente ou não à tupla: ", self.tuple)
        self.idx = self.tuple.index(self.input.capitalize())

    def divide(self):
        """
        This function divides the input tuple by half.
        """
        half = len(self.tuple)//2
        common_order_1 = self.tuple[:half]
        common_order_2 = self.tuple[half:]
        return common_order_1, common_order_2

    def remove(self):
        """
        This function removes the input item from tuple.
        """
        pop = list(self.tuple)
        pop.remove(self.input.capitalize())
        return tuple(pop)

    def reverse(self):
        """
        This function reverses the input tuple.
        """
        rev = list(self.tuple)
        rev.reverse()
        return tuple(rev)

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 05'.center(75),
              '===' * 25, 'Dada a seguinte tupla: {}'.format(self.tuple), sep='\n')
        self.init_class()
        print(
            '---' * 25,
            'O elemento digitado pertence à tupla e seu índice é: {}.'.format(
                self.idx),
            "Dividindo-se a tupla obtém-se: \n   tupla 1 {} e \n   tupla 2 {}.".format(
                self.divide()[0], self.divide()[1]),
            "Eliminando-se o elemento digitado: \n   {}.".format(
                self.remove()),
            "Invertendo a tupla obtém-se: \n   {}.".format(self.reverse()),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_05().print_result()
