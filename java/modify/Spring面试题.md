### Spring模块
1. Spring Core：核心类库，提供IOC服务；
2. Spring Context：提供框架式的Bean访问方式，以及企业级功能（JNDI、定时任务等）；
3. Spring AOP：AOP服务；
4. Spring DAO：对JDBC的抽象，简化了数据访问异常的处理；
5. Spring ORM：对现有的ORM框架的支持；
6. Spring Web：提供了基本的面向Web的综合特性，例如多方文件上传；
7. Spring MVC：提供面向Web应用的Model-View-Controller实现。

### Spring优点
1. spring属于低侵入式设计，代码的污染极低；
2. spring的DI机制将对象之间的依赖关系交由框架处理，减低组件的耦合性；
3. Spring提供了AOP技术，支持将一些通用任务，如安全、事务、日志、权限等进行集中式管理，从而提供更好的复用。
4. spring对于主流的应用框架提供了集成支持。

### AOP（Aspect Oriented Programming）
1. Aspect（切面）： Aspect 声明类似于 Java 中的类声明，在 Aspect 中会包含着一些 Pointcut 以及相应的 Advice。
2. Joint point（连接点）：表示在程序中明确定义的点，典型的包括方法调用，对类成员的访问以及异常处理程序块的执行等等，它自身还可以嵌套其它 joint point。
3. Pointcut（切点）：表示一组 joint point，这些 joint point 或是通过逻辑关系组合起来，或是通过通配、正则表达式等方式集中起来，它定义了相应的 Advice 将要发生的地方。
4. Advice（增强）：Advice 定义了在 Pointcut 里面定义的程序点具体要做的操作，它通过 before、after 和 around 来区别是在每个 joint point 之前、之后还是代替执行的代码。
5. Target（目标对象）：织入 Advice 的目标对象.。
6. Weaving（织入）：将 Aspect 和其他对象连接起来, 并创建 Adviced object 的过程

### OOP 与 AOP 的区别
1. 面向目标不同：简单来说 OOP 是面向名词领域，AOP 面向动词领域。
2. 思想结构不同：OOP 是纵向结构，AOP 是横向结构。
3. 注重方面不同：OOP 注重业务逻辑单元的划分，AOP 偏重业务处理过程中的某个步骤或阶段。

### Spring框架中的单例Beans是线程安全的么？
1. Spring框架并没有对单例bean进行任何多线程的封装处理。关于单例bean的线程安全和并发问题需要开发者自行去搞定。但实际上，大部分的Spring bean并没有可变的状态(比如Serview类和DAO类)，所以在某种程度上说Spring的单例bean是线程安全的。如果你的bean有多种状态的话（比如 View Model 对象），就需要自行保证线程安全。最浅显的解决办法就是将多态bean的作用域由“singleton”变更为“prototype”。

### Spring 框架中都用到了哪些设计模式？
1. 工厂模式：BeanFactory就是简单工厂模式的体现，用来创建对象的实例；
2. 单例模式：Bean默认为单例模式。
3. 代理模式：Spring的AOP功能用到了JDK的动态代理和CGLIB字节码生成技术；
4. 模板方法：用来解决代码重复的问题。比如. RestTemplate, JmsTemplate, JpaTemplate。
5. 观察者模式：定义对象键一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都会得到通知被制动更新，如Spring中listener的实现--ApplicationListener。

### spring的事务传播行为：
1. spring事务的传播行为说的是，当多个事务同时存在的时候，spring如何处理这些事务的行为。
2. PROPAGATION_REQUIRED：如果当前没有事务，就创建一个新事务，如果当前存在事务，就加入该事务，该设置是最常用的设置。
3. PROPAGATION_SUPPORTS：支持当前事务，如果当前存在事务，就加入该事务，如果当前不存在事务，就以非事务执行。
4. PROPAGATION_MANDATORY：支持当前事务，如果当前存在事务，就加入该事务，如果当前不存在事务，就抛出异常。
5. PROPAGATION_REQUIRES_NEW：创建新事务，无论当前存不存在事务，都创建新事务。
6. PROPAGATION_NOT_SUPPORTED：以非事务方式执行操作，如果当前存在事务，就把当前事务挂起。
7. PROPAGATION_NEVER：以非事务方式执行，如果当前存在事务，则抛出异常。
8. PROPAGATION_NESTED：如果当前存在事务，则在嵌套事务内执行。如果当前没有事务，则按REQUIRED属性执行。

### Spring中的隔离级别：
1. ISOLATION_DEFAULT：这是个 PlatfromTransactionManager 默认的隔离级别，使用数据库默认的事务隔离级别。
2. ISOLATION_READ_UNCOMMITTED：读未提交，允许另外一个事务可以看到这个事务未提交的数据。
3. ISOLATION_READ_COMMITTED：读已提交，保证一个事务修改的数据提交后才能被另一事务读取，而且能看到该事务对已有记录的更新。
4. ISOLATION_REPEATABLE_READ：可重复读，保证一个事务修改的数据提交后才能被另一事务读取，但是不能看到该事务对已有记录的更新。
5. ISOLATION_SERIALIZABLE：一个事务在执行的过程中完全看不到其他事务对数据库所做的更新。

### 什么是Spring IOC 容器
1. Spring IOC 负责创建对象，管理对象（通过依赖注入（DI），装配对象，配置对象，并且管理这些对象的整个生命周期

### 什么是Spring的依赖注入
1. 依赖注入，是IOC的一个方面，是个通常的概念，它有多种解释。这概念是说你不用创建对象，而只需要描述它如何被创建。你不在代码里直接组装你的组件和服务，但是要在配置文件里描述哪些组件需要哪些服务，之后一个容器（IOC容器）负责把他们组装起来。







