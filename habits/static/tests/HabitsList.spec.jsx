import React from 'react';
import { mount } from 'enzyme';
import { expect } from 'chai';

import HabitsList from '../src/HabitsList.jsx';

function makeWrapper(json) {
    return mount(<HabitsList list={json} />);
}

const fixture0 = makeWrapper([]);
const fixture1 = makeWrapper([{ "id": 1, "name": "Reading" }]);
const fixture3 = makeWrapper([{ "id": 1, "name": "Reading" },
                              { "id": 2, "name": "Writing" },
                              { "id": 3, "name": "Coding"  }]);

describe('<HabitsList/>', function () {

    it('should show an error on empty input-list.', function () {
        expect(fixture0.find('.err')).to.have.length(1);
    });

    it('should show an unordered list of habits.', function () {
        expect(fixture1.find('ul')).to.have.length(1);
    });

    it('should show all given habits.', function () {
        expect(fixture1.find('li')).to.have.length(1);
        expect(fixture3.find('li')).to.have.length(3);
    });

});
