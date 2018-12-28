#include <iostream>
#include "heap_sort.h"
#include <vector>
#include <stdlib.h>

using namespace std;

int main() {
    vector<double> numArray;

    for (int i = 0; i < 50; i++) numArray.push_back(rand() % 100 + 1);

    for (auto d: numArray) cout << d << " ";
    cout << "\n";
    heapSort(numArray);
    for (auto d: numArray) cout << d << " ";
    cout << "\n";
}