#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void print_array(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void BubbleSort(vector<int>& arr) {
    for (int i = 0; i < arr.size()-1; i++) {
        bool swapped = false;
        for (int j = 0; j < arr.size()-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped) return;
    }
}

int main() {
    vector<int> arr {644, 34, 1, 0, -3, 45, 2, 2};
    BubbleSort(arr);
    print_array(arr);
    return 0;
}