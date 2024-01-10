people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people : 
    print(person['name'], person['age'])
    

for person in people : 
    if person['name'] == 'bob' :
        print(person['age'])
        

def get_age(someonename) :
    for person in people :
        if person['name']  == someonename :
            return person['age']
    return '해당하는 이름이 없습니다.'

print(get_age('bob'))
print(get_age('moon'))