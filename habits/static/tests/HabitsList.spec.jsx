import React from 'react';
import { mount } from 'enzyme';
import { expect } from 'chai';

import HabitsList from '../src/HabitsList.jsx';

describe('<HabitsList/>', function () {

    it('should show an error on empty input-list.', function () {
        const wrapper = mount(<HabitsList list={[]} />);
        expect(wrapper.find('.err')).to.have.length(1);
    });

});
