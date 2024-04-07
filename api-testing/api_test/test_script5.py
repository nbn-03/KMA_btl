from locust import HttpUser, task

class UserBehavior(HttpUser):

    @task
    def get_tests(self):
        self.client.get("/public/v2/users")

    @task
    def post_tests(self):
        data = {
            "id": "5555649",
            "name": "load testing",
            "email": "api@gmail.com",
            "gender": "male"
        }
        self.client.post("/public/v2/users", json=data)