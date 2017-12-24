import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { deleteHabitRequest } from '../store/actions'
import SelectionList from '../components/SelectionList'

const mapStateToProps = (state, ownProps) => ({
    itemsMap: state,
    submitText: ownProps.submitText,
    multipleValueSelect: ownProps.multipleValueSelect
})

const mapDispatchToProps = (dispatch, ownProps) => ({
    onSubmit: items => dispatch(ownProps.action(items))
})

const HabitsList = connect(
    mapStateToProps,
    mapDispatchToProps
)(SelectionList)

HabitsList.propTypes = {
    action: PropTypes.func.isRequired,
    submitText: PropTypes.string,
    multipleValueSelect: PropTypes.bool
}

export default HabitsList
