import { connect } from 'react-redux'
import Main from '../components/Main'

const mapStateToProps = state => ({
    noHabits: state.length === 0
})

const HabitsTracker = connect(
    mapStateToProps
)(Main)

export default HabitsTracker
