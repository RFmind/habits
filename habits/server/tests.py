import unittest
import json
import tempfile
import re
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

from app import create_app, db

class HabitsTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('TEST')

        with app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()

        self.client = app.test_client
        self.newhabit = json.dumps(dict(name='Somehabit'))

    def test_index_route_status_ok(self):
        self.assertEqual(
            self.client().get('/').status_code,
            200)

    def test_habits_route_status_ok(self):
        self.assertEqual(
            self.client().get('/habits/').status_code,
            200)

    def test_get_empty_list_of_habits(self):
        self.assertEqual(
            json.loads(self.client().get('/habits/').data),
            [])

    def test_get_list_of_habits(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        self.assertEqual(
            json.loads(self.client().get('/habits/').data),
            [dict(id=1, name='Somehabit')])

    def test_404_when_habit_not_found(self):
        response = self.client().get('/habits/1')
        self.assertEqual(response.status_code, 404)

    def test_added_habit_is_gettable(self):
        added_response = self.client().post(
            '/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().get('/habits/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), dict(id=1,name='Somehabit'))

    def test_status_201_when_added_habit(self):
        response = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_bad_input_when_adding_habit(self):
        response = self.client().post('/habits/',
            data="23 23")
        self.assertEqual(response.status_code, 400)

    def test_status_404_when_deleting_habit(self):
        response = self.client().delete('/habits/1')
        self.assertEqual(response.status_code, 404)

    def test_status_200_when_deleted_habit(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().delete('/habits/1')
        self.assertEqual(response.status_code, 200)

    def test_returns_deleted_habit(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().delete('/habits/1')
        self.assertEqual(
            json.loads(response.data),
            dict(id=1, name='Somehabit'))

    def test_deleted_item_not_gettable(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        added_habit = json.loads(added.data)
        deleted = self.client().delete(
            '/habits/{}'.format(added_habit['id']))
        response = self.client().get(
            '/habits/{}'.format(added_habit['id']))
        self.assertEqual(
            response.status_code,
            404)

    def test_returns_400_when_name_not_given(self):
        response = self.client().post('/habits/',
            data=json.dumps(dict(noname='notaname')),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_returns_400_when_name_is_longer_than_50(self):
        response = self.client().post('/habits/',
            data=json.dumps(dict(
                name='azertyuiqospalskdjfuehdkshdkejdshzjshak   jahzjehqkjdh')),
                content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_as_json_should_return_none_when_none(self):
        from app.habits_api.util import as_json
        from app.habits_api.models import Habit

        self.assertEqual(as_json(None), None)

    def test_as_json_should_handle_single_habit(self):
        from app.habits_api.util import as_json
        from app.habits_api.models import Habit

        self.assertEqual(
            as_json(Habit(name='somename')),
            json.dumps({'name': 'somename'}))
    
    def test_as_json_should_handle_list_of_habits(self):
        from app.habits_api.util import as_json
        from app.habits_api.models import Habit

        self.assertEqual(
            as_json([Habit(name='somename'), Habit(name='other')]),
            json.dumps([{'name': 'somename'}, {'name': 'other'}]))

    def test_should_return_404_when_updating_non_existent(self):
        response = self.client().put('/habits/1',
            data=json.dumps(dict(name='something')),
            content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_put_request_should_400_when_no_name_supplied(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().put('/habits/1',
            data=None,
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_put_request_should_200(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().put('/habits/1',
            data=json.dumps(dict(name='NewName')),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_put_request_should_return_updated_habit(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().put('/habits/1',
            data=json.dumps(dict(name='NewName')),
            content_type='application/json')
        self.assertEqual(
            json.loads(response.data),
            dict(id=1, name='NewName'))

    def test_batch_delete_should_400_when_no_ids_supplied(self):
        response = self.client().post('/habits/batch-delete/',
            data=json.dumps([]),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_batch_delete_should_allow_for_partial_error(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().post('/habits/batch-delete/',
            data=json.dumps([1,2]),
            content_type='application/json')
        self.assertEqual(
            json.loads(response.data),
            {'success': [1], 'failure': [2]})

    def test_batch_delete_should_200_on_ok_or_partial_error(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().post('/habits/batch-delete/',
            data=json.dumps([1,2]),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_batch_delete_should_404_when_nothing_found(self):
        response = self.client().post('/habits/batch-delete/',
            data=json.dumps([1,2]),
            content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_trigger_should_404_when_habit_not_found(self):
        response = self.client().get('/habits/1/trigger/')
        self.assertEqual(response.status_code, 404)

    def test_trigger_should_200(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().get('/habits/1/trigger/')
        self.assertEqual(response.status_code, 200)

    def test_trigger_should_return_datetime_in_correct_format(self):
        added = self.client().post('/habits/',
            data=self.newhabit,
            content_type='application/json')
        response = self.client().get('/habits/1/trigger/')

        self.assertTrue(
            re.match(
                '\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',
                json.loads(response.data)['trigger_time']) is not None)
 
if __name__ == '__main__':
    unittest.main()

