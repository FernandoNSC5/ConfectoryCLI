import collections
from PyInquirer import style_from_dict, Token
import colorama

"""
@author: tiannamen (FernandoNSC5)
12/08/2021
"""
class Style():

    def __init__(self):
        colorama.init()
        self.__loadStyles()
        self.__loadColors()

    def __loadColors(self):
        self.RED = colorama.Fore.RED
        self.GREEN = colorama.Fore.GREEN
        self.CYAN = colorama.Fore.CYAN
        self.MAGENTA = colorama.Fore.LIGHTMAGENTA_EX
        self.RESET = colorama.Fore.RESET

    def __loadStyles(self):
        self.CLI_FORMAT = style_from_dict({
            Token.Separator: '#cc5454',
            Token.QuestionMark: '#673ab7 bold',
            Token.Selected: '#cc5454',  # default
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#f44336 bold',
            Token.Question: '',
        })