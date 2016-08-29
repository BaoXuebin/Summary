# 基础开发规范（5）

#### switch语句

+ 在任何的情况下，必须在最后写default语句。 
```[java]
switch (condition) { 
    case ABC: 
        instruction;
    case DEF; 
        instruction; 
    break; 
    case XYZ; 
        instruction; 
    break; 
    default: 
        instruction; 
    break; 
} 
```

#### 异常

JAVA语言中提供了try/catch来方便用户捕捉异常，进行异常的处理。但是如果使用不当，也会给JAVA程序的性能带来影响。因此，要注意以下两点。 

+ 避免对应用程序的逻辑使用try/catch ，如果可以用if、while等逻辑语句来处理，那么就尽可能的不用try/catch语句。
+ 重用异常，在必须要进行异常的处理时，要尽可能的重用已经存在的异常对象。因为在异常的处理中，生成一个异常对象要消耗掉大部分的时间。
+ 尽量不要在方法上定义显式异常（throws），推荐在方法内使用隐式异常（throw）。
+ 在方法内catch异常后，一定要根据业务需要进行相关处理，比如记录日志，重新抛出异常等。

#### 日志和调试信息

+ 不要直接的使用System.out或者System.err或者Exception的printStackTrace()方法打印出调试信息或Exception，这回影响应用运行效率。
+ 推荐使用Apache Log4J来实现。Log4j布局可以控制日志输出的位置，也可以控制日志输出的级别。log4j的输出信息分五个级别，严重程度从低到高，分别为：
 - DEBUG ： 调试信息
 - INFO ： 一般信息
 - WARN ： 警告信息
 - ERROR ： 一般错误信息
 - FATAL ： 致命错误信息    
 
使用的示例：
```[java]
private static Logger logger = Logger.getLogger(Test.class);
if (logger.isDebugEnabled()) {
    logger.debug(ex.getMessage(), ex);
}
```

#### 资源释放

+ 使用的资源要及时释放，比如文件资源、数据库资源等。

#### java.util包的注意事项

+ 谨慎使用java.util包里面的java.util.Vector和java.util.Hashtable，因为这两个类是synchronized的，比不是synchronized的容器类速度会慢很多。当在单线程的情况下，请使用java.util.ArrayList（接口是：java.util.List）和java.util.HashMap（接口是java.util.Map）。

#### SQL注入攻击

+ 为避免留有恶意SQL注入攻击的漏洞，对于JDBC编程，请使用PreparedStatement，将变量以参数的形式传递到SQL中，避免使用Statement；对于JPA或者Hibernate编程，也请不要将参数直接拼接在jpql或者hql中，而是以参数的形式设置。
+ Hql中避免直接拼接，而是用占位符的方式；

### 代码管理

所有代码都必须放入配置管理，比如SVN。

所有代码都应该及时放入配置管理中，每天离开公司前，都应该将代码check in。

配置管理中的代码，必须是可以编译的，如果下班前代码没有完成，可以加  `//TODO` 或 `//FIXME` 等标志，或加注释，再提交到配置库。