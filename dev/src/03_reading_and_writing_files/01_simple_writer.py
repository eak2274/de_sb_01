import csv

def write_sample_file():
    output = open('myCSV.CSV', mode='w', newline='', encoding='utf-8')
    writer = csv.writer(output)
    header = ['name', 'age']
    writer.writerow(header)
    data_row_1 = ['Billy Jones', 30]
    data_row_2 = ['Maggy Ryan', 25]
    writer.writerow(data_row_1)
    writer.writerow((data_row_2))
    output.close()

if __name__ == '__main__':
    write_sample_file()
