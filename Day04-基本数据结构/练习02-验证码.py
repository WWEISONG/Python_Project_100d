import random

def gengerate_code(code_len = 4):
    """
    generate verification code of specified length
    :param code_len: length is 4 default
    :return: randon code consisting of numbers, letters
    """
    all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_char) - 1
    code = ''
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_char[index]
    return code

if __name__ == '__main__':
    gengerate_code(code_len = 4)