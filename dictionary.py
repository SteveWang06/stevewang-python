iter_ = ('你好','什麼','很好')
dic=dict.fromkeys(iter_,'xin chao',)
dic['什麼']='cai gi\n這個是什麼東西'
dic['很']='rat\n我很好'
print(dic[input()])