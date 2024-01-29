
// [3,4,5,2,1]

// [1,2,3,4,5] -- Sorting this

#include <iostream>
using namespace std;

int main()
{

    int arr[5] = { 3,
                   4,
                   5,
                   2,
                   1 }

    int size = 5;

    for (int i = 0; i < size - 1; i++)
    {

        int index = 0;

        for (int j = i + 1; j < size; j++)
        {

            if (arr[j] < arr[index])
            {
                swap(arr[j], arr[index])
            }
        }
    }
}