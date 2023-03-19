import requests
import json
import argparse

class FuckSnus:
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, terms):
        search_data = {
            "terms": terms,
            "types": ["username", "email", "lastip", "hash", "password", "name"],
            "auth_code": self.api_key
        }
        with requests.Session() as session:
            search_response = session.post("https://one.snusbase.com/data/search", json=search_data)
            combo_results = {}
            for term in terms:
                combo_url = f"https://beta.snusbase.com/v2/combo/{term}"
                combo_response = session.get(combo_url)
                combo_results[term] = combo_response.json()
        search_result = search_response.json()
        combined_result = {"search_result": search_result, "combo_results": combo_results}
        with open('snusbase_results.json', 'w') as f:
            json.dump(combined_result, f, indent=6)
        return combined_result


if __name__ == '__main__':
    api_key = "Dkfjdsakljfdsfajkkljsdaj"
    search = FuckSnus(api_key)

    parser = argparse.ArgumentParser(description='Search Snusbase for given terms.')
    parser.add_argument('num_terms', type=int, help='Number of search terms to enter.')
    args = parser.parse_args()

    terms = []
    for i in range(args.num_terms):
        term = input(f"Enter search term {i+1}: ")
        terms.append(term)

    result = search.search(terms)
