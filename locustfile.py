import time
import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1,5)

# Load sản phẩm
    @task
    def get_product(self):
        self.client.get("/products/604e419eae68b60380ca1452")
        self.client.get("/products/6056414b3aadd34688aabb43")
        self.client.get("/products/604e419eae68b60380ca144e")
    # Load all sản phẩm
    @task 
    def get(self):
        self.client.get("/products?keyword=&pageNumber=1")
    # Load đăng nhập
    @task
    def on_start(self):
        user_id=str(random.randint(0,100))
        username="daihoang"+user_id+"@gmail.com"
        self.client.post("/users/login", json={"email":username, "password":"123456"})

