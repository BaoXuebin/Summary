<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page import="java.util.*" %>
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
</head>
<body>
	 <c:set var="salary" scope="session" value="5000"></c:set>
	 <c:set var="list" value="${list}"></c:set>
	 <c:out value="${salary}"></c:out>
	 
	 <c:choose>
	 	<c:when test="${salary > 2000}">
	 		嗯，不错！
	 	</c:when>
	 	<c:when test="${salary > 4000}">
	 		非常好！
	 	</c:when>
	 	<c:otherwise>
	 		很糟糕！
	 	</c:otherwise>
	 </c:choose>
	 
	 <c:forEach items="${list}" var="str" varStatus="status">
	 	${str}, ${status.first}
	 </c:forEach>
	 
</body>
</html>