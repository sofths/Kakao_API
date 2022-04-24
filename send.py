import requests
import json

# #1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","r") as fp:
#     tokens = json.load(fp)

#2.

def kakao_alram(threshold,sensor):
    with open("kakao_code.json","r") as fp:
        tokens = json.load(fp)

    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # kapi.kakao.com/v2/api/talk/memo/default/send
    #https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri=https://example.com/oauth&response_type=code&scope=profile_nickname,friends,talk_message

    headers={"Authorization" : "Bearer " + tokens["access_token"]}
    data={
        "template_object": json.dumps({
            "object_type":"text",
            "text":"""\
            RESHENIE Alarm
        - 이상 징후 감지 센서: %s
        - 이상 징후 발생 값: %s
        - Alarm Level 기준값 대비 10%% 이상 발생.
        - 설비를 점검해 주시기 바랍니다.""" %(str(sensor),str(threshold)),
            "link":{
                "web_url":"http://reshenie.co.kr/"
            }
        })
    }
    response = requests.post(url, headers=headers, data=data)
    response.status_code

if __name__=="__main__":
    threshold = 30
    sensor = "test sensor"
    kakao_alram(threshold,sensor)