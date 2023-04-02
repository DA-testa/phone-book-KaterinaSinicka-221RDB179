# python3

class PhoneBookManager:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, number, name):
        self.contacts[number] = name
    def del_contact(self,number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return 'not found'
    def process_queries(self, queries):
        result = []
        for query in queries:
            query_type = query[0]
            number = int(query[1])
            if query_type == 'add':
                name = query[2]
                self.add_contact(number, name)
            elif query_type == 'del':
                self.del_contact(number)
            elif query_type == 'find':
                result.append(self.find_contact(number))
        return result

if __name__ == '__main__':
    pbm = PhoneBookManager()
    n = int(input())
    queries = [input().split() for i in range(n)]
    results = pbm.process_queries(queries)
    print('\n'.join(results))


