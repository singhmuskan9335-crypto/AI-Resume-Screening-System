import fitz

def extract_text_from_pdf(pdf_file):

    # Reset the file pointer
    pdf_file.seek(0)

    text = ""

    pdf = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text