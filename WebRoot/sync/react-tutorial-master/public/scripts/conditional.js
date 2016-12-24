function UserGreeting(props) {
	return <h1>Welcome back.</h1>;
}

function GuestGreeting(props) {
	return <h1>Pleasse sign up.</h1>;
}

function Greeting(props) {
	const isLoggedIn = props.isLoggedIn;
	if (isLoggedIn) {
		return <UserGreeting />;
	}
	return <GuestGreeting />
}

function LoginButton(props) {
	return (
		<button onClick={props.onClick}>
			Login
		</button>
	);
}

function LogoutButton(props) {
	return (
		<button onClick={props.onClick}>
			Logout
		</button>
	);
}

class LoginControl extends React.Component {
	constructor(props) {
		super(props);
		this.handleLoginClick = this.handleLoginClick.bind(this);
		this.handleLogoutClick = this.handleLogoutClick.bind(this);
		this.state = {isLoggedIn: false};
	}

	handleLoginClick() {
		this.setState({isLoggedIn: true});
	}

	handleLogoutClick() {
		this.setState({isLoggedIn: false});
	}

	render() {
		const isLoggedIn = this.state.isLoggedIn;

		let button = null;
		if (isLoggedIn) {
			button = <LogoutButton onClick={this.handleLogoutClick} />;
		} else {
			button = <LoginButton onClick={this.handleLoginClick} />;
		}
		return (
			<div>
				<Greeting isLoggedIn={isLoggedIn} />
				{button}
			</div>
		);
	}
}

ReactDOM.render(
	<LoginControl />,
	$('#conditional')[0]
);

//  MailBox
function Mailbox(props) {
	const unreadMessages = props.unreadMessages;
	return (
		<div>
			<h1>Hello!</h1>
			{unreadMessages.length > 0 &&
				<h2>
					You have {unreadMessages.length} unread!
				</h2>
			}
		</div>
	);
}

const messages = ['React', 'Re: React', 'Re:Re: React'];
const messages1 = [];
ReactDOM.render(
	<Mailbox unreadMessages={messages1}/>,
	$('#Mailbox')[0]
);