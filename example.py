from pubmed_fetcher_test import fetch

# If file_path not provided, the results are displayed in terminal.
fetch(query="cancer", file_path="results.csv", debug=True)