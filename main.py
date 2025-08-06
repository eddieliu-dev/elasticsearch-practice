from elasticsearch import Elasticsearch

index_name = "search-94hm"
mappings = {
    "properties": {
        "text": {
            "type": "text"
        }
    }
}
mapping_response = client.indices.put_mapping(index=index_name, body=mappings)
print(mapping_response)