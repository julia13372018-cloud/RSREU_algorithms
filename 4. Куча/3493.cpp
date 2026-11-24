#include <iostream>
#include <vector>
#include <string>

struct MinHeap {
    std::vector<int> heap;

    void clear() {
        heap.clear();
    }

    void add(int val) {
        heap.push_back(val);
        int i = heap.size() - 1;
        while (i > 0) {
            int p = (i - 1) / 2;
            if (heap[i] >= heap[p]) break;
            std::swap(heap[i], heap[p]);
            i = p;
        }
    }

    void extract() {
        if (heap.empty()) {
            std::cout << "CANNOT\n";
            return;
        }
        std::cout << heap[0] << "\n";
        if (heap.size() == 1) {
            heap.pop_back();
            return;
        }
        heap[0] = heap.back();
        heap.pop_back();
        int i = 0;
        int n = heap.size();
        while (2 * i + 1 < n) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int j = left;
            if (right < n && heap[right] < heap[left]) j = right;
            if (heap[i] <= heap[j]) break;
            std::swap(heap[i], heap[j]);
            i = j;
        }
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    MinHeap hp;
    std::string cmd;
    while (std::cin >> cmd) {
        if (cmd == "CLEAR") {
            hp.clear();
        } else if (cmd == "ADD") {
            int n;
            std::cin >> n;
            hp.add(n);
        } else if (cmd == "EXTRACT") {
            hp.extract();
        }
    }
    return 0;
}

