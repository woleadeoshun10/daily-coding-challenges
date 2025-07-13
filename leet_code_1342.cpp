/* 
Prompt:

Write a program that takes a number as input and counts how many steps it takes to reduce the number to zero.

Rules:

If the number is even, divide it by 2.
If the number is odd, subtract 1.
Repeat this process until the number becomes 0.
Print the number of steps it took.
Example Input:
num = 14

Example Output:
6

*/


#include <iostream>
using namespace std;

int main(){
   int num;
  int count = 0;

  cout << "Enter a num: ";
  cin >> num;

  while (num > 0){
    if (num % 2 == 0){
      num /= 2;
    }
    else{
      num--;
    }
    count++;    
  }

  cout << "\nCount: " << count << endl;
  return 0;
}
