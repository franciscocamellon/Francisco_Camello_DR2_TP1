# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 01 **************************
*    Questao 02                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Fundamentos do Desenvolvimento Python           *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_02.py                                   *
***************************************************************************/
"""


class Questao_02():
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

    def init_class(self, number):
        """
        This function receives and orders the input data from users.
        """
        while len(self.data) < 3:
            a = int(input('    Digite agora os anos: '))
            self.data['years'] = a
            m = int(input('    Os meses: '))
            self.data['months'] = m
            d = int(input('    E os dias: '))
            self.data['days'] = d
        num = []
        for k, v in self.data.items():
            if k == 'years':
                num.append(v * 365)
            elif k == 'months':
                num.append(v * 30)
            else:
                num.append(v)
        self.num = sum(num)

    def print_result(self):
        """
        This is a printer! It prints.
        """
        print('===' * 25, '{:^75}'.format('Questão 02'), '===' * 25,
              '  Digite sua idade conforme o exemplo: 27 anos 7 meses e 23 dias.', sep='\n')
        self.init_class(self.input)
        print(
            '---' * 25, 'Parabéns! Você tem {} dias de idade!'.format(self.num),
            '---' * 25, '{:>75}'.format('Aluno: Francisco Camello'), sep="\n"
            )


Questao_02().print_result()
