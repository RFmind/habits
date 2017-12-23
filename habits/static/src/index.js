import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { store } from './store'
import HabitsTracker from './containers/HabitsTracker'

render(
   <Provider store={store}>
     <HabitsTracker />
   </Provider>,
   document.getElementById('root')
)
