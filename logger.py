from datetime import datetime

"""
Logger 1.0
made by peaisyamyam
reference Prism Launcher Log
use datetime moduel
"""

def defaultlog(log_message):
    now = datetime.now()
    print(f"[{now.strftime('%H:%M:%S')}] [INFO] {log_message}")

def warninglog(log_message):
    now = datetime.now()
    print(f"[{now.strftime('%H:%M:%S')}] [WARN] {log_message}")

def errorlog(log_message):
    now = datetime.now()
    print(f"[{now.strftime('%H:%M:%S')}] [ERROR] {log_message}")

def fatallog(log_message):
    now = datetime.now()
    print(f"[{now.strftime('%H:%M:%S')}] [FATAL] {log_message}")