# 核心标签库

[查看实例演示](../example/jstl_core.jsp)

在 jsp 页面的头部加上语句：`<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`

|     标签      |                                   描述                                    |
| :-----------: | :-----------------------------------------------------------------------: |
|    <c:out>    |                       用于在JSP中显示数据，就像<%=                        |
|    <c:set>    |                               用于保存数据                                |
|  <c:remove>   |                               用于删除数据                                |
|   <c:catch>   |            用来处理产生错误的异常状况，并且将错误信息储存起来             |
|    <c:if>     |                       与我们在一般程序中用的if一样                        |
|  <c:choose>   |                 本身只当做<c:when>和<c:otherwise>的父标签                 |
|   <c:when>    |                 <c:choose>的子标签，用来判断条件是否成立                  |
| <c:otherwise> | <c:choose>的子标签，接在<c:when>标签后，当<c:when>标签判断为false时被执行 |
|  <c:import>   |                            检索一个绝对或相对                             |
|  <c:forEach>  |                      基础迭代标签，接受多种集合类型                       |
| <c:forTokens> |                   根据指定的分隔符来分隔内容并迭代输出                    |
|   <c:param>   |                     用来给包含或重定向的页面传递参数                      |
| <c:redirect>  |                           重定向至一个新的URL.                            |
|    <c:url>    |                      使用可选的查询参数来创造一个URL                      |

下面，将依照标签的重要程度列出。

### <c:if> 标签

用于判断指定表达式的值，如果值为 True ，则执行主体内容。

**语法**

	<c:if test="<boolean>" var="<string>" scope="<string>">
	    ...主体内容
	</c:if>
**属性**

|      属性       |      描述       |    是否必要     |     默认值     |
| :---------: | :---------: | :---------: | :---------: |
|    test     |      条件       |      是      |      无      |
|     var     | 用于存储条件结果的变量 |      否      |      无      |
|    scope    |  var属性的作用域  |      否      |    page     |

### <c:forEach>,<c:forTokens> 标签

<c:forEach>标签是更加通用的标签，因为它迭代一个集合中的对象。    
<c:forTokens>标签通过指定分隔符将字符串分隔为一个数组然后迭代它们。

**语法**
    #forEach 语法
	<c:forEach items="<object>" begin="<int>" end="<int>" step="<int>" 
	    var="<string>" varStatus="<string>">
	</c:forEach>
	
	#forTokens 语法
	<c:forTokens items="<string>" delims="<string>" begin="<int>" end="<int>"
        step="<int>" var="<string>" varStatus="<string>">
    </c:forTokens>

**属性**

<c:forEach>标签有如下属性：

|   属性    |                    描述                    | 是否必要 |    默认值    |
| :-------: | :----------------------------------------: | :------: | :----------: |
|   items   |               要被循环的信息               |    否    |      无      |
|   begin   |  开始的元素（0=第一个元素，1=第二个元素）  |    否    |      0       |
|    end    | 最后一个元素（0=第一个元素，1=第二个元素） |    否    | Last element |
|   step    |              每一次迭代的步长              |    否    |      1       |
|    var    |           代表当前条目的变量名称           |    否    |      无      |
| varStatus |           代表循环状态的变量名称           |    否    |      无      |

<c:forTokens> 还有另一个属性

|  属性  |  描述  | 是否必要 | 默认值 |
| :----: | :----: | :------: | :----: |
| delims | 分隔符 |    是    |   无   |

### <c:choose>, <c:when>, <c:otherwise> 标签

<c:choose>标签与Java switch语句的功能一样，用于在众多选项中做出选择。
switch语句中有case，而<c:choose>标签中对应有<c:when>，switch语句中有default，而<c:choose>标签中有<c:otherwise>。

**语法**

	<c:choose>
        <c:when test="<boolean>"/>
            ...
        </c:when>
        <c:when test="<boolean>"/>
            ...
        </c:when>
        ...
        ...
        <c:otherwise>
            ...
        </c:otherwise>
	</c:choose>

**属性**

- <c:choose>标签没有属性。
- <c:when>标签只有一个属性，在下表中有给出。
- <c:otherwise>标签没有属性。
- <c:when>标签的属性如下：

| 属性 | 描述 | 是否必要 | 默认值 |
| :--: | :--: | :------: | :----: |
| test | 条件 |    是    |   无   |

### <c:redirect> 标签

<c:redirect>标签通过自动重写URL来将浏览器重定向至一个新的URL，它提供内容相关的URL，并且支持c:param标签。

**语法**

	<c:redirect url="<string>" context="<string>"/>
	
**属性**

|  属性   |               描述               | 是否必要 |    默认值    |
| :-----: | :------------------------------: | :------: | :----------: |
|   url   |             目标URL              |    是    |      无      |
| context | 紧接着一个本地网络应用程序的名称 |    否    | 当前应用程序 |

### <c:url> 标签

<c:url>标签将URL格式化为一个字符串，然后存储在一个变量中。    
这个标签在需要的时候会自动重写URL。    
var属性用于存储格式化后的URL。    
<c:url>标签只是用于调用response.encodeURL()方法的一种可选的方法。它真正的优势在于提供了合适的URL编码，包括<c:param>中指定的参数。

**语法**

	<c:url
  	    var="<string>"
 	    scope="<string>"
        value="<string>"
        context="<string>"/>

**属性**

|  属性   |          描述          | 是否必要 |    默认值     |
| :-----: | :--------------------: | :------: | :-----------: |
|  value  |        基础URL         |    是    |      无       |
| context | 本地网络应用程序的名称 |    否    | 当前应用程序  |
|   var   |    代表URL的变量名     |    否    | Print to page |
|  scope  |    var属性的作用域     |    否    |     Page      |

### <c:param> 标签

<c:param>标签用于在<c:url>标签中指定参数，而且与URL编码相关。    
在<c:param>标签内，name属性表明参数的名称，value属性表明参数的值。

**语法**

	<c:param name="<string>" value="<string>"/>

**属性**

| 属性  |          描述           | 是否必要 | 默认值 |
| :---: | :---------------------: | :------: | :----: |
| name  | URL中要设置的参数的名称 |    是    |   无   |
| value |        参数的值         |    否    |  Body  |
