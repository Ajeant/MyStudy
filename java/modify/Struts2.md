### 说下Struts的设计模式
MVC模式:  
1. web应用程序启动时就会加载并初始化ActionServler。
2. 用户提交表单时，一个配置好的ActionForm对象被创建，并被填入表单相应的数据，ActionServler根据Struts-config.xml文件配置好的设置决定是否需要表单验证，如果需要就调用ActionForm的Validate（）验证后选择将请求发送到哪个Action，如果Action不存在，ActionServlet会先创建这个对象，然后调用Action的execute（）方法.
3. Execute（）从ActionForm对象中获取数据，完成业务逻辑，返回一个ActionForward对象，ActionServlet再把客户请求转发给ActionForward对象指定的jsp组件，ActionForward对象指定的jsp生成动态的网页，返回给客户。

### 拦截器和过滤器的区别
1. 拦截器是基于java反射机制的，而过滤器是基于函数回调的。
2. 过滤器依赖于servlet容器，而拦截器不依赖于servlet容器。
3. 拦截器只能对Action请求起作用，而过滤器则可以对几乎所有请求起作用。
4. 拦截器可以访问Action上下文、值栈里的对象，而过滤器不能。
5. 在Action的生命周期中，拦截器可以多次调用，而过滤器只能在容器初始化时被调用一次。

### struts2是如何启动的？
1. struts2框架是通过Filter启动的，即StrutsPrepareAndExecuteFilter，此过滤器为struts2的核心过滤器； 
2. StrutsPrepareAndExecuteFilter的init()方法中将会读取类路径下默认的配置文件struts.xml完成初始化操作。struts2读取到struts.xml的内容后，是将内容封装进javabean对象然后存放在内存中，以后用户的每次请求处理将使用内存中的数据，而不是每次请求都读取struts.xml文件。

### struts2是如何管理action的？这种管理方式有什么好处？ 
1. struts2框架中使用包来管理Action，包的作用和java中的类包是非常类似的。主要用于管理一组业务功能相关的action。在实际应用中，我们应该把一组业务功能相关的Action放在同一个包下。 

### struts2中的默认包struts-default有什么作用？ 
1. struts-default包是由struts内置的，它定义了struts2内部的众多拦截器和Result类型，而Struts2很多核心的功能都是通过这些内置的拦截器实现，如：从请求中把请求参数封装到action、文件上传和数据验证等等都是通过拦截器实现的。当包继承了struts-default包才能使用struts2为我们提供的这些功能。  
2. struts-default包是在struts-default.xml中定义，struts-default.xml也是Struts2默认配置文件。 Struts2每次都会自动加载 struts-default.xml文件。 
3. 通常每个包都应该继承struts-default包。

### struts2如何对指定的方法进行验证？ 
1. validate()方法会校验action中所有与execute方法签名相同的方法； 

### struts2的执行流程
1. 客户端浏览器发出HTTP请求。
2. 根据web.xml配置，该请求被FilterDispatcher接收。
3. 根据struts.xml配置，找到需要调用的Action类和方法， 并通过IoC方式，将值注入给Aciton。
4. Action调用业务逻辑组件处理业务逻辑，这一步包含表单验证。
5. Action执行完毕，根据struts.xml中的配置找到对应的返回结果result，并跳转到相应页面。
6. 返回HTTP响应到客户端浏览器。