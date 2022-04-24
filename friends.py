import requests
import json


def kakao_alram(threshold,sensor):

    with open(r"kakao_code.json","r") as fp:
        tokens = json.load(fp)

    friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
    headers={"Authorization" : "Bearer " + tokens["access_token"]}
    result = json.loads(requests.get(friend_url, headers=headers).text)

    print(type(result))
    print("=============================================")
    print(result)
    print("=============================================")
    friends_list = result.get("elements")
    print(friends_list)
    # print(type(friends_list))
    print("=============================================")
    print(friends_list[0].get("uuid"))
    friend_id = friends_list[0].get("uuid")
    print(friend_id)
    try:
        if threshold == True:
            send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
            data={
                'receiver_uuids': '["{}"]'.format(friend_id),
                "template_object": json.dumps({
                    "object_type":"text",
                     "text":"""\
                        RESHENIE Alarm
                        - 이상 징후 감지 센서: %s
                        - 이상 징후 발생 값: %s
                        - Alarm Level 기준값 대비 10%% 이상 발생.
                        - 설비를 점검해 주시기 바랍니다.""" %(str(sensor),str(threshold)),
                    "link":{
                        "web_url":"www.daum.net",
                        "web_url":"www.naver.com"
                    },
                    "button_title": "설비 상태 확인하기"
                })
            }
            response = requests.post(send_url, headers=headers, data=data)
            response.status_code
            if response.json().get('result_code') == 0:
                print('메시지 전송 성공')
                return 1
            else:
                print("메시지를 성공적으로 보내지 못했습니다. 오류 내용:" + str(response.json()))
                return 0
    except Exception as e:
        print("KaKao module Error")
    return

if __name__ == "__main__":
    threshold = 30
    sensor = "test sensor"
    kakao_alram(threshold, sensor)