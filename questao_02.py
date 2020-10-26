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
from validation import Validate


class Questao_02():
    """ This function calculates the age of users in days. """

    def __init__(self):
        """ Constructor. """

        self.input = 0
        self.data = {}
        self.num = 0

    def init_class(self):
        """ This function receives the input data from users. """

        while len(self.data) < 3:
            self.data['years'] = Validate().validate_values(
                '  Digite os anos: ', True)
            self.data['months'] = Validate().validate_age(
                '  Digite os meses: ', months=True)
            self.data['days'] = Validate().validate_age(
                '  Digite os dias: ', days=True)

    def process_data(self):
        """ This function process the input data from init_class. """

        _list = []
        self.init_class()

        for k, v in self.data.items():
            if k == 'years':
                _list.append(v * 365)
            elif k == 'months':
                _list.append(v * 30)
            else:
                _list.append(v)
        self.num = sum(_list)

    def print_result(self):
        """ This is a printer! It prints. """

        print('===' * 25, 'Questão 02'.center(75), '===' * 25,
              ' Digite sua idade conforme o exemplo: 27 anos 7 meses e 23 dias.', sep='\n')
        self.process_data()
        print(
            '---' *
            25, '  Parabéns! Você tem {} dias de idade!'.format(self.num),
            '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n"
        )


Questao_02().print_result()
