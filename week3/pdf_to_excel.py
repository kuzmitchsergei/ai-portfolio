from pypdf import PdfReader
from openpyxl import Workbook
from openpyxl.styles import Font

reader = PdfReader('week3/sample.pdf')

wb = Workbook()
ws = wb.active
ws.title = 'Pages'
ws.append(['Page', 'Words', 'Check'])

for i in range(len(reader.pages)):
    text = reader.pages[i].extract_text()
    words = text.split()
    if len(words) < 20:
        flag = 'yes'
    else:
        flag = ''
    ws.append([i + 1, len(words), flag])

ws.freeze_panes = 'A2'
ws.auto_filter.ref = ws.dimensions
for cell in ws[1]:
    cell.font = Font(bold=True)

wb.save('week3/tender_pages.xlsx')
print('Saved week3/tender_pages.xlsx')


