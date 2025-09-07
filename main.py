import sys
sys.path.append("libs")
from modules.fetcher import Fetcher
from modules.reporter import Reporter


def run():
    print("Fetching sample data from JSONPlaceholder API...")

    fetcher = Fetcher("https://jsonplaceholder.typicode.com/todos")
    data = fetcher.fetch()
    print(f"Fetched {len(data)} items.")

    reporter = Reporter(data)
    reporter.print_report()

if __name__ == "__main__":
    run()
