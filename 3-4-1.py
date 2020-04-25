import sys
import io
from bs4 import BeautifulSoup
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저 정보
LOGIN_INFO = {
    'user_id' : 'gkscoals1',
    'user_pw' : 'rjwufkrh1!'
}

#Session 생성, with 구문 안에서 유지
with requests.Session () as s :
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data = LOGIN_INFO)
    #HTML 소스 확인
    print('login_req', login_req.text)

    #Header 확인
    print('headers', login_req.headers)

    if login_req.status_code == 200 and login_req.ok :
        post_one = s.get('https://bbs.ruliweb.com/market/board/32/read/4711646?')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #board_read > div > div.board_main > div.board_main_view > div.view_content.autolink
        # print(soup.prettify())
        article = soup.select("#board_read > div > div.board_main > div.board_main_view > div.view_content.autolink > div")
        print(article)

        #ex
        for i in article :
            if i.string is not None :
                #DB INSERT, 엑셀로 저장, 텍스트 가공
                print(i.string)
