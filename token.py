# # 샘플 Python 스크립트입니다.
#
# # Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# # 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
#
#
import requests
# 이건 나에게
# url = 'https://kauth.kakao.com/oauth/token'
# rest_api_key = 'bcc25462aacf0ec8c9bc01a4b9eccfb1'
# redirect_uri = 'https://localhost:9988'
# authorize_code = 'd7xRYUVp1Zl8eOGqdDTcxMogz5Y5yqPaOa68SFw4iA4fdOWJLq3OX2Z7BWwT1I7ds_6ROQopyNkAAAGATrPEcA'
#
# data = {
#     'grant_type':'authorization_code',
#     'client_id':'bcc25462aacf0ec8c9bc01a4b9eccfb1',
#     'redirect_uri':redirect_uri,
#     'code': authorize_code,
#     'client_secret' : 'ecuwWZTCW0rjGFtKJMZCQmeogHxAijib'
#     }
#
# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)
#
# # json 저장
# import json
# #1.
# with open(r"C:\Users\user\PycharmProjects\pythonProject4\kakao_code.json","w") as fp:
#     json.dump(tokens, fp)
#
# #2.
# with open("kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

# # json 읽어오기
import json
#
# # 1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json", "r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])
#
# 2.
# with open("kakao_code.json", "r") as fp:
#     ts = json.load(fp)
#     print(ts)
#     print(ts["access_token"])
# 아래는 친구에게
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'bcc25462aacf0ec8c9bc01a4b9eccfb1'
redirect_uri = 'https://localhost:9988'
authorize_code = 'ILEL2Vg9VofME-5RBFbBWrfB9uThjkp0qaVAn6Dwj32CIdM9gaxOqoxmY7MRv8LnMuMxjwopcJ4AAAGAT-rirg'

data = {
    'grant_type' : 'authorization_code',
    'client_id' : rest_api_key,
    'redirect_uri' : redirect_uri,
    'code' : authorize_code,
    'client_secret' : 'ecuwWZTCW0rjGFtKJMZCQmeogHxAijib'
}

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

with open("kakao_code.json", "w") as fp:
    json.dump(tokens,fp)