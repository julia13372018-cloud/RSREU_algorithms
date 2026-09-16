#include <iostream>
#include <vector>

void BubbleSort(std::vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (A[j] < A[j + 1]) {
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }
}

int main() {
    std::vector<int> A;
    int num;
    while (std::cin >> num) {
        A.push_back(num);
    }
    BubbleSort(A);
    for (int i = 0; i < A.size(); i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}

