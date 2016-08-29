# 基础开发规范（4）

### 代码优化

#### 代码大小

+ 每个java文件的行数不要超过2000行，尽量控制在1000行以内，避免“上帝类”的产生。当一个类的行数超过1000行时，就是要注意了，是不是有变成“上帝类”的可能性了。
+ 每个方法尽量的保持在200行的代码量以内，不能超过500行。尽量将一些逻辑实现，尤其是可复用的逻辑实现，分离到不同的方法中。
+ 一个方法行数比较多时，请使用空行来分隔不同的逻辑块，再配以注释，提高程序的可读性。

#### 方法

+ 尽量保持最少的public method数量，太多的public method会引起类的误读而破坏OO封装原则。
+ 在有可能的情况下，请尽量重用方法而不要自己创建。尽量保持系统中方法实现的单一性，以便能加强维护。
+ 请严格的依照JavaBean的统一方式来写属性访问getter、setter方法，否则在java的反射机制实现时，会有问题。Eclipse提供了很好的自动创建功能。
+ 方法调用的速度比较，从快到慢排列： static < final < instance method < interface method < synchronized。

#### 属性和变量

+ 公有类（public class）应该尽量不包含公有属性（public attribute），除非是公有的静态final属性（public static final attribute）。一般属性请使用私有（private attribute），然后对外通过共有的get和set方法访问。
+ 避免在同一个类中调用方法（get或set）来设置或调用类共有属性。
+ 尽可能的使用静态变量。如果类中的变量不会随他的实例而变化，就可以定义为静态变量，从而使他所有的实例都共享这个变量。
+ 不要在代码中进行具体数值硬编码，把它定义为静态常量，然后在代码中引用。
+ 请将运行环境变量信息配置在配置文件或数据库中。不可以在代码中直接写死运行环境配置值。比如数据库连接信息等。
+ 尽量使用接口申明属性和变量。如果没有特别的理由，那么对于参数、返回值、变量、属性的声明，都应该通过接口类型而不是具体类。通过接口引用对象，使程序能够接受不同的实现，从而变得更加灵活。因此请养成下面的习惯；
```[java]
Map map = new HashMap();
List list = new ArrayList();
```
当然，如果没有合适的接口存在，或者程序确实需要依赖某个特定类的特定实现，那么使用具体类来引用一个对象是完全可以接受的。
+  在方法中使用局部变量，一定要确定变量赋值的唯一性。否则，代码将难以维护，形成歧义，而且是隐含bug的温床。
```[java]
// 推荐使用
int nbrClient; 
int nbrProduct; 
… 
nbrClient = getNbrClient(); 
…
nbrProduct = getNbrProduct();
```
```[java]
// 不推荐使用
int nbrClient; 
… 
nbrClient = getNbrClient(); 
… 
nbrClient = getNbrProduct();
```

#### 代码格式

+ 每行申明一个变量，下面格式则不推荐使用：
```[java]
int level, size;
```
+ 不同类型的声明应放在不同的行，下面的格式是不正确的；当然，Eclipse的Format操作可以避免这种写法，不过要养成良好的习惯。
```[java]
int foo, fooarray[]; //WRONG!
每一行至多包含一个Statement。例如：
argv++; // Correct
argc++; // Correct
argv++; argc--; // AVOID!
```

#### 字符串处理

+ 对于三次或三次以上的字符串连接操作，避免使用多个`+`号来进行，请使用`StringBuilder`或者`StringBuffer`来做这件事情。`StringBuilder`是非线程安全的，`StringBuffer`是线程安全的，如果不涉及到多线程处理，请优先使用`StringBuilder`，它比`StringBuffer`速度更快。
+  在使用`equals`和`equalsIgnoreCase`方法判断两个字符串类型操作数是否相等时，如果两个操作数之中有一个为字符串常量，应该将它置于点操作符`.`的左边，将变量放在点操作符的右边。这样做的好处在于，程序员在使用`equals`和`equalsIgnoreCase`方法时，可以不必先判断变量操作数是否为`null`。例如：
```[java]
if ("anConstant".equals(value))  {
……
}
```

#### 循环

+ 请避免使用goto语句。
+ 当使用循环的时候，请不要直接在条件判断里面使用方法，
例如：
```[java]
//推荐的 
for (Object o : myList) {
    instructions;
}
```
```[java]
//不推荐的
for (int i = 0; i < myList.size(); i++) { 
    instructions; 
}
```
