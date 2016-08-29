# 标签库（下）

### select

列表框，包含的属性有：

+ items：集合对象名称，根据request.getAttribute(名称)获取。
+ itemKey：对象的key
+ itemValue：对象的value
+ emptyOption：是否显示空项（true or false）。
+ emptyOptionDesc：空项显示内容，例如：请选择项目，默认值为“请选择”。

例如：

```[jsp]
<form:select id="organId" name="bean.organId" items="mapOrgan" emptyOption="true" value="010000"/>
编译解析为：
<select id="organId" name="bean.organId">
    <option value=''>请选择</option>
    <option value='000000'>福州市工商局</option>
    <option value='010000' selected >黄浦分局</option>
    <option value='030000'>卢湾分局</option>
    <option value='040000'>徐汇分局</option>
    <option value='050000'>长宁分局</option>
    <option value='060000'>静安分局</option>
</select>
```

### radio

单选框组合，包含的属性：

+ items：集合对象名称，根据request.getAttribute(名称)获取。
+ itemKey：对象的key
+ itemValue：对象的value

例如：

```[jsp]
<form:radio id="caseType" name="bean.caseType" items="mapOrgan" />
编译解析为：
<span>
<input type='radio' id='caseType1' name='bean.caseType' value='000000' id="caseType" name="bean.caseType" /><label for='caseType1'>福州市工商局</label>
</span>
<span>
<input type='radio' id='caseType2' name='bean.caseType' value='010000' id="caseType" name="bean.caseType" /><label for='caseType2'>黄浦分局</label>
</span>
<span>
<input type='radio' id='caseType3' name='bean.caseType' value='030000' id="caseType" name="bean.caseType" /><label for='caseType3'>卢湾分局</label>
</span>
<span>
<input type='radio' id='caseType4' name='bean.caseType' value='040000' id="caseType" name="bean.caseType" /><label for='caseType4'>徐汇分局</label>
</span>
<span>
<input type='radio' id='caseType5' name='bean.caseType' value='050000' checked  id="caseType" name="bean.caseType" /><label for='caseType5'>长宁分局</label>
</span>
<span>
<input type='radio' id='caseType6' name='bean.caseType' value='060000' id="caseType" name="bean.caseType" /><label for='caseType6'>静安分局</label>
</span>
```

### checkbox

复选框组合，包含的属性：

+ items：集合对象名称，根据request.getAttribute(名称)获取。
+ itemKey：对象的key
+ itemValue：对象的value

例如：

```[jsp]
<form:checkbox id="caseSource" name="bean.caseSource" items="mapOrgan" />        
编译解析为：
<span>
<input type='checkbox' id='caseType1' name='bean.caseType' value='000000' id="caseType" name="bean.caseType" /><label for='caseType1'>福州市工商局</label>
</span>
<span>
<input type='checkbox' id='caseType2' name='bean.caseType' value='010000' id="caseType" name="bean.caseType" /><label for='caseType2'>黄浦分局</label>
</span>
<span>
<input type='checkbox' id='caseType3' name='bean.caseType' value='030000' id="caseType" name="bean.caseType" /><label for='caseType3'>卢湾分局</label>
</span>
<span>
<input type='checkbox' id='caseType4' name='bean.caseType' value='040000' id="caseType" name="bean.caseType" /><label for='caseType4'>徐汇分局</label>
</span>
<span>
<input type='checkbox' id='caseType5' name='bean.caseType' value='050000' checked  id="caseType" name="bean.caseType" /><label for='caseType5'>长宁分局</label>
</span>
<span>
<input type='checkbox' id='caseType6' name='bean.caseType' value='060000' id="caseType" name="bean.caseType" /><label for='caseType6'>静安分局</label>
</span>
```

### autocompelete

自动完成组件标签，包含的属性：

+ autocompleteUrl：自动完成加载数据的地址。
+ autocompleteCallback：加载数据完成后的回调函数。
+ readonly：只读。
+ minLength：当文本框输入的内容长度不小于minLength时，显示自动完成内容。当minlength=0时，获得焦点时，就显示自动完成内容。

例如：

```[jsp]
<form:autocomplete name="a" autocompleteUrl="filter.jsp" minLength="0"/>
编译解析为：
<input type="text" name="a" value="" autocomplete="filter.jsp" minLength="0"/>
```