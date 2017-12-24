import React from 'react'

import HabitsList from '../containers/HabitsList'
import AddHabit from '../containers/AddHabit'
import { deleteHabitsRequest } from '../store/actions'

const Main = ({ noHabits }) => {
    let maybeList

    if (noHabits) {
        maybeList = (
            <p className="err">You have not registered any habits yet.</p>
        )
    } else {
        maybeList = (
            <HabitsList action={deleteHabitsRequest} submitText="Delete" />
        )
    }

    return (
        <div className="HabitsTracker">
          <header><h1>Habits Tracker</h1></header>
          {maybeList}
          <AddHabit />
        </div>
    )
}

export default Main
