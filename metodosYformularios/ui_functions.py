
## ==> GUI FILE
from main import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):
  
    ## ==> UI DEFINITIONS
    def uiDefinitions(self):


        # MINIMIZE
        self.ui.pushButton_8.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.pushButton_7.clicked.connect(lambda: self.close())

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE
