import React from 'react'
import { shallow } from 'enzyme'
import { expect } from 'chai'
import SelectionList from '../src/components/SelectionList'

describe('<SelectionList />', () => {

    describe('<ul>', () => {

        const wrapper = items => shallow(
            <SelectionList itemsMap={items} onSubmit={() => {}} />
        )

        it('should be rendered every time.', () => {
            expect(wrapper([]).find('ul')).to.have.length(1)

            expect(wrapper([{ "id": 1, "name": "Reading" }]).find('ul'))
                .to.have.length(1)
        })

        it('should contain all, if any, items', () => {
            expect(wrapper([]).find('ul li')).to.have.length(0)

            expect(wrapper([{ "id": 1, "name": "Reading" }]).find('ul li'))
                .to.have.length(1)

            expect(wrapper([{ "id": 1, "name": "Reading" },
                            { "id": 2, "name": "Writing" },
                            { "id": 3, "name": "Coding"  }]).find('ul li'))
                .to.have.length(3)
        })
    })
    
    it('should contain a submit input button with the appropriate text.', () => {
        const wrapper = shallow(
            <SelectionList itemsMap={[]} onSubmit={() => {}}
                           submitText="Test" />
        )

        expect(wrapper.find('input[type="submit"]')).to.have.length(1)
        expect(wrapper.find('input[type="submit"]').first().props().value)
            .to.equal('Test')
    })
})
