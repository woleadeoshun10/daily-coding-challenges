/* 
🔹 Challenge Title:
Count and Sum All Numbers Between 1–200 Where the Product of Digits Is Even

🔹 Instructions:
Loop through numbers from 1 to 200.
For each number, calculate the product of its digits.
If the product is even, print the number.
Also, keep track of:
The count of such numbers
The sum of such numbers
Print 5 numbers per line.
At the end, display the total count and sum.
*/


#include <iostream>
using namespace std;

int main(){
   int count = 0;
   int sum = 0;

  for (int i = 1; i <= 200; i++){
    int product = 1;
     int digit = 0;
     int temp = i;
    while(temp > 0){
      digit = temp % 10;
      product *= digit;
      temp /= 10; }

      if(product % 2 == 0){
        cout << i << " ";
        count++;
        sum += i;
        if(count % 5 == 0){
          cout << endl;
        }
    }
    }
  cout << "\nCount: " << count << endl;
  cout << "Sum: " << sum << endl;



  
  return 0;
}
