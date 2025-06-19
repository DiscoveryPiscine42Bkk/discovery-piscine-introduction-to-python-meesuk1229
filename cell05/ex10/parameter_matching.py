import sys
if len(sys.argv) != 2:
    print("none")
else:
    word = input("What was the parameter? ")
    print("Good job!" if word == sys.argv[1] else "Nope, sorry...")