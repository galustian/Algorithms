#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void print_array(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

void InsertionSort(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        int j = i;        
        while (arr[j] < arr[j-1] && j > 0) {
            swap(arr[j-1], arr[j]);
            j--;
        }
    }
}

int main() {
    vector<int> arr {644, 34, 1, 0, -3, 45, 2, 2, -42, 42};
    InsertionSort(arr);
    print_array(arr);
    return 0;
}