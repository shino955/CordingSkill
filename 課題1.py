# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 08:54:02 2019

@author: n1260148
"""

#当たり判定--------------------------------------

#自機入力---------------------------------------
print("自機の「左上 x座標」「左上 y座標」「幅」 「高さ」 間に空白入力")
Lcoli = input('>>')
Mcoli = (Lcoli.split())
#print(Mcoli)
    #自機判定を計算しやすくする為「右下 x座標」「右下 y座標」を後半に入れたlistを作成
MRect = Mcoli
MRect[0] = int(Mcoli[0])
MRect[1] = int(Mcoli[1])
MRect[2] = int(Mcoli[0]) + int(Mcoli[2])
MRect[3] = int(Mcoli[1]) - int(Mcoli[3])
#print(MRect)

#敵機数入力-------------------------------------
print("敵機数を入力")
Enemy = int(input(">>>"))

#敵機入力---------------------------------------
Ecoli = []
for j in range(Enemy): 
    print("敵機の「左上 x座標」「左上 y座標」「幅」 「高さ」 間に空白入力")
    Lcoli = input('>>')
    Ecoli.append(Lcoli.split())
    #print(Ecoli)
    #敵機判定を計算しやすくする為「右下 x座標」「右下 y座標」を後半に入れたlistを作成
for k in range(Enemy):
    ERect = Ecoli
    ERect[k][0] = int(Ecoli[k][0])
    ERect[k][1] = int(Ecoli[k][1])
    ERect[k][2] = int(Ecoli[k][0]) + int(Ecoli[k][2])
    ERect[k][3] = int(Ecoli[k][1]) - int(Ecoli[k][3])
#print(ERect)


#判定用-------------------
for l in range(Enemy):
    if(int(max(MRect[0],ERect[l][0])) <= int(min(MRect[2],ERect[l][2])) 
        and int(min(MRect[1],ERect[l][1])) >= int(max(MRect[3],ERect[l][3]))):
        print("敵機", l+1 ,"と接触")

               




