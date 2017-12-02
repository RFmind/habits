import unittest
import json
import tempfile
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


if __name__ == '__main__':
    unittest.main()

