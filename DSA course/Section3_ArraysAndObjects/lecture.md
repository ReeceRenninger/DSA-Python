# Arrays and Objects

## Objects

- Objects are a collection of properties. Properties are a key-value pair. The key is a string and the value can be anything. The value can be a string, number, boolean, array, or another object.
- Objects have constant time access to properties. This means that no matter how many properties an object has, it will always take the same amount of time to access a property. O(1) time.
- Insertion/Removal/Access is O(1) time. While searching is O(n) time, such as checking if a specific value is stored to any key.
- When ordering is not needed, objects are an excellent choice for storing data.
- Object.keys(), Object.values(), and Object.entries() are all O(n) time because they require looping through the object.
- Object.hasOwnProperty() is O(1) time because it does not require looping through the object.

## Arrays

- Arrays are great when you need order, but they are not great when you need fast access/insertion/removal.
- Insertion/removal depends on where you are inserting/removing. If you are inserting/removing at the end of the array, it is O(1) time. If you are inserting/removing at the **beginning** of the array, it is O(n) time because all the indexes need to be updated.
- Searching is O(n) time. This is because you need to loop through the array to find the value you are looking for.
- Access is O(1) time. This is because you can access any index in the array in constant time.

## Big O of Array Methods

- push() and pop() are O(1) time.
- shift() and unshift() are O(n) time.
- concat(), slice(), splice() are O(n) time.
- sort() is O(n * log n) time. This is because it uses a sorting algorithm called merge sort.
- forEach(), map(), filter(), and reduce() are O(n) time.
- If we have to reindex the array then it is O(n) time and this occurs whenever altering the array at the beginning. Whether we are adding, inserting, or removing at the beginning of the array, we have to reindex the array.
