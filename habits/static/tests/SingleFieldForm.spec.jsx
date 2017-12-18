import React from 'react'
import { shallow } from 'enzyme'
import { expect } from 'chai'
import SingleFieldForm from '../src/components/SingleFieldForm'

describe('<SingleFieldForm />', () => {

    const wrapper = shallow(
        <SingleFieldForm onSubmit={() => {}} submitText='Test' />
    )

    it('should contain exactly one text input field.', () => {
        expect(wrapper.find('input[type="text"]')).to.have.length(1)
    })

    it('should contain a submit input button with the appropriate text.', () => {
        expect(wrapper.find('input[type="submit"]')).to.have.length(1)
        expect(wrapper.find('input[type="submit"]').first().props().value)
            .to.equal('Test')
    })
})
