import requests, asyncio, lxml, re, concurrent.futures
from bs4 import BeautifulSoup

class PortalLoginSession:
    '''Class to login to and handle the sessions for the work portal sites'''
    
    def __init__(self):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}
        self.s = requests.Session()
        self.s.headers.update(headers)

    def login(self, login_user, password):
        
        URL = "http://inspect.portal.manheim.co.uk/Login.aspx"
        page = self.s.get(URL)
        soup = BeautifulSoup(page.content, 'lxml')
        VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
        VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value']
        login_data = {"__VIEWSTATE":VIEWSTATE,
        "__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
        "ctl00$ContentPlaceHolder1$Login1$UserName":login_user,
        "ctl00$ContentPlaceHolder1$Login1$Password":password,
        "ctl00$ContentPlaceHolder1$Login1$LoginButton":"Log In"}
        return self.s.post(URL, data=login_data)

    def is_regInspected(self):
        params = {'s&r' : reg, 'brnchid' : 41}
        resp = self.s.get('http://inspect.portal.manheim.co.uk/InspectionSearch.aspx', params=params) #VN61LNG no pdf
        soup = BeautifulSoup(resp.content, 'lxml')
        tbl = soup.findChildren(id="InspectionListGridView")
        try:
            myTable = tbl[0]
        except:
            print("No Inspection")
            return False
            pass
        else:
            print("Inspected")
            return True
    
    def is_regAborted(self):
        resp = self.s.get('http://inspect.portal.manheim.co.uk/InspectionSearch.aspx?s&r=' + 'SH15VOM' + '&brnchid=41&') #VN61LNG no pdf
        soup = BeautifulSoup(resp.content, 'lxml')
        tbl = soup.findChildren(id="InspectionListGridView")
        data = {}
        myTable = tbl[0]

        table_body = myTable.find('tbody')
        rows = table_body.findChildren('tr')
        #cols = table_body.findChildren('td')
        #link = table_body.findChildren('a')

        #Logic to detect cell values here
        for row in rows[:1]:
            cells = row.findChildren('td')
            data['url'] = cells[1].find(text=True)   #Link to Inspection
            data['Registration'] = cells[2].find(text=True)    #Registration
            data['Name'] = cells[3].find(text=True)    #Inspector Name
            data['Abort'] = cells[9].find(text=True)   #Aborted or Not
            print (data)
        
        if 'Aborted' in data.values():
            print("True")
            return True
        elif 'Aborted' not in data.values():
            print("False")
            return False
        pass
    
    def is_pdfAvailible(self):
        resp = self.s.get('http://inspect.portal.manheim.co.uk/ViewInspection.aspx?id=' + '1108872') # no pdf 1090878
        soup = BeautifulSoup(resp.content, 'lxml')
        pdflinks = []
        try:
            if soup.select_one("span[id*=ctl00_ContentPlaceHolder1_MissingDocumentsLabel]").text == 'No documents were returned.':
                print(soup.select_one("span[id*=ctl00_ContentPlaceHolder1_MissingDocumentsLabel]").text)
            
            #nopdf = soup.findChildren(id="ctl00_ContentPlaceHolder1_MissingDocumentsLabel")
            #if re.search(r'\bNo documents were returned\b',str(nopdf)) is not None:
            pass
        except:
            return True

    def get_Pdflink(self):
        resp = self.s.get('http://inspect.portal.manheim.co.uk/ViewInspection.aspx?id=' + '1108872') # no pdf 1090878
        soup = BeautifulSoup(resp.content, 'lxml')
        pdflinks = []
        print('PDF availible... continuing')
        tbl = soup.findChildren(id="ctl00_ContentPlaceHolder1_pnlConditionReports")
        data = {}
        try:
            myTable = tbl[0]
        except:
            print("No PDF")
            pass
        else:
            #Get PDF Links
            table_body = myTable.find('tbody')
            link = table_body.find_all('a', href = True)
            for lnk in link:
                lnkStr = str(lnk)
                if re.search(r'\bIMS\b',lnkStr):
                    pdflinks.append(lnk['href'])
                else:
                    pass
            print(set(pdflinks))

##### End of Class #####

async def main1():

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get, 'http://inspect.portal.manheim.co.uk/')
            for i in range(2000)
                ]
        for response in await asyncio.gather(*futures):
            print(response)
            pass

def main():
    a = PortalLoginSession()
    a.login('Username', 'Password')
    a.is_regInspected()
    a.is_regAborted
    a.is_pdfAvailible()
    a.get_Pdflink()

# End of Global Functions ###

if __name__ == '__main__':
    main()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())