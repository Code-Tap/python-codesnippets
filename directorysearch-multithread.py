import logging, os, sys, xlrd
import multiprocessing as mp
from time import sleep
# import openpyxl as xl

source_folder = r'Y:\Unresourced reports\2018'
searchstring = sys.argv[1]

LOG_FILENAME = r'C:\Users\le_wilson\Documents\code\log.txt'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.WARNING,
                    format='%(asctime)s %(message)s'
                    )

Keeplooking = True

def openXls(xls, i, quit, foundit):

    while not quit.is_set():
        workbook = xlrd.open_workbook(xls)
        ws = workbook.sheet_by_index(0)
        for row in range(2, ws.nrows):
            row_value = ws.row_values(row)
            if row_value != xlrd.empty_cell.value:
                if row_value[8] == searchstring:
                    print(f'{i} found {xls}')
                    foundit.set()
                    print(f"Reg Found in {xls}")
                    logging.warning(xls)
                    pass
        print(f'{i} is Done')
        break

def generateFilepaths():
    for root, dirs, files in os.walk(source_folder):
        for name in files:
            (base, ext) = os.path.splitext(name) # split base and extension
            if ext in ('.xls'):          # check the extension
                full_name = os.path.join(root, name) # create full path
                print(full_name)
                yield full_name

if __name__ == '__main__':
    quit = mp.Event()
    foundit = mp.Event()
    for i in range(mp.cpu_count()):
        p = mp.Process(target=openXls, args=(generateFilepaths(), i, quit, foundit))
        p.start()
    foundit.wait()
    quit.set()