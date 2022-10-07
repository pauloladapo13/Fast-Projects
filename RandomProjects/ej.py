
import base64
import hashlib
import json
import random
import sys
import threading
import uuid
import requests
import time


def generate_device_id(seed):
    return "android-" + seed[:16]


def generate_UUID(uuid_type):
    generated_uuid = str(uuid.uuid4())
    if uuid_type:
        return generated_uuid
    else:
        return generated_uuid.replace("-", "")


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.


def login_with_cookie(cookie: str):
    sessionid = cookie.split(':')[0]
    userid = cookie.split(':')[0].split('%')[0]
    to_encrypt = {"ds_user_id": userid, "sessionid": sessionid, "should_use_header_over_cookies": True}
    to_encrypt = str(to_encrypt).replace("'", '"').replace('True', 'true').replace(' ', '')
    message_bytes = to_encrypt.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    auth = base64_bytes.decode('ascii')
    send_dm('recipe_user_id', 'Hello, this is a test message', auth)


def send_dm(id_to_dm, message, AUTHORIZATION):
    json_auth = json.loads(base64.b64decode(AUTHORIZATION).decode('utf-8'))
    my_user_id = json_auth['ds_user_id']

    a_uuid = generate_UUID(True)
    a_device_id = generate_device_id(generate_UUID(False))

    REQUEST_HEADERS = {
        "X-Pigeon-Rawclienttime": str(round(time.time() * 1000)),
        "X-IG-Bandwidth-Speed-KBPS": str(random.randint(7000, 10000)),
        "X-IG-Bandwidth-TotalBytes-B": str(random.randint(500000, 900000)),
        "X-IG-Bandwidth-TotalTime-MS": str(random.randint(50, 150)),
        "x-ig-app-startup-country": "AR",
        "x-bloks-version-id": "251c3023d7ef985a0e5d91b885c0c03bbb32b4b721d8de33bf9f667ba39b41ff",
        "x-ig-www-claim": "hmac.AR3ilHwjy8Cu_OTGprygpxuify0pDUKnrJvY1wRvzNSFRwwD",
        "x-bloks-is-layout-rtl": "false",
        "x-bloks-is-panorama-enabled": "true",
        "x-ig-device-id": a_uuid,
        "x-ig-family-device-id": "0ff91d16-df30-4b83-91bb-ef6fe5a751fa",
        "x-ig-android-id": a_device_id,
        "x-ig-timezone-offset": "-7200",
        "x-ig-nav-chain": "1kw:feed_timeline:1,UserDetailFragment:profile:5,ProfileMediaTabFragment:profile:6,3xM:direct_thread:7",
        "x-ig-salt-ids": "1061163349",
        "x-ig-connection-type": "WIFI",
        "x-ig-capabilities": "3brTvx0=",
        "x-ig-app-id": "567067343352427",
        "priority": "u=3",
        "user-agent": "Instagram 207.0.0.39.120 Android (22/5.1.1; 240dpi; 720x1280; samsung; SM-G977N; beyond1q; shamu; es_ES; 321039156)",
        "accept-language": "es-ES, en-US",
        "authorization": "Bearer IGT:2:" + AUTHORIZATION,
        "x-mid": "YYMo4AALAAFf64y70slcLACzpklN",
        "ig-u-ig-direct-region-hint": "ATN,48835113737,1667518455:01f7b0ee46fcbbaff69dfacfa670268aabc23145ec3868c74813073fb68730959e36791f",
        "ig-u-shbid": "9315,48835113737,1667316351:01f7d3483a632756a67739318c409667f8bf628ab96357ac142d5f8d8b1aec633e00925d",
        "ig-u-shbt": "1635780351,48835113737,1667316351:01f71ee7fe18abe0f30183c1e9ee8bf2e11701e107f982cf35ad9f2095bf08e0b3d69414",
        "ig-u-ds-user-id": str(my_user_id),
        "ig-u-rur": "VLL,48835113737,1667518478:01f7e869dc139eee715e5c5bfff4db350fe9c7f4c59979f70010e4333adbede244d9d068",
        "ig-intended-user-id": str(my_user_id),
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "accept-encoding": "zstd, gzip, deflate",
        "x-fb-http-engine": "Liger",
        "x-fb-client-ip": "True",
        "x-fb-server-cluster": "True"

    }

    print('Dm to [{}] current session-id {}'.format(id_to_dm, my_user_id))

    send_media = {
        "client_context": generate_UUID(True),
        "action": "send_item",
        "recipient_users": "[[" + id_to_dm + "]]",
        "send_attribution": "photo_view_other",
        "media_id": "2687403059380025174_3949224551",
        "_uuid": a_uuid
    }
    send_txt = {
        "client_context": generate_UUID(True),
        "action": "send_item",
        "recipient_users": "[[" + id_to_dm + "]]",
        "text": message,
        "_uuid": a_uuid
    }

    resp = requests.post('https://i.instagram.com/api/v1/direct_v2/threads/broadcast/media_share/?media_type=photo',
                         headers=REQUEST_HEADERS, data=send_media)
    if resp.status_code == 200:
        resp_message = requests.post('https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/',
                                     headers=REQUEST_HEADERS, data=send_txt)
        if resp_message.status_code == 200:
            print('Status: message sent succefully')
        else:
            print('Status: error', resp.text)
    else:
        print('Status: error', resp.text)


login_with_cookie('session_id=paste_sessionid_here;csfrtoken=paste_csfrtokenhere')




