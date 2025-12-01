#!/usr/bin/env python3
# safe_checker.py
# سكربت تعليمي: فحص توافر أسماء على API (استخدمه قانونياً فقط)

import requests
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ====== إعدادات ======
API_TEMPLATE = "https://example.com/check/{}"  # غيّر إلى endpoint مسموح لك باستخدامه
INPUT_FILE = "ids.txt"     # كل سطر: اسم_أو_id
PROXIES_FILE = "proxies.txt"  # اختياري: كل سطر host:port
THREADS = 20
TIMEOUT = 10  # ثواني

# ===== ألوان للطباعة (بحذر في Windows قد لا تعمل) =====
C_OK = "\033[92m"
C_WARN = "\033[93m"
C_ERR = "\033[91m"
C_RESET = "\033[0m"

def load_list(path):
    p = Path(path)
    if not p.exists():
        return []
    return [line.strip() for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]

def pick_proxy(proxies, idx):
    if not proxies:
        return None
    # اختيار بسيط: تناوب على القائمة
    proxy = proxies[idx % len(proxies)]
    return {"http": f"http://{proxy}", "https": f"http://{proxy}"}

def check_name(name, proxy=None):
    """استدعاء آمن إلى API للتحقق. يُفترض أن يعيد 200 => موجود، 404 => غير موجود."""
    url = API_TEMPLATE.format(requests.utils.quote(name, safe=''))
    try:
        resp = requests.get(url, proxies=proxy, timeout=TIMEOUT)
        # تعديل المنطق بناءً على وثائق الـ API الذي تستخدمه
        if resp.status_code == 200:
            return True, resp.status_code, resp.text
        else:
            return False, resp.status_code, resp.text
    except requests.exceptions.RequestException as e:
        return None, str(e), ""

def worker(name, idx, proxies):
    proxy = pick_proxy(proxies, idx)
    ok, info, body = check_name(name, proxy)
    return name, ok, info

def main():
    start = time.time()
    ids = load_list(INPUT_FILE)
    proxies = load_list(PROXIES_FILE)
    if not ids:
        print(f"{C_ERR}لم أجد أي معرفات في {INPUT_FILE}. ضع أسماء أو IDs في الملف ثم شغّل السكربت.{C_RESET}")
        sys.exit(1)

    found_file = open("found.txt", "a", encoding="utf-8")
    notfound_file = open("not_found.txt", "a", encoding="utf-8")

    print(f"بدء الفحص -- عناصر: {len(ids)}, ثريدات: {THREADS}, بروكسيات: {len(proxies)}")
    with ThreadPoolExecutor(max_workers=THREADS) as exe:
        futures = {exe.submit(worker, name, i, proxies): (name, i) for i, name in enumerate(ids)}
        for fut in as_completed(futures):
            name, idx = futures[fut]
            try:
                name, ok, info = fut.result()
            except Exception as e:
                print(f"{C_ERR}[ERROR]{C_RESET} {name} -> استثناء: {e}")
                continue

            if ok is True:
                print(f"{C_OK}[FOUND]{C_RESET} {name} (code: {info})")
                found_file.write(f"{name}\n")
                found_file.flush()
            elif ok is False:
                print(f"{C_WARN}[NOT]{C_RESET} {name} (code: {info})")
                notfound_file.write(f"{name}\n")
                notfound_file.flush()
            else:
                # ok is None => خطأ اتصال
                print(f"{C_ERR}[ERR]{C_RESET} {name} -> {info}")

    found_file.close()
    notfound_file.close()
    print("انتهى الفحص. المدة:", round(time.time() - start, 2), "ثانية")
    print("نتائج موجودة في: found.txt و not_found.txt")

if __name__ == "__main__":
    main()
