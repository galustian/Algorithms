#include <vector>
#include <algorithm>

using namespace std;

// essentially a priority queue
template <typename T>
class MinHeap {

    public:

    T getMin() {
        T min = storage[1];
        storage[1] = storage[storage.size()-1];
        storage.pop_back();
        topDownHeapify();
        return min;
    }
    
    void insert(T value) {
        storage.push_back(value);
        bottomUpHeapify();
    }

    bool isEmpty() { return storage.size() == 1; }

    private:
    
    vector<T> storage {0};

    void bottomUpHeapify() {
        int i = storage.size()-1;

        while (i > 1 && storage[i/2] > storage[i]) {
            swap(storage[i], storage[i/2]);
            i /= 2;
        }
    }

    void topDownHeapify() {
        int i = 1;

        while (2*i <= storage.size()-1) {
            int j = 2*i;
            if (j < storage.size()-1 && storage[j] > storage[j+1]) j++;
            if (storage[i] < storage[j]) break;
            swap(storage[i], storage[j]);
            i = j;
        }
    }
};