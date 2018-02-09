from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



class Mark():

    def add(pdffile,nome,cpf,user_pass):


        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(10, 10, 'Conteúdo liberado para: %s.%s.%s-%s | %s'%(cpf[0:3],cpf[3:6],cpf[6:9],cpf[9:11],nome))
        can.save()


        packet.seek(0)

        new_pdf = PdfFileReader(packet)

        existing_pdf = PdfFileReader(open(pdffile, "rb"))
        output = PdfFileWriter()
        output.encrypt(user_pass, use_128bit=True)
        outputStream = open('%s_%s.pdf'%(pdffile[:-4],cpf[6:]), "wb")
        count_page = 0
        while count_page < existing_pdf.getNumPages():
            page = existing_pdf.getPage(count_page)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            output.write(outputStream)
            count_page += 1

        outputStream.close()

        return None

if __name__ == '__main__':
    result = Mark.add('Files\\a-criptomoeda-que-pode-render-mais-que-o-bitcoin-em-2018.pdf','Diego Fellipe Antunes Pedrosa','30312122233','Senha123')
