class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        chr_constant = 48

        def str_to_int(x):
            sum = 0
            constant = 1
            for ind in range(len(x)):
                str_element = x[len(x) - 1 - ind]
                int_element = ord(str_element) - chr_constant
                sum += int_element * constant
                constant *= 10
            return sum, constant
    
        def int_to_str(x, constant):
            def find(_x, _mul):
                while _x < _mul:
                    _mul //= 10
                return _mul
            def divide(_x, _constant):
                _div = 0
                while _x >= 0:
                    _div += 1
                    _x -= _constant
                return _div - 1, _x + _constant

            
            constant = find(x, constant)
            l = []
            while constant >= 1:
                element, x = divide(x, constant)
                constant //= 10
                l.append(chr(chr_constant + element))
            return ''.join(l)

        if num1 == '0' or num2 == '0':
            return '0'

        int_num1, constant_num1 = str_to_int(num1)
        int_num2, constant_num2 = str_to_int(num2)

        multiple_10 = constant_num1 * constant_num2

        return(int_to_str(int_num1 * int_num2, multiple_10))