
#include <iostream>
using namespace std;

/*
    *
    * *
    * * *
    * * * *
    * * * * *

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5


    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5

    a
    b b
    c c c
    d d d d
    e e e e e


    * * * * *
    * * * *
    * * *
    * *
    *

    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
 */

int main()
{

    int rows = 5;

    for (int i = rows; i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j
                 << " ";
        }
        cout << endl;
    }
}