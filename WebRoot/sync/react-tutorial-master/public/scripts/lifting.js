function BoilingVerdict(props) {
    if (props.celsius >= 100) {
        return <p>The water would boil.</p>
    }
    return <p>The water would not boil.</p>
}

class Calculator extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.state = {value: ''};
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    render() {
        const value = this.state.value;
        return (
            <fieldset>
                <legend>Enter temperature in Celsius:</legend>
                <input value={value} onChange={this.handleChange} />
                <BoilingVerdict celius={parseFloat(value)} />
            </fieldset>
        );
    }
}

ReactDOM.render(
    <Calculator />,
    $('#Calculator')[0]
);