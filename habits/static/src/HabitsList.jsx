import React from 'react';
import PropTypes from 'prop-types';

export default class HabitsList extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        if (this.props.list.length == 0) {
            return (
                <p className="err">You have not registered any habits yet.</p>);
        } else {
            return(<ul><li>Test</li></ul>);
        }
    }
};

HabitsList.propTypes = {
    list: PropTypes.array
};

