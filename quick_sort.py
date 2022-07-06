import time


def partition(data,head,tail,drawData,timeTick):
    border = head
    pivot = data[tail]

    drawData(data,colorArray(len(data),head,tail,border,border))
    time.sleep(timeTick)

    for j in range(head,tail):
        if(data[j]<pivot):
            drawData(data,colorArray(len(data),head,tail,border,j,True))
            time.sleep(timeTick)

            data[border],data[j] = data[j],data[border]
            border+=1
            drawData(data,colorArray(len(data),head,tail,border,j))
            time.sleep(timeTick)
    

    drawData(data,colorArray(len(data),head,tail,border,tail,True))
    time.sleep(timeTick)
    data[border],data[tail] = data[tail],data[border]
    return border

def quicksort(data,head,tail,drawData,timeTick):
    if head<tail:
        partitionIdx = partition(data,head,tail,drawData,timeTick)

        # left partition
        quicksort(data,head,partitionIdx-1,drawData,timeTick)

        # now right partition
        quicksort(data,partitionIdx+1,tail,drawData,timeTick)


def colorArray(datalen,head,tail,border,currIdx,isSwapping=False):
    colorArray = []
    for i in range(datalen):

        # color when no operation is performed or base color
        if i>=head and i<=tail:
            colorArray.append("gray")
        else:
            colorArray.append("white")
        
        if i==tail:
            colorArray[i] = 'orange'

        elif i==border:
            colorArray[i] = 'red'

        elif i ==currIdx:
            colorArray[i] = 'yellow'
        
        if isSwapping:
            if i==border or i==currIdx:
                colorArray[i] = 'green'

    return colorArray

# check algorithm is working or not
# data = [20,3,1,60,4,3]
# quicksort(data,0,len(data)-1,0,0)
# print(data)