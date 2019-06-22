from src.employee import Employee


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
