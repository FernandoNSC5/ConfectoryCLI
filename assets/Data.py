"""
@author: tiannamen (FernandoNSC5)
12/08/2021
"""
class Data():
    def __init__(self):
        self.__loadHeader()
        self.__loadSteps()
        self.__loadQuestions()
        self.__loadTemplates()
        self.__loadTargetTypes()
        self.__loadMetadata()

    def __loadTargetTypes(self):
        self.TARGET_TYPES = {
            "StringMapper"      : "String",
            "PropertiesMapper"  : "Properties"
        }

    """
    Loads the Confectory Logo and version data
    """
    def __loadHeader(self):
        self.VERSION = "V0.1.0"
        self.HEADER = "CONFECTORY-CLI - " + self.VERSION
        self.LOGO = "                    ____          __                  \n  _________  ____  / __/__  _____/ /_____  _______  __\n / ___/ __ \/ __ \/ /_/ _ \/ ___/ __/ __ \/ ___/ / / /\n/ /__/ /_/ / / / / __/  __/ /__/ /_/ /_/ / /  / /_/ / \n\___/\____/_/ /_/_/  \___/\___/\__/\____/_/   \__, /  \n                                             /____/ \n"
        self.BR = "-------------------------------------------------------"

    """
    Loads the Steps Array

    A list of steps' list containing:
        . The Step name
        . The Step Options:
            L True: The answer for the step
            |                must be a list
            L False: The answer for the step
                      must be a String entry
    """
    def __loadSteps(self):
        self.STEPS = [
            ["[Step 1A]", False],
            ["[Step 1B]", False],
            ["[Step 1C]", True],
            ["[Step 1D]", False],
            ["[Step 1E]", True],
            ["[Step 1F]", True],
            ["[Step 1G]", True]
        ]

    """
    Loads CLI questions

    Loads a Dictionary containing the available
    question for each step.
    If the given step requires a List of possible
    pre-made answers, the dict value will be
    an {List} which the first Index represents
    the question Itself and the other indexes the
    possible answers.
    """
    def __loadQuestions(self):
        self.QUESTIONS = {
            "[Step 1A]" : "Define a namespace for the new Configuration (default=""): ",
            "[Step 1B]" : "Enter a precedence for the new Configuration (default=0): ",
            "[Step 1C]" : ["Choose a Source: ", "Dynamic", "Classpath File Source", "File Source"],
            "[Step 1D]" : "Enter the file/resource path (required): ",
            "[Step 1E]" : ["Choose a Mapper: ", "StringMapper", "PropertiesMapper"],
            "[Step 1F]" : ["Is the new configuration Required?", "Yes", "No"],
            "[Step 1G]" : ["Do you want to add another Configuration?", "Yes", "No"]
        }

    """
    Loads the MetaData.

    A MetaData consists of a array which each position
    corresponds a Step from {self.QUESTIONS} dictionary
    MetaData:
    [Required, DefaultValue if any]
    """
    def __loadMetadata(self):
        self.METADATA = {
            "[Step 1A]" : [False, ""],
            "[Step 1B]" : [False, 0],
            "[Step 1C]" : [False, ""],
            "[Step 1D]" : [True, ""],
            "[Step 1E]" : [False, ""],
            "[Step 1F]" : [False, ""],
            "[Step 1G]" : [False, ""]
        }

    """
    Loads the Java code Template
    """
    def __loadTemplates(self):
        self.TEMPLATE = "\n\n\tConfiguration<${targetType}> config = Configuration.<${targetType}>builder()${BR}.namespace(\"[Step 1A]\")${BR}.precedence([Step 1B])${BR}.source(SourceFactory.[Step 1C](\"[Step 1D]\")${BR}.mapper(new [Step 1E]())${BR}.[Step 1F]()${BR}.build()"