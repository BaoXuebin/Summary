// 商品类别
class ProductCategoryRow extends React.Component {
	render() {
		return (
			<tr>
				<th colSpan="2">
					{this.props.category}
				</th>
			</tr>
		);
	}
}

// 商品行
class ProductRow extends React.Component {
	render() {
		var name = this.props.product.stocked ? 
			this.props.product.name : 
			<span style={{color: 'red'}}>{this.props.product.name}</span>
		return (
			<tr>
				<td>{name}</td>
				<td>{this.props.product.price}</td>
			</tr>
		);
	}
}

// 商品列表
class ProductTable extends React.Component {
	render () {
		var rows = [];
		var lastCategory = null;

		this.props.products.forEach((product) => {
			if (product.name.indexOf(this.props.filterText) === -1 || (!product.stocked && this.props.inStockOnly)) {
				return;
			}
			if (product.category !== lastCategory) {
				rows.push(<ProductCategoryRow category={product.category} key={product.category} />);
			}

			rows.push(<ProductRow product={product} key={product.name} />);

			lastCategory = product.category;
		});

		return (
			<table>
				<thead>
					<tr>
						<th>Name</th>
						<th>Price</th>
					</tr>
				</thead>
				<tbody>{rows}</tbody>
			</table>
		);
	}
}

//  搜索框
class SearchBar extends React.Component {
	constructor(props) {
		super(props);
		this.handleChange = this.handleChange.bind(this);
	}

	// 点击事件
	handleChange() {
		this.props.onUserInput(
			this.filterTextInput.value,
			this.inStockOnlyInput.checked
		);
	}

	render() {
		return (
			<form>
				<input type="text" placeholder="Search..." value={this.props.filterText} ref={(input) => this.filterTextInput = input}
					onChange={this.handleChange}
				/>
				<p>
					<input type="checkbox" checked={this.props.inStockOnly} ref={(input)  => this.inStockOnlyInput =  input} onChange={this.handleChange}/>
					{' '} Only show products in stock
				</p>
			</form>
		);
	}
}

class FilterableProductTable extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			testText: '',
			filterText: '',
			inStockOnly: false
		};
		this.handleUserInput = this.handleUserInput.bind(this);
		this.test = this.test.bind(this);
	}

	// 输入事件
	handleUserInput(filterText, inStockOnly) {
		this.setState({
			filterText: filterText,
			inStockOnly: inStockOnly
		});
	}

	test(e) {
		this.setState({
			testText: e.target.value
		});
		console.log(e);
	}

	render() {
		return (
			<div>
				<input type="text" onChange={this.test} />
				<span>{this.state.testText}</span>
				<SearchBar filterText={this.state.filterText} inStockOnly={this.state.inStockOnly} onUserInput={this.handleUserInput}/>
				<ProductTable products={this.props.products}  filterText={this.state.filterText} inStockOnly={this.state.inStockOnly} />
			</div>
		);
	}
}

var PRODUCTS = [
	{category: 'Sporting Goods', price: '$49.99', stocked: true, name: 'Football'},
  	{category: 'Sporting Goods', price: '$9.99', stocked: true, name: 'Baseball'},
  	{category: 'Sporting Goods', price: '$29.99', stocked: false, name: 'Basketball'},
  	{category: 'Electronics', price: '$99.99', stocked: true, name: 'iPod Touch'},
  	{category: 'Electronics', price: '$399.99', stocked: false, name: 'iPhone 5'},
  	{category: 'Electronics', price: '$199.99', stocked: true, name: 'Nexus 7'}
];

ReactDOM.render(
	<FilterableProductTable products={PRODUCTS} />,
	$('#FilterableProductTable')[0]
);

/*Let's go through each one and figure out which one is state. Simply ask three questions about each piece of data:

Is it passed in from a parent via props? If so, it probably isn't state.
Does it remain unchanged over time? If so, it probably isn't state.
Can you compute it based on any other state or props in your component? If so, it isn't state.*/