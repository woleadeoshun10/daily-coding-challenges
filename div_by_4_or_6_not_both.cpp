// Print numbers from 1 to 100 divisible by 4 or 6 but not both
// Print 5 numbers per line
// Show count and sum

#include <iostream>
using namespace std;

int main() {
    int count = 0, sum = 0;

    for (int i = 1; i <= 100; i++) {
        if ((i % 4 == 0 || i % 6 == 0) && i % 12 != 0) {
            cout << i << " ";
            count++;
            sum += i;
            if (count % 5 == 0) cout << endl;
        }
    }

    cout << "\nCount: " << count << endl;
    cout << "Sum: " << sum;
    cout<< endl;

    return 0;
}
