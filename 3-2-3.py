import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream = True)
# print(r.text)

#출력해보면 json 오류, array가 아닌 개행처리로 쭉 나열 되어 있음
# print(r.json())
print(r.encoding)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    # print(line)
    b = json.loads(line)
    print(b['origin'])
    for e in b.keys():
        print('key : ', e , 'value : ', b[e])
