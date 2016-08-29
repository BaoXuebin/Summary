# 字典缓存

### 功能说明

字典缓存管理的主要目的是将数据库中的字典代码、名称或其他属性加载到应用服务器内存中，以方便页面的使用。

字典缓存冲的字典分两种类型，字典数据全部存放在数据库中：

+ 简单字典：只查询key和value两个字段的字典，第一个字段为key，第二个字段为value，比如民族代码和民族名称。
+ 复杂字典：查询出三个或三个以上字段的字典，第一个字段为key，其他字段为value，比如部门代码、部门名称、部门类型、部门负责人。

字典缓存管理功能如下：

|功能简述	|功能描述|
| -: | :-: |
|取得一个字典数据|	根据字典的编号（一般定义为常量），可以直接取出字典key和value的Map对象|
|取得一个简单字典项名称	|根据字典的编号和字典项key值，可以直接取出简单字典项value值|
|取得一个复杂字典项Map|	根据字典的编号和字典项key值，可以直接取出复杂字典value的Map对象|
|加载所有字典数据	|将所有字典数据加载到内存中，可在应用启动时调用，也可在应用系统运行过程中重新加载|
|加载一个字典数据	|应用启动后，如果某个字典的内容发生了变化，可以对某个具体字典的的数据进行重载。|
|加载某张数据库表相关的所有字典数据	|应用启动后，如果某张数据库表的内容发生了变化，可以对该表相关的所有字典数据进行重载。|

### 字典缓存加载配置

1  字典缓存加载信息配置在classes目录下的dicLoadConfig.xml文件中，配置文件格式如下：

```[xml]
<?xml version="1.0" encoding="UTF-8"?>
<dics>
	<dic dicId="userIdName" dicType="simple" keyDataType="String" sql="select user_id, user_name from spt_user where user_id != 'admin'" />
	<dic dicId="user" dicType="complex" keyDataType="String" sql="select user_id, user_name, login_name, sex, removed from spt_user where user_id != 'admin'"/>
</dics>
```

字典缓存配置属性说明如下：

| 属性	|属性说明|
| -: | :-: |
|dicId	|字典编号，是应用系统调用该字典缓存数据的字典编号，一般在应用系统中定义为常量|
|dicType|	字典类型：Simple：简单字典，sql查询结果中第一个字段为key，第二个字段为value。complex：复杂字典，sql查询结果中第一个字段为key，其他字段为value，可以有多个value字段|
|sql|	查出字典数据的原生sql语句，select结果中的第一个字段为key字段，select语句中只放需要的字段，不建议使用*号。格式： select ... from ... where ... order by ...|

2 在数据库表DIC\_LOAD\_CONFIG中添加；

|字段名称|	字段说明|
| -: | :-: |
|DIC_ID	|字典编号，是应用系统调用该字典缓存数据的字典编号，一般在应用系统中定义为常量|
|DIC_NAME	|字典名称|
|DIC_TYPE	|字典类型：Simple：简单字典，sql查询结果中第一个字段为key，第二个字段为value。complex：复杂字典，sql查询结果中第一个字段为key，其他字段为value，可以有多个value字段|
|TABLE_NAME	|表名|
|ITEM\_KEY\_COLUMN|	Key字段|
|ITEM\_NAME\_COLUMN	|Value字段|
|APPEND\_SQL|	Where语句或者order by语句。格式： where … order by …|
|VALUE\_LIST	|Json格式字符串，例如：{"1":"局领导","2":"注册领导","3":"工商所领导"}|
|DIC\_DESC	|备注说明|

**建议都在数据库表中配置。**

### 字典缓存调用说明

应用系统通过com.wondersgroup.esf.dicload.util.DicLoadUtil工具类实现对字典缓存数据的调用。它是一个单例类，必须通过getInstance方法获得实例后，才能使用该类的其它方法。

以下为该类API列表。

|方法名	|功能|
| -: | :-: |
|getInstance|	取得单例实例|
|getDic	|根据子带你编号取得某字典数据的Map列表|
|getDicValueByKey|	根据字典项键值，取得某字典的字典项value值|
|getComplexDicItemMap|	根据字典项键值，取得某复杂字典的字典数据Map，Map中的key为字段名，value为字段值|
|loadAllDic|	加载所有字典数据|
|loadDicById	|根据字典编号加载特定字典数据|
|loadDicByTable	|根据数据库表名加载所有和该表相关的字典数据|

### 更新缓存数据

系统每个小时自动重新加载所有字典数据。

可通过提供后台页面操作方式，或者提供REST服务的方式，更新缓存中的字典数据，更新方式为全部更新、按字典编号更新、按数据库表更新。


