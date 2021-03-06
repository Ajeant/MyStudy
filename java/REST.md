### REST 架构风格最重要的架构约束有 6 个：
1. 客户 - 服务器（Client-Server）  
通信只能由客户端单方面发起，表现为请求 - 响应的形式。
2. 无状态（Stateless）  
通信的会话状态（Session State）应该全部由客户端负责维护。
3. 缓存（Cache）  
响应内容可以在通信链的某处被缓存，以改善网络效率。
4. 统一接口（Uniform Interface）  
通信链的组件之间通过统一的接口相互通信，以提高交互的可见性。
5. 分层系统（Layered System）  
通过限制组件的行为（即，每个组件只能“看到”与其交互的紧邻层），将架构分解为若干等级的层。
6. 按需代码（Code-On-Demand，可选）  
支持通过下载并执行一些代码（例如 Java Applet、Flash 或 JavaScript），对客户端的功能进行扩展。