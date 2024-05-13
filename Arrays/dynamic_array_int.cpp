#include <iostream>
using namespace std;

int main() {

   int* intArray = new int[4];
   intArray[0] = 5;
   intArray[1] = 6;
   intArray[2] = 7;
   intArray[3] = 8;
   cout << "Array Elements: ";
   for (int j = 0; j < 4; j++) {
       cout << intArray[j];
       cout << " ";
   }
   delete[] intArray;
  
   return 0;
}