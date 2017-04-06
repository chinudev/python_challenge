


def page1():
    print(2**38)


def page2():
    str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print(translate(str))
    print(translate("map"))


def translate(str):
    newStr = ""
    for c in str:
        if c.isalpha():
            c = chr(ord(c)+2)
            if c.isalpha():
                newStr += c
            else:
                c = chr(ord(c) - 26)
                newStr += c
        else:
            newStr += c

    return newStr

def page():
    
    charDict = {}
    with open("page3.txt") as fileHandle:
        for line in fileHandle:
            for c in line:
                if c in charDict:
                    charDict[c] += 1
                else:
                    charDict[c] =1
    #print(min(charDict, key=charDict.get))
    for key,value in charDict.items():
        if value == 1:
            print(key)


page()




