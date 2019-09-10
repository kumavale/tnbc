import sys
import requests
from bs4 import BeautifulSoup

class Color:
    RESET = '\033[0m'
    RED   = '\033[38;05;009m'

global argc, argv
URL = 'https://www.toshocardnext.ne.jp/tosho/pc/CardUserLoginPage/'

def open():
    card_no1 = argv[1]
    card_no2 = argv[2]
    card_no3 = argv[3]
    card_no4 = argv[4]
    pin      = argv[5]

    ses = requests.Session()
    res = ses.get(URL + 'open.do')
    res.raise_for_status()

    bs4_obj = BeautifulSoup(res.text, 'html.parser')

    struts = bs4_obj.find('input', {'name':'org.apache.struts.taglib.html.TOKEN'})['value']

    payload = {
            'org.apache.struts.taglib.html.TOKEN': struts,
            'cardNo1': card_no1,
            'cardNo2': card_no2,
            'cardNo3': card_no3,
            'cardNo4': card_no4,
            'pin': pin,
            'dummyPassword1': ' ',
            'x': '0',
            'y': '0'
            }

    res = ses.post(URL + 'login.do', data=payload)
    res.raise_for_status()

    return res


def result(res):
    bs4_obj = BeautifulSoup(res.text, 'html.parser')

    cloud_login = bs4_obj.select('.login')[0].text
    if cloud_login != 'ご利用状況':
        print(f'tnbc: {Color.RED}error: {Color.RESET}Login failed', file=sys.stderr)
        sys.exit(1)

    cell_names  = bs4_obj.select('.cell-name')
    cell_items  = bs4_obj.select('.cell-item')

    for i in range(3):
        print(cell_names[i].text.replace('\n','') + ' : ' + cell_items[i].text.replace('\n',''))

    # History
    # Not just yet.


if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)

    if (argc != 6):
        print(f'tnbc: {Color.RED}error: {Color.RESET}Invalid arguments', file=sys.stderr)
        print("Usage: `python tnbc.py [ID1] [ID2] [ID3] [ID4] [PIN]`")
        sys.exit(1)

    res = open()
    result(res)

