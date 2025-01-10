# PubMed Paper Fetcher

A Python program to fetch research papers from PubMed, filter authors based on their affiliations, and output the results in a user-friendly CSV format.

## Features

1. Fetches papers using the PubMed API.
2. Supports full PubMed query syntax.
3. Identifies papers with authors affiliated with pharmaceutical or biotech companies.
4. Outputs results as a CSV file or prints them to the console.
5. Includes command-line options:
   - `-f` or `--file`: Specify a filename for the output.
   - `-d` or `--debug`: Enable debug logging.
   - `-h` or `--help`: Display usage instructions.

## Installation

### test-pypi
```bash
pip install -i https://test.pypi.org/simple/ pubmed-fetcher-test==0.1.1
```

### Git repository
1. Clone the repository:
    ```bash
    git clone https://github.com/arthiondaena/pubmed.git
    cd pubmed
    ```

2. Install dependencies using [Poetry](https://python-poetry.org/):
    ```bash
    poetry install
    ```

3. Activate the virtual environment:
    ```bash
    poetry shell
    ```

## Usage

To execute the program, use the following command:

```bash
pubmed "your query here" [-f output.csv] [-d]
