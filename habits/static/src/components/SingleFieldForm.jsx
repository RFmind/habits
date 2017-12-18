import React from 'react'
import PropTypes from 'prop-types'

const SingleFieldForm = ({ onSubmit, submitText='Confirm' }) => (
    <form onSubmit={event => {
        onSubmit(document.getElementById('SFF-field').value)
        event.preventDefault()
    }}>
      <input type="text" name="name" id="SFF-field" />
      <input type="submit" value={submitText} />
    </form>
)

SingleFieldForm.propTypes = {
    onSubmit: PropTypes.func.isRequired,
    submitText: PropTypes.string
}

export default SingleFieldForm
