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
        """ Constructor. """

        self.tuple = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')
        self.tuple1, self.tuple2, self.pop, self.rev = (), (), (), ()
        self.idx = 0
        self.input = ''

    def init_class(self):
        """ This function receives the input data from users. """

        self.input = Validate().validate_value_tuple(
            "Digite um elemento pertencente ou não à tupla: ", self.tuple)
        self.idx = self.tuple.index(self.input.capitalize())

    def process_data(self):
        """ This function divides the input tuple by half. """

        self.init_class()

        half = len(self.tuple)//2
        self.tuple1 = self.tuple[:half]
        self.tuple2 = self.tuple[half:]

        self.pop = list(self.tuple)
        self.pop.remove(self.input.capitalize())
        self.pop = tuple(self.pop)

        self.rev = list(self.tuple)
        self.rev.reverse()
        self.rev = tuple(self.rev)

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, 'Questão 05'.center(75),
              '===' * 25, 'Dada a seguinte tupla: {}'.format(self.tuple), sep='\n')
        self.process_data()
        print(
            '---' * 25,
            'O elemento digitado pertence à tupla e seu índice é: {}.'.format(
                self.idx),
            "Dividindo-se a tupla obtém-se: \n   tupla 1 {} e \n   tupla 2 {}.".format(
                self.tuple1, self.tuple2),
            "Eliminando-se o elemento digitado: \n   {}.".format(
                self.pop),
            "Invertendo a tupla obtém-se: \n   {}.".format(self.rev),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_05().print_result()
