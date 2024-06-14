import xlwt
import MySQLdb

class BookExporter:
    def __init__(self):
        self.db = None
        self.cur = None

    def export_books(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT book_code, book_name, book_description, book_category, book_author, book_publisher, book_price FROM book''')
        data = self.cur.fetchall()

        wb = xlwt.Workbook()
        sheet = wb.add_sheet('Books')

        sheet.write(0, 0, 'Book Code')
        sheet.write(0, 1, 'Book Name')
        sheet.write(0, 2, 'Book Description')
        sheet.write(0, 3, 'Book Category')
        sheet.write(0, 4, 'Book Author')
        sheet.write(0, 5, 'Book Publisher')
        sheet.write(0, 6, 'Book Price')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.save('all_books.xls')
        print('Book Report Created Successfully')

        self.cur.close()
        self.db.close()

# Create an instance of the BookExporter class and call the export_books method
exporter = BookExporter()
exporter.export_books()