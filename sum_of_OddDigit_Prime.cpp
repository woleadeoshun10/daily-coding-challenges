#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int count = 0;
    int sum_num = 0;

    for (int i = 10; i <= 300; i++) {
        int temp = i;
        int oddSum = 0;
        while (temp > 0) {
            int digit = temp % 10;
            if (digit % 2 == 1) {
                oddSum += digit;
            }
            temp /= 10;
        }

        if (isPrime(oddSum)) {
            cout << i << " ";
            count++;
            sum_num += i;
            if (count % 5 == 0) cout << endl;
        }
    }

    cout << "\nCount: " << count << endl;
    cout << "Sum: " << sum_num << endl;

    return 0;
}
