class Machine:
    def print(self,document):
        pass
    def scan(self,document):
        pass
    def fax(self,document):
        pass

class Oldprinter(Machine):
    def print(self,document):
        print("Printing document")
    def scan(self,document):
        raise NotImplementedError("Scan not supported")
    def fax(self,document):
        raise NotImplementedError("Fax not supported")
    
x = Oldprinter()
x.print("My Document")
