# 基础开发规范（1）

### 开发工具(Eclipse\MyEclipse)

Java代码的编写工具有很多，如Eclipse、MyEclipse、JBuilder，甚至UltraEdit、Notepad等也可以作为java代码编写工具。

各项目组成员应该使用统一的java编写工具，这样，在代码变更后，可以方便的查看作了哪些变更。由于不少人同时参与多个项目，因此，所有人都应该使用统一的java编写工具。

Eclipse（包括MyEcipse）作为一个强大的java代码开发工具，以及它的普及性、免费开源性，我们统一使用Eclipse作为java开发工具。

### 代码格式

Eclipse中，默认已经定义了规范的代码显示格式，我们将以Eclipse的默认代码格式为基础，在Eclipse默认代码格式的基础上作出少量调整即可，这样可以最方便的保持各开发人员的代码格式一致性。调整后的Eclipse代码格式，就是我们需要遵循的java代码格式。

#### 代码缩进

在java代码中，以4个空格作为一个缩进的单位，而不以tab作为缩进。

设置方法为，在Eclipse的`Window>>Preference>>Java>>Code Style>>Formatter>>Edit>>Identation`中：

+ “Tab Policy”项选择“Space Only”
+ “Identation size”设置为“4”
+ “Tab size”设置为“4”

注：我们有时候会使用UltraEdit来编辑文件，如xml文件等，UltraEdit中，也可以进行相关的配置，配置方法为：`高级>>配置>>编辑>>tab`，选择`用空格代替制表符`，然后`制表符宽度`和`缩进空格`都设置为4即可。

#### 代码行长度

代码行的最大长度设置为120个字符，超出这个长度时，Eclipse在代码格式化时，会根据默认的规则进行换行。

设置方法为，在Eclipse的`Window>>Preference>>Java>>Code Style>>Formatter>>Edit>>Line Wrapping`中：

+ `Maximum line width`设置为120

#### Eclipse代码格式化

Eclipse提供了根据代码格式化设置进行代码格式化的功能，通过以下方式可以对当前打开的类进行代码格式化操作：

+ 快捷键：`Ctrl+Shift+F` （注：如快捷键不起作用，那么可能是和其他软件的快捷键冲突。比如搜狗输入法有这个快捷键，可关闭搜狗输入法该快捷键功能，或修改快捷键设置）
+ 系统菜单：`Source>>Format`
+ 代码区快捷菜单：`Source>>Format`

请养成代码编写后，进行代码格式化的习惯。

### 字符集

新的J2EE项目，统一使用UTF-8字符集（注意，请统一使用大写的UTF-8，不要使用小写的utf-8）。对于使用UTF-8字符集的J2EE项目：

+ 所有的文本性的文件（SQL文件除外）都应该基于utf-8字符集进行编码，将Eclipse中的字符集设置为UTF-8
+ web.xml文件中的filter“Set Character Encoding”中的字符集设置为UTF-8
+ 所有jsp、html文件中的charset，设置为UTF-8

使用NotePad、UltraEdit创建的文件，默认字符集不是UTF-8，需要另存是转换。对于已经是utf-8格式的文件，NotePad、UltraEdit等编辑器可以自动辨认。

Eclipse中设置字符集的方式：

+ 修改Eclipse默认的字符集：在Eclipse的`Windows>>Preference>>General>>Workspace`页面中，设置`Text file encoding`为`UTF-8`。这样，在Eclipse中建立的项目，如果项目没有特别指定字符集，就会使用Eclipse的默认字符集。
+ 修改项目的字符集：在项目名称的右键弹出菜单的`Preference>>Resource`页面中，选择`Text file encoding`为`UTF-8`。这样，该项目的字符集就是UTF-8，而不管Eclipse默认的字符集是什么。

另外，还需要进行另外的设置：
在Eclipse的`Window>>Preferences>>General>>Content Types`页面中，将各类型的`Default encoding`都改成`UTF-8`。