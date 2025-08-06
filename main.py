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
        es_function.create_or_get_index(index_name)

        for record in file:
            filled_title_prompt = llm_client.fill_prompt(prompt.title_prompt, prompt.title_prompt)
            title = asyncio.run(llm_client.call_llama(filled_title_prompt))

            filled_keyword_prompt = llm_client.fill_prompt(prompt.keywords_prompt, prompt.keywords_prompt)
            keywords = asyncio.run(llm_client.call_llama(filled_keyword_prompt))

            doc_id = doc_helper.generate_rand_id()
            created_by = doc_helper.generate_rand_name()
            created_at = doc_helper.generate_rand_time(start_year=2024, start_month=1, start_day=1, end_year=2025,
                                                       end_month=1, end_day=1)

            doc = {
                "title": title,
                "keywords":keywords,
                "created_by":created_by,
                "created_at":created_at
            }

            es_function.add_document(index_name= index_name, doc_id=doc_id, doc_name=doc)

    else:
        print("Query")


if __name__ == "__main__":
    main()
