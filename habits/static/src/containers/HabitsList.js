import { connect } from 'react-redux'
import { deleteHabit } from '../actions'
import SelectionList from '../components/SelectionList'

const mapStateToProps = state => ({
    itemsMap: state,
    submitText: 'Delete'
})

const mapDispatchToProps = dispatch => ({
    onSubmit: items => {
        items.forEach(item => {
            const req = new XMLHttpRequest()
            req.open('DELETE', '/habits/' + item.id)
            req.onload = event => {
                if (req.status === 200) {
                    dispatch(deleteHabit(JSON.parse(req.responseText)))
                }
            }
            req.send(null)
        })
    }
})

const HabitsList = connect(
    mapStateToProps,
    mapDispatchToProps
)(SelectionList)

export default HabitsList
