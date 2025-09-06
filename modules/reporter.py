from tabulate import tabulate

class Reporter:
    def __init__(self, data):
        self.data = data

    def print_report(self):
        if not self.data:
            print("No data to report.")
            return
        table = []
        for item in self.data[:5]:  # only first 5 items
            table.append([item.get("id"), item.get("title")])
        print(tabulate(table, headers=["ID", "Title"]))
