import { connect } from 'react-redux'
import { addHabit } from '../actions'
import SingleFieldForm from '../components/SingleFieldForm'

const mapStateToProps = state => ({
    submitText: 'Add habit'
})

const mapDispatchToProps = dispatch => ({
    onSubmit: habitName => {
        const req = new XMLHttpRequest()
        req.open('POST', '/habits/')
        req.setRequestHeader('Content-Type', 'application/json')
        req.onload = event => {
            if (req.status === 201) {
                dispatch(addHabit(JSON.parse(req.responseText)))
            }
        }
        req.send(JSON.stringify({ "name": habitName }))
    }
})

const AddHabit = connect(
    mapStateToProps,
    mapDispatchToProps
)(SingleFieldForm)

export default AddHabit
