from pypdf import PdfReader

reader = PdfReader('week3/sample.pdf')
print('Pages', len(reader.pages))

total = 0
for i in range(len(reader.pages)):
    text = reader.pages[i].extract_text()
    words = text.split()
    print('Page', i + 1, ':', len(words), 'words')
    total = total + len(words)
    if len(words) < 20:
        print('Page', i + 1, ':', '<- check this page')
print('Total in all document', ':', total, 'words')
