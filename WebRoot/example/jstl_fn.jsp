<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>jstl 核心标签库</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="../css/bootstrap.min.css" rel="stylesheet">
<link href="../css/desert.css" rel="stylesheet">
<script src="../js/jquery-1.12.1.js"></script>
<style type="text/css">
.esf-container {
	width: 950px;
	margin: 30px auto;
}
</style>
<script type="text/javascript">
	$(function() {
		$("pre").addClass("prettyprint");
		prettyPrint();
	});
</script>
</head>
<body>
	<div class="esf-container">
		<ol class="breadcrumb">
			<li><a href="../summary.html">学习总结</a></li>
			<li><a href="../jsp.html">JSP</a></li>
			<li class="active">JSTL 核心库实例展示</li>
		</ol>
		<div class="esf-content" id="esf-content">
			<h1>JSTL 函数</h1>
			
			<!-- contains -->
			<h3>fn:contains()</h3>
			<pre><code>\${fn:contains("aa", "a")}
\${fn:contains("a", "aa")}</code></pre>
			<p>${fn:contains("aa", "a")}, ${fn:contains("a", "aa")}</p>
			
			<!-- containsIgnoreCase() -->
			<h3>fn:containsIgnoreCase()</h3>
			<pre><code>\${fn:containsIgnoreCase("AA", "a")}</code></pre>
			<p>${fn:containsIgnoreCase("AA", "a")}</p>
			
			<!-- endsWith(), startsWith()-->
			<h3>fn:endsWith(), fn:startsWith()</h3>
			<pre><code>\${fn:endsWith("www.baidu.com", ".com")}
\${fn:startsWith("www.baidu.com", "www")}
\${fn:startsWith("www.baidu.com", "http")}
\${fn:endsWith("www.baidu.com", ".cn")}</code></pre>
			<p>${fn:endsWith("www.baidu.com", ".com")},${fn:startsWith("www.baidu.com", "www")},
${fn:startsWith("www.baidu.com", "http")}, ${fn:endsWith("www.baidu.com", ".cn")}</p>			
			
			<!-- escapeXml() -->
			<h3>fn:endsWith()</h3>
			<pre><code>\${fn:escapeXml("&lt;bean&gt;bean&lt;/bean&gt;")}
\${"<bean>bean</bean>"}</code></pre>
			<p>${fn:escapeXml("<bean>bean</bean>")}, ${"<bean>bean</bean>"}</p>
			
			<!-- indexOf() -->
			<h3>fn:indexOf()</h3>
			<pre><code>\${fn:indexOf("abcde", "e")}</code></pre>
			<p>${fn:indexOf("abcde", "e")}</p>
			
			<!-- join(), split()-->
			<h3>fn:join(), fn:split()</h3>
			<c:set var="str" value='${fn:split("i am ABC", " ")}'/>
			<pre><code>&lt;c:set var="str" value='\${fn:split("i am ABC", " ")}'/&gt;
\${fn:join(str ,'-')}</code></pre>
			<p>${fn:join(str ,'-')}</p>
			
			<!-- length() -->
			<h3>fn:length()</h3>
			<pre><code>\${fn:length(str)}
\${fn:length("abc")}</code></pre>
			<p>${fn:length(str)}, ${fn:length("abc")}</p>
    	</div>
	</div>

	<script src="../js/bootstrap.min.js"></script>
	<script src="../js/markdown.js"></script>
	<script src="../js/prettify.js"></script>
</body>
</html>