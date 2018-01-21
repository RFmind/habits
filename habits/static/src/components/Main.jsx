import React from 'react'

import HabitsList from '../containers/HabitsList'
import AddHabit from '../containers/AddHabit'
import { deleteHabitsRequest, triggerHabitRequest } from '../store/actions'

const Main = ({ noHabits }) => {
    return (
        <div className="HabitsTracker">
          <header><h1>Habits Tracker</h1></header>
          {noHabits? (<p className="err">
                        You have not registered any habits yet.
                      </p>) :
                     (<HabitsList action={deleteHabitsRequest}
                                  submitText="Delete" />)}
          <AddHabit />
          {!noHabits &&
              <HabitsList action={triggerHabitRequest}
                          submitText="Trigger"
                          multipleValueSelect={false} />}
        </div>
    )
}

export default Main
