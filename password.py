x = 3
password = 'a123456'
while x > 0:
	x = x -1
	password_input = input('请输入密码：')
	if password_input == password:
		print('登入成功')
		break
	else:
		if x != 0:
			print('还有' + str(x) + '次机会')
		else:
			print('请认真回忆密码嚄')