#include <iostream>
using namespace std;

int main() {
   // Print a pyramid of stars with 10 rows
   for(int row = 1; row <= 10; row++){
     // Print spaces to align stars to the right
     for(int space = 1; space <= 10 - row; space++){
       cout << "  "; // double space for indentation
     }
     // Print stars for the current row
     for(int star = 1; star <= row; star++){
       cout << "* ";
     }
     cout << endl; // Newline after each row
   }
   return 0;
}


/*
                  *
                * * 
              * * * 
            * * * * 
          * * * * * 
        * * * * * * 
      * * * * * * * 
    * * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * *

*/
