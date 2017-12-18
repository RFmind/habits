import React from 'react'
import { shallow } from 'enzyme'
import { expect } from 'chai'
import Main from '../src/components/Main'
import HabitsList from '../src/containers/HabitsList'
import AddHabit from '../src/containers/AddHabit'

describe('<Main />', () => {

    const wrapper = noHabits => shallow(<Main noHabits={noHabits} />)

    it('should show an error message if there are no habits.', () => {
        expect(wrapper(true).find('p.err')).to.have.length(1)
    })

    it('should show a HabitsList component if there are habits.', () => {
        expect(wrapper(false).find(HabitsList)).to.have.length(1)
    })

    it('should show a AddHabit component.', () => {
        expect(wrapper(true).find(AddHabit)).to.have.length(1)
        expect(wrapper(false).find(AddHabit)).to.have.length(1)
    })
})
