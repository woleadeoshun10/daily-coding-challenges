/* 
Challenge: "Self-Dividing Numbers"
🟢 LeetCode-Style Easy Problem
📘 Problem Statement:
A number is called a self-dividing number if:

It is divisible by each of its digits
It does not contain the digit 0
Write a function that prints all the self-dividing numbers between 1 and 200.
*/


#include <iostream>

using namespace std;
void printSelfDividingNumbers(int start, int end) {
  for(int num = start; num <= end; num++){
    int temp = num;
    bool is_valid = true;

    while (temp > 0){
      int digit = temp % 10;
      if (digit == 0 || num % digit != 0){
       is_valid = false;
        break;
        
      }
      temp /= 10;
    }
    if (is_valid){
      cout << num << " ";
    }
  }
}

int main() {
    // ✅ Test the function
    printSelfDividingNumbers(1, 200);
    return 0;
}
 