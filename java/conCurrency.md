### 注解
1. @Retention
    - 定义了该Annotation被保留的时间长短：某些Annotation仅出现在源代码中，而被编译器丢弃；而另一些却被编译在class文件中；编译在class文件中的Annotation可能会被虚拟机忽略，而另一些在class被装载时将被读取（请注意并不影响class的执行，因为Annotation与class在使用上是被分离的）。使用这个meta-Annotation可以对 Annotation的“生命周期”限制。
    - RetentionPolicy.RUNTIME 注解会在class字节码文件中存在，在运行时可以通过反射获取到
    - RetentionPolicy.CLASS 默认的保留策略，注解会在class字节码文件中存在，但运行时无法获得
    - RetentionPolicy.SOURCE 注解仅存在于源码中，在class字节码文件中不包含
2. @Target
    - 说明了Annotation所修饰的对象范围：Annotation可被用于 packages、types（类、接口、枚举、Annotation类型）、类型成员（方法、构造方法、成员变量、枚举值）、方法参数和本地变量（如循环变量、catch参数）。
    - ElementType.CONSTRUCTOR  作用于构造器
    - ElementType.FIELD 作用于域/属性
    ElementType.LOCAL_VARIABLE  用于描述局部变量
    - ElementType.METHOD 作用于方法
    - ElementType.PACKAGE 用于描述包
    - ElementType.PARAMETER 用于描述参数
    ElementType.TYPE 用于描述类、接口(包括注解类型) 或enum声明，最常用
3. @Documented                           javadoc文档生成工具的使用

4. @Inherited 如果一个使用了@Inherited修饰的annotation类型被用于一个class，则这个annotation将被用于该class的子类。

### 多线程
1. AtomicInteger等
2. synchronized作用当前对象，不同对象互不影响；不遗传，父类的synchronized不作用于子类；不可中断，适合竞争不激烈
	1. 可见性：JMM关于synchronized的两条规定
		1. 线程解锁前，必须把共享变量的最新值刷新到主内存
		2. 线程加锁时，将清空工作内存中共享变量的值，从而使用共享变量时需要从主内存中重新读取最新的值（注意，加锁和解锁是同一把）
3. volatile——可见性（非原子性）
	1. 通过加入**内存屏障和禁止重排序***优化来实现的
4. 有序性——Lock、volatile、synchronized
	1. volatile：读操作在写操作之前
	2. 程序次序规则：一个线程内，按照代码顺序，书写在前面的先于后面的
	3. 锁定规则：unLock先于后面对同一个锁的lock
	4. 传递规则：如果A先于B，B先于C，则A先于C
	5. 线程启动规则：Thread对象的start（）方法先于此线程的每一个动作
	6. 线程中断规则：对线程interrupt（）方法先于被中断线程的代码检测到的中断事件的发生
	7. 线程终结规则：线程中所有的操作都先行发生于线程的终止检测，可以通过Thread.join()方法结束、Thread.isAlive()的返回值手段检测到线程已经终止执行
	8. 对象终结规则：一个对象的初始化先于finalize()方法的开始
5. 安全发布对象
	1. 在静态初始化函数中初始化一个对象引用
	2. 将对象的引用保存到volatile类型域或者AtomicReference对象中
	3. 将对象的引用保存到某个正确构造对象的final类型域中
	4. 将对象的引用保存到一个由锁保护的域中
6. 不可变对象需满足条件（final、Collections.unmodifiableXXX：Collection、List等）
	1. 对象创建以后其状态就不能修改
	2. 对象所有域都是final类型
	3. 对象是正确创建的（在对象创建期间，this引用没有逸出
7. 线程封闭：ThreadLocal
8. StringBuilder和StringBuffer
9. 同步容器
	1. ArrayList -> Vector, Stack
	2. HashMap -> HashTable
	3. Collections.synchronized(List、Set、Map)
10. 线程安全——并发容器J.U.C
	1. ArrayList -> CopyOnWriteArrayList
	2. HashSet、TreeSet -> CopyOnWriteArraySet、ConcurrentSkipListSet
	3. HashMap、TreeMap -> ConcurrentHashMap、ConcurrentSkipListMap
11. AQS同步组件
	1. CountDownLatch
	2. Semaphore
	3. CyclicBarrier
	4. ReentrantLock(独有功能：指定公平锁还是非公平锁(synchronized只能是公平锁)；提供了一个Condition类，可以分组唤醒需要唤醒的线程；提供能够中断等待锁的线程的机制，lock.lockInterruptibly)
	5. Condition
	6. FutureTask
12. ReentrantLock(可重入锁)和synchronized的区别
	1. 可重入
	2. 锁的实现
	3. 性能的区别
	4. 功能区别
13. 多线程并发实践
	1. 使用本地变量
	2. 使用不可变类
	3. 最小化锁的作用域范围：S=1/(1-a+a/n)
	4. 使用线程池的Executor，而不是直接使用new Thread执行
	5. 宁可使用同步也不使用线程的wait和notify
	6. 使用BlockingQueue实现生产-消费模式
	7. 使用并发集合而不是加了锁的同步集合
	8. 使用Semaphore创建有界的访问
	9. 宁可使用同步代码块也不使用同步方法
	10. 避免使用静态变量

### 高并发
1. 扩容
	1. 垂直扩容（纵向扩展）：提高系统部件能力（增加内存
	2. 水平扩展（横向扩展）：增加更多系统成员来实现（增加服务器
	3. 扩容——数据库
		1. 读操作扩展：memcache、redis、CDN等缓存
		2. 写操作扩展：Cassandra、Hbase等
2. 缓存特征
	1. 命中率
	2. 最大元素（空间）
	3. 清空策略：FIFO, LFU, LRU, 过期实践, 随机等
3. 缓存分类
	1. 本地缓存：编程实现（成员变量、局部变量、静态变量）、Guaua Cache
	2. 分布式缓存：MemCache、redis
4. 高并发场景下缓存常见问题
	1. 缓存一致性
	2. 缓存并发问题
	3. 缓存穿透问题
	4. 缓存的雪崩现象
5. 消息队列特性
	1. 业务无关：只做消息分发
	2. FIFO：先投递先到达
	3. 容灾：节点的动态增删和消息的持久化
	4. 性能：吞吐量提升，系统内部通信效率提高
6. 为什么需要消息队列
	1. 【生产】和【消费】的速度或稳定性等因素不一致
7. 消息队列好处
	1. 业务解耦
	2. 最终一致性
	3. 广播
	4. 错峰与流控
8. 应用限流——算法
	1. 计数器法
	2. 滑动窗口
	3. 漏桶算法
	4. 令牌桶算法