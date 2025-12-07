#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VIP Key Tool — Minimal Clean with Key Approval
Safe & local only — no network, no payments, no hacking features.
"""

import os
import sys
import json
import uuid
import hashlib
from datetime import datetime, timedelta

DATA_DIR = "data"
KEYS_FILE = os.path.join(DATA_DIR, "keys.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")

# Colors
G = "\033[1;32m"
R = "\033[1;31m"
Y = "\033[1;33m"
W = "\033[0m"

# -------------------------
# Helpers
# -------------------------
def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_json(path):
    ensure_data_dir()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_json(path, data):
    ensure_data_dir()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# -------------------------
# Key management
# -------------------------
def generate_key():
    # Generate a human-friendly unique key
    u = uuid.uuid4().hex
    raw = f"{u}{uuid.uuid4().hex}"
    k = hashlib.sha256(raw.encode()).hexdigest()[:28]
    # Format like NIXxxxxx-xxxxx for readability
    formatted = "VIP" + "-" + "-".join([k[i:i+6] for i in range(0, 24, 6)])
    return formatted.upper()

def create_key_entry(days_valid, buyer_name="guest"):
    keys = load_json(KEYS_FILE)
    key = generate_key()
    created = now_str()
    expires = (datetime.now() + timedelta(days=days_valid)).strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "key": key,
        "buyer": buyer_name,
        "created": created,
        "expires": expires,
        "approved": False,
        "approved_by": None,
        "approved_at": None,
        "note": ""
    }
    keys[key] = entry
    save_json(KEYS_FILE, keys)
    return entry

def list_keys(show_all=True):
    keys = load_json(KEYS_FILE)
    if not keys:
        print("لا يوجد مفاتيح حتى الآن.")
        return
    for k, v in keys.items():
        status = "APPROVED" if v.get("approved") else "PENDING"
        print(f"{G}{k}{W}  — {v.get('buyer')}  [{status}]  exp: {v.get('expires')}")

def approve_key(admin, key, note=""):
    keys = load_json(KEYS_FILE)
    if key not in keys:
        return False, "Key not found"
    keys[key]["approved"] = True
    keys[key]["approved_by"] = admin
    keys[key]["approved_at"] = now_str()
    keys[key]["note"] = note
    save_json(KEYS_FILE, keys)
    return True, "Key approved"

def revoke_key(key):
    keys = load_json(KEYS_FILE)
    if key not in keys:
        return False, "Key not found"
    del keys[key]
    save_json(KEYS_FILE, keys)
    return True, "Key removed"

def check_key_valid(key):
    keys = load_json(KEYS_FILE)
    v = keys.get(key)
    if not v:
        return False, "Key not found"
    if not v.get("approved"):
        return False, "Key not approved yet"
    exp = datetime.strptime(v.get("expires"), "%Y-%m-%d %H:%M:%S")
    if datetime.now() > exp:
        return False, "Key expired"
    return True, f"Key valid (buyer={v.get('buyer')}, exp={v.get('expires')})"

# -------------------------
# Simple local owner/user system
# -------------------------
def ensure_admin():
    users = load_json(USERS_FILE)
    if "owner" not in users:
        # default owner password is "owner" -> **change it** after first run
        users["owner"] = {"password": "owner", "role": "owner"}
        save_json(USERS_FILE, users)

def owner_login():
    users = load_json(USERS_FILE)
    username = input("Owner username: ").strip()
    pw = input("Password: ").strip()
    entry = users.get(username)
    if not entry or entry.get("password") != pw or entry.get("role") != "owner":
        print(R + "فشل تسجيل دخول المدير" + W)
        return None
    print(G + "مرحبًا مالك الأداة." + W)
    return username

# -------------------------
# UI / Menus
# -------------------------
def ascii_header():
    clear = lambda: os.system("cls" if os.name == "nt" else "clear")
    clear()
    print(G + " _   _ _____ _    ___  " + W)
    print(G + "| | | |_   _| |  / _ \\ " + W)
    print(G + "| | | | | | | | | | | |" + W)
    print(G + "| |_| | | | | | | |_| |" + W)
    print(G + " \\___/  |_| |_|  \\___/  ~ VIP TOOL (Minimal Clean)" + W)
    print("-"*60)

def main_menu():
    ensure_data_dir()
    ensure_admin()
    while True:
        ascii_header()
        print(f"{G}Owner key:{W} (local)  |  {Y}Select Buy Option{W}")
        print()
        print("[1] $8 Approval For 1 month")
        print("[2] $6 Approval For 15 days")
        print("[3] $3 Approval For 7 days")
        print("[4] Enter your key (Check)")
        print("[5] Owner Panel (approve/revoke)")
        print("[0] Exit")
        choice = input("Select Buy Option: ").strip()
        if choice == "1":
            buyer = input("Your name (buyer): ").strip() or "guest"
            entry = create_key_entry(30, buyer)
            print(G + "Your Key : " + entry["key"] + W)
            print(Y + "Note: Owner must approve the key manually (Owner Panel)." + W)
            input("Press Enter...")
        elif choice == "2":
            buyer = input("Your name (buyer): ").strip() or "guest"
            entry = create_key_entry(15, buyer)
            print(G + "Your Key : " + entry["key"] + W)
            print(Y + "Note: Owner must approve the key manually (Owner Panel)." + W)
            input("Press Enter...")
        elif choice == "3":
            buyer = input("Your name (buyer): ").strip() or "guest"
            entry = create_key_entry(7, buyer)
            print(G + "Your Key : " + entry["key"] + W)
            print(Y + "Note: Owner must approve the key manually (Owner Panel)." + W)
            input("Press Enter...")
        elif choice == "4":
            key = input("Enter your key: ").strip().upper()
            ok, msg = check_key_valid(key)
            if ok:
                print(G + "OK: " + msg + W)
            else:
                print(R + "FAILED: " + msg + W)
            input("Press Enter...")
        elif choice == "5":
            admin = owner_login()
            if admin:
                owner_panel(admin)
        elif choice == "0":
            print("Bye.")
            sys.exit(0)
        else:
            print("Invalid choice.")
            input("Press Enter...")

def owner_panel(admin):
    while True:
        ascii_header()
        print(G + f"Owner Panel — {admin}" + W)
        print("[1] List keys")
        print("[2] Approve a key")
        print("[3] Revoke (delete) a key")
        print("[4] View key details")
        print("[0] Back")
        ch = input("Choose: ").strip()
        if ch == "1":
            list_keys()
            input("Press Enter...")
        elif ch == "2":
            k = input("Key to approve: ").strip().upper()
            note = input("Note (optional): ").strip()
            ok, msg = approve_key(admin, k, note)
            if ok:
                print(G + msg + W)
            else:
                print(R + msg + W)
            input("Press Enter...")
        elif ch == "3":
            k = input("Key to revoke: ").strip().upper()
            ok, msg = revoke_key(k)
            if ok:
                print(G + msg + W)
            else:
                print(R + msg + W)
            input("Press Enter...")
        elif ch == "4":
            k = input("Key to view: ").strip().upper()
            keys = load_json(KEYS_FILE)
            v = keys.get(k)
            if not v:
                print(R + "Key not found." + W)
            else:
                print(json.dumps(v, indent=2, ensure_ascii=False))
            input("Press Enter...")
        elif ch == "0":
            return
        else:
            print("Invalid choice.")
            input("Press Enter...")

# -------------------------
# Entrypoint
# -------------------------
if __name__ == "__main__":
    main_menu()
