

#include <iostream>
using namespace std;

// Leture number 6

/*
    Print easy pattern 1

    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *

    // * Pattern 2

    10 10 10 10 10
    10 10 10 10 10
    10 10 10 10 10
    10 10 10 10 10
    10 10 10 10 10

    // Pattern 3

    1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5

    // Pattern 4

    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1

    // Pattern 5

    1 4 9 16 25
    1 4 9 16 25
    1 4 9 16 25
    1 4 9 16 25
    1 4 9 16 25

    // Pattern 6

    a a a a a
    b b b b b
    c c c c c
    d d d d d
    e e e e e

    // Pattern 7
    1 2 3 4 5
    6 7 8 9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
*/
int main()
{

    int rows = 5;
    int count = 1;
    for (int i = 1; i <= rows; i++)
    {
        for (int j = 1; j <= rows; j++)
        {
            cout << count << " ";
            count++;
        }

        cout << endl;
    }
}