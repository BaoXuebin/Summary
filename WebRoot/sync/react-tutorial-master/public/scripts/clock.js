function tick() {
    const element = (
        <div>
            <h1>Hello World!</h1>
            <h2>It's {new Date().toLocaleTimeString()}.</h2>
        </div>
    );
    ReactDOM.render(
        element,
        $('#clock')[0]
    );
}

setInterval(tick, 1000);
