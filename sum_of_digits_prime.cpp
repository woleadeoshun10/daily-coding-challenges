/*
🧠 Challenge: Sum of Digits Is Prime
Problem Statement:
Write a program that prints all numbers from 1 to 300 such that the sum of their digits is a prime number.
Also:

Keep track of how many such numbers there are.
Print 5 numbers per line.
At the end, print the total count and the sum of all valid numbers.
🔢 Example:
If 23 → 2 + 3 = 5, and 5 is prime → ✅ print 23.
If 45 → 4 + 5 = 9, and 9 is not prime → ❌ skip.
*/

#include <iostream>
using 

  bool isPrime (int n){
      if (n < 2) return false;
      int i = 2;
      while (i*i <= n){
          if (n % i == 0){
              return false;
          }
          i++;      
        }
      return true;
  }
  
  int main() {
      int count = 0;
      int sum_prime = 0;
      int digit; 
      int digitSum;
      
      for (int i = 1; i <= 300; i++){
          int temp = i;
          int digitSum = 0;
          while (temp > 0){
          digitSum += temp % 10;
          temp /= 10;}
          
      if(isPrime(digitSum)){
          cout << i << " ";
          count++;
          sum_prime += i;
          if (count % 5 == 0){
              cout << endl;
              }
            }
          }
    cout << "\nCount: " << count << endl;
    cout << "Sum: " << sum_prime << endl;
    
    
  return 0;
}


//Im not gonna lie, I had an hardtime with this because I did not know to get a prime number I needed a function. 
