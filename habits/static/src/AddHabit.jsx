import React from 'react';
import ReactDOM from 'react-dom';

function sendJSON(json) {
    const req = new XMLHttpRequest();
    req.open('POST', '/habits/');
    req.setRequestHeader('Content-Type', 'application/json');
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
    
    handleFormSubmit(event) {
        event.preventDefault();
        sendJSON({ "name" : this.elements["name"].value });
    }

    componentDidMount() {
        const DOMNode = ReactDOM.findDOMNode(this);
        DOMNode.addEventListener('submit', this.handleFormSubmit.bind(DOMNode));
    }
}
