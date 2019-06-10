class ExcelConverter:
    column_start_ascii = 65
    column = None
    column_number = None
    column_literal_base = 26

    def value(self, column_literal):
        return (ord(column_literal) - self.column_start_ascii) + 1

    def is_valid_column(self):
        return self.column.isalpha()

    def to_capital(self):
        self.column = self.column.upper()

    def to_column_number(self):
        if self.is_valid_column():
            self.to_capital()
            self.column = self.column[::-1]
            self.column_number = 0
            for i, literal in enumerate(self.column):
                self.column_number += pow(self.column_literal_base, i) * self.value(literal)
