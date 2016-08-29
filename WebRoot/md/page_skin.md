# 页面换肤

换肤功能的实现方式是，把所有的样式都加载进去，但都不启用，然后动态启用当前风格的所有样式。

由于页面的原因，在主页面上的操作区是一个IFrame，就相当于两个document，所以样式的动态变换就放在主页面上统一处理。

在g\_current\_info.jsp中：

+ JS函数：setActiveStyleSheet(title,documentObj)，启用当前风格样式。
+ title：当前的风格名称。
+ documentObj：document的Jquery对象。

在实际开发的时候，**ESF采用统一放在init.jsp中来实现**，所以在一般情况下，就不需要开发人员去关心这部分的代码，了解即可。

参考文件 `\WEB-INF\jsp\common\init.jsp`