import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청 URL
URL = 'https://www.wishket.com/accounts/login/'

#Fake User-Agent 생성
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)

with requests.Session() as s:
    #URL 연결
    s.get(URL)

    #Login 정보 Payload
    LOGIN_INFO = {
        'identification' : 'gkscoals1',
        'password': 'rjwufkrh1!',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    # print('header', s.headers)
    # print('token', s.cookies['csrftoken'])

    # {'Connection': 'keep-alive', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'python-requests/2.23.0'}

    #요청
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer' : 'https://www.wishket.com/accounts/login/'})

    #HTML 결과 확인
    print('response' , response)
    # print('response' , response.text)

    if response.status_code == 200 and response.ok :
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("table.table-responsive > tbody > tr")
        # print(projectList)
        for i in projectList :
            print(i.find('th').string, i.find('td').text)
