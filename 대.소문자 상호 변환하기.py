# 2017038093 김동민

ins, outs= "",""
ch = ""
count, i = 0, 0

if __name__ == "__main__" :
    ins = input ("문자열을 입력하세요 : ")
    count = len(ins)
    
    for i in range (0, count) :
        ch = ins[i]
        if (ord(ch) >= ord("A") and ord(ch) <= ord("Z")) :
            newCh = ch. lower()
        elif (ord(ch) >= ord("a") and ord(ch) <= ord("z")) :
            newCh = ch.upper ()
        else:
            newCh = ch
            
        outs += newCh
        
    print("대소문자 변환 결과---> %s" % outs)
