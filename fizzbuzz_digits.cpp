// From 1 to 150:
// - Print "FizzBuzz" if divisible by 15
// - Print "Fizz" if divisible by 3
// - Print "Buzz" if divisible by 5
// - Else, print the number if its digit sum is even
// - Print 5 values per line

#include <iostream>
using namespace std;

int main() {
    int count = 0;

    for (int i = 1; i <= 150; i++) {
        bool printed = false;

        if (i % 15 == 0) {
            cout << "FizzBuzz ";
            printed = true;
        }
        else if (i % 3 == 0) {
            cout << "Fizz ";
            printed = true;
        }
        else if (i % 5 == 0) {
            cout << "Buzz ";
            printed = true;
        }

        if (!printed) {
            int temp = i, digitSum = 0;
            while (temp > 0) {
                digitSum += temp % 10;
                temp /= 10;
            }
            if (digitSum % 2 == 0) {
                cout << i << " ";
                printed = true;
            }
        }

        if (printed) {
            count++;
            if (count % 5 == 0) cout << endl;
        }
    }

    return 0;
}
