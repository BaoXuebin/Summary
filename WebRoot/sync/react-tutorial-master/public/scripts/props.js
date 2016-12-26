function Welcome(props) {
    return <h1>Hello, {props.name}</h1>
}

// 注意：Components must return a single root element. This is why we added a <div> to contain all the <Welcome /> elements.
function App() {
    return (
        <div>
            <Welcome name="BaoXuebin" />
            <Welcome name="BaoXuebin1" />
            <Welcome name="BaoXuebin2" />
        </div>
    );
}

ReactDOM.render(
    <App />,
    $('#props')[0]
);

const avatar = <img  />

function Comment(props) {
    return (
        <div className="Comment">
            <div className="UserInfo">
                <img className="Avatar"
                    src={props.author.avatarUrl}
                    alt={props.author.name}
                />
                <div className="UserInfo-name">
                    {props.author.name}
                </div>
            </div>
            <div className="Comment-text">
                {props.text}
            </div>
            <div className="Comment-date">
                {formatDate(props.date)}
            </div>
        </div>
    );
}
