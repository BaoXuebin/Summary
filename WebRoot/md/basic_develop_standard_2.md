# 基础开发规范（2）

### 命名规范

#### 包命名

全部使用小写字母，尽量使用有意义的单词，例：com.wondersgroup.esf。

#### 类和接口命名

使用有意义的单词或单词简写，各单词首字母大写，其他字母小写，所有接口命名统一以I字母开头。例如：class UserInfo; interface IUserInfo。

本框架中，类的功能分多个层次，各层次类的命名有各自的特点。以下，包含了大多数常用的、基本类型的类的命名规则，但无法包罗所有类的情况。其他类的命名可以以此为参考。

|类型 | 规则 | 示例|
| :- | :-------: |:-------:|
|BO对象| BO类根据数据库表名转换而来，接口在前面增加一个字母I |数据库表user_info，BO类UserInfo，BO接口IUserInfo|
|BO对象复合主键| BO对象名 + PK（不推荐使用复合主键） |  UserGroupPK|
|持久层对象  | 数据库对象类名 + Dao，接口在前面增加一个字母I | JpaBaseDao，IBaseDao|
|业务层对象   |业务逻辑名 + Service，接口在前面增加一个字母I  |  SecurityService，ISecurityService|
|控制层对象   |页面逻辑门 + Controller | LoginController|
|工具类 |工具描述 + Util| AppPropertyUtil|
|常量类 |模块名称 + Constants  |  DicLoadConstants|

注1：数据库表名一般是使用下划线的，而java对象不用下划线。因此，数据库对象类的名称，以数据库表名为基础，但并不一致。将数据库表名首字母大写，去除下划线，下划线后的首字母大写，就得到数据库对象类名。例如，数据库用户信息表user_info的数据库对象类名为UserInfo。

#### 方法命名

原则上首字母小写，后面的各单词首字母大写。使用有意义的单词或单词简写，例：myMethod()。

业务层类的基本方法命名规范所下表所示：

|功能描述  |  方法名 参数|  返回值|
| :- | :-------: |:-------:|
|新增对象   | addXxx | 值对象 void|
|修改对象  |  modifyXxx|   值对象 void|
|删除对象   | removeXxx  | 值对象 void|
|获取单个对象  |getXxx | Id，值对象|
|获取对象列表  |queryXxx |   查询对象    List、Map等|

注：业务层是数据库事务控制层，以get、query、find、load等开头的方法，将统一设置为只读事务，请不要在这些方法中加入写数据库的逻辑。

控制层的基本方法命名规范。本框架中使用注解方式，控制层的方法名和页面jsp的文件名有密切的关联关系。因此控制层方法命名参照jsp文件命名规范，不完全参照java方法命名规范。

#### 前台文件命名

页面文件的命名，字母全部使用小写，单词之间用下划线分开。页面文件的类型包括：

+ htm和html文件，如info_detail.html
+ jsp文件，如info_detail.jsp
+ javascript的js文件，如validator_1.1.0.js
+ css文件，如style.css
+ 图片文件，如buttom_small.jpg

这里重点讲一下jsp的命名规则。对于jsp文件，必须将模块的名称包含在文件名开头，命名规则如下：

|功能描述  |  方法名 |参数|
| :- | :-------: |:-------:|
|新增 | xxx_add.jsp ||
|修改|  xxx_modify.jsp  |值对象|
|编辑（新增、修改的合并）  |  xxx_edit.jsp   | 值对象|
|详细信息|    xxx_detail.jsp|  值对象|
|列表|  xxx_list.jsp |  List，分页信息|
|查询条件|    xxx_search.jsp | |

#### 常量、变量、数组命名

|类型  |说明| 例子|
| :- | :-------: |:-------:|
| 属性、变量 |首字母小写，后面的各单词首字母大写，使用有意义的属性命名。  | int i;float myWidth;|
|常量  |应该都大写，单词之间用下划线分开，并且指出完整含义。 | static final int MAX_WIDTH = 999;|
|方法的参数  | 首字母小写，后面的各单词首字母大写。使用有意义的参数命名，如果可能的话，使用和要赋值的变量一样的名字。| myMethod(String infoId);|
|数组|  方括号放在变量类型后面。  |  byte[] buffer;|



