// Print even numbers from 50 to 100
// Print 5 numbers per line
// Show total count and sum

#include <iostream>
using namespace std;

int main() {
    int count = 0, sum = 0;

    for (int i = 50; i <= 100; i += 2) {
        cout << i << " ";
        count++;
        sum += i;
        if (count % 5 == 0) cout << endl;
    }

    cout << "\nCount: " << count << endl;
    cout << "Sum: " << sum << endl;

    return 0;
}
