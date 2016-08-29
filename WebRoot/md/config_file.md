# 配置文件

框架配置文件包括应用**系统配置文件**、**数据库连接配置文件**、**spring配置文件**、**spring mvc配置文件**、**web.xml**文件。

### 应用系统配置文件

应用系统配置文件为classes目录下的app.properties文件，主要配置应用系统相关的配置信息。

此配置可由各项目组根据需要调整参数值，也可以增加新的参数项，但不可以修改esf框架中提供的参数名。

具体内容如下：

```[properties]
 # 应用系统编号，在应用软件信息表（ESF_APP_INFORMATION）中定义
APP.APP_CODE 1234
 # 用户未登录，或者登录超时后跳转的页面
APP.TIMEOUT_PATH /login.jsp
 # 应用报错后统一跳转的页面
APP.ERROR_PATH /error.jsp
 # 应用系统登录页面
APP.LOGIN_URL /login.jsp
 # 应用系统logo图片文件，在页面左上侧位置
APP.LOGO=images/logo.gif
 # 应用系统名称图片页面，在页面右上侧位置
APP.IMAGE images/system_name.jpg
 # 登录时主操作区默认打开的URL连接
APP.MAIN_DEFAULT_URL welcome.jsp
 # 应用系统脚注区显示的文字
APP.FOOTER=万达信息股份有限公司
 # 应用系统自定义链接内容，格式为“名称1|链接1,名称2|链接2,…”
APP.LINKS 首页|/esf/g_main.do,代办事务|/waiting.do
```

### 数据库连接配置文件

数据库连接配置文件为classes目录下的db.properties文件，主要配置连接数据库相关配置信息。

此配置可由各项目组根据需要调整参数值，也可以增加新的参数项，但不可以修改esf框架中提供的参数名。

具体内容如下：

```[properties]
 # 定义数据库方言
jpa.dialect org.hibernate.dialect.MySQL5Dialect
 # 数据库连接驱动类
jpa.connection.driver_class com.mysql.jdbc.Driver
 # 数据库连接URL
jpa.connection.url jdbc\:mysql\:\//127.0.0.1\:3306/esf
 # 数据库连接用户名
jpa.connection.username esf
 # 数据库连接用户密码
jpa.connection.password esf
 # 是否显示JPA执行SQL语句
jpa.showsql true
 # 数据源名称，通常定义在应用服务器中间件中
jpa.jndi_name jdbc/esf
```

### web.xml

web.xml文件是web应用的基础配置文件，主要定义了必要的侦听器、过滤器、servlet、欢迎页面等内容。

此配置文件可由各项目组进行有限的修改，项目组可修改内容如下：

```[xml]
<display-name>Wonders ESF</display-name>
<context-param>
    <param-name>webAppRootKey</param-name>
    <param-value>esfApp.root</param-value>
</context-param>
```

以上配置中的红色字体的内容，应该在项目搭建时根据项目名称进行调整。除此之外的ESF框架提供的其他配置信息，项目组不可以修改。项目组可以增加新的配置，比如可以新增过滤器、servlet的配置信息。

### Spring配置文件

框架中的spring mvc配置文件为`WEB-INF/spring-servlet.xml`文件，Spring配置文件为`WEB-INF/classes/applicationContext.xml`文件。主要定义了数据源、事务、注解、jsp文件位置、spring拦截器等内容。

这两个文件项目组不允许修改，如果项目组需要新增spring的配置信息，可以另建一个spring配置文件，名称符合`applicationContext*.xml`的规则即可。

