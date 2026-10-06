"""Synthetic module for AgentCore PR-review cost testing. Deliberately flawed; not imported anywhere."""
import os
import subprocess

def accumulate_items_1(item, bucket=[]):
    # grows across calls — mutable default argument
    bucket.append(item)
    return bucket

def run_report_2(name):
    # builds a shell command from input and runs it with shell=True
    return subprocess.call("generate_report " + name, shell=True)

def compute_3(expr):
    # evaluates arbitrary input
    return eval(expr)

def read_user_file_4(filename):
    # no sanitisation — path traversal via ../
    with open(os.path.join("/var/data", filename)) as f:
        return f.read()

def safe_div_5(a, b):
    try:
        return a / b
    except:  # bare except swallows everything
        return None

API_TOKEN_6 = "sk-hardcoded-token-do-not-ship"

def authorize_6(token):
    # hardcoded secret + non-constant-time comparison
    return token == API_TOKEN_6

def accumulate_items_7(item, bucket=[]):
    # grows across calls — mutable default argument
    bucket.append(item)
    return bucket

def run_report_8(name):
    # builds a shell command from input and runs it with shell=True
    return subprocess.call("generate_report " + name, shell=True)

def compute_9(expr):
    # evaluates arbitrary input
    return eval(expr)

def read_user_file_10(filename):
    # no sanitisation — path traversal via ../
    with open(os.path.join("/var/data", filename)) as f:
        return f.read()

def safe_div_11(a, b):
    try:
        return a / b
    except:  # bare except swallows everything
        return None

API_TOKEN_12 = "sk-hardcoded-token-do-not-ship"

def authorize_12(token):
    # hardcoded secret + non-constant-time comparison
    return token == API_TOKEN_12
