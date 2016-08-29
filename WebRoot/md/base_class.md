# 开发基类

本框架com.wondersgroup.esf.base下的类，为框架的基础类，应用程序中的大多数类，都是从基础类中继承和实现的。

### bo

数据对象的基础类。

| 类名/接口名 |  说明    |
| :- | :-------: |
| BaseBo  | Bo基类，dao所有的对象操作都基于这个BO  |

### dao

持久层的基础接口和基础类。**在实际开发中，dao层可以不写，在Service层直接继承BaseService即可**

| 包名 |  说明    |
| :- | :-------: |
| IBaseDAO  | 封装底层数据操作的公用接口。其他模块的service层和dao层通过注入bean的方式调用该接口。  |
| BaseJpaDAO | JPA持久层实现基础类，实现IBaseDAO接口，封装常用增删改查操作，及其他jpql查询、分页查询等公用方法。 |
| ... | ... |

### service

业务层的基础接口和基础类。

### exception

基础的异常类。

### web

web层基础类。

### util

外部的开源代码中，有很多成熟的工具，比如apache的工具包org.apache.commons.lang。本框架根据实际需要，又另外提炼了一些需要的工具类，这些公共工具类位于com.wondersgroup.esf.base.util包或其子包中。各功能模块中也可以有一些工具类，不过那些工具类是各模块专用的。

本框架中的公共工具类，类名都是以Util结尾的。

| 类名或包名 |  说明    |
| :- | :-------: |
| ApplicationContextUtil | 上下文工具类。获取Spring的Bean，上下文路径等。 |
| StringUtil | 字符处理工具类。包含 org.apache.commons.lang.StringUtils 中没有的字符串处理方法。比如html字符串处理、字符编码转换等。 |
| DateUtil |    日期处理工具类。相关的日期处理工具类为org.apache.commons.lang.time.DateFormatUtils。|
| NumberUtil |  数字处理工具类。包含 org.apache.commons.lang.math.NumberUtils 中没有的或处理方式有差异的数字处理方法。比如数字的字符串显示格式，字符串的数字构造等。|
| SecurityUtil |    密码加密解密工具类。如MD5加密算法、随机密码等。|
| DatabaseUtil  |   数据库操作工具类。包括产生分页语句等方法，处理分页列表的方法、释放数据库资源等。|
| IDCardUtil | 身份证号码处理工具类。|
| ListMapUtil | List和Map处理工具类。在前台中使用的比较多，比如AJAX和TagLib。  |
| BeanUtils |   位于ext子包中，扩展了apache的BeanUtils类，解决了java.sql.Date的复制问题，解决了null转换结果变化的问题。| 
| ExcelUtil  |  读、写、导出Excel文件。| 
| ... | ... | 

