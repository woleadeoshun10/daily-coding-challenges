// Challenge:
// - Print all numbers between 1 and 100 that are divisible by 3
// - Count how many there are
// - Print their sum

#include <iostream>
using namespace std;

int main() {
  int count = 0;
  int sum = 0;
  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0) {
      cout << i << " ";
      count++;
      sum += i;
    }
  }
  cout << endl;
  cout << "Count: " << count << endl;
  cout << "Sum: " << sum << endl;

  return 0;
}
