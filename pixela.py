import requests
import os
import datetime
from datetime import timedelta


class Pixela:
    def __init__(self):
        self.token = os.environ.get('PIXELA_TOKEN')
        self.username = os.environ.get('PIXELA_USER')
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_title = "weekdays-coding"
        self.graph_name = "Weekday Coding"

    def create_user_account(self):
        parameters = {'token': self.token, 'username': self.username, 'agreeTermsOfService': 'yes', 'notMinor': 'yes'}
        response = requests.post(url=f"{self.pixela_endpoint}", json=parameters)
        response.raise_for_status()
        print(response.text)

    def create_graph(self):
        graph_parameters = {"id": self.graph_title, "name": self.graph_name, "unit": "commit", "type": "int",
                            "color": "momiji"}
        new_graph = requests.post(url=f"{self.pixela_endpoint}/{self.username}/graphs", json=graph_parameters,
                                  headers={'X-USER-TOKEN': self.token})
        new_graph.raise_for_status()
        print(new_graph.text)

    def post_to_graph(self):
        timestamp = datetime.datetime.today().strftime('%Y%m%d')  # format example: 20180915

        parameters = {"date": timestamp, "quantity": "5"}

        post_request = requests.post(url=f'{self.pixela_endpoint}/{self.username}/graphs/{self.graph_title}',
                                     headers={'X-USER-TOKEN': self.token}, json=parameters)
        post_request.raise_for_status()
        print(post_request.text)
        return

    def update_graph(self):
        today = datetime.datetime.today()
        remove_timestamp = today - timedelta(days=1)
        remove_timestamp = remove_timestamp.strftime('%Y%m%d')
        parameters = {'quantity': '0'}
        update_request = requests.put(
            url=f'{self.pixela_endpoint}/{self.username}/graphs/{self.graph_title}/{remove_timestamp}',
            json=parameters, headers={'X-USER-TOKEN': self.token})
        update_request.raise_for_status()
        print(update_request.text)
