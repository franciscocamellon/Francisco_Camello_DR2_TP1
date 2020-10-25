# -*- coding: utf-8 -*-
"""
Validate exceptions
"""


class Custom_Error(Exception):
    """
    Handle exceptions.
    """

    def __init__(self):
        super().__init__()


class Less_Than_Zero(Custom_Error):
    """Raised when the input value is less than zero"""
    pass


class Is_Integer(Custom_Error):
    """Raised when the input value isnt an integer"""
    pass


class Is_Float(Custom_Error):
    """Raised when the input value isnt a float"""
    pass


class Is_String(Custom_Error):
    """Raised when the input value isnt a string"""
    pass


class Validate(Custom_Error):

    def error(self, value):
        """
        Raises a customized exception.
        """
        if value <= 0:
            raise Less_Than_Zero()
        else:
            return value

    def _integer(self, value):
        """
        Raises a customized exception.
        """
        if isinstance(value, [float, str]):
            raise Is_Integer()
        else:
            return value

    def _float(self, value):
        """
        Raises a customized exception.
        """
        if isinstance(value, [int, str]):
            raise Is_Float()
        else:
            return value

    def _string(self, title):
        """
        Raises a customized exception.
        """
        while True:
            try:
                value = str(input(title))
                if not value.isnumeric():
                

                

                break
            except ValueError:
                print('Digite uma string!')
            except Is_String:
                print('Digite um número maior que zero!')
        # if isinstance(value, [float, int]):
        #     raise Is_String()
        # else:
        #     return value

    def validate_values(self, title):
        """
        Validates the input value from wage given by the user.
        """
        while True:
            try:
                value = int(input(title))
                self.error(value)
                self._integer(value)

                

                break
            except ValueError:
                print('Digite um número!')
            except Less_Than_Zero:
                print('Digite um número maior que zero!')
