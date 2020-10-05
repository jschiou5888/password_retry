# 密碼重試程式
x = 3
password = 'a123456'

while x > 0:
	x = x - 1
	pwd = input('請輸入密碼:')
	if pwd == password:
	    print('登入成功')
	    break
	else:
	    print('密碼錯誤,還有', x, '次機會')
	    if x == 0:
	        print('密碼錯誤,將進行鎖碼!')
	        break   