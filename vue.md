### 引包、留坑、实例化 、插值表达式{{}}
1. 引包
   - 确认已经下载了node,然后执行命令 npm install vue (如需下载自己要的版本在vue后面加上@版本号)
   - 页面引入刚下载的包
   ​	```<script type="text/javascript" src="vue.js"></script>```
2. 留坑:即留一个vue模板插入的地方或者是vue代码对其生效的地方
3. 实例化：即启动vue
	- 启动：new Vue({el:目的地,template:模板内容});实例化传入的是一个对象options
	- options
	- el  目的地，对应上面留坑的坑位，可通过id名，类名标签名来查找。方式与JQuery一样
	- template  内容
	- data 数据
4. 插值表达式{{}}
	- 插值表达式内填入data里面的变量即可在页面取到变量值{{ data里的变量 }}

### 常用指令
1. ```<div v-xxx=''></div>```
2. 指令就是以数据去驱动DOM行为的，简化DOM操作
3. 指令
	```
	v-text   不可解析html标签
	v-html    可解析html标签
	v-if    做元素的插入（append）和移除（remove）操作
	v-else-if
	v-else
	v-show   display:none 和display：block的切换
	v-for
	数组  item，index
	对象 value，key ，index
	```
 
### vue双向绑定
- v-model   只作用于有value属性的元素 
	```<input v-model="name" v-bind:class="name">```
- 双向数据绑定  页面对于input的value改变，能影响内存中name变量
- 内存js改变name的值，会影响页面重新渲染最新值

### 过滤器
- 过滤器就是可以对我们的数据进行添油加醋然后再显示
- 过滤器有全局过滤器和组件内的过滤器
  - 全局过滤器Vue.filter('过滤器名',过滤方式fn );
  - 组件内的过滤器 filters:{ '过滤器名',过滤方式fn  }
  - {{ msg | 过滤器名}}
- 最终都是在过滤方式fn里面return产出最终你需要的数据
   
### vue中的this是vue封装好给我们使用的，跟平常方法里面的this是不同的 
   
### 数据监听watch计算属性computed
1. 当watch监听的是复杂数据类型的时候需要做深度监听（写法如下）
	```
	watch:{
		msg:{
		  handler(val){
		   if(val.text=='love'){
			alert(val.text)
		   }
		  },
		  deep:true//开启深度监听
		}
	}
 	```
2. computed  监视对象,写在了函数内部,凡是函数内部有this.相关属性,
改变都会触发当前函数   

### 组件化开发
1. 创建组件的两种方式
	```
    var Header = { 
		template:'模板' , 
		data是一个函数,
		methods:功能,
		components:子组件们 
		}//局部声明
    ```

    ```
    Vue.component('组件名',组件对象);//全局注册 等于注册加声明了
    ```
2. 组件类型
	- 通用组件（例如表单、弹窗、布局类等)
	- 业务组件（抽奖、机器分类）
	- 页面组件（单页面开发程序的每个页面的都是一个组件、只完成功能、不复用）
   
### slot插槽和ref、$parent  
1. slot插槽
	- slot就是子组件里给DOM留下的坑位
	- <子组件>DOM</子组件>
	- slot是动态的DOM
2. ref获取子组件实例
	- 识别：在子组件或元素上使用属性ref="xxxx"
	- 获取：this.$refs.xxxx 获取元素
	- $el 是拿其DOM
3. $parent获取父组件实例（可在子组件直接使用this.$parent即可）

### 父子组件的通信
1. 父传子
	- 父用子的时候通过属性传递
	- 子要声明props:['属性名'] 来接收
	- 收到就是自己的了，随便你用
		- 在template中 直接用
		- 在js中 this.属性名用
2. 子传父
	- 子组件里通过$emit('自定义事件名',变量1，变量2)触发
	- 父组件@自定义事件名=‘事件名’监听
		```
		子组件方法里  this.$emit('sendfather',val1,val2)触发自定义事件
		父组件里  <child @sendfather='mymethods'></child>
		```
   
### 非父子组件的通信
1. 创建一个空实例（bus中央事件总线也可以叫中间组件）
2. 利用$emit  $on的触发和监听事件实现非父子组件的通信   
	```
	Vue.prototype.$bus=new Vue()//在vue上面挂载一个$bus作为中央处理组件
	this.$bus.$emit('自定义事件名','传递的数据')//触发自定义事件传递数据
	this.$bus.$on('自定义事件名'，fn)//监听自定义事件获取数据
	```
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   