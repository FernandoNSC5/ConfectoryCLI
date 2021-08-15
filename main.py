import sys

from PyInquirer.prompt import prompt
from pprint import pprint
import Processor
sys.path.insert(1, 'assets/')
import Data, Style

"""
@author: tiannamen (FernandoNSC5)
12/08/2021
"""
class Main():

    def __init__(self):
        self.data = Data.Data()
        self.style = Style.Style()
        processor = Processor.Processor(self.data.STEPS)

        anotherConfiguration = True

        while(anotherConfiguration):
            self.answers = list()
            self.printHeader()
            self.printQuestion()
            generatedCode = processor.processAnswers(self.answers, self.data.TEMPLATE)
            print(generatedCode.replace("${BR}", "\n"))
            anotherConfiguration = False

    def printHeader(self):
        print(self.style.RED + self.data.LOGO)
        print(self.style.RESET + self.data.HEADER)
        print(self.style.RESET + self.data.BR)

    def printQuestion(self):
        for step in self.data.STEPS:
            if(step[1]):
                question = self.buildListQuestion(step[0], self.data.QUESTIONS[step[0]])
            else:
                question = self.buildQuestion(step[0], self.data.QUESTIONS[step[0]])

            self.answers.append(prompt(question, style = self.style.CLI_FORMAT))

    def buildListQuestion(self, step, data):
        header = data[0]
        answers = list()
        for i in range(1, len(data)):
            answers.append(data[i])
        return [
            {
                'type'      : 'list',
                'message'   : header,
                'name'      : step,
                'choices'   : answers
            }
        ]

    def buildQuestion(self, step, data):
        return [
            {
                'type'      : 'input',
                'message'   : data,
                'name'      : step
            }
        ]

m = Main()
pprint(m.answers)