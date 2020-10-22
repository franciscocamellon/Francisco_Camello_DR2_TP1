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


class Questao_17():
    """
    Docstring
    """

    def __init__(self):
        """
        Constructor
        """
        self.input = int
        self.data = {}
        self.num = int

    def funcname(self):
        """
        Docstring
        """
        size = []
        while len(size) < 3:
            self.input = int(input('Digite uma string: '))
            size.append(self.input)
        size.append(size[0])
        self.data = tuple(size)

        return print(self.data)
        return

    def print_result(self):
        """
        This is a printer! It prints.
        """


Questao_17().print_result()
