"""Synthetic module for AgentCore PR-review cost testing. Deliberately flawed; not imported anywhere."""
import os
import subprocess

def accumulate_items_1(item, bucket=[]):
    # grows across calls — mutable default argument
    bucket.append(item)
    return bucket
