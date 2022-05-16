def printsubset(str,ans):
    if len(str)==0:
        print(ans)
        return
    printsubset(str[1:],ans)
    incl=str[0]+ans
    printsubset(str[1:],incl)
printsubset('23','')