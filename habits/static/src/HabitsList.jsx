import React from 'react';
import PropTypes from 'prop-types';

export default class HabitsList extends React.Component {

    render() {
        if (this.props.list.length == 0) {
            return (
                <p className="err">You have not registered any habits yet.</p>);
        } else {
            return(
                <ul>
                    {this.props.list.map((item) =>
                        (<li key={item.id}>{item.name}</li>))}
                </ul>
            );
        }
    }
};

HabitsList.propTypes = {
    list: PropTypes.array
};

