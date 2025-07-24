/*
🧠 Challenge: Multiply Even Digit Sum
Problem Statement:
Print numbers from 1 to 250 where the sum of even digits in the number is divisible by 4.
Your Task:

Print only those numbers where the sum of even digits (like 0, 2, 4, 6, 8) is divisible by 4.
Print 5 numbers per line.
At the end, print the total count and the sum of all valid numbers.

"""

"""
Challenge:
Print numbers from 4 to 250 where the sum of their even digits is divisible by 4.
- Print 5 numbers per line.
- At the end, print total count and sum.
*/

#include <iostream>
using namespace std;
int main(){
    int count = 0;
    int sum_num = 0;
    
    for (int i = 4; i <= 250; i++){
        int temp = i;
        int digitSum = 0;
        int digit;
        while (temp > 0){
            digit = temp % 10;
            if(digit % 2 == 0){
                digitSum += digit;
            }
            temp /= 10;
        }
        if ((digitSum != 0) && (digitSum % 4 == 0)){
            cout << i << " ";
            count++;
            sum_num += i;
            if (count % 5 == 0) cout << endl;
        }
    }
    cout << "\nCount: " << count << endl;
    cout << "Sum: " << sum_num << endl;
    
  
}
