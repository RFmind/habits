import React from 'react';

import HabitsList from './HabitsList.jsx';
import AddHabit from './AddHabit.jsx';

function updateList(setState) {
    const req = new XMLHttpRequest();
    req.open('GET', '/habits/');
    req.onload = (e) => {
        const response = JSON.parse(req.responseText);
        setState({'list': response});
    };
    req.send(null);
}

export default class HabitsTracker extends React.Component {

    constructor(props) {
        super(props);

        this.state = { 'list': [] };
        updateList(this.setState.bind(this));
    }

    render() {
        return (
            <div className="HabitsTracker">
              <header><h1>Habits Tracker</h1></header>
              <HabitsList list={this.state.list}/>
              <AddHabit/>
            </div>
        );
    }
}
