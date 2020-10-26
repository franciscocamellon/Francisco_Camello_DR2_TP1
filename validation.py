# -*- coding: utf-8 -*-
""" Validate exceptions """
import re


class Custom_Error(Exception):
    """ Handle custom exceptions. """

    def __init__(self):
        super().__init__()


class Less_Than_Zero(Custom_Error):
    """ Raised when the input value is less than zero. """
    pass


class Zero(Custom_Error):
    """ Raised when the input value is equal zero. """
    pass


class Equal_Length(Custom_Error):
    """ Raised when the input value is not an integer. """
    pass


class Months(Custom_Error):
    """ Raised when the input value is greater than 12. """
    pass


class Days(Custom_Error):
    """ Raised when the input value is greater than 30. """
    pass


class String(Custom_Error):
    """ Raised when the error involves strings. """
    pass


class Not_Found(Custom_Error):
    """ Raised when the input value is not found. """
    pass


class Validate(Custom_Error):

    def validate_factorial(self, title):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = int(input(title))
                if value < 0:
                    raise Less_Than_Zero
                else:
                    return value
                break
            except ValueError:
                print('  Erro! Digite um número inteiro positivo!')
            except Less_Than_Zero:
                print('  Erro! Não é possível calcular fatorial de números negativos!')

    def validate_value_tuple(self, title, _tuple):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = input(title)
                for i in range(len(_tuple)):
                    if re.search(value, _tuple[i], re.IGNORECASE):
                        return value
                else:
                    raise Not_Found
                break
            except ValueError:
                print('  Erro!')
            except Not_Found:
                print('  Erro! O elemento digitado não pertence à tupla!')

    def validate_values(self, title, zero=True):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = int(input(title))
                if value < 0:
                    raise Less_Than_Zero
                elif value == 0 and zero == False:
                    raise Zero
                else:
                    return value
                break
            except ValueError:
                print('  Erro! Digite um número inteiro!')
            except Less_Than_Zero:
                print('  Erro! Digite um número maior que zero!')
            except Zero:
                print('  Erro! Digite um número diferente de zero!')

    def validate_strings(self, title, length):
        """ Validates the input data given by the user. """

        while True:
            try:
                value = str(input(title))
                if len(value) == length:
                    raise Equal_Length
                elif len(value) < length:
                    raise String
                else:
                    return value
                break
            except ValueError:
                print('  Erro! Digite uma string!')
            except String:
                print('  Erro! String tem menos de {} caracteres!'.format(length))
            except Equal_Length:
                print(
                    '  Aviso! Tamanho da string igual ao número, nenhuma mudança será percebida!', sep="\n")

    def validate_age(self, title, years=False, months=False, days=False):
        """ Validates the input data given by the user. """

        while True:
            try:
                if months:
                    _months = self.validate_values(title, True)
                    if _months > 12:
                        raise Months
                    else:
                        return _months
                elif days:
                    _days = self.validate_values(title, True)
                    if _days > 30:
                        raise Days
                    else:
                        return _days
                break
            except ValueError:
                print('  Erro! Digite um número inteiro!')
            except Months:
                print('  Erro! Aquantidade de meses não pode ser maior que 12!')
            except Days:
                print('  Erro! Aquantidade de dias não pode ser maior que 30!')
