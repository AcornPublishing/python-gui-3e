'''
Created on Jun 9, 2019
Ch08
@author: Burkhard
'''

import unittest
from Ch08_Code.LanguageResources import I18N
from Ch08_Code.GUI_Refactored import OOP as GUI

class GuiUnitTests(unittest.TestCase):
    
    def test_TitleIsEnglish(self):
        i18n = I18N('en')
        self.assertEqual(i18n.title, 
                         "Python Graphical User Interface")
        
    def test_TitleIsGerman(self):
        # i18n = I18N('en')           # <= Bug in Unit Test
        i18n = I18N('de') 
        self.assertEqual(i18n.title, 
                         'Python Grafische Benutzeroberfl' 
                         + "\u00E4" + 'che')
 
class WidgetsTestsEnglish(unittest.TestCase):
     
    def setUp(self):
        self.gui = GUI('en')
        
    def tearDown(self):
        self.gui = None
         
    def test_WidgetLabels(self):
        self.assertEqual(self.gui.i18n.file, "File")
        self.assertEqual(self.gui.i18n.mgrFiles, ' Manage Files ')
        self.assertEqual(self.gui.i18n.browseTo, 
                                            "Browse to File...")

#==========================                          
if __name__ == '__main__':
    unittest.main()
    
    

