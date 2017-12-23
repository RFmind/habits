import { connect } from 'react-redux'
import { deleteHabitRequest } from '../store'
import SelectionList from '../components/SelectionList'

const mapStateToProps = (state, ownProps) => ({
    itemsMap: state,
    submitText: ownProps.submitText || 'Confirm'
})

const mapDispatchToProps = (dispatch, ownProps) => ({
    onSubmit: items =>
        items.forEach(item =>
            dispatch(deleteHabitRequest(item.id))
        )
})

const HabitsList = connect(
    mapStateToProps,
    mapDispatchToProps
)(SelectionList)

export default HabitsList
