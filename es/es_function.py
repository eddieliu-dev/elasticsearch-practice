# es_function.py
#
# This file defines helper functions for interacting with Elasticsearch via the `es_client`.
# It provides operations for:
# - Creating or retrieving an index
# - Deleting an index
# - Adding, retrieving, updating, and deleting documents
# - Counting documents in an index
# - Querying documents with a search body
# These functions encapsulate Elasticsearch API calls for easier reuse across the project.

from . import es_client

def create_or_get_index(index_name) -> str:
    if es_client.client.indices.exists(index=index_name):
        response = es_client.client.indices.get(index=index_name)
    else:
        response = es_client.client.indices.create(index=index_name)
    return str(response)
        # print("Index created.")

def delete_index(index_name):
    if es_client.client.indices.exists(index=index_name):
        es_client.client.indices.delete(index=index_name)
    else:
        return

def add_document(index_name, doc_id, doc_name):
    es_client.client.index(index=index_name, id=doc_id, document=doc_name)

def get_document(index_name, doc_id) -> str:
    response = es_client.client.get(index=index_name, id=doc_id)
    return str(response)

def update_document(index_name, doc_id, updated_doc):
    es_client.client.update(index=index_name, id=doc_id, doc=updated_doc)

def delete_document(index_name, doc_id):
    es_client.client.delete(index=index_name, id=doc_id)

def count_documents(index_name) -> int:
    count = es_client.client.count(index=index_name)
    return count

def query_document(index_name, query_body) -> str:
    response = es_client.client.search(index=index_name, body=query_body)
    for hit in response["hits"]["hits"]:
        return str(hit)

# Testing purposes:
# def main():
#     index = "book"
#     doc_id = "1"
#     doc = {
#         "title": "Elasticsearch 简明教程",
#         "author": "eddieliu-dev",
#         "year": 2025
#     }
#     # print(create_or_get_index("book"))
#     # # print(type(create_or_get_index("book")))
#     # add_document(index_name=index, doc_id=doc_id, doc_name=doc)
#     # print(get_document(index_name=index, doc_id=doc_id))
#     # print(type(get_document(index_name=index, doc_id=doc_id)))
#     print(query_document(index_name=index, field="year", keyword=2025))
#
# if __name__ == "__main__":
#     main()