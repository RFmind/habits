import React from 'react';
import ReactDOM from 'react-dom';

function sendJSON(json, callback) {
    const req = new XMLHttpRequest();
    req.open('POST', '/habits/');
    req.setRequestHeader('Content-Type', 'application/json');
    req.onload = e => {
        const response = JSON.parse(req.responseText);
        callback(json);
    }
    req.send(JSON.stringify(json));
}

export default class AddHabit extends React.Component {
    render() {
        return (
            <form id="addHabitForm">
                <input type="text" name="name" id="name-field" />
                <input type="submit" id="addHabit" />
            </form>
        );
    }
    
    componentDidMount() {
        const DOMNode = ReactDOM.findDOMNode(this);
        DOMNode.addEventListener('submit', event => {
            event.preventDefault();
            const json = { "name" : DOMNode.elements['name'].value };
            const callback = json => this.props.updateData();
            sendJSON(json, callback);
        });
    }
}
