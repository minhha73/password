# password ='a123456'
# 讓使用者重複輸入密碼,最多輸入3次密碼
# 不對列出'密碼錯誤 ! 還有___次機會'
# 對的話, 印出'輸入成功'
password = 'a123456'
i = 3
while True :
	pwd=input('請輸入密碼 : ')
	if pwd == password :
		print('輸入成功 ')
		break
	else :
	    i = i - 1
	    print('密碼錯誤 ! 還有', i ,' 次機會')
	    if i==0 :
	    	break