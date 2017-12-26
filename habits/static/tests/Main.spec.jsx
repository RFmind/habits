import React from 'react'
import { shallow } from 'enzyme'
import { expect } from 'chai'
import Main from '../src/components/Main'
import HabitsList from '../src/containers/HabitsList'
import AddHabit from '../src/containers/AddHabit'

describe('<Main />', () => {

    const wrapper = noHabits => shallow(<Main noHabits={noHabits} />)

    it('should allow the user to add a new habit.', () => {
        expect(wrapper(true).find(AddHabit)).to.have.length(1)
        expect(wrapper(false).find(AddHabit)).to.have.length(1)
    })

    describe('noHabits={true}', () => {

        it('should cause the user to be informed of the lack of habits', () => {
            expect(wrapper(true).find('p.err')).to.have.length(1)
        })

        it('should prevent any habit manipulation components from beeing ' +
            'rendered.', () => {
            expect(wrapper(true).find(HabitsList)).to.have.length(0)
        })
    })

    describe('noHabits={false}', () => {

        it('should cause a habit deletion list to get rendered.', () => {
            expect(wrapper(false).find(HabitsList)
                .find({submitText: 'Delete'})).to.have.length(1)
        })

        it('should cause a habit triggering list to get rendered.', () => {
            expect(wrapper(false).find(HabitsList)
                .find({submitText: 'Trigger'})).to.have.length(1)
        })
    })
})
