/*
Challenge: Reverse and Check Divisibility
Problem Statement:
Print all numbers from 10 to 300 where:
If you reverse the number, the reversed number is divisible by 7.
Print 5 numbers per line.
At the end, print the total count and sum of all valid numbers.
Example:
Number 70 → reversed = 07 = 7 → 7 is divisible by 7 → ✅ print 70.
Number 21 → reversed = 12 → 12 is not divisible by 7 → ❌ skip.

*/
#include <iostream>
using namespace std;
int reversedNum(int n){
   int reverse = 0;
    while(n > 0){
        int digit = n % 10;
        reverse = reverse * 10 + digit;
        n /= 10;
    }
    return reverse;
}

int main() {
    int count = 0;
    int sum_rev = 0;
    
    for (int i = 10; i<=300; i++){
        int reverse_num = reversedNum(i);
        if (reverse_num % 7 == 0){
            cout << i << " ";
            count++;
            sum_rev+=i;
            if (count % 5 == 0){
                cout << endl;
            }
        }
    }
    cout << "\nCount: "<< count << endl;
    cout << "Sum: "<< sum_rev << endl;

    return 0;
}