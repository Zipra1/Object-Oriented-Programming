from cat import ScratchPost
from cat import Cat

cat1=Cat('Cheetos','Tabby','Orange')
post1=ScratchPost()
print(cat1)
print(post1)
print(cat1.name,cat1.breed,cat1.colour) # Accessing an attribute

if cat1.is_hungry:
    print(f'{cat1.name} is hungry.') # f means formatting
    cat1.eat('Food?')
else:
    print(f'{cat1.name} is not hungry.')
cat1.scratch(post1)

