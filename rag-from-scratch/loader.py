import PyPDF2


class Loader:
    """
    loads the text from the pdf files
    """
    def __init__(self,file_path):
        self.file = file_path

    def load(self):
        reader = PyPDF2.PdfReader(self.file)
        text = ""

        for page in reader.pages:
            text = text + page.extract_text()
        return text