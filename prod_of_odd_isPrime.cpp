/*
🧠 Challenge: Product of Odd Digits is Prime
Problem Statement:

Print all numbers from 10 to 300 where:

The product of the odd digits in the number is a prime number.

Print 5 numbers per line.

At the end, print the total count and the sum of all valid numbers.

🔍 Example:
35 → digits: 3, 5 → 3 × 5 = 15 → ❌ Not prime

73 → digits: 7, 3 → 7 × 3 = 21 → ❌ Not prime

53 → 5 × 3 = 15 → ❌

23 → 2 (even), 3 (odd) → product = 3 → ✅ (3 is prime) → print 23
*/

#include <iostream>
using namespace std;

// Function to check if a number is prime
bool isPrime(int n) {
    if (n < 2) return false;
    int i = 2;
    while (i * i <= n) {
        if (n % i == 0) return false;
        i++;
    }
    return true;
}

int main() {
    int count = 0;
    int sum_valid = 0;

    for (int i = 10; i <= 300; i++) {
        int temp = i;
        int product = 1;
        bool hasOdd = false;

        while (temp > 0) {
            int digit = temp % 10;
            if (digit % 2 == 1) {
                product *= digit;
                hasOdd = true;
            }
            temp /= 10;
        }

        if (hasOdd && isPrime(product)) {
            cout << i << " ";
            count++;
            sum_valid += i;
            if (count % 5 == 0) cout << endl;
        }
    }

    cout << "\nCount: " << count << endl;
    cout << "Sum: " << sum_valid << endl;

    return 0;
}
