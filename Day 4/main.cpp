
#include <iostream>
using namespace std;

/*
            *
          * *
        * * *
      * * * *
    * * * * *

            1
           12
          123
         1234
        12345

            1
          2 2
        3 3 3
      4 4 4 4
    5 5 5 5 5

            A
          A B
        A B C
      A B C D
    A B C D E

            1
          2 1
        3 2 1
      4 3 2 1
    5 4 3 2 1
 */

int main()
{

    int rows = 5;

    for (int i = 1; i <= rows; i++)
    {
        for (int j = 1; j <= rows - i; j++)
        {
            cout << " ";
        }
        for (int k = i; k >= 1; k--)
        {
            cout << k;
        }

        cout << endl;
    }
}