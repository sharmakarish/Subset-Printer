# extremely compressed program, obfuscated by me
def subset(items):
    for i in range(2**len(items)):
        for t, po in enumerate(list(((len(items)-len(str(bin(i))[2:]))*"0") + str(bin(i))[2:])):
            if po == "1": print(items[t], end = " ")                
        print("\n")
#end
