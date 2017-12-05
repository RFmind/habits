import React from 'react';
import PropTypes from 'prop-types';

import HabitsList from './HabitsList.jsx';

export default class HabitsTracker extends React.Component {

    constructor(props) {
        super(props);

        this.state = { 'list': [] };
        const setState = this.setState.bind(this);
        const req = new XMLHttpRequest();
        req.open('GET', '/habits/');
        req.onload = (e) => {
            const response = JSON.parse(req.responseText);
            setState({'list': response});
        };
        req.send(null);
    }

    render() {
        return (
            <div className="HabitsTracker">
              <header><h1>Habits Tracker</h1></header>
              <HabitsList list={this.state.list}/>
            </div>
        );
    }
}
