/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let stack = [] //create a stack to push characters in to
  
  for (let character of s){ // loop through each character of string
      if(character === '(' || character === '[' || character === '{'){ //if its an opening bracket we push into stack
          stack.push(character)
      } else {
          if(!stack.length || 
          // if there is NO stack length OR the closing bracket doesn't match the opening bracket in the stack we return false
          (character === ')' && stack[stack.length - 1] !== '(') || 
          (character === ']' && stack[stack.length - 1] !== '[') ||
          (character === '}' && stack[stack.length - 1] !== '{') 
          ){
              return false;
          }
          stack.pop() // pop the opening bracket if if statement isnt met
      }
  }
      return !stack.length; 
  };