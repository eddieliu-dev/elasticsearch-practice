# main.py
#
# This is the main entry point for the Elasticsearch document management workflow.
# It can run in two modes based on user input:
# 1. Add mode:
#    - Deletes and recreates the specified index
#    - Reads documents from a file
#    - Uses an LLM to generate titles and keywords for each document
#    - Generates metadata (ID, creator, creation date)
#    - Adds the documents to Elasticsearch
# 2. Query mode:
#    - Counts documents in the specified index
#    - Performs a multi-field full-text search on title, keywords, and content
# This script integrates functions from helper modules and the LLM client.

from elasticsearch import Elasticsearch
from es import es_client, es_function
from helpers import doc_helper, prompt
from llm import llm_client
import asyncio


def main():
    file = doc_helper.file_reader("data/documents_dup_part_1_part_1_short")

    index_name = "news"

    command = input("Add or Query?")

    if command.casefold() == "add":
        es_function.delete_index(index_name)
        es_function.create_or_get_index(index_name)

        for record in file:
            filled_title_prompt = llm_client.fill_prompt(prompt.title_prompt, record)
            title = asyncio.run(llm_client.call_llama(filled_title_prompt))

            filled_keyword_prompt = llm_client.fill_prompt(prompt.keywords_prompt, record)
            keywords = asyncio.run(llm_client.call_llama(filled_keyword_prompt))

            doc_id = doc_helper.generate_rand_id()
            created_by = doc_helper.generate_rand_name()
            created_at = doc_helper.generate_rand_time(start_year=2024, start_month=1, start_day=1, end_year=2025,
                                                       end_month=1, end_day=1)

            doc = {
                "title": title,
                "keywords": keywords,
                "content": record,
                "created_by": created_by,
                "created_at": created_at
            }

            es_function.add_document(index_name=index_name, doc_id=doc_id, doc_name=doc)

    else:
        # print("Query")
        # to be done: extract keywords from query using llm and set the keywords as query
        print(es_function.count_documents(index_name))
        query_body = {
            "query": {
                "multi_match": {
                    "query": "美国大火",
                    "fields": ["title","keywords","content"]
                    # "operator": "and"
                    # "minimum_should_match": 2
                }
            }
        }
        print(es_function.query_document(index_name=index_name, query_body=query_body))


if __name__ == "__main__":
    main()
