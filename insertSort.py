# -*- coding: utf-8 -*-

#ascending order sort
#data
_list = [11,4,2,5,3,9,0,1,7]

for i in range(1, len(_list)):
    #x(x>0)番目の数を
    tmp = _list[i]
    ins = 0

    for j in range((i-1), -1, -1):
        #1番目からx番目までの数と比較
        if(_list[j] > tmp):
            _list[j+1] = _list[j]
        else:
            ins = j+1
            break
    _list[ins] = tmp
    print(_list)

print("ソート後: {}".format(_list))
