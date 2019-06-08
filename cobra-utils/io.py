import math, os
class query:
    @staticmethod
    def query(query: str, invalid_msg: str = '') -> str:
        while(True):
            try: return input(query)
            except:
                if(invalid_msg != ''):
                    print(invalid_msg)
                continue
    @staticmethod            
    def query_int(query: str, invalid_msg: str = '') -> int:
        while(True):
            try: return int(input(query))
            except:
                if(invalid_msg != ''):
                    print(invalid_msg)
                continue
    @staticmethod
    def query_float(query: str, invalid_msg: str = '') -> float:
        while(True):
            try: return float(input(query))
            except:
                if(invalid_msg != ''):
                    print(invalid_msg)
                continue
    @staticmethod
    def query_mchoice(query: str,invalid_msg: str = '',*options: str) -> int:
        print(query)
        for i in range(len(options)): print(str(i+1) + '.' + options[i])
        while(True):
            res = query.query_int('enter the number of your choice: ',invalid_msg)
            if(res <= 0 or res > len(options)): print(invalid_msg)
            else: return res
class ostyler:
    lwidth = 24
    @staticmethod
    def setWidth(n: int) -> None:
        ostyler.line()
        lwidth = n
    @staticmethod
    def line(c: chr = '-') -> None:
        res = ''
        for i in range(ostyler.lwidth):
            res += c
        print(res)
    @staticmethod
    def printHeader(txt: str, line_char: chr = '-') -> None:
        res = ''
        len1 = (ostyler.lwidth - 2 - len(txt)) # len 1 is the length of the prefix line
        if len(txt) % 2 != 0:                  # len 2 is the length of the suffix line
            len2 = int((len1+1)/2)             # 2 is subtracted to compensate for the
            len1 = int((len1-1)/2)             # additional spaces between the lines.
        else:                                  
            len1 = int(len1/2)
            len2 = len1
        for i in range(len1):
            res += line_char
        res += ' ' + txt + ' '
        for i in range(len2):
            res += line_char
        print(res)
    @staticmethod
    def cls():
        os.system('cls')