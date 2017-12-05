import React from 'react';
import PropTypes from 'prop-types';

function deleteHabit(id) {
    const req = new XMLHttpRequest();
    req.open('DELETE', '/habits/' + id);
    req.send(null);
}

export default class HabitsList extends React.Component {

    render() {
        if (this.props.list.length == 0) {
            return (
                <p className="err">You have not registered any habits yet.</p>);
        } else {
            return(
                <ul>
                    {this.props.list.map((item) =>
                        //(<li key={item.id}>{item.name}</li>))}
                        (<Habit key={item.id} id={item.id} value={item.name} />))}
                </ul>
            );
        }
    }
};

class Habit extends React.Component {

    render() {
        return (
            //<input type="checkbox" value={props.id}>{props.value}<br>
            <li> 
                <span onClick={e => deleteHabit(this.props.id)}> X </span>
                {this.props.value}
            </li>
        );
    }
};

HabitsList.propTypes = {
    list: PropTypes.array
};

