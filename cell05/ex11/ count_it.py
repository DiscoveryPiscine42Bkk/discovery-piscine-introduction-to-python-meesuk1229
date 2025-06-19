import sys
arg = sys.arg[1:]
if len (arg) ==0:
    print("none")
else:
    print(f"parameters: {len(arg)})")
for arg in arg :
    print(f"{arg}:{len(arg)}")
