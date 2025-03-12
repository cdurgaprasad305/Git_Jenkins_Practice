# import openpyxl
import xlrd # used for Excel (97-2000 .xls formate file)

class ExcelUtility:
    def __init__(self, file_path):
        self.file_path = file_path
        print("----Excel file Path", file_path)
        self.workbook = xlrd.open_workbook(file_path)

    def get_cell_data(self, sheet_name, row, column):
        sheet = self.workbook.sheet_by_name(sheet_name)
        return sheet.cell_value(row, column)  # xlrd is 0-based index

    def get_row_count(self, sheet_name):
        sheet = self.workbook.sheet_by_name(sheet_name)
        return sheet.max_row
