#!/usr/bin/env python3
"""Generate a synthetic, deliberately-flawed Python module with N functions.

Used by the batch fan-out workflow (and runnable locally) to produce a
review target whose size scales with N. Usage: cost_gen_change.py [N]
"""
import sys

SNIPPETS = [
    'def accumulate_{i}(item, bucket=[]):\n    bucket.append(item)\n    return bucket\n',
    'def run_report_{i}(name):\n    import subprocess\n    return subprocess.call("generate_report " + name, shell=True)\n',
    'def compute_{i}(expr):\n    return eval(expr)\n',
    'def read_user_file_{i}(filename):\n    import os\n    with open(os.path.join("/var/data", filename)) as f:\n        return f.read()\n',
    'def safe_div_{i}(a, b):\n    try:\n        return a / b\n    except:\n        return None\n',
    'API_TOKEN_{i} = "sk-hardcoded-token-do-not-ship"\n\n\ndef authorize_{i}(token):\n    return token == API_TOKEN_{i}\n',
]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    parts = ['"""Synthetic module for AgentCore PR-review cost testing. Deliberately flawed; not imported anywhere."""']
    for i in range(1, n + 1):
        parts.append("")
        parts.append("")
        parts.append(SNIPPETS[(i - 1) % len(SNIPPETS)].format(i=i))
    sys.stdout.write("\n".join(parts) + "\n")


if __name__ == "__main__":
    main()
