# password ='a123456'
# 讓使用者重複輸入密碼,最多輸入3次密碼
# 不對列出'密碼錯誤 ! 還有___次機會'
# 對的話, 印出'輸入成功'
password = 'a123456'
i=3
while i>0 :
	i = i - 1
	pwd=input('請輸入密碼 : ')
	if pwd == password :
		print('輸入成功 ')
		break
	else :
	    print('密碼錯誤 ! ')
	    if i > 0 :
	    	print('還有', i ,' 次機會')
	    else:
	    	print('沒機會嘗試 ，要鎖帳號了 ! ')