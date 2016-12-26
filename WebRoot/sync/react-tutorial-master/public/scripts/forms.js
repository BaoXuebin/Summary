class NameForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        console.log(event.target);
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Name: 
                    <input type="text" value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}

ReactDOM.render(
    <NameForm />,
    $('#NameForm')[0]
);


class EssayForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: 'Please write an essay about your favorite DOM element.'
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('An essay was submitted: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Name: 
                    <textarea rows="3" cols="20" value={this.state.value} onChange={this.handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}

ReactDOM.render(
    <EssayForm />,
    $('#EssayForm')[0]
);


// FlavorForm
function FlavorOption(props) {
    return (
        <option value={props.data.key}>{props.data.value}</option>
    );
}

class FlavorForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: this.props.defaultValue};
        this.map = this.props.map;

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('Your favorite is: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Pick your favorite La Croix flavor:
                    <select value={this.state.value} onChange={this.handleChange}>
                        {this.map.map((data) => 
                            <FlavorOption data={data} key={data.key} />
                        )}
                    </select>
                </label>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}

const defaultValue = 'coconut';
const flavorMap = [
    {key: 'coconut', value: 'Coconut'},
    {key: 'grapefruit', value: 'Grapefruit'},
    {key: 'lime', value: 'Lime'},
    {key: 'mango', value: 'Mango'}
];
ReactDOM.render(
    <FlavorForm map={flavorMap} defaultValue={defaultValue}/>,
    $('#FlavorForm')[0]
);