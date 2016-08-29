# 安装

### 下载

首先去 Apache 相关网站下载所需要的 jar 包。
[http://archive.apache.org/dist/jakarta/taglibs/standard/binaries/](http://archive.apache.org/dist/jakarta/taglibs/standard/binaries/)

或者使用 Maven 

	#<!-- https://mvnrepository.com/artifact/jstl/jstl -->
	<dependency>
	    <groupId>jstl</groupId>
	    <artifactId>jstl</artifactId>
	    <version>1.2</version>
	</dependency>    
 
然后，将解压后的 jar 包导入 web 项目的 lib 目录下。

### 使用

每次在使用的时候，必须在 jsp 的头部引入 `<taglib>`标签。    
例如，我要引入核心标签库，则需要加上：   
`<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`


