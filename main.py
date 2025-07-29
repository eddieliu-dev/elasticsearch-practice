from elasticsearch import Elasticsearch, helpers
client = Elasticsearch(
    "https://my-elasticsearch-project-e02a24.es.us-central1.gcp.elastic.cloud:443",
    api_key="VWJDVFZKZ0JqdDA1cHVuLWtFZTI6WHRVTDVjRVdUNFNBejI2RTJuQUNZdw=="
)
# client.indices.create(
#     index="search-fbp7",
#     mappings={
#         "properties": {
#             "vector": {"type": "dense_vector", "dims": 3 },
#             "text": {"type": "text"}
#         }
#     }
# )
# index_name = "search-fbp7"

# docs = [
#     {
#         "text": "Yellowstone National Park is one of the largest national parks in the United States. It ranges from the Wyoming to Montana and Idaho, and contains an area of 2,219,791 acress across three different states. Its most famous for hosting the geyser Old Faithful and is centered on the Yellowstone Caldera, the largest super volcano on the American continent. Yellowstone is host to hundreds of species of animal, many of which are endangered or threatened. Most notably, it contains free-ranging herds of bison and elk, alongside bears, cougars and wolves. The national park receives over 4.5 million visitors annually and is a UNESCO World Heritage Site.",
#         "vector": [
#             9.575,
#             1.643,
#             2.124
#         ]
#     },
#     {
#         "text": "Yosemite National Park is a United States National Park, covering over 750,000 acres of land in California. A UNESCO World Heritage Site, the park is best known for its granite cliffs, waterfalls and giant sequoia trees. Yosemite hosts over four million visitors in most years, with a peak of five million visitors in 2016. The park is home to a diverse range of wildlife, including mule deer, black bears, and the endangered Sierra Nevada bighorn sheep. The park has 1,200 square miles of wilderness, and is a popular destination for rock climbers, with over 3,000 feet of vertical granite to climb. Its most famous and cliff is the El Capitan, a 3,000 feet monolith along its tallest face.",
#         "vector": [
#             6.45,
#             3.879,
#             0.828
#         ]
#     },
#     {
#         "text": "Rocky Mountain National Park  is one of the most popular national parks in the United States. It receives over 4.5 million visitors annually, and is known for its mountainous terrain, including Longs Peak, which is the highest peak in the park. The park is home to a variety of wildlife, including elk, mule deer, moose, and bighorn sheep. The park is also home to a variety of ecosystems, including montane, subalpine, and alpine tundra. The park is a popular destination for hiking, camping, and wildlife viewing, and is a UNESCO World Heritage Site.",
#         "vector": [
#             1.5,
#             6.374,
#             3.806
#         ]
#     }
# ]
#
# bulk_response = helpers.bulk(client, docs, index=index_name)
# print(bulk_response)
retriever_object = {
    "standard": {
        "query": {
            "knn": {
                "field": "vector",
                "num_candidates": 100,
                "query_vector_builder": {
                    "text_embedding": {
                        "model_id": "",
                        "model_text": "What is Yellowstone Park?"
                    }
                }
            }
        }
    }
}

search_response = client.search(
    index="search-fbp7",
    retriever=retriever_object,
)
print(search_response['hits']['hits'])