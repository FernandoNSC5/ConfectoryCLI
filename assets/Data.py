"""
@author: tiannamen (FernandoNSC5)
12/08/2021
"""
class Data():
    def __init__(self):
        self.__loadHeader()
        self.__loadSteps()
        self.__loadTemplates()
        self.__loadTargetTypes()

    def __loadTargetTypes(self):
        self.TARGET_TYPES = {
            "StringMapper"      : "String",
            "PropertiesMapper"  : "Properties"
        }

    def __loadHeader(self):
        self.VERSION = "V0.1.0"
        self.HEADER = "CONFECTORY-CLI - " + self.VERSION
        self.LOGO = "                    ____          __                  \n  _________  ____  / __/__  _____/ /_____  _______  __\n / ___/ __ \/ __ \/ /_/ _ \/ ___/ __/ __ \/ ___/ / / /\n/ /__/ /_/ / / / / __/  __/ /__/ /_/ /_/ / /  / /_/ / \n\___/\____/_/ /_/_/  \___/\___/\__/\____/_/   \__, /  \n                                             /____/ \n"
        self.BR = "-------------------------------------------------------"

    def __loadSteps(self):
        self.STEPS = [["[Step 1A]", False], ["[Step 1B]", False], ["[Step 1C]", True], ["[Step 1D]", False], ["[Step 1E]", True], ["[Step 1F]", True], ["[Step 1G]", True]]
        self.QUESTIONS = {
            "[Step 1A]" : "Define a namespace for the new Configuration (default=""): ",
            "[Step 1B]" : "Enter a precedence for the new Configuration (default=0): ",
            "[Step 1C]" : ["Choose a Source: ", "Dynamic", "Classpath File Source", "File Source"],
            "[Step 1D]" : "Enter the file/resource path (required): ",
            "[Step 1E]" : ["Choose a Mapper: ", "StringMapper", "PropertiesMapper"],
            "[Step 1F]" : ["Is the new configuration Required?", "Yes", "No"],
            "[Step 1G]" : ["Do you want to add another Configuration?", "Yes", "No"]
        }

    def __loadTemplates(self):
        self.TEMPLATE = "Configuration<${targetType}> config = Configuration.<${targetType}>builder()${BR}.namespace(\"[Step 1A]\")${BR}.precedence([Step 1B])${BR}.source(SourceFactory.[Step 1C](\"[Step 1D]\")${BR}.mapper(new [Step 1E]())${BR}.[Step 1F]()${BR}.build()"