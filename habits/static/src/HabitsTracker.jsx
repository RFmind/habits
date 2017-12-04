import React from 'react';
import HabitsList from './HabitsList.jsx';

export default class HabitsTracker extends React.Component {
    render() {
        return (
            <div className="HabitsTracker">
              <header><h1>Habits Tracker</h1></header>
              <HabitsList list={[]}/>
            </div>
        );
    }
}
