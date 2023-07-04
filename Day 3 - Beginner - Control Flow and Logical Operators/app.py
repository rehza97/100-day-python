myname = input('write ur name : ')
hername = input("write her name : ")

ourname = myname+hername
myname = myname.lower()
hername = hername.lower()
true = 'true'
love = 'love'
cnt_love = 0
cnt_true = 0
for c in true:
    # print(c , ourname.count(c))
    cnt_true += ourname.count(c)
print('_______________') 
for c in love:
    # print(c , ourname.count(c))
    cnt_love += ourname.count(c)
    

score = f'{cnt_true}{cnt_love}'

print(score)