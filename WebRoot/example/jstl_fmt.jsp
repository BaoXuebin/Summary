<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>JSTL 标准标签库</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="../css/bootstrap.min.css" rel="stylesheet">
<link href="../css/desert.css" rel="stylesheet">
<script src="../js/jquery-1.12.1.js"></script>
<style type="text/css">
    .esf-container{
        width: 950px;
        margin: 30px auto;
    }
</style>
<script type="text/javascript">
    $(function(){
    	$("pre").addClass("prettyprint");
        prettyPrint();
    })
</script>
</head>
<body>
	<div class="esf-container">
       <ol class="breadcrumb">
           <li><a href="../summary.html">学习总结</a></li>
           <li><a href="../jsp.html">JSP</a></li>
           <li class="active">JSTL 标准标签库</li>
       </ol>
       <div class="esf-content" id="esf-content">
           <h1>格式化标签</h1>
           <h3>数字格式化</h3>
           <p><b>给 balance 赋值</b></p>
           <c:set var="balance" value="12000.782"></c:set>
           <pre><code>&lt;c:set var="balance" value="12000.782"&gt;&lt;/c:set&gt;</code></pre>
           <h4>货币</h4>
           <p><b>以人民币的形式 表示</b></p>
		   <pre><code>&lt;fmt:formatNumber value="${balance}" type="currency"&gt;&lt;/fmt:formatNumber&gt;</code></pre>
           <p><fmt:formatNumber value="${balance}" type="currency"></fmt:formatNumber></p>
           <p><b>以美元的形式 表示</b></p>
<pre><code>&lt;fmt:setLocale value="en_US"/&gt;
&lt;fmt:formatNumber value="${balance}" type="currency"&gt;&lt;/fmt:formatNumber&gt;</code></pre>
           <p><fmt:setLocale value="en_US"/><fmt:formatNumber value="${balance}" type="currency"></fmt:formatNumber></p>
           <h4>百分数</h4>
           <p><b>以百分数表示</b></p>
           <pre><code>&lt;fmt:formatNumber value="${balance}" type="percent"&gt;&lt;/fmt:formatNumber&gt;</code></pre>
           <p><fmt:formatNumber value="${balance}" type="percent"></fmt:formatNumber></p>
           <h4>位数</h4>
           <p><b>小数点前整数位数</b></p>
           <pre><code>&lt;fmt:formatNumber value="${balance}" type="number" maxIntegerDigits="5"&gt;&lt;/fmt:formatNumber&gt;
&lt;fmt:formatNumber value="${balance}" type="number" maxIntegerDigits="3"&gt;&lt;/fmt:formatNumber&gt;</code></pre>
           <p><fmt:formatNumber value="${balance}" type="number" maxIntegerDigits="5"></fmt:formatNumber></p>
           <p><fmt:formatNumber value="${balance}" type="number" maxIntegerDigits="3"></fmt:formatNumber></p>
           <p>注意：这个属性并没有数值意义，仅仅是进行字符串的截取。</p>
           <p><b>小数点后位数</b></p>
           <pre><code>&lt;fmt:formatNumber value="${balance}" type="number" maxFractionDigits="5"&gt;&lt;/fmt:formatNumber&gt;
&lt;fmt:formatNumber value="${balance}" type="number" maxFractionDigits="3"&gt;&lt;/fmt:formatNumber&gt;</code></pre>
           <p><fmt:formatNumber value="${balance}" type="number" maxFractionDigits="3"></fmt:formatNumber></p>
           <p><fmt:formatNumber value="${balance}" type="number" maxFractionDigits="1"></fmt:formatNumber></p>
           <p>注意：这个属性在超过实际小数点位数时，并不会发生变化；而当小于时，则进行四舍五入取值。</p>
           <h3>GroupUsed</h3>
           <pre><code>&lt;fmt:formatNumber value="${balance}" type="number" groupingUsed="false"&gt;&lt;/fmt:formatNumber&gt;
&lt;fmt:formatNumber value="${balance}" type="number" groupingUsed="true"&gt;&lt;/fmt:formatNumber&gt;</code></pre>
           <p><fmt:formatNumber value="${balance}" type="number" groupingUsed="false"></fmt:formatNumber></p>
           <p><fmt:formatNumber value="${balance}" type="number" groupingUsed="true"></fmt:formatNumber></p>
           <h3>Pattern</h3>
           <pre><code>&lt;fmt:formatNumber value="${balance}" type="number" pattern="###.###E0"&gt;&lt;/fmt:formatNumber&gt;</code></pre>
           <p><fmt:formatNumber value="${balance}" type="number" pattern="###.###E0"></fmt:formatNumber><br></p>
       </div>
       <hr>
       <nav>
           <ul class="pager">
               <li><a href="#">X</a></li>
               <li><a href="#">X</a></li>
           </ul>
       </nav>
   </div>
   
   <script src="../js/bootstrap.min.js"></script>
   <script src="../js/markdown.js"></script>
   <script src="../js/prettify.js"></script>
</body>
</html>