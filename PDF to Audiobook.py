import pyttsx3
import PyPDF2
book = open('XII BST Case Studies-ch-2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()

speaker.say('Hey listen I can speak')
speaker.runAndWait()