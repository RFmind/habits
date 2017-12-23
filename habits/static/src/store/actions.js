import { postHabit, requestToDeleteHabit } from '../backendDriver'
import { createActions, handleActions } from 'redux-actions'

// Actions
const { addHabit, deleteHabit } = createActions('ADD_HABIT', 'DELETE_HABIT')

// Reducers
const habitsList = handleActions(
    {
        'ADD_HABIT': (state, action) => {
            return state.concat([action.payload])
        },
        'DELETE_HABIT': (state, action) => {
            return state.filter(item => item.id != action.payload.id)
        }
    },
    []
)

// Thunks
export const addHabitRequest = habit =>
    dispatch => postHabit(habit, response => dispatch(addHabit(response)))

export const deleteHabitRequest = habitId =>
    dispatch => requestToDeleteHabit(habitId, response =>
                                              dispatch(deleteHabit(response)))
