from json import JSONEncoder
from app.habits_api.models import Habit, Activity

class HabitEncoder(JSONEncoder):

    def default(self, obj):

        if isinstance(obj, Habit):
            serializable = {}

            for field in obj.json_fields():
                serializable[field] = getattr(obj, field)

            return serializable

        return super(HabitEncoder, self).default(obj)


class DeepHabitEncoder(HabitEncoder):

    def default(self, obj):

        if isinstance(obj, Habit):

            serializable = super(DeepHabitEncoder, self).default(obj)
            serializable['activities'] = list(map(
                lambda activity: activity.as_dict(),
                getattr(obj, 'activities')))

            return serializable
        
        return super(DeepHabitEncoder, self).default(obj)

