import sys

state = "State"
capital = "Capital"
print("%20s %20s" % (state, capital))
print("-" * 42)

args = sys.argv[1:]  
for i in range(0, len(args), 2):
    print("%20s %20s" % (args[i], args[i+1]))
