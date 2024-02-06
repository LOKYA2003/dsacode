#include <iostream>
using namespace std;

int searchInsert(int arr[], int size, int k)
{
    int start = 0;
    int end = size - 1;
    int ans = size;
    while (start <= end)
    {
        int mid = start + (end - start) / 2; // Fix the calculation of mid

        if (arr[mid] == k)
        {
            return mid;
        }
        else if (arr[mid] < k)
        {
            // Right
            start = mid + 1;
        }
        else
        {
            // Left
            ans = mid;
            end = mid - 1;
        }qrt x
        
    }

    return ans;
}

int main()
{
    int arr[5] = {1, 3, 5, 6, 8};
    int size = 5; // Fix the size to 5
    int k = 7;

    int output = searchInsert(arr, size, k);

    cout << output << endl;
}
