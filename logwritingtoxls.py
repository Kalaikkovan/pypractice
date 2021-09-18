import re,csv,openpyxl

read_location = '/home/kalai/Projects/python/IBM_log.txt'
write_location = '/home/kalai/Projects/python/output.txt'
op_location = '/home/kalai/Projects/python/output.xls'    

def log_fetch():
    read_location = '/home/kalai/Projects/python/IBM_log.txt'
    write_location = '/home/kalai/Projects/python/output.txt'
    
    file = open(read_location, "r")
    pattern = "TRACE"
    
    output_file = open(write_location,'w')


    for line in file:
        if re.search(pattern, line):
            output_file.write(line)
    output_file.close()

def txtToXls():
    
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]
    
    with open(write_location, 'r') as data:
        reader = csv.reader(data, delimiter = ' ')
        for row in reader:
            ws.append(row)
    wb.save(op_location)
    

log_fetch()
txtToXls()