import xlrd
import json

# Open the Excel file
excel_book = xlrd.open_workbook('/home/kathirvel/Downloads/English-Tamil-Dictionary.xls')

# Get the sheet
# sheet '1' is unicode
excel_sheet = excel_book.sheet_by_index(1)
# Create word dictionary
word_dictionary = []
# World List
word_list = []

# Read row from excels sheet to get tamil and english words
# Get the totals rows
for row in range(2, excel_sheet.nrows):
    english_word = str(excel_sheet.cell_value(row, 0)).encode("utf-8")
    tamil_word = unicode(excel_sheet.cell_value(row, 1)).encode("utf-8")
    word_dictionary.append({"eng":english_word, "tamil":tamil_word})
    word_list.append(english_word)
    print "%s\n" % english_word
    print "%d/%d rows completed!" % (row, excel_sheet.nrows-1)

word_dictionary.append({"word_list":word_list})

with open('dictionary.json', 'w') as f:
    json.dump(word_dictionary, f, ensure_ascii=False)
