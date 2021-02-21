import PyPDF2 
import sys
import os 
import random
import string
import webbrowser


try:
    droppedFile = sys.argv[1]
    name = ""
    path = os.path.expanduser('~')+"\Documents\Lipdukai\\"
    with open(sys.argv[1],'rb') as fin:
        pdf = PyPDF2.PdfFileReader(fin)
        page = pdf.getPage(0)
    
        page.cropBox.lowerLeft = (10, 415.196850394)
        page.cropBox.upperRight = (303.464566929, 821)

    
        output = PyPDF2.PdfFileWriter()
        output.addPage(page)

        name = path+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))+".pdf"
        if not os.path.exists(path):
            os.makedirs(path)            
        with open(name,'wb') as fo:
            output.write(fo)
    webbrowser.open_new(name)
    
    
except IndexError:
    print("No file dropped")