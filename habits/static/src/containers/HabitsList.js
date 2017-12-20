import { connect } from 'react-redux'
import { deleteHabit } from '../actions'
import { requestToDeleteHabit } from '../backendDriver'
import SelectionList from '../components/SelectionList'

const mapStateToProps = (state, ownProps) => ({
    itemsMap: state,
    submitText: ownProps.submitText || 'Confirm'
})

const mapDispatchToProps = (dispatch, ownProps) => ({
    onSubmit: items =>
        items.forEach(item =>
            requestToDeleteHabit(item.id,
                                 response => dispatch(deleteHabit(response)))
        )
})

const HabitsList = connect(
    mapStateToProps,
    mapDispatchToProps
)(SelectionList)

export default HabitsList
