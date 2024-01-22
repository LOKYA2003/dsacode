#include <iostream>
using namespace std;

/*
Print from 1 to 100
& Print from 101 to 200
Print alphabet from A to Z
Reverse a number from 10 to 1
Multiplication table using for loop
Sum of natural numbers
Factorials
Prime number
*/

// 101 - 200
// a b c d

int main()
{

    //    1+2+3... num = output

    int fact = 1;
    int num;
    cout << "Enter number : ";
    cin >> num;

    for (int i = 1; i <= num; i++)
    {
        fact = fact * i;
    }

    cout << "the fact is " << fact;
}