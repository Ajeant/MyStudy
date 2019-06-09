1. 查看文档python -m pydoc 5678
2. 实例的变量名如果以 __ 开头，就变成了一个私有变量（private）
3. 列表推导式
	[x*x for x in range(10)]  
	[x*x for x in range(10) if x % 3 == 0]
4. exec和eval执行和求值字符串  
	exec "print 'hello"  
	eval(raw_input("enter an arithmetic expression"))