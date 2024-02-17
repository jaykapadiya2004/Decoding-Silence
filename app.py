# app.py
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from generate_question import *
app = Flask(__name__)

def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PdfReader(pdf_file)
    num_pages = len(reader.pages)
    for page_number in range(num_pages):
        page = reader.pages[page_number]
        text += page.extract_text()
    return text

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    pdf_file = request.files.get('pdf_file')
    image_file = request.files.get('image_file')
    text_input = request.form.get('text_input')
    output = ''
    if pdf_file:
        pdf_text = extract_text_from_pdf(pdf_file)
        output = choice(0,pdf_text)
    elif image_file:
        # Process the image file...
        output = choice(1,image_file)
    elif text_input:
        output = choice(0,text_input)
    else:
        return 'No input provided'
    return output

if __name__ == '__main__':
    app.run(debug=True)
