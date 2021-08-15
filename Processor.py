import ast

"""
@author: tiannamen (FernandoNSC5)
14/08/2021
"""
class Processor():

    def __init__(self, steps):
        self.steps = steps

    def processAnswers(self, answers, template):
        #evaluatedAnswer = ast.literal_eval(answers)
        for i in range(7):
            template.replace(self.steps[i][0], answers[i][self.steps[i][0]])
        return template