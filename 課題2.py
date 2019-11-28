# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 08:54:02 2019

@author: n1260148
"""
import collections

#説明---------------------------------------
print("マークは　s, c, d, h の4個")
print("数字は 2,3,4,5,6,7,8,9,10,11,12,13,1　の13個")
print("マークと数字の間にスペースを入れて入力")

#カード入力------------------------------------
hand = []
handdet = []
hmark = []
hnum = []
print("カードを5回入力")
for i in range(5):
    print("「マーク〇数字」で入力して下さい")
    hand.append(input('>>'))
print(hand)

for j in range(5):
    handdet.append(hand[j].split())

for k in range(5):
    hmark.append(handdet[k][0])
for l in range(5):
    hnum.append(handdet[l][1])   
#print(hmark)
#print(hnum)
#print(hmark.count("s" or "c" or "d" or "h"))

#長いのでここにストレートの処理-----------------------
def straight(hnum):
    Snum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for m in range(5):
        x = int(hnum[m]) -1
        if x == 0:
            Snum[13] = 0
        Snum[x] = 0
        #print(Snum)
    for n in range(10):
        if Snum[n] == 0 and Snum[n+1] == 0 and Snum[n+2] == 0 and Snum[n+3] == 0 and Snum[n+4] == 0:
            return True
       
#ペア数の処理-------------------------------
numcount = collections.Counter(hnum)
pairc = list(numcount.values())
list.sort(pairc, reverse=True)
#print(pairc)

#役判定---------------------------------------
#ファイブカード　今回無し
#ロイヤルストレートフラッシュ
if  (set(hnum) == set(['10','11','12','13','1']) and hmark.count("s" or "c" or "d" or "h") == 5):
    print("ロイヤルストレートフラッシュ")
    
#ストレートフラッシュ
elif hmark.count("s" or "c" or "d" or "h") == 5 and straight(hnum):
    print("ストレートフラッシュ")
    
#フォーカード
elif pairc[0] == 4:
    print("フォーカード")
    
#フルハウス    
elif pairc[0] == 3 and pairc[1] == 2:
    print("フルハウス")

#フラッシュ
elif hmark.count("s" or "c" or "d" or "h") == 5:
    print("フラッシュ")
    
#ストレート
elif straight(hnum):
    print("ストレート")
    
#スリーカード
elif pairc[0] == 3:
    print("スリーカード")
    
#ツーペア
elif pairc[0] == 2 and pairc[1] == 2:
    print("ツーペア")
    
#ワンペア
elif pairc[0] == 2:
    print("ワンペア")
    
#ノーペア
else:
    print("ノーペア")


#        
    













