# python3

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, number, name):
        self.contacts[number] = name

    def delete_contact(self,number):
        if number in self.contacts:
            del self.contacts[number]
    
    def fine_contact(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "not found"

def process_queries(queries):
    result = []
    phone_book = PhoneBook()
    for query in queries:
        if query.type == 'add':
            phone_book.add_contact(query.number, query.name)
        elif query.type == 'del':
            phone_book.delete_contact(query.number)
        elif query.type == 'find':
            result.append(phone_book.find_contact(query.number))
    return result
       
if __name__ == '__main__':
    n = int(input())
    queries = []
    for i in range(n):
        query = Query(input().split())
        queries.append(query)
    result = process_queries(queries)
    write_responses(result)


