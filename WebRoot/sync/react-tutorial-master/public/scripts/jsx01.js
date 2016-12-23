/**
 * 
 * @Author  BaoXuebin
 * @Date    2016-12-23 01:04:29
 */
'use strict'

function formatName(user) {
	return user.firstName + ' ' + user.lastName;
}

const user1 = {
	firstName: 'Xuebin',
	lastName: 'Bao'
};

const element = (
	<div>111</div>
);

function getGeeting(user) {
	alert(user);
	if (user) {
		return <h1>Hello, {formatName(user)}!</h1>;
	}
	return <h1>Hello, Stranger.</h1>
}

ReactDOM.render(
	element,
	$('#content2')[0]
);
