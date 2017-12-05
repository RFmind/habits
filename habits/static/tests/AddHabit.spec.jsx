import React from 'react';
import { mount } from 'enzyme';
import { expect } from 'chai';

import AddHabit from '../src/AddHabit.jsx';

describe('<AddHabit/>', function() {

    const fixture = mount(<AddHabit/>);

    it('should contain a button for adding habits', function () {
        expect(fixture.find('#addHabit')).to.have.length(1);
    });

    it('should contain a text field for the name of the habit.', function () {
        expect(fixture.find('#name-field')).to.have.length(1);
    });

});
