
from flask import Flask, render_template, flash, request, Markup, send_file
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from datetime import datetime, timedelta
from collections import defaultdict
import os, sys, xlrd, requests, json, quotepush

q = quotepush.quoteGenForever(quotepush.quotes)
source_folder = r'Y:\Unresourced reports'
source_folder_list = []
found_file = defaultdict(dict)

local_link = '<a href="'
local_link_mid = '">'
local_link_close = '</a>'

# App config.
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    reg = TextField('reg:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def regsearch():
    form = ReusableForm(request.form)
    results = []
    today = currDate()
    yesterdaysDate()
    q2 = next(q)
    if request.method == 'POST':
        reg=request.form['reg']
        dirselect=request.form['dirselect']
        if form.validate():
            cleaned = reg.replace(" ", "").upper() #remove spaces and change to upper case
            main(cleaned, dirselect, results, today) 
            try:
                flashMot(results[4].replace(" ", "").upper())
            except IndexError:
                flashMot(reg)
        else:
            flash('Error: All the form fields are required. ')
    return render_template('regsearch.html', form=form, data=results, sources=source_folder_list, quote_list=q2)

# URL Query string format : /getXLS?timestamp=1-1-10&reg=ABC12DE
@app.route('/getXLS') # this is a job for GET, not POST
def xls_file():
    timestamp  = request.args.get('timestamp', None)
    reg  = request.args.get('reg', None)
    try:
        return send_file(found_file[timestamp][reg],
                        attachment_filename=f'{reg}_report.xls',
                        as_attachment=True)
    except KeyError:
        return ''

@app.route("/", methods=['GET', 'POST'])
def motsearch():
    return ''

def openXls(xls, reg, results, today):
    workbook = xlrd.open_workbook(xls)
    ws = workbook.sheet_by_index(0)
    for row in range(2, ws.nrows):
        row_value = ws.row_values(row)
        if row_value != xlrd.empty_cell.value:
            try:
                if row_value[8].upper() == reg or row_value[3].replace(" ", "").upper() == reg or reg in row_value[20].replace(" ", ""):
                    found_file[today][reg] = xls
                    message = Markup(f"{local_link}/getXLS?timestamp={today}&reg={reg}{local_link_mid}{xls}{local_link_close}") #{reg} Found in 
                    flash(message)
                    results.append(row_value[0])
                    results.append(row_value[2])
                    results.append(row_value[3])
                    results.append(row_value[7])
                    results.append(row_value[8])
                    results.append(row_value[17])
                    results.append(row_value[19])
                    results.append(row_value[20])
                    return xls
            except:
                pass
    return False

def sources():
    for root, dirs, files in os.walk(source_folder):
        if os.path.abspath(root) not in source_folder_list:
            source_folder_list.append(os.path.abspath(root))

def main(reg, dirselect, results, today):
    found = False
    for root, dirs, files in os.walk(dirselect):
        files.sort(reverse=True)
        for name in files:
            (base, ext) = os.path.splitext(name) # split base and extension
            if ext in ('.xls'):          # check the extension
                full_name = os.path.join(root, name) # create full path
                if openXls(full_name, reg, results, today) != False:
                    found = True
                    break
        else:
            #if not excel file.. continue
            continue
        # If you get here, Its not been found
    if not found:
        flash(f'Error: {reg} Not Found. ')

def getDetails(registration):
    headers = {
        'Accept': 'application/json+v3', 
        'x-api-key': 'APIKEY'
        }
    url = f'https://beta.check-mot.service.gov.uk/trade/vehicles/mot-tests?registration={registration}'
    r = requests.get(url, headers=headers)
    return r.json()

def yesterdaysDate():
    d = datetime.now()
    y = d + timedelta(days=-1)
    y.strftime("%Y-%m-%d")
    if y in found_file:
        found_file.pop(y)
        sources()
    # print('Sleeping for 2 Hours')
    # sleep(7200)

def currDate():
    d = datetime.now()
    return d.strftime("%Y-%m-%d")

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return (d2 - d1).days

def days_betweenDot(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y.%m.%d")
    return (d2 - d1).days

def checkResponse(json_date):
    try:
        if json_date['httpStatus'] == '404':
            return str('404')
    except:
        pass
    try:
        datetime.strptime(json_date[0]['motTests'][0]['expiryDate'], "%Y.%m.%d")
    except:
        pass
    else:
        return str('Nested')

    try:
       datetime.strptime(json_date[0]['motTestDueDate'],"%Y-%m-%d")
    except:
        pass
    else:
        return str('Notnested')

def flashMot(reg):
    try:
        i = getDetails(reg)
        if checkResponse(i) == 'Notnested':
            mot = i[0]['motTestDueDate']
            mot1 = datetime.strptime(mot, '%Y-%m-%d').strftime('%d/%m/%Y')
            if days_between(currDate(), mot) < 0:
                flash(f'Error : uh-oh MOT Expired {mot1}')
            else:
                flash(f'This car has a Valid MOT until {mot1}')
        elif checkResponse(i) == 'Nested':
            mot = i[0]['motTests'][0]['expiryDate']
            mot1 = datetime.strptime(mot, '%Y.%m.%d').strftime('%d/%m/%Y')
            if days_betweenDot(currDate(), mot) < 0:
                flash(f'Error : uh-oh MOT Expired {mot1}')
            else:
                flash(f'This car has a Valid MOT until {mot1}')
        elif checkResponse(i) == '404':
            flash('Error : Could not confirm the MOT status of this Vehicle')
        elif not checkResponse(i):
            flash('Error : uh-oh MOT Expired')
    except:
        flash('Error : DVLA MOT Service currently down')   #Could not confirm the MOT status of this Vehicle
        pass

if __name__ == "__main__":
    sources()
    app.run(host='0.0.0.0', debug=False, port=5000, threaded=True)