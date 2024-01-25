#include <iostream>
using namespace std;

// Search single element
// Swap elements

int main()
{
    int arr[4] = {1,
                  2,
                  3,
                  9};

    int target = 9;
    for (int i = 0; i < 4; i++)
    {
        if (arr[i] == target)
        {
            cout << "Key is present";
        }
        else
        {
            cout << "Key is not present";
        }
    }
}