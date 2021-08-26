"""
@author: tiannamen (FernandoNSC5)
14/08/2021
"""
class Processor():

    def __init__(self, steps):
        self.steps = steps

    def processAnswers(self, answers, template, targets):
        for i in range(7):
            template = template.replace(self.steps[i][0], answers[i][self.steps[i][0]])
        template = template.replace("${targetType}", targets[answers[4][self.steps[4][0]]])
        template = template.replace("Yes", "required")
        template = template.replace("No", "optional")
        return template