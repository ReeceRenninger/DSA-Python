/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isAnagram = function(s, t) {
  if (s.length !== t.length){
      return false;
  }
  let sObject = {};
  let tObject = {};

  for(let letter of s){
      //look into object at letter string, if it exists then we add 1 to it to prevent overriding the keys, otherwise we set it to 1
      sObject[letter] ? sObject[letter] += 1 : sObject[letter] = 1
  }

      for(let letter of t){
      tObject[letter] ? tObject[letter] += 1 : tObject[letter] = 1
  }

  for(let letter in sObject){
      // testing if all the sObject letters are equal to the tObject letters, if not return false, if completes return true
      if(sObject[letter] !== tObject[letter]){
          return false;
      }
  }
  return true;
};