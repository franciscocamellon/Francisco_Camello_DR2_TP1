# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 08                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_08.py                                   *
***************************************************************************/
"""


class Questao_08():
    """
    Docstring
    """

    def __init__(self):
        """
        Constructor
        """
        self.input = int
        self.data = ()
        self.num = int

    def init_class(self):
        """
        Docstring
        """
        size = []
        while len(size) < 3:
            self.input = int(input('Digite o primeiro lado do triangulo: '))
            size.append(self.input)
        size.append(size[0])
        self.data = tuple(size)

        return print(self.data)

    def validate_sides(self):
        self.init_class()
        count = 0
        soma = []
        while count < 3:
            side = self.data[count]
            if count == 0:
                side_sum = self.data[count+1] + self.data[count+2]
            elif count == 1:
                side_sum = self.data[count+1] + self.data[count-2]
            else:
                side_sum = self.data[count-2] + self.data[count-1]
            soma.append((side, side_sum))
            count += 1
        if soma[0][0] < soma[0][1] and soma[1][0] < soma[1][1] and soma[2][0] < soma[2][1]:
            print('pode ser trinagulo')
        else:
            print('nao pode ser trinagulo')
        return soma

    def validate_types(self):
        data = self.validate_sides()
        if data[0][0] == data[1][0] and data[0][0] == data[2][0]:
            return print('triangulo equilatero')
        elif data[0][0] == data[1][0] and data[0][0] != data[2][0] or data[0][0] != data[1][0] and data[0][0] == data[2][0]:
            return print('triangulo isosceles')
        elif data[0][0] != data[1][0] and data[0][0] != data[2][0] and data[1][0] != data[2][0]:
            return print('triangulo Escaleno')
        else:
            pass

    def print_result(self):
        """
        This is a printer! It prints.
        """


Questao_08().validate_types()
