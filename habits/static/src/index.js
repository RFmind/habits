import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { createStore } from 'redux'
import { habitsList } from './reducers'
import HabitsTracker from './containers/HabitsTracker'

const req = new XMLHttpRequest()
req.open('GET', '/habits/')
req.onload = event => {
    if (req.status === 200) {
        const store = createStore(habitsList, JSON.parse(req.responseText))

        render(
            <Provider store={store}>
              <HabitsTracker />
            </Provider>,
            document.getElementById('root')
        )
    }
}
req.send(null)
