function FancyBorder(props) {
	return (
		<div className={'FancyBorder FancyBorder-' + props.color}>
			{props.children}
		</div>
	);
}

function WelcomeDialog() {
	return (
		<FancyBorder color="blue">
			<h1 className="Dialog-title">
				Welcome
			</h1>
			<p className="Dialog-message">
				Thank you for visiting our spacecraft!
			</p>
		</FancyBorder>
	);
}

ReactDOM.render(
	<WelcomeDialog />,
	$('#WelcomeDialog')[0]
);

function Dialog(props) {
	return (
		<FancyBorder color="blue">
			<h1 className="Dialog-title">
				{props.title}
			</h1>
			<p className="Dialog-message">
				{props.messgae}
			</p>
			{props.children}
		</FancyBorder>
	);
}

class SignUpDialog extends React.Component {
	constructor(props) {
		super(props);
		// reg event
		this.handleChange = this.handleChange.bind(this);
		this.handleSignUp = this.handleSignUp.bind(this);
		this.state = {login: ''};
	}

	render() {
		return (
			<Dialog title="Mars Exploration Program" message="How should we refer to you?">
				<input value={this.state.login} onChange={this.handleChange} />
				<button onClick={this.handleSignUp}>Sign up</button>
			</Dialog>
		);
	}

	handleChange(e) {
		this.setState({login: e.target.value});
	}

	handleSignUp() {
		alert(`Welcome aboard,  ${this.state.login}!`);
	}
}

ReactDOM.render(
	<SignUpDialog />,
	$('#SignUpDialog')[0]
);