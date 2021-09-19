import xlrd
import re,csv,openpyxl

read_location = 'C:\\Users\\1254312\\source\\eBBS.log'
write_location = 'C:\\Users\\1254312\\source\\Log_output.txt'
op_location = 'C:\\Users\\1254312\\source\\Logoutput.xlsx'    
output_sumary = 'C:\\Users\\1254312\\source\\output_summary.txt'
pattern = "## OUT #"
delim = '#'
class EbbsLogAnalysis:
    
    
    def log_fetch():

        #pattern = "## OUT #"
        file = open(read_location, "r")
             
        output_file = open(write_location,'w')
        
        for line in file:
            if re.search(pattern, line):
                output_file.write(line)
        output_file.close()

    def txtToXls():
        #delim = '#'
        wb = openpyxl.Workbook()
        ws = wb.worksheets[0]
        
        with open(write_location, 'r') as data:
            reader = csv.reader(data, delimiter = delim)
            for row in reader:
                ws.append(row)
        wb.save(op_location)


    def logAnalysis():
        wb = openpyxl.load_workbook(op_location)
        sheet = wb.active
        row_count = sheet.max_row
        

        
        zerototwohundred = 0
        twohundredtofour = 0 
        fourhundredtosix = 0
        eighthundredtothousand = 0
        sixhundredtoeight = 0
        twosecondandabove = 0
        twoseconds = 0

        #header = float(sheet.cell_value(0,6))
        #print(header)


        for cell in sheet['B']:
                
                if float(cell.value) < 200:
                    zerototwohundred += 1
                elif float(cell.value)>=200 and float(cell.value)<400:
                    twohundredtofour += 1
                elif float(cell.value)>=400 and float(cell.value)<600:
                    fourhundredtosix += 1
                elif float(cell.value)>=600 and float(cell.value)<800:
                    sixhundredtoeight += 1
                elif float(cell.value)>=800 and float(cell.value)<1000:
                    eighthundredtothousand += 1
                elif float(cell.value)>=1000 and float(cell.value)<2000:
                    twoseconds += 1
                else:
                    twosecondandabove += 1

        zerototwohundred_percent = (zerototwohundred / row_count) * 100
        twohundredtofour_percent = (twohundredtofour / row_count) * 100
        fourhundredtosix_percent = (fourhundredtosix / row_count) * 100
        sixhundredtoeight_percent = (sixhundredtoeight / row_count) * 100
        eighthundredtothousand_percent = (eighthundredtothousand / row_count) * 100
        twoseconds_percent = (twoseconds / row_count) * 100
        twosecondandabove_percent = (twosecondandabove / row_count) * 100

        output_file = open(output_sumary,'w')
        output_file.write('Overall EBBS records considered for Analysis      : {}'.format(row_count))
        output_file.write('\nResponse time from EBBS - 0 to 200 ms             : {} \tand percentage         \t: {}'.format(zerototwohundred,round(zerototwohundred_percent,0)))
        output_file.write('\nResponse time from EBBS - 200 to 400 ms           : {} \tand percentage         \t: {}'.format(twohundredtofour,round(twohundredtofour_percent,0)))
        output_file.write('\nResponse time from EBBS - 400 to 600 ms           : {} \tand percentage         \t: {}'.format(fourhundredtosix,round(fourhundredtosix_percent,0)))
        output_file.write('\nResponse time from EBBS - 600 to 800 ms           : {} \tand percentage         \t: {}'.format(sixhundredtoeight,round(sixhundredtoeight_percent,0)))
        output_file.write('\nResponse time from EBBS - 800 to 1sec             : {} \tand percentage         \t: {}'.format(eighthundredtothousand,round(eighthundredtothousand_percent,0)))
        output_file.write('\nResponse time from EBBS - 1 to 2sec               : {} \tand percentage         \t: {}'.format(twoseconds,round(twoseconds_percent,0)))
        output_file.write('\nResponse time from EBBS - 2secs and above         : {} \tand percentage         \t: {}'.format(twosecondandabove,round(twosecondandabove_percent,0)))

        output_file.close()


    if __name__ == '__main__':
        log_fetch()
        txtToXls()
        logAnalysis()
