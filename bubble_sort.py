import time


def bubblesort(data,drawData,timeTick):
    for _ in range(len(data)-1):

        for j in range(len(data)-1):

            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

                drawData(data,["yellow" if x==j or x==j+1 else "red" for x in range(len(data))])
                time.sleep(timeTick) # we can set time from speedscale

    drawData(data,['yellow' for x in range(len(data))])