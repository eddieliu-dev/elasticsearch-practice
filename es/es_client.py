# es_client.py
#
# This file initializes an Elasticsearch client connection to a local server.
# It uses an API key for authentication and sets a 60-second request timeout.
# The `client` object can be imported and reused across the project for
# performing Elasticsearch operations such as indexing, searching, and updating.

from elasticsearch import Elasticsearch

client = Elasticsearch(
    "http://localhost:9200",
    api_key="T2gxN1k1Z0IzYUZXM084bkR2dTE6RGx4bElGdE8wWEdWdUVURERfWUtrdw==",
    request_timeout=60
)