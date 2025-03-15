hour, minute, second= map(int,input().split())
C= int(input())

cho = C%60
sigan = C//3600
boon = (C-3600*sigan)//60


total_cho = second+cho

if total_cho//60>0:
    boon += (total_cho)//60
    total_cho = total_cho%60

total_boon = minute+boon

if total_boon//60 >0:
    sigan += (minute+boon)//60
    total_boon = (minute+boon)%60



print((sigan+hour)%24, total_boon, total_cho)
