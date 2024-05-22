from django.test import TestCase
from django.test import Client
from journalists import models


class Tests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = '/journalists/'
        self.it_department = models.Department.objects.create(title='IT')
        self.marketing_department = models.Department.objects.create(
            title='Marketing')
        self.journalist_1 = models.Journalist.objects.create(
            first_name='Егор',
            last_name='Королев',
            birthday='1990-04-01',
            department=self.it_department,
            is_married=True,
            salary=90_000,
        )
        self.journalist_2 = models.Journalist.objects.create(
            first_name='Стас',
            last_name='Васильев',
            birthday='1993-05-16',
            department=self.marketing_department,
            is_married=False,
            salary=95_200,
        )

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(models.Journalist.objects.all()), 2)

    def test_detail(self):
        response = self.client.get(f'{self.url}{self.journalist_2.id}/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['first_name'], 'Стас')

    def test_create(self):
        new_journalist = {
            'first_name': 'Маша',
            'last_name': 'Мишина',
            'birthday': '2000-05-01',
            'department': 1,
            'is_married': False,
            'salary': 112_000,
        }

        response = self.client.post(
            self.url, new_journalist, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(models.Journalist.objects.all()), 3)
        self.assertEqual(models.Journalist.objects.get(
            id=response.data['id']).first_name, 'Маша')

    def test_update(self):
        updated_journalist = {
            'first_name': 'Миша',
            'last_name': 'Королев',
            'birthday': '1990-04-01',
            'photo': None,
            'department': 1,
            'is_married': True,
            'salary': 90_000,
        }

        response = self.client.put(
            path=f'{self.url}{self.journalist_1.id}/',
            data=updated_journalist,
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Journalist.objects.get(
            id=response.data['id']).first_name, 'Миша')

    def test_partial_update(self):
        updated_journalist = {
            'last_name': 'Никонов',
        }

        response = self.client.patch(
            path=f'{self.url}{self.journalist_1.id}/',
            data=updated_journalist,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Journalist.objects.get(
            id=response.data['id']).last_name, 'Никонов')

    def test_delete(self):
        response = self.client.delete(f'{self.url}{self.journalist_1.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(models.Journalist.objects.all()), 1)
