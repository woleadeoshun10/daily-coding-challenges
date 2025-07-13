/* 
💡 Challenge: Sum of Squares for Odd Digits Only
Task:
Print numbers between 1 and 300 where the sum of the squares of their digits is divisible by 3.

Rules:

Only include odd digits (1, 3, 5, 7, 9) when calculating the sum of squares.
Print 5 results per line.
At the end, display the total count and sum of all such numbers.
 total count and sum.
*/


#include <iostream>
using namespace std;

int main(){
   int count = 0;
   int sum = 0;
   int digitProduct = 0;

  for (int i = 1; i <= 300; i++){
    int digitSum = 0;
     int temp = i;
    while(temp > 0){
      digitSum += temp % 10;
      temp /= 10; }
    digitProduct = digitSum * digitSum;

      // check if product is divisible by 3
      if(digitProduct % 3 == 0){
        cout << i << " ";
        count++;
        sum += i;
        
        // Print a newline every 5 numbers
        if(count % 5 == 0){
          cout << endl;
        }
    }
    }
  cout << "\nCount: " << count << endl;
  cout << "Sum: " << sum << endl;



  
  return 0;
}
