import { createStore, applyMiddleware } from 'redux'
import thunkMiddleware from 'redux-thunk'
import { habitsList } from './actions'

const request = new XMLHttpRequest()
request.open('GET', '/habits/', false)
request.send(null)

export const store = createStore(
    habitsList,
    (request.status === 200) ? JSON.parse(request.responseText) : [],
    applyMiddleware(thunkMiddleware)
)
