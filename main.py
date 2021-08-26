import sys

from PyInquirer import prompt
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
            generatedCode = processor.processAnswers(self.answers, self.data.TEMPLATE, self.data.TARGET_TYPES)
            print(generatedCode.replace("${BR}", "\n\t\t\t\t"))

            if(self.answers[6]["[Step 1G]"] == "No"):
                break

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

            qAnswer = prompt(question, style = self.style.CLI_FORMAT)

            if len(qAnswer) is 0:
                if step[0] == self.data.STEPS[3][0]:
                    print(self.style.RED + self.data.ERROR["REQUIRED_FIELD_CANCELED"])
                    exit()
                qAnswer = {step[0]: self.data.METADATA[step[0]][1]}

            self.answers.append(qAnswer)

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
                'name'      : step,
                'validate'  : lambda entry: self.validate(entry, step) or "Mandatory field",
            }
        ]

    def validate(self, cliEntry, step):
        if (not self.data.METADATA[step][0]):
            return True
        elif(len(cliEntry) < 1):
            return False
        return True

m = Main()
