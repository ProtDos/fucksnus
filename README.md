# fucksnus

fucksnus is a Python class that provides a simple interface to search the Snusbase database using its API. The program takes as input a list of search terms and returns a JSON object containing the results of the search as well as additional information retrieved through the API. The results are stored in a file called snusbase_results.json.

## Prerequisites

A brain

## Usage

To use fucksnus create an instant of the class like so:

```py
search = FuckSnus(api_key)
```


Then, call the `search` method with a list of search terms:

```py
result = search.search(terms)
```


The `search` method returns a JSON object containing the results of the search.

## Command line interface

fucksnus also provides a simple command line interface. To use it, run the program with the desired number of search terms as an argument:

```
python fucksnus.py <num_terms>
```
You will be prompted to enter the search terms one by one. The results of the search will be stored in a file called snusbase_results.json.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
