import { connect } from 'react-redux'
import { addHabit } from '../actions'
import { postHabit } from '../backendDriver'
import SingleFieldForm from '../components/SingleFieldForm'

const mapStateToProps = state => ({
    submitText: 'Add habit'
})

const mapDispatchToProps = dispatch => ({
    onSubmit: habitName => postHabit({ "name": habitName },
                                     response => dispatch(addHabit(response)))
})

const AddHabit = connect(
    mapStateToProps,
    mapDispatchToProps
)(SingleFieldForm)

export default AddHabit
