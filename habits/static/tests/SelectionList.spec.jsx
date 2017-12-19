import React from 'react'
import { shallow } from 'enzyme'
import { expect } from 'chai'
import SelectionList from '../src/components/SelectionList'

describe('<SelectionList />', () => {

    const testItems = [{ "id": 1, "name": "Reading" },
                       { "id": 2, "name": "Writing" },
                       { "id": 3, "name": "Coding" }]

    const wrapper = ({ itemsMap = testItems, onSubmit = () => {},
                       submitText = 'Test', multipleValueSelect = true }) =>
        shallow(
            <SelectionList itemsMap={itemsMap} onSubmit={onSubmit}
                           submitText={submitText}
                           multipleValueSelect={multipleValueSelect} />
        )

    describe('The list', () => {
        it('should contain all items, and no more.', () => {
            expect(wrapper({}).find('ul li'))
                .to.have.length(testItems.length)
        })
    })

    describe('The items', () => {
        it('should be of the correct type.', () => {
            expect(wrapper({})
                .find({type: 'checkbox'})).to.have.length(testItems.length)
            expect(wrapper({multipleValueSelect: false})
                .find({type: 'radio'})).to.have.length(testItems.length)
        })
    })
    
    describe('The submit button', () => {
        it('should have the appropriate text.', () => {
            expect(wrapper({}).find({ type: 'submit', value: 'Test' }))
                .to.have.length(1)
        })
    })
})
