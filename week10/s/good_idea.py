#Good Idea :
class PDFReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        # PDF generation logic
        pass
class ExelReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        # Excel generation logic
        pass

class EmailSender:
    def __init__(self, recipient, subject, body):
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send(self):
        # Email sending logic
        pass