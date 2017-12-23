import { connect } from 'react-redux'
import { addHabitRequest } from '../store/actions'
import SingleFieldForm from '../components/SingleFieldForm'

const mapStateToProps = state => ({
    submitText: 'Add habit'
})

const mapDispatchToProps = dispatch => ({
    onSubmit: habitName => dispatch(addHabitRequest({ "name": habitName }))
})

const AddHabit = connect(
    mapStateToProps,
    mapDispatchToProps
)(SingleFieldForm)

export default AddHabit
