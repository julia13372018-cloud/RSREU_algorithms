#include <iostream>
#include <vector>

void InsertionSort(std::vector<int>& A) {
    int n = A.size();
    for (int i = 1; i < n; i++) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = key;
    }
}

int main() {
    std::vector<int> A;
    int num;
    while (std::cin >> num) {
        A.push_back(num);
    }
    InsertionSort(A);
    for (int i = 0; i < A.size(); i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}

