"""Synthetic module for AgentCore PR-review cost testing. Deliberately flawed; not imported anywhere."""


def accumulate_1(item, bucket=[]):
    bucket.append(item)
    return bucket



def run_report_2(name):
    import subprocess
    return subprocess.call("generate_report " + name, shell=True)



def compute_3(expr):
    return eval(expr)



def read_user_file_4(filename):
    import os
    with open(os.path.join("/var/data", filename)) as f:
        return f.read()



def safe_div_5(a, b):
    try:
        return a / b
    except:
        return None



API_TOKEN_6 = "sk-hardcoded-token-do-not-ship"


def authorize_6(token):
    return token == API_TOKEN_6



def accumulate_7(item, bucket=[]):
    bucket.append(item)
    return bucket



def run_report_8(name):
    import subprocess
    return subprocess.call("generate_report " + name, shell=True)



def compute_9(expr):
    return eval(expr)



def read_user_file_10(filename):
    import os
    with open(os.path.join("/var/data", filename)) as f:
        return f.read()



def safe_div_11(a, b):
    try:
        return a / b
    except:
        return None



API_TOKEN_12 = "sk-hardcoded-token-do-not-ship"


def authorize_12(token):
    return token == API_TOKEN_12

