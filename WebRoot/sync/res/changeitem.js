/**
 * 
 * @Author  BaoXuebin
 * @Date    2016-09-13 22:11:57
 */
'use strict'

$(function(){

});

function addItem(obj_id) {
	console.log(obj_id);
	console.log($('#' + obj_id)[0].outerHTML);
}

function delItem(obj) {
	var d_obj = obj.parentNode.parentNode.parentNode.parentNode.parentNode;
	console.log(d_obj);
	d_obj.parentNode.removeChild(d_obj);
}
