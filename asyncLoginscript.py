import asyncio
from concurrent.futures import ProcessPoolExecutor

import aiohttp
import lxml.html

def process_login_page(html):
    page = lxml.html.fromstring(html)
    VIEWSTATE = page.xpath('//input[@id="__VIEWSTATE"]/@value')
    VIEWSTATEGENERATOR = page.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')
    login_data = {
        "__VIEWSTATE":VIEWSTATE,
        "__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
        "ctl00$ContentPlaceHolder1$Login1$UserName":'LOGINGREDENTIALS',
        "ctl00$ContentPlaceHolder1$Login1$Password":'LOGINGREDENTIALS',
        "ctl00$ContentPlaceHolder1$Login1$LoginButton":"Log In"
        }
    return login_data

def check_loggedin(html):
    page = lxml.html.fromstring(html)
    if page.xpath('//a[@id="ctl00_LoginView1_UserLoginStatus"]/@VALUE') == 'Log in':
        return False
    elif if page.xpath('//a[@id="ctl00_LoginView1_UserLoginStatus"]/@VALUE') != 'Log in':
        return True

def process_page(html):
    '''Meant for CPU-bound workload'''

    tree = lxml.html.fromstring(html)
    return tree.find('.//title').text


async def fetch_page(url, session):
    '''Meant for IO-bound workload'''
    async with session.get(url, timeout = 15) as res:
      return await res.text()


async def process(url, session, pool):
    html = await fetch_page(url, session)
    return await asyncio.wrap_future(pool.submit(process_page, html)

async def loginsession(url, session):
    async with session.get(url) as res:
          loginpayload = await res.read()
            async with session.post(url,
              data=process_login_page(loginpayload)) as res:
                return await check_loggedin(res.text())

async def dispatch(urls):
    pool = ProcessPoolExecutor()
    async with aiohttp.ClientSession() as session:
        if loginsession(loginurl, session)
        coros = (process(url, session, pool) for url in urls)
        return await asyncio.gather(*coros)


def main():
    loginurl = 'http://inspect.portal.manheim.co.uk/Login.aspx'
    urls = ['https://facebook.com',
            'https://bbc.co.uk',
            'http://www.abc.net.au',
            'http://www.xinhuanet.com',
            'https://github.com',
            'https://google.com',
            'https://microsoft.com',
            'https://yahoo.com',
            'https://www.amazon.co.uk',
            'https://www.pistonheads.com',
            'http://inspect.portal.manheim.co.uk',
            'https://www.passmyparcel.com',
            'https://etlsh.com',
            'https://gist.githubusercontent.com',
            'http://kata.coderdojo.com/wiki/Home_Page',
            'https://gkoberger.github.io/stacksort'
            'https://stackoverflow.com/',
            'https://serverfault.com/',
            'https://askubuntu.com/',
            'https://unix.stackexchange.com/'            
            ]
    result = asyncio.get_event_loop().run_until_complete(dispatch(urls))
    print(result)

if __name__ == '__main__':
    main()
