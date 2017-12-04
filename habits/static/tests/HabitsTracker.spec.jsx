import React from 'react';
import { mount } from 'enzyme';
import { expect } from 'chai';

import HabitsTracker from '../src/HabitsTracker.jsx';

describe('<HabitsTracker/>', function () {

    it('should contain a HabitsList.', function () {
        const wrapper = mount(<HabitsTracker/>);
        expect(wrapper.find(HabitsTracker)).to.have.length(1);
    });

});
