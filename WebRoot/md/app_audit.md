# 应用审计接口

### 功能说明

该接口是应用审计信息的统一接口，实现发送审计信息到服务器，以便统一管理、查询、分析、监测。

该接口只有一个方法。

### 实现说明

接口：com.wondersgroup.esf.security.service ISendAppAuditService

方法：sendAppAuditInfo(AppAuditInfo appAuditInfo)

功能：发送审计记录

默认实现：com.wondersgroup.esfimpl.defaultimpl.service.SendAppAuditServiceImpl

默认实现说明：通过配置拦截器的方式，根据系统配置的WebService服务地址，通过WebService发送审计信息到服务器，保存审计信息到数据库中。

### 配置文件

#### 审计信息配置文件

审计信息配置为数据库表SYS_CONFIG；

```[sql]
INSERT INTO SYS_CONFIG(‘APPAUDIT.STATU’,’true’); 
INSERT INTO SYS_CONFIG(‘APPAUDIT.SERVICE_URL’,’http://127.0.0.1/esf/securityWebService’);
INSERT INTO SYS_CONFIG(‘APPAUDIT.METHOD_NAME’,’ saveAuditInfo);
```

配置文件说明如下：

```[properties]
APPAUDIT.STATU：发送审计信息的开关，true为是，false为否。
APPAUDIT.SERVICE_URL：接收审计信息的WebService地址。
APPAUDIT.METHOD_NAME：接收审计信息的WebService方法。
```

该文件的作用是：在发送应用审计信息时，需要的WebService信息。

该文件通过com.wondersgroup.esf.security.util.AppAuditUtil工具类来操作，读取配置信息，设置开关状态。工具类在实现接口的时候可以用到。

#### 审计方法配置表

审计方法配置表存在于数据库中，表名为dic_audit_method，该表记录controller的方法对应的审计日志记录说明，所有需要记录应用审计日志信息的controller方法都需要配置到该表中。

拦截器com.wondersgroup.esf.security.controller.AppAuditInterceptor会根据配置表信息判断是否发送审计日志，并按配置组装审计日志描述信息。

dic_audit_method表的字段说明：

|字段|	字段名称|	字段说明|
| :- | :-------: |
|ID	|审计事件编号	||
|SYS_ID|	应用系统编号	||
|AUDIT_LEVEL|	日志级别	||
|METHOD_NAME|	方法名	||
|METHOD_DESC|	审计事件描述	||
|EVENT_DETAIL|	审计事件详细信息|	例如：“用户{loginName}登录系统！”，{loginName}为参数名称，拦截器会通过request获取参数内容|

