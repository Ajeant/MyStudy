### @SpringBootApplication
1. 开启了Spring的组件扫描和Spring Boot的自动配置功能。实际
上，@SpringBootApplication将三个有用的注解组合在了一起。
	1. Spring的@Configuration：标明该类使用Spring基于Java的配置
	2. Spring的@ComponentScan：启用组件扫描，这样你写的Web控制器类和其他组件才能被自动发现并注册为Spring应用程序上下文里的Bean。本章稍后会写一个简单的Spring MVC控制器，使用@Controller进行注解，这样组件扫描才能找到它。
	3. SpringBoot的@EnableAutoConfiguration：这个不起眼的小注解也可以称为@Abracadabra，就是这一行配置开启了SpringBoot自动配置的魔力，让你不用再写成篇的配置了

### application.properties
1. server.port=80(修改tomcat监听端口)

### 排除传递依赖
1. 如果在用Gradle，你可以这样排除传递依赖：  
compile("org.springframework.boot:spring-boot-starter-web") { 
	exclude group: 'com.fasterxml.jackson.core' 
} 
2. 在Maven里，可以用<exclusions>元素来排除传递依赖。下面这个引入Spring Boot的
build.gradle的<dependency>增加了<exclusions>元素去除Jackson：
<dependency> 
	<groupId>org.springframework.boot</groupId> 
	<artifactId>spring-boot-starter-web</artifactId>
	<exclusions> 
		<exclusion> 
			<groupId>com.fasterxml.jackson.core</groupId> 
		</exclusion> 
	</exclusions> 
</dependency>

### @Controller和@RestController的区别
1. 如果只是使用@RestController注解Controller，则Controller中的方法无法返回jsp页面，或者html，配置的视图解析器 InternalResourceViewResolver不起作用，返回的内容就是Return 里的内容。(相当于加上注解@ResponseBody)
2. 如果需要返回到指定页面，则需要用 @Controller配合视图解析器InternalResourceViewResolver才行。如果需要返回JSON，XML或自定义mediaType内容到页面，则需要在对应的方法上加上@ResponseBody注解。