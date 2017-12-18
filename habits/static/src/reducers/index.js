import { handleActions } from 'redux-actions'

export const habitsList = handleActions(
    {
        'ADD_HABIT': (state, action) => {
            return state.concat([action.payload])
        },
        'DEL_HABIT': (state, action) => {
            return state.filter(item => item.id != action.payload.id)
        }
    },
    []
)
