import React from 'react';

import HabitsList from './HabitsList.jsx';
import AddHabit from './AddHabit.jsx';

function fetchData(callback) {
    const req = new XMLHttpRequest();
    req.open('GET', '/habits/');
    req.onload = e => {
        const response = JSON.parse(req.responseText);
        callback(response);
    };
    req.send(null);
}

export default class HabitsTracker extends React.Component {

    updateData() {
        fetchData(json => this.setState({'list': json}));
    }

    constructor(props) {
        super(props);

        this.state = { 'list': [] };
        this.updateData();
    }

    render() {
        return (
            <div className="HabitsTracker">
              <header><h1>Habits Tracker</h1></header>
              <HabitsList list={this.state.list} />
              <AddHabit updateData={this.updateData.bind(this)}/>
            </div>
        );
    }
}
