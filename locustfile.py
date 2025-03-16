
from locust import HttpUser, task, between
import random

class N11User(HttpUser):
    wait_time = between(1, 5)  # Simulate users waiting between 1 and 5 seconds between tasks

    @task # basic search with only one item
    def search_product(self):
        search_query = "laptop"
        self.client.get(f"/arama?q={search_query}", name="/arama?q=[search_query]")

    @task # Tests how the search box handles multiple concurrent requests.
    def high_concurrency_search(self):
        search_queries = ["smartphone", "headphones", "watch", "laptop", "camera"]
        search_query = random.choice(search_queries)
        self.client.get(f"/arama?q={search_query}", name="/arama?q=[search_query]")

    @task  # Tests how the search box handles long and complex queries.
    def long_search_query(self):
        search_query = "high-performance gaming laptop with 16GB RAM and 1TB SSD"
        self.client.get(f"/arama?q={search_query}", name="/arama?q=[long_search_query]")

    @task # Tests how the search box handles non-alphanumeric chars.
    def search_with_special_chars(self):
        search_query = "laptop@2023"
        self.client.get(f"/arama?q={search_query}", name="/arama?q=[special_chars]")

    @task # Tests the performance of the autocomplete
    def search_with_autocomplete(self):
        partial_query = "lap"
        self.client.get(f"/autocomplete?q={partial_query}", name="/autocomplete?q=[partial_query]")
