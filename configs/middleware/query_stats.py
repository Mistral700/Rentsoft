import time

from django.db import connection
from django.utils.deprecation import MiddlewareMixin


class QueryStatsMiddleware(MiddlewareMixin):
    """
    A middleware to measure and add query statistics (number of queries and total execution time)
    to the API response.
    """

    def process_request(self, request):
        # Store the start time
        self.start_time = time.time()

        # Reset queries for request
        connection.queries_log.clear()

    def process_response(self, request, response):
        # Capture the number of queries executed
        num_queries = len(connection.queries)

        # Calculate total query execution time
        total_time_spent = sum(float(q["time"]) for q in connection.queries)

        # Calculate the total request execution time
        elapsed_time = time.time() - self.start_time

        # Modify the response to include query stats (only for JSON API responses)
        if response.get("Content-Type") == "application/json":
            import json

            # Decode the original response's content
            content = json.loads(response.content)
            if isinstance(content, dict):
                # Add query stats to response
                content["_query_stats"] = {
                    "number_of_queries": num_queries,
                    "total_query_time": f"{total_time_spent:.2f} ms",
                    "elapsed_time": f"{elapsed_time:.2f} ms",
                }
                # Re-encode the response
                response.content = json.dumps(content)

        return response
