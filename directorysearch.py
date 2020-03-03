import logging, os, sys, xlrd, ctypes
from plyer import notification
from tkinter import *

MessageBox = ctypes.windll.user32.MessageBoxW

source_folder = r'Y:\Unresourced reports\2018'
searchstring = sys.argv[1]

LOG_FILENAME = r'C:\Users\le_wilson\Documents\code\log.txt'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.WARNING,
                    format='%(asctime)s %(message)s'
                    )

def openXls(xls):
    workbook = xlrd.open_workbook(xls)
    ws = workbook.sheet_by_index(0)
    for row in range(2, ws.nrows):
        row_value = ws.row_values(row)
        if row_value != xlrd.empty_cell.value:
            if row_value[8] == searchstring:
                print(f"Reg Found in {xls}")
                results.extend(row_value)
                notification.notify(
                    title=f'{sys.argv[1]} FOUND!',
                    message=f'{xls}',
                    )
                return xls
    return False

def main():
    for root, dirs, files in os.walk(source_folder):
        for name in files:
            (base, ext) = os.path.splitext(name) # split base and extension
            if ext in ('.xls'):          # check the extension
                full_name = os.path.join(root, name) # create full path
                #print(full_name)
                if openXls(full_name) != False:
                    logging.warning(full_name)
                    results.insert(0,full_name)
                    break
        else:
            continue
        break


        
if __name__ == "__main__":

    results = []
    notification.notify(title= 'Unresourced Report Search',
        message= '                   scanning started',
        timeout=3)
    main()
    display = results[0],results[1],results[3],results[8],results[9],results[10],results[20],results[21]
    '\n'.join(display)
    print(display)
    
    #MessageBox(None, f'{results}', 'Registration Found!', 0)
    MessageBox(None, f'{(display)}', 'Registration Found!', 0)

    del results[:]

# MessageBox = ctypes.windll.user32.MessageBoxW
# MessageBox(None, 'Hello', 'Window title', 0) 'range from 0 to 7'
