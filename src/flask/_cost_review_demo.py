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

