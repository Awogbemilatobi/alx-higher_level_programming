class MyList(list):

    def print_sorted(self):
            print(list(sorted(reversed(self))))
