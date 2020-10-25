from validation import Handle_Exception


# string = input('Digite uma string: ')
_title = 'Digite um inteiro: '

Handle_Exception().validate_integer('Digite um inteiro: ')

# if integer.isnumeric():
#     new_integer = int(integer)
#     if isinstance(new_integer, int):
#         print('numero inteiro')
#     else:
#         print('error')

# elif integer.replace('.','',1).isdigit():
#     new = float(integer)
#     if isinstance(new, float):
#         print('numero decimal')
#     else:
#         print('error')

# elif integer.replace(',','.',1).replace('.','',1).isdigit():
#     new = float(integer.replace(',','.',1).replace('.','',1))
#     if isinstance(new, float):
#         print('numero decimal')
#     else:
#         print('error')

# elif integer.isalpha():
#     print('string')
# else:
#     print('error')

