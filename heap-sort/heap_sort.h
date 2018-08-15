#include "heap.h"

template <typename T>
void heapSort(vector<T>& array) {
    auto heap = MinHeap<T>();
    
    for (T d: array) heap.insert(d);
    for (int i = 0; i < array.size(); i++) array[i] = heap.getMin();
}