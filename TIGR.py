#!/usr/bin/env python3
# VIP_DJALIL launcher (safe, UI + offline license)
# For legal use only.

import os, sys, time, hashlib, hmac, json, getpass, uuid

APP_NAME = "VIP_DJALIL"
LICENSE_FILE = os.path.expanduser("~/.vip_djalil_license")
# NOTE: keep this secret on your license-server. For local testing you can set it here,
# but DO NOT publish the real secret in public repos.
SERVER_SECRET = b"REPLACE_WITH_STRONG_SECRET_ONLY_ON_YOUR_SERVER"

ASCII_LOGO = r"""
██╗   ██╗██╗██████╗     ██████╗ ██████╗ ██╗██╗
██║   ██║██║██╔══██╗    ██╔══██╗██╔══██╗██║██║
██║   ██║██║██████╔╝    ██████╔╝██████╔╝██║██║
██║   ██║██║██╔══██╗    ██╔═══╝ ██╔═══╝ ██║╚═╝
╚██████╔╝██║██║  ██║    ██║     ██║     ██║██╗
 ╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝     ╚═╝╚═╝
      VIP_DJALIL — PRO EDITION
"""

def slow_print(s, delay=0.008):
    for ch in s:
        sys.stdout.write(ch); sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner(seconds=2, text="Loading"):
    t0 = time.time()
    chars = "|/-\\"
    i = 0
    while time.time()-t0 < seconds:
        sys.stdout.write(f"\r{text} {chars[i%4]} "); sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 40 + "\r")

def fingerprint():
    # Simple machine fingerprint for offline license binding
    # Use multiple stable identifiers in production
    uid = uuid.getnode()  # MAC or pseudo
    uname = os.getenv("USER") or os.getenv("USERNAME") or "user"
    info = f"{uid}-{uname}"
    return hashlib.sha256(info.encode()).hexdigest()

def make_license_token(key_str, fingerprint_hex):
    # token = HMAC(secret, key || ":" || fingerprint)
    msg = (key_str + ":" + fingerprint_hex).encode()
    mac = hmac.new(SERVER_SECRET, msg, hashlib.sha256).hexdigest()
    return mac

def verify_license(key_str, token, fingerprint_hex):
    expected = make_license_token(key_str, fingerprint_hex)
    return hmac.compare_digest(expected, token)

def save_license(data):
    with open(LICENSE_FILE, "w") as f:
        json.dump(data, f)

def load_license():
    if not os.path.exists(LICENSE_FILE): return None
    try:
        with open(LICENSE_FILE,"r") as f:
            return json.load(f)
    except:
        return None

def interactive_activate():
    print("\n== VIP Activation ==")
    key = input("Enter your VIP Key: ").strip()
    token = input("Enter your License Token: ").strip()
    fp = fingerprint()
    if verify_license(key, token, fp):
        save_license({"key": key, "token": token, "fingerprint": fp, "activated_at": time.time()})
        print("\n✅ Activation successful. Welcome VIP!")
        return True
    else:
        print("\n❌ Invalid key/token for this machine.")
        return False

def check_activation():
    lic = load_license()
    if not lic:
        return False
    fp = fingerprint()
    if lic.get("fingerprint") != fp:
        return False
    return verify_license(lic.get("key",""), lic.get("token",""), fp)

def main_menu():
    clear()
    print(ASCII_LOGO)
    print("1) Run VIP Tools (Legal modules)")
    print("2) Show System Info")
    print("3) Deactivate License")
    print("0) Exit")
    choice = input("\nChoose: ").strip()
    if choice == "1":
        clear(); print("Running legal VIP features...\n")
        print("[Demo] This is where your legal modules run.")
        input("\nPress Enter to return to menu...")
    elif choice == "2":
        clear()
        print("System info:")
        print("Fingerprint:", fingerprint())
        print("License file:", LICENSE_FILE)
        input("\nPress Enter to return to menu...")
    elif choice == "3":
        if os.path.exists(LICENSE_FILE):
            os.remove(LICENSE_FILE)
            print("License deactivated.")
        else:
            print("No license found.")
        time.sleep(1)
    elif choice == "0":
        print("Goodbye.")
        sys.exit(0)
    else:
        print("Invalid choice.")
    main_menu()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner_and_start():
    clear()
    slow_print(ASCII_LOGO, delay=0.002)
    spinner(1.6, "Initializing VIP Core")
    print("\nWelcome to", APP_NAME)
    if check_activation():
        print("License: \033[1;32mActivated\033[0m")
        time.sleep(0.6)
        main_menu()
    else:
        print("License: \033[1;31mNot Activated\033[0m")
        print("\nYou must activate your VIP copy to continue.")
        print("1) Activate")
        print("2) How to get a key (demo)")
        print("0) Exit")
        ch = input("\nChoose: ").strip()
        if ch == "1":
            if interactive_activate():
                time.sleep(0.6); main_menu()
            else:
                input("\nPress Enter to return...")
                banner_and_start()
        elif ch == "2":
            print("\nTo get a key, generate it from your license-server using this machine fingerprint:")
            print("Fingerprint:", fingerprint())
            print("\n(For demo you can run generate_key.py on your machine to create a test key & token.)")
            input("\nPress Enter to return...")
            banner_and_start()
        else:
            print("Bye."); sys.exit(0)

if __name__ == "__main__":
    banner_and_start()
