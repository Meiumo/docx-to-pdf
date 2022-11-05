from docx import Document
import tkinter
import tkinter.filedialog
from fpdf import FPDF

def write():
    file = open('output.txt', 'w', encoding='utf-8')
    root = None # tkinter.Tk()
    files = tkinter.filedialog.askopenfiles(parent=root, mode='rb', title='Choose a file')
    for i in files:
        doc = Document(i)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        for a in fullText:
            file.write(f'{a}\n')
    file.close()
    txt_to_pdf()

def txt_to_pdf():
    print('second function is working')
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    # pdf.add_font('Times New Roman', '', 'times-new-roman.ttf', uni=True)
    pdf.add_font('arial', '', r"c:\WINDOWS\Fonts\arial.ttf", uni=True)
    pdf.set_font('arial', size = 15)
    file = open('output.txt', 'r', encoding='utf-8')
    for i in file.readlines():
        pdf.multi_cell(w = 0, h = 7, txt = i, align = 'L')
    pdf.output('output.pdf')

write()