# Big O Notation

## Objectives

- Motivate the need for something like Big O Notation
- Describe what Big O Notation is
- Simplify Big O Expressions
- Define "time complexity" and "space complexity"
- Evaluate the time complexity and space complexity of different algorithms using Big O Notation
- Describe what a logarithm is (MATTTTHHHHHHH)

## What is the Big O Notation?

- Big O Notation is a way "rate" code based on how much time or space it takes up.
- It is shown in a numeric representation. Such as O(n) or O(1)
- It is a way to compare different implementations of the same algorithm.

## Timing Our Code

- Is this implementation of the same algorithm faster? or less memory intensive? or more readable?
- speed and memory are usually what we care about when it comes to Big O Notation, readable is always a good thing to aim for if solution allows for it.

```js
// add up to n
// 1 + 2 + 3 + 4 + 5 + ... + n

// solution 1
function addUpTo(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total += i;
  }
  return total;
}

// solution 2
function addUpTo(n) {
  return (n * (n + 1)) / 2;
}
```

- The two functions do the same thing but they are very different in terms of how they are written.
- The first function is a for loop that adds up all the numbers from 1 to n.
- The second function uses a formula to calculate the same thing.
- Which one is better? Which one is faster? Which one is more readable?
- We can use the built in `performance.now()` method to time how long a function takes to run.

```js
let t1 = performance.now();
addUpTo(1000000000);
let t2 = performance.now();
console.log(`Time Elapsed: ${(t2 - t1) / 1000} seconds.`);
```

- timing is not a good way to measure due to limitations by machine, same machine can have different run times and it may not be precise enough.

## Counting Operations

- Rather than counting seconds which are so variable, we can count the number of simple operations the computer has to perform. The number of operations will stay the same no matter the machine.
- Regardless of n exact number, the number of operations grow roughly proportionally with n.

## Visualizing Time Complexities

- We can visualize the time complexity of an algorithm by using a graph.
- The x-axis is the size of the input (n)
- The y-axis is the time elapsed
- The graph will show us how the time elapsed grows as the input grows.

## Official Introduction to Big O

- Big O Notation is a way to formalize fuzzy counting.
- It allows us to talk formally about how the runtime of an algorithm grows as the inputs grow.
- We say that an algorithm is O(f(n)) if the number of simple operations the computer has to do is eventually less than a constant times f(n), as n increases.
  - f(n) could be linear (f(n) = n)
  - f(n) could be quadratic (f(n) = n^2)
  - f(n) could be constant (f(n) = 1)
  - f(n) could be something entirely different!
- Nested loops are O(n^2) because an O(n) operation nested in another O(n) operation is O(n * n) which is O(n^2)

## Simplifying Big O Expressions

- O(1) is the best time complexity because it is constant time. It does not matter how big the input is, it will always take the same amount of time to run.
- O(n) is linear time. The time it takes to run will grow proportionally to the size of the input.
- O(n^2) is quadratic time. The time it takes to run will grow proportionally to the square of the size of the input.
- O(n!) is factorial time. The time it takes to run will grow proportionally to the factorial of the size of the input.
- O(2n) simplifies to O(n) because the constant 2 does not matter as n grows.
- O(500) simplifies to O(1) because the constant 500 does not matter as n grows.
- O(13n^2) simplifies to O(n^2) because the constant 13 does not matter as n grows.
- O(n + 10) simplifies to O(n) because the constant 10 does not matter as n grows.
- O(1000n + 50) simplifies to O(n) because the constant 1000 and 50 do not matter as n grows.
- O(n^2 + 5n + 8) simplifies to O(n^2) because the constants 5 and 8 do not matter as n grows.
  - Big O Shorthands
    - Arithmetic operations are constant
    - Variable assignment is constant
    - Accessing elements in an array (by index) or object (by key) is constant
    - In a loop, the complexity is the length of the loop **times** the complexity of whatever happens inside of the loop
![simple chart](Screenshot%202023-11-07%20121225.png)

## Space Complexity

- We can also use Big O Notation to analyze space complexity.
- Space complexity is a way to quantify how much additional memory we need to allocate in order to run the code in our algorithm.
- Auxiliary space complexity refers to the space required by the algorithm, not including space taken up by the inputs.
  - Rules of Thumb
    - Most primitives (booleans, numbers, undefined, null) are constant space.
    - Strings require O(n) space (where n is the string length)
    - Reference types are generally O(n), where n is the length (for arrays) or the number of keys (for objects)

## Logarithms

- A logarithm is the inverse of exponentiation.
- sometimes big O expressions involve more complex mathematical expressions.
- log2(8) = 3 because 2^3 = 8
- log2(value) = exponent because 2^exponent = value
- log === log2 we omit the 2 because it is implied in regards to how we are calculating the logarithm.
- O(log n) is great! It is even better than O(n) because it grows slower.
- O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)

## Recap

- To analyze the performance of an algorithm, we use Big O Notation.
- Big O Notation can give us a high level understanding of the time or space complexity of an algorithm.
- Big O Notation does not care about precision, only about general trends (linear? quadratic? constant?)
- The time or space complexity (as measured by Big O) depends only on the algorithm, not the hardware used to run the algorithm.
- Big O Notation is everywhere, so get lots of practice!


