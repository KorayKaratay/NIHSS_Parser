import libNIHHSParser as np
import os
'''
Written by Koray Karatay
koray.karatay@hotmail.com
Following Python script parses the NIHSS score from an XML file
You can find how NIHSS is calculated from here->
https://www.ninds.nih.gov/sites/default/files/documents/NIH_Stroke_Scale_508C_0.pdf
For now XML files has to be filled manually, No GUI
'''


def printExamine(file):    
    np.setXML(file)
    np.patientİnfoPrint()
    for np.exams in np.exams:
        np.patientExamPrint(np.exams)
def printHeader(file):
    np.setXML(file)
    np.patientİnfoPrint()

def calcuteExamine(file):
    np.setXML(file)
    for np.exams in np.exams:
        np.calculateNIHSS(np.exams,np.tree,np.filename)

#Test statement 
''' 
Output Must be this=
#John Doe={18, 11, 3}
#Jen  Doe={16, 12, 3}
#Jane Doe={15, 9 , 1}
directory = './Test_Data'
files = os.listdir(directory)
for file in files:
    printHeader(f'./Test_Data/{file}')
    calcuteExamine(f'./Test_Data/{file}')
'''
'''Main Call. İteretas over all files in Data directory and calculates
NIHSS score for each respectively
'''
directory = './Data'
files = os.listdir(directory)
for file in files:
    printHeader(f'./Data/{file}')
    calcuteExamine(f'./Data/{file}')
