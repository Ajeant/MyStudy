##### 扫描包注解
1. <context:annotation-config> declares support for general annotations such as @Required, @Autowired, @PostConstruct, and so on.
2. <mvc:annotation-driven /> is actually rather pointless. It declares explicit support for annotation-driven MVC controllers 
3. <context:component-scan>除了具有<context:annotation-config>的功能之外，<context:component-scan>还可以在指定的package下扫描以及注册javabean 
4. <context:component-scan>除了具有<context:annotation-config />的功能之外，还具有自动将带有@component,@service,@Repository等注解的对象注册到spring容器中的功能。
5. 解决Invalid bound statement (not found): com.blog.dao.ArticleDao.getFirst10Article
```java
<!-- 如果不添加此节点mybatis的mapper.xml文件都会被漏掉。 -->
		<resources>
            <resource>
                <directory>src/main/java</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <filtering>false</filtering>
            </resource>
        </resources>
```

###spring监听器
1. Spring框架由此启动, contextInitialized也就是监听器类的main入口函数

###DispatcherServelt主要用作职责调度工作，本身主要用于控制流程，主要职责如下：
1. 文件上传解析，如果请求类型是multipart将通过MultipartResolver进行文件上传解析；
2. 通过HandlerMapping，将请求映射到处理器（返回一个HandlerExecutionChain，它包括一个处理器、多个HandlerInterceptor拦截器）；
3. 通过HandlerAdapter支持多种类型的处理器(HandlerExecutionChain中的处理器)；
4. 通过ViewResolver解析逻辑视图名到具体视图实现；
5. 本地化解析；
6. 渲染具体的视图等；
7. 如果执行过程中遇到异常将交给HandlerExceptionResolver来解析。

### DispatcherServlet 处理流程
1. Tomcat 启动，对 DispatcherServlet 进行实例化，然后调用它的 init() 方法进行初始化，在这个初始化过程中完成了：对web.xml 中初始化参数的加载；建立 WebApplicationContext (SpringMVC的IOC容器)；进行组件的初始化；
2. 客户端发出请求，由Tomcat 接收到这个请求，如果匹配 DispatcherServlet 在 web.xml 中配置的映射路径，Tomcat 就将请求转交给 DispatcherServlet 处理；
3. DispatcherServlet 从容器中取出所有 HandlerMapping 实例（每个实例对应一个 HandlerMapping 接口的实现类）并遍历，每个 HandlerMapping 会根据请求信息，通过自己实现类中的方式去找到处理该请求的 Handler (执行程序，如Controller中的方法)，并且将这个 Handler 与一堆 HandlerInterceptor (拦截器) 封装成一个 HandlerExecutionChain 对象，一旦有一个 HandlerMapping 可以找到 Handler 则退出循环
4. DispatcherServlet 取出 HandlerAdapter 组件，根据已经找到的 Handler，再从所有 HandlerAdapter 中找到可以处理该 Handler 的 HandlerAdapter 对象；
5. 执行 HandlerExecutionChain 中所有拦截器的 preHandler() 方法，然后再利用 HandlerAdapter 执行 Handler ，执行完成得到 ModelAndView，再依次调用拦截器的 postHandler() 方法；
6. 利用 ViewResolver 将 ModelAndView 或是 Exception（可解析成 ModelAndView）解析成 View，然后 View 会调用 render() 方法再根据 ModelAndView 中的数据渲染出页面；
7. 最后再依次调用拦截器的 afterCompletion() 方法，这一次请求就结束了。

### bean准备就绪之前
1. Spring对bean进行实例化
2. Spring将值和bean的引用注入到bean对应的属性中
3. 如果bean实现了BeanNameAware接口， Spring将bean的ID传递给setBean-Name()方法
4. 如果bean实现了BeanFactoryAware接口，Spring将调用setBeanFactory()方法，将BeanFactory容器实例传入
5. 如果bean实现了ApplicationContextAware接口，Spring将调用setApplicationContext()方法，将bean所在的应用上下文的引用传入进来
6. 如果bean实现了BeanPostProcessor接口，Spring将调用他们的postProcessBeforeInitialization()方法
7. 如果bean实现了InitializingBean接口，Spring将调用afterPropertiesSet()方法。类似的，如果bean使用init-method声明了初始化方法，该方法也会被调用
8. 如果bean实现了DisposableBean接口，Spring将调用他的postProcessAfterInitialization()方法。
9. 此时，bean已经准备就绪，可以被应用程序使用了，他们将一直在ApplicationContext中，直到它被销毁
10. 如果bean实现了DisposableBean接口，Spring将调用他的destroy()接口方法。如果bean使用destroy-method声明了销毁方法，该方法也会被调用 

### bean装配
1. 在XML中显示配置
2. 在Java中显式配置
3. 隐式的bean发现机制和自动装配

### @profile
1. 通过设定environment的Active Profiles来设定当前的context需要使用的配置环境，在开发中使用@profile注解类或方法，达到在不同的情况下实例化不同的Bean

### 密码校验
1. @NotNull
2. @Size(min=5, max=16, message="{username.size}")
3. 根路径创建ValidationMessages.properties
username.size=Username must be between {min} and {max} characters long.

### @Inject
1. @Inject注解让Spring自动将一个Session Factory注入到HibernateSpitterRepository的sessionFactory属性中，接下来currentSession（）方法中，我们使用这个SessionFactory来获取当前事务的Session

### @ResponseBody（对应有RequestBody）
注解会告知Spring，我们要将返回的对象作为资源发送给客户端，并将其转换为可接受的表述类型，即consumes or produces

### @RestController
他的方法所返回的对象将会通过消息转换机制，产生客户端所需的资源表述(相当于@Controller和@Responsebody)

