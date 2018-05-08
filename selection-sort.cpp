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

void SelectionSort(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        int smallest = arr[i];
        int smallest_i = i;
        for (int j = i; j < arr.size(); j++) {
            if (arr[j] <= smallest) {
                smallest = arr[j];
                smallest_i = j;        
            }
        }
        swap(arr[i], arr[smallest_i]);
    }
}

int main() {
    vector<int> arr {644, 34, 1, 0, -3, 45, 2, 2};
    SelectionSort(arr);
    print_array(arr);
    return 0;
}