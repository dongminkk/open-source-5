import random

# 2017038093 김동민

def get (str) :
    numStr= ''
    for ch in str:
        if ch.isdigit():
            numStr += ch
        
    return int(numStr)

data = []
i, k = 0,0
if __name__ == "__main__" :
    for i in range(0, 10) :
        tmp = hex(random.randrange (0, 100000))
        tmp = tmp[2:]
        data.append (tmp)

    print( '정렬 전 데이터 : ', end = '')
    [print(num, end =' ') for num in data]

    for i in range (0, len(data) - 1) :
        for k in range(i + 1, len(data)) :
            if get (data[i]) > get (data[k]) :
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
    
    print( '\n정렬 후 데이터 : ', end = '')
    [print(num, end =' ') for num in data]
