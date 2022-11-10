# Ready
import pickle

a = {'BMW e30', 'Passat B5', 'Passat B8', 'Toyota Corolla'}
pickle.dump(a, open('03.json', 'wb'))

b = pickle.load(open('03.json', 'rb'))
print(b)
