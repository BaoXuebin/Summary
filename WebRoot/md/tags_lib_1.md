# 标签库（上）

自定义标签库的目的是为了一些自定义属性，能够集成到标签中，方便开发人员统一使用。但是自定义标签具有一定的局限性，在开发人员使用的时候，不能用自定义属性（也就是标签未定义的属性），否则jsp不能编译通过。

ESF中的标签库，是参照spring的标签库实现的，name能够绑定request中的attribute，能够自动设置控件的value。

所有的控件统一的属性有：name、value、helpId、attribute1、attribute2、attribute3、attribute4、attriute5、cssClass、style、lang、title、dir、tabindex、disabled、onclick、odblclick、onmousedown、onmouseup、onmouseover、onmousemove、onmouseut、onkeypress、onkeyup、onkeydown、onfocus、onblur、onchange、accessey、size、alt、onselect、multiple。

特殊说明：

+ helpId：控件的帮助编号。
+ attribute1、attribute2、attribute3、attribute4、attribute5：提供了5个自定义属性，方便开发人一些特殊使用。

### input

文本框标签，包含的属性：

+ Autocomplete：自动完成加载数据的地址。
+ autocompleteCallback：加载数据完成后的回调函数。
+ Readonly：只读。
+ Maxlength：最大长度。

例如：
```[jsp]
<form:input name="input1" autocomplete="filter.jsp" autocompleteCallback="autoCallback" /> 
编译解析为：
<input type="text" name="input1" autocomplete="filter.jsp" autocompleteCallback="autoCallback"/>
自动完成功能，可直接使用autocomplete标签。
```

### password

密码框标签，包含的属性：

+ showPassword，是否显示密码，true为密码，false则等同于input框。

例如：

```[jsp]
<form:password name="password1" showPassword="true" />
编译解析为：
<input type="password" name="password1" />
```

### hidden

隐藏域标签。

例如：

```[jsp]
<form:hidden name="hidden1" />
编译解析为：
<input type="hidden" name="hidden1" />
```

### dataInput

日期标签，包含属性：

+ Format：日期的格式；例如：yyyy-MM-dd 、yyyy-MM-dd hh:mm:ss等。

例如：

```[jsp]
<form:dateInput name="date1" format="yyyy-MM-dd" />
编译解析为：
<input type="text" name="date1" datepiker="DATE" />
```

### textarea

文本域标签，包含的属性有：

+ cols：列宽度。
+ rows：行高度
+ readonly：只读。
+ maxlength：最大长度。

例如：

```[jsp]
<form:textarea name="textarea1" cols="50" rows="5" />
编译解析为：
<textarea name="textarea1" cols="50" rows="5"></textarea>
```