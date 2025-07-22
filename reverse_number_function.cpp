#include <iostream>
using namespace std;
int reverseNumber(int n) {
    int reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + (n % 10);
        n /= 10;
    }
    return reversed;
}

int main() {
  int n;
  cout << "Enter a number: ";
  cin >> n;
  while (n < 10){
      cout << "Retry: ";
      cin >> n;
  }
  int reversed = reverseNumber(n);
      cout << "reversed: "<<reversed<< endl;
 
return 0;
}