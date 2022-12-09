from fpdf import FPDF
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=15)
f=open("new2.txt","r")
for x in f :
    pdf.cell(200,10,txt=x , ln=1,align="c")
pdf.output("new2.pdf")