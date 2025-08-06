from pyarrow import field

import es_config

def create_or_get_index(index_name) -> str:
    if es_config.client.indices.exists(index=index_name):
        response = es_config.client.indices.get(index=index_name)
    else:
        response = es_config.client.indices.create(index=index_name)
    return str(response)
        # print("Index created.")

def delete_index(index_name, doc_id):
    es_config.client.delete(index=index_name, id=doc_id)

def add_document(index_name, doc_id, doc_name):
    es_config.client.index(index=index_name, id=doc_id, document=doc_name)

def get_document(index_name, doc_id) -> str:
    response = es_config.client.get(index=index_name, id=doc_id)
    return str(response)

def update_document(index_name, doc_id, updated_doc):
    es_config.client.update(index=index_name, id=doc_id, doc=updated_doc)

def query_document(index_name, field, keyword) -> str:
    query = {
        "query": {
            "match": {
                field: keyword
            }
        }
    }
    response = es_config.client.search(index=index_name, body=query)
    for hit in response["hits"]["hits"]:
        return str(hit)


def main():
    index = "book"
    doc_id = "1"
    doc = {
        "title": "Elasticsearch 简明教程",
        "author": "eddieliu-dev",
        "year": 2025
    }
    # print(create_or_get_index("book"))
    # # print(type(create_or_get_index("book")))
    # add_document(index_name=index, doc_id=doc_id, doc_name=doc)
    # print(get_document(index_name=index, doc_id=doc_id))
    # print(type(get_document(index_name=index, doc_id=doc_id)))
    print(query_document(index_name=index, field="year", keyword=2025))

if __name__ == "__main__":
    main()