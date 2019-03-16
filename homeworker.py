from gui import *
def showdoc():
	Print(title="提醒：",text="""这个程序属于
		方块娱乐，
		请谨慎使用。""")
def 获取因数():
	shu=eval(input("请输入数:"))
	yin=1
	array=[]
	while (yin-1)!=shu:
		if shu%yin==0:
			array.append(yin)
		yin+=1
	tuple1=tuple(array)
	output=str(shu)+"的因数有："+str(tuple1)
	Print(output)
def 最小公倍数():
	first=eval(input("请输入较大的数:"))
	second=eval(input("请输入较小的数:"))
	while True:
		if(first % second == 0):
			afirst = first
			break
		first += 1
	Print(str(afirst)+"和"+str(second)+"的最小公倍数为"+str(first))
def 是否质数():
	flag=0
	n=eval(input("请输入需要判断合数或质数的数:"))
	if n <= 1:
	    Print("错误")
	    flag = 1
	i = 2
	while i*i <= n and flag != 1:    
	    if n % i == 0:  
	        Print("合数")
	        flag=1
	        break
	    i += 1
	if flag==0:
	    Print("质数")
是否质数()
