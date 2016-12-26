// preventDefault
// (handleClick) onClick => camelCase 
function Light(props) {
	render() {
		return (
			// (handleClick) onClick => camelCase 
			<span>
				   {this.props.state ? '亮' : '灭'}
			</span>
		);
	}
}

// Toggle Example (ES6)
class Toggle extends React.Component {
	constructor(props) {
		super(props);
		this.state = {isToggleOn: true};
		// 注册事件监听
		this.handleClick = this.handleClick.bind(this);
	}
    
	handleClick() {
		this.setState(
			prevState => ({
				isToggleOn: !prevState.isToggleOn
			}));
	}

	render() {
		return (
			<div>
				<button onClick={this.handleClick}>
					{this.state.isToggleOn ? 'ON' : 'OFF'}
				</button>
				<Light props={this.state.isToggleOn} />
			</div>
		);
	}
}

ReactDOM.render(
	<Toggle />,
	$('#event')[0]
);