import React from 'react'
import PropTypes from 'prop-types'

const SelectionList = ({ itemsMap, onSubmit, submitText = 'Confirm' }) => (
    <form onSubmit={event => {
        onSubmit(itemsMap.filter(item =>
            document.getElementById("selectableItem-"+item.id).checked))
        event.preventDefault()
    }}>
      <ul>
        {itemsMap.map(item => (
            <li key={item.id}>
              <input type="checkbox" id={"selectableItem-"+item.id} />
              {item.name}
            </li>
        ))}
      </ul>
      <input type="submit" value={submitText} />
    </form>
)

SelectionList.propTypes = {
    itemsMap: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.number.isRequired,
        name: PropTypes.string.isRequired
    })),
    onSubmit: PropTypes.func.isRequired,
    submitText: PropTypes.string
}

export default SelectionList
