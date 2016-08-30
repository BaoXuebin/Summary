<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page import="java.util.*"%>
<%
	List<String> list = new ArrayList<String>();
	list.add("上海");
	list.add("北京");
	list.add("杭州");
	request.getSession().setAttribute("list", list);
%>
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
			<h1>核心库标签</h1>
			<hr>
<pre><code>&lt;%
    List<String> list = new ArrayList<String>();
    list.add("上海");
    list.add("北京");
    list.add("杭州");
    request.getSession().setAttribute("list", list);
%&gt;
&lt;c:set var="salary" value="5000"&gt;&lt;/c:set&gt;
&lt;c:set var="list" value="\${list}"&gt;&lt;/c:set&gt;
&lt;c:out value="\${salary}"&gt;&lt;/c:out&gt;</code></pre>
<hr>
<pre><code>&lt;c:choose&gt;
    &lt;c:when test="${salary > 2000}"&gt;
	嗯，不错！
    &lt;/c:when&gt;
    &lt;c:when test="${salary > 4000}"&gt;
	非常好！
    &lt;/c:when&gt;
    &lt;c:otherwise&gt;
	很糟糕！
    &lt;/c:otherwise&gt;
&lt;/c:choose&gt;</code></pre>
		<p><c:choose>
			<c:when test="${salary > 2000}">
		 		嗯，不错！
		 	</c:when>
			<c:when test="${salary > 4000}">
		 		非常好！
		 	</c:when>
			<c:otherwise>
		 		很糟糕！
		 	</c:otherwise>
		</c:choose></p>
		<hr>
		<pre><code>&lt;c:forEach items="\${list}" var="str" varStatus="status"&gt;
\${str}, \${status.first}
&lt;/c:forEach&gt;</code></pre>
		<p><c:forEach items="${list}" var="str" varStatus="status">
	 		${str}, ${status.first}
		</c:forEach></p>
		<hr>
		<pre><code>&lt;c:import url="jstl_fmt.jsp" var="data"&gt;&lt;/c:import&gt;
&lt;c:out value="\${data}"&gt;&lt;/c:out&gt;</code></pre>
		<textarea rows="10" cols="120">
			<c:import url="jstl_fmt.jsp" var="data"></c:import>
    		<c:out value="${data}"></c:out>
		</textarea>
    	</div>
	</div>

	<script src="../js/bootstrap.min.js"></script>
	<script src="../js/markdown.js"></script>
	<script src="../js/prettify.js"></script>
</body>
</html>