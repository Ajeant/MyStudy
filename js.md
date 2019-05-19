### 高阶函数
```javascript
function add(x, y, f) {
	return f(x) + f(y);
}
```

### map
function pow(x) {
return x * x;
}
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arr.map(pow); // [1, 4, 9, 16, 25, 36, 49, 64, 81]

### reduce
[x1, x2, x3, x4].reduce(f) = f(f(f(x1, x2), x3), x4)  
var arr = [1, 3, 5, 7, 9];
arr.reduce(function (x, y) {
return x + y;
}); // 25

### 闭包
返回函数不要引用任何循环变量，或者后续会发生变化的变量
```html
<!DOCTYPE html>
<html>
<head>
	<script type="text/javascript">
		function count() {
			var arr = [];
			for (var i=1; i<=3; i++) {
				arr.push(function () {
					return i * i;
				});
			}
			return arr;
		}
		var results = count();
		var f1 = results[0];
		var f2 = results[1];
		var f3 = results[2];
		console.log(f1());//16
		console.log(f2());//16
		console.log(f3());//16
	</script>
<meta charset="UTF-8">
<title>javascript</title>
</head>
<body>
</body>
</html>
```
修改为
```html
<!DOCTYPE html>
<html>
<head>
	<script type="text/javascript">
		function count() {
			var arr = [];
			for (var i=1; i<=3; i++) {
				arr.push((function (n) {
					return function () {
						return n * n;
					}
				})(i));
			}
			return arr;
		}
		var results = count();
		var f1 = results[0];
		var f2 = results[1];
		var f3 = results[2];
		console.log(f1());//1
		console.log(f2());//4
		console.log(f3());//9
	</script>
<meta charset="UTF-8">
<title>javascript</title>
</head>
<body>
</body>
</html>
```

### Date
```html
<!DOCTYPE html>
<html>
<head>
	<script type="text/javascript">
		var now = new Date();
		console.log(now); // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
		console.log(now.getFullYear()); // 2015, 年份
		console.log(now.getMonth()); // 5, 月份，注意月份范围是0~11，5表示六月
		console.log(now.getDate()); // 24, 表示24号
		console.log(now.getDay()); // 3, 表示星期三
		console.log(now.getHours()); // 19, 24小时制
		console.log(now.getMinutes()); // 49, 分钟
		console.log(now.getSeconds()); // 22, 秒
		console.log(now.getMilliseconds()); // 875, 毫秒数
		console.log(now.getTime()); // 1435146562875, 以number形式表示的时间戳
	</script>
<meta charset="UTF-8">
<title>javascript</title>
</head>
<body>
</body>
</html>
```



