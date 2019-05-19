1. 下载后在bin中新建mongodb.config
	- 在mongodb.config中加一行：dbpath=PATH_TO_WHERE_YOU_WANT_TO_STORE_YOUR_DATABASE_FILES。例如，在Windows中您需要添加的可能是dbpath=c:\mongodb\data而在Linux下可能就是dbpath=/etc/mongodb/data。
2. 启动
	- mongod --config E:\mongodb\bin\mongodb.config
3. use learn切换数据库
4. 
	- db.unicorns.insert({name: 'Aurora', gender: 'f', weight: 450})
	- db.unicorns.find()
	- db.unicorns.remove()
5. db、show collections
