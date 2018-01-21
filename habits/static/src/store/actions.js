import { postHabit, requestToDeleteHabit, requestToTriggerHabit } from '../backendDriver'
import { createActions, handleActions } from 'redux-actions'

// Actions
const { addHabit, deleteHabit, triggerHabit } =
    createActions('ADD_HABIT', 'DELETE_HABIT', 'TRIGGER_HABIT')

// Reducers
export const habitsList = handleActions(
    {
        'ADD_HABIT': (state, action) => {
            return state.concat([{...action.payload, activities: []}])
        },
        'DELETE_HABIT': (state, action) => {
            return state.filter(item => item.id != action.payload.id)
        },
        'TRIGGER_HABIT': (state, action) => {
            newState = state.filter(item => item.id != action.payload.id)
            newHabit = state.find(item => item.id === action.payload.id)
            newHabit = {
                ...newHabit,
                activities: newHabit.activities.concat([{
                    "trigger_time": action.payload.trigger_time
                }])
            }
            return [ ...newState, newHabit]
        }
    },
    []
)

// Thunks
export const addHabitRequest = habit =>
    dispatch => postHabit(habit, response => dispatch(addHabit(response)))

export const deleteHabitRequest = habitId =>
    dispatch => requestToDeleteHabit
                  (habitId, response => dispatch(deleteHabit(response)))

export const deleteHabitsRequest = habits =>
    dispatch => habits.map(habit =>
                           requestToDeleteHabit
                             (habit.id, response =>
                                        dispatch(deleteHabit(response))))

export const triggerHabitRequest = habit =>
    dispatch => requestToTriggerHabit(habit.id, response => dispatch(triggerHabit(
        { ...habit, ...response })))
