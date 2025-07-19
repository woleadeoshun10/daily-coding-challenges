/*
🧠 Problem Name: "Count of Special Even Digits"
🔹 Difficulty: Easy-Medium
🔸 Prompt:
Write a program that prints all numbers from 1 to 250 that meet the following condition:
The number has only even digits (e.g., 2, 4, 6, 8, 0 — no odd digits allowed).
At the end, print:
Total count of such numbers
Their sum
5 values per line for readability
💡 Example Output:
2 4 6 8 20  
22 24 26 28 40  
...
Total Count: 31  
Sum: 3078

*/

#include <iostream>
using namespace std;

int main(){
  int count = 0;
  int sum_even = 0;
  

  for (int i = 1; i <= 250; i++){
   int temp = i;
   bool isEven = true;
   while(temp > 0){
    int digit = temp % 10;
    if (temp % 2 != 0){
    isEven = false;
    break;
    }
   temp /= 10;
   }
   if (isEven){
    cout << i << " ";
    count++;
    sum_even += i;
    if (count % 5 == 0){
        cout << endl;
    }
   }
  }
 cout << "\n Total Count: " << count <<endl;
 cout << "Sum: " << sum_even << endl;


  return 0;
}

/*
steps:
print number from 1 - 250
only print the number if its digits is even
do not print if odd
count of numbers that exist
their sum

*/