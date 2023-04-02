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

def read_queries():
    n = int(input())
    return [input().split for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    phonebook = PhoneBook()
    result = []
    for query in queries:
        if query[0] == 'add':
            phonebook.add_contact(query[1], query[2])
        elif query[0] == 'del':
            phonebook.delete_contact(query[1])
        elif query[0] == 'find':
            result.append(phonebook.find_contact(query[1]))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))





    


