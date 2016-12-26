// React 实现日期的每秒刷新
/*function tick() {
	const element = (
		<div>
			<h1>Hello, world!</h1>
			<h2>It is {new Date().toLocaleTimeString()}</h2>
		</div>
	);
	ReactDOM.render(
		element,
		$('#tick')[0]	
	);
}*/
//setInterval(tick, 1000);

// 进一步的封装
// props private
/*function Clock(props) {
	return (
		<div>
			<h1>Hello, world!</h1>
			<h2>It is {props.date.toLocaleTimeString()}</h2>
		</div>
	);
}

function tick() {
	ReactDOM.render(
		<Clock date={new Date()} />,
		$('#tick')[0]
	);
}
setInterval(tick, 1000);*/

// ES6 class 
class Clock extends React.Component {
	constructor(props) {
		super(props);
		this.state  = {
			date: new Date()
		};
	}

	componentDidMount() {
		this.timeId = setInterval(() => this.tick(), 1000);
	}

	componentWillUnmount() {
		clearInterval(this.timeId);
	}

	tick() {
		this.setState({
			date: new Date()
		});
	}

	render() {
		return (
			<div>
				<h1>Hello, world!</h1>
				<h2>It is {this.state.date.toLocaleTimeString()}.</h2>
			</div>
		);
	}
}

ReactDOM.render(
	<Clock />,
	$('#tick')[0]
);

// State 不能直接修改，只能通过 setState() 方法
// setState会触发diff算法：判断state和页面结果的区别，是否需要更新
