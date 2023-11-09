# Problem Solving Approach

How to solve it by George Polya is a good resource for problem solving.

## Introduction to Problem Solving Approach

- Problem solving is the process of formulating the problem, finding a solution, and expressing the solution.
- Problem solving is a process of transforming the description of a problem into the solution of that problem by using our knowledge of the problem domain and by relying on our ability to select and use appropriate problem-solving strategies, techniques and tools.

## What is an Algorithm?

- An algorithm is a finite set of instructions that, if followed, accomplishes a particular task.
- Foundation for being successful in programming is to understand the algorithmic approach to problem solving.

## How do you improve?

- Devise a plan for solving problems.
- Master common problem-solving techniques.
- Become familiar with the algorithmic approach to problem solving.

## Problem Solving Strategies

- Understand the problem
- Explore concrete examples
- Break it down
- Solve/Simplify
- Look back and refactor

## Step One: Understand the problem

- Can I restate the problem in my own words?
- What are the inputs that go into the problem?
- What are the outputs that should come from the solution to the problem?
- Can the outputs be determined from the inputs? In other words, do I have enough information to solve the problem?
- How should I label the important pieces of data that are a part of the problem?

```javascript
// Write a function which takes two numbers and returns their sum.
 // 1. Can I restate the problem in my own words?
  "implement addition"
  // 2. What are the inputs that go into the problem?
   ints? strings?
   // 3. What are the outputs that should come from the solution to the problem?
    int? float? string?
    // 4. Can the outputs be determined from the inputs? In other words, do I have enough information to solve the problem?
     yes
     // 5. How should I label the important pieces of data that are a part of the problem?
      function name: add
      
```

## Step Two: Explore concrete examples

- Coming up with examples can help you understand the problem better.
- Examples also provide sanity checks that your eventual solution works how it should.
- User stories!
- Unit tests!

### Explore examples

- Start with simple examples
- Progress to more complex examples
- Explore examples with empty inputs
- Explore examples with invalid inputs

```javascript
// Write a function which takes in a string and returns counts of each character in the string.
charCount("aaaa"); // output: {a:4} counts of each character in the string.
charCount("hello"); // output: {h:1, e:1, l:2, o:1}

// Explore examples
"my phone number is 182763" // do we count spaces? numbers? special characters?
"Hello hi" // do we count uppercase and lowercase letters as the same?

charCount(""); // do we return null? empty object? undefined?

charCount(123); // do we return null? empty object? undefined?

```

## Step Three: Break it down

- Explicitly write out the steps you need to take.
- This forces you to think about the code you'll write before you write it, and helps you catch any lingering conceptual issues or misunderstandings before you dive in and have to worry about details (e.g. language syntax) as well.

```javascript

// Write a function which takes in a string and returns counts of each character in the string.
 // return an object with keys that are lowercase alphanumeric characters in the string; values should be the counts for those characters

function charCount(str) {
  // make an object to return at end

  //loop over string for each string if char is a number/letter in object, add one to count if char is not in object, add it and set value to 1

  // return object
}

```

## Step Four: Solve or Simplify

- Solve the problem if you can. If you can't, solve a simpler problem.

### Simplify

- Find the core difficulty in what you're trying to do.
- Temporarily ignore that difficulty.
- Write a simplified solution.
- Then incorporate that difficulty back in.

```javascript

// simple brute approach
function charCount(str){
  let result = {};
  for(let i = 0; i < str.length; i++){
    let char = str[i].toLowerCase();
    //!! need an if statement to check if char is alphanumeric still
    if(result[char] > 0){ // if char exists in object 
      result[char]++; // increment count
    } else {
      result[char] = 1; // char doesnt exist in object, add it and set value to 1
    }
  }
  return result;
}

```

## Step Five: Look back and refactor

- Refactoring questions:
  - Can you check the result?
  - Can you derive the result differently?
  - Can you understand it at a glance?
  - Can you use the result or method for some other problem?
  - Can you improve the performance of your solution?
  - Can you think of other ways to refactor?
  - How have other people solved this problem?

```javascript
// first brute approach
function charCount(str){
  let result = {};
  for(let i = 0; i < str.length; i++){
    let char = str[i].toLowerCase();
    if(/[a-z0-9]/.test(char)){ // if char is alphanumeric using regex
      if(result[char] > 0){ // if char exists in object 
      result[char]++; // increment count
      } else {
      result[char] = 1; // char doesnt exist in object, add it and set value to 1
      }
    }
  }
  return result;
}

// second approach using for of loop with truthy check to either increment or set to 1
function charCount(str){
  let result = {};
  for(let char of str){
    if(isAlphaNumeric(char)){ 
    char = char.toLowerCase();
    obj[char] = ++obj[char] || 1; // increment count or set to 1
    }
  }
  return result;
}

//create a helper function to check if char is alphanumeric
function isAlphaNumeric(char){
  let code = char.charCodeAt(0);
  if(!(code > 47 && code < 58) && // numeric (0-9)
     !(code > 64 && code < 91) && // upper alpha (A-Z)
     !(code > 96 && code < 123)){ // lower alpha (a-z)
    return false;
  }
  return true;
}
```

## Recap and Interview Strategies

- **Understand the problem**: ask questions, clarify the problem, and make sure you understand your inputs and desired outputs. Think of invalid inputs and edge cases.
- **Explore concrete examples**: come up with examples that can help you understand the problem better. Examples also provide sanity checks that your eventual solution works how it should.
- **Break it down**: explicitly write out the steps you need to take. This forces you to think about the code you'll write before you write it, and helps you catch any lingering conceptual issues or misunderstandings before you dive in and have to worry about details (e.g. language syntax) as well.
- **Solve or simplify**: solve the problem if you can. If you can't, solve a simpler problem. Ignore the stuck portions and solve the rest. Then incorporate the difficulty back in.
- **Look back and refactor**: refactor your solution if you can. Look for ways to improve your code. Think about how other people have solved this problem.
