/* 
Write a program that prints numbers from 1 to 100, but:
Add the number to the sum if the number is at an odd index (like 1st, 3rd, 5th...).
Subtract the number from the sum if the number is at an even index.
At the end, print:
All the numbers with their operation (+ or -)
The final result of the alternating sum
The total count of numbers added and subtracted
🔢 Sample Output Format:
+1 -2 +3 -4 +5 -6 ... +99 -100
Final Result: -50
Added Count: 50
Subtracted Count: 50
*/



#include <iostream>
using namespace std;

int main (){
  int sum_odd = 0;
  int diff_even = 0;
  int count = 0;

  for (int i = 1; i <= 100 ; i++){
    if (i % 2 == 1){
      sum_odd += i;
      cout << "+" << i << " ";
    }
    else{
      diff_even -= i;
      cout << "-" << i << " ";
    }
    count++;
      if (count % 10 == 0){
      cout << endl;
      }
  }
  int total_res = sum_odd + diff_even;
  cout << "\nFinal Result: " << total_res << endl;
  cout << "Added Count: " << sum_odd << endl;
  cout << "Subtracted Count: " << diff_even << endl;


