import openpyxl
from scripts.handle_os import EXCEL_PATH


class Obj:
    pass


class HandleExcel:
    def __init__(self, sheetname, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = EXCEL_PATH
        self.sheetname = sheetname

    def open_excel(self):
        self.workbook = openpyxl.open(self.filepath)
        self.sheet = self.workbook[self.sheetname]

    def read_excel(self):
        self.open_excel()
        result_rows = list(self.sheet.rows)
        head_li = [h.value for h in result_rows[0]]
        list_obj = []
        for va in result_rows[1:]:
            obj = Obj()
            value_li = [v.value for v in va]
            zip_vh = zip(head_li, value_li)
            for zv in zip_vh:
                setattr(obj, zv[0], zv[1])
            list_obj.append(obj)
        self.workbook.close()
        return list_obj

    def write_excel(self, row_num, col_num, value):
        self.open_excel()
        self.sheet.cell(row=row_num, column=col_num, value=value)
        self.workbook.save(self.filepath)
        self.workbook.close()


if __name__ == '__main__':
    he = HandleExcel('register')
    print(he.read_excel())
    print(he.read_excel()[0].data)
    he.write_excel(2, 7, 'ok')