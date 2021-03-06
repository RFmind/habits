import React from 'react'
import PropTypes from 'prop-types'

const SelectionList = ({ itemsMap, onSubmit, submitText = 'Confirm',
                         multipleValueSelect = true }) => {
    const id = Math.random()
    return (
        <form onSubmit={event => {
            const selection = itemsMap.filter(item =>
                document.getElementById(`${id}-${item.id}`).checked)
            onSubmit(multipleValueSelect? selection : selection[0])
            event.preventDefault()
        }}>
          <ul>
            {itemsMap.map(item => (
                <li key={item.id}>
                  <input type={multipleValueSelect ? 'checkbox' : 'radio'}
                         id={`${id}-${item.id}`}
                         name="selection" />
                  {item.name}
                </li>
            ))}
          </ul>
          <input type="submit" value={submitText} />
        </form>
    )
}

SelectionList.propTypes = {
    itemsMap: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.number.isRequired,
        name: PropTypes.string.isRequired
    }).isRequired).isRequired,
    onSubmit: PropTypes.func.isRequired,
    submitText: PropTypes.string,
    multipleValueSelect: PropTypes.bool
}

export default SelectionList
