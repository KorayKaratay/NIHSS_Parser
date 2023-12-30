#Contains function def and bodyies for NIHSS_Parser.py
import xml.etree.ElementTree as ET 

#Global variable for XML file
tree=0
root=0
exams=0
filename=0

#Setter funciton for XML file
def setXML(file):
    global tree,root,exams,filename
    filename=file    
    tree = ET.parse(file)
    root = tree.getroot()
    exams =[ root.find('Exam_Entry'), root.find('Exam_Extern'), root.find('Exam_1MControl')]
    

def patientİnfoPrint():
    print("Patient İnofrmation\n--")
    # Prints the Patient information in the XML child note Patient_info
    print("Patient Dossier No:",root.find('Patient_info').find('ID').text)
    print("Name:",root.find('Patient_info').find('Name').text)
    print("Surname:",root.find('Patient_info').find('Surname').text)
    #İf statement to detect if tPA is given to patient
    if (root.find('is_tPA_given').text)=='True':
        print("Patient has taken tPA")
    else:
        print("Patitent has not taken tPA")
    print("--")

def patientExamPrint(Exam):
    #All values in the patient xml is string. Check the test.xml for that 'magic values'
    #An index value will change over course
    print(Exam.tag,"-> Begin Examination--")
    print("Examination:",Exam.tag)
    index = int(Exam.find('Consiousness').text)
    if index == 3:
        print("1a.Komatous")
    elif index == 2:
        print("1a.Stupor")
    elif index == 1:
        print("1a.Konfous/Obluntation")
    else:
        print("1a.Alert")
    index=int(Exam.find('Orientation').text)
    if index == 2:
        print("1b.No Orientation")
    elif index ==1:
        print("1b.Semi-orientated")
    else:
        print("1b.Orientated")
    index = int(Exam.find('Consiousness').text)
    if index == 2:
        print("1c.Not cooperated")
    elif index ==1:
        print("1c.Semi cooperated")
    else:
        print("1c.Full cooperation")
    index=int(Exam.find('Eye').find('Movements').text)
    if index == 2:
        print("2.Total paralysis or deviation")
    elif index == 1:
        print("2.Oftalmoparsia")
    else :
        print("2.Normal eye movement")
    index = int(Exam.find('Eye').find('Vision').text)
    if index == 3:
        print("3.Bilateral Hemianopsia")
    elif index == 2:
        print("3.Unilateral Hemianopsia")
    elif index == 1:
        print("3.Parsial Hemianopsia")
    else :
        print("3.Normal eye vision")
    index = int(Exam.find('Facial').text)
    if index == 3:
        print("4.Total facial paralysis")
    elif index == 2:
        print("4.Complete lower facial paralysis")
    elif index == 1:
        print("4.Slight facial asymetry")
    else :
        print("4.Normal facial exam")
    index =Exam.find('Muscle')
    print("5. and 6.")
    for child in index:
        print("Muscle stenght in",child.tag,":",int(child.text))
    index = int(Exam.find('Cerebellar').text)
    if index == 2:
        print("7.Bilateral ataxia")
    elif index == 1:
        print("7.Unilateral ataxia")
    else :
        print("7.No ataxic movement")
    index = int(Exam.find('Sensory').text)
    if index == 2:
        print("8.Coma or complete anestesia")
    elif index == 1:
        print("8.Hypoestesia")
    else :
        print("8.Normal sensory exam")
    index = Exam.find('Language')
    #Language has two childs. Afphazia and Disartia
    if (int(index.find("Aphasia").text))==3:
        print("9.Global Aphasia")
    elif (int(index.find("Aphasia").text))==2:
        print("9.Heavy Aphasia")
    elif (int(index.find("Aphasia").text))==1:
        print("9.Mild Aphasia")
    else:
        print("9.No Aphasia")
    if (int(index.find("Dysarthria").text))==2:
        print("10.Heavy Dysarthria")
    elif (int(index.find("Dysarthria").text))==1:
        print("10.Mild Dysarthria")
    else:
        print("10.No Dysarthria")
    index =int(Exam.find('Neglect').text)
    if index == 2:
        print("11.Multipl modality neglect")
    elif index == 1:
        print("11.One modality neglect")
    else :
        print("11.No neglect")
    print("Calculated NIHSS Score:",Exam.find('NIHSS_Score').text)
    print("--End Examination--\n")

def calculateNIHSS(Exam,tree,filename):
    #tree and filename must be included in order to write it to the file
    #All values in the patient xml is string. Check the test.xml for that 'magic values'
    NIHSS_Score=0
    #an index value that will iterate over the examination findings
    index=int(Exam.find('Consiousness').text)
    NIHSS_Score += index
    index=int(Exam.find('Orientation').text)
    NIHSS_Score += index
    index=int(Exam.find('Cooperation').text)
    NIHSS_Score += index
    index=int(Exam.find('Eye').find('Movements').text)
    NIHSS_Score += index
    index=int(Exam.find('Eye').find('Vision').text)
    NIHSS_Score += index
    index=int(Exam.find('Facial').text)
    NIHSS_Score += index
    index=Exam.find('Muscle')
    for child in index:
        if((int(child.text))<4):
            NIHSS_Score += (4-int(child.text)) 
    '''This converts muscle stenght grading into NIHSS score
    Muscle strenght 5/5 and 4/5 should be counted
    as 0 while patient won't hit the bed when arms and legs
    are raised 3/5=1(won't touch bed) and so on until 0/5 = 4
    '''
    index=int(Exam.find('Cerebellar').text)
    NIHSS_Score += index
    index=int(Exam.find('Sensory').text)
    NIHSS_Score += index
    index=Exam.find('Language')
    #Language has two childs. Afazia and Disartia
    NIHSS_Score+=(int(index.find("Aphasia").text))
    NIHSS_Score+=(int(index.find("Dysarthria").text))
    index=int(Exam.find('Neglect').text)
    NIHSS_Score += index
    Exam.find('NIHSS_Score').text=str(NIHSS_Score)
    tree.write(filename)
