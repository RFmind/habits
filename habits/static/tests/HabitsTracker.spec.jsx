import React from 'react';
import { mount } from 'enzyme';
import { expect } from 'chai';

import HabitsTracker from '../src/HabitsTracker.jsx';

describe('<HabitsTracker/>', function () {

    const fixture = mount(<HabitsTracker/>);

    it('should contain a HabitsList.', function () {
        expect(fixture.find('HabitsList')).to.have.length(1);
    });

});
