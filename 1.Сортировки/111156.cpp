// ??????? 3: ???????????? ? ????????? ??????? ???????
#include <iostream>
#include <vector>

void SelectionSort(std::vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n - 1; i++) {
        int max_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[max_idx]) {
                max_idx = j;
            }
        }
        int temp = A[i];
        A[i] = A[max_idx];
        A[max_idx] = temp;
    }
}

int main() {
    std::vector<int> A;
    int num;
    while (std::cin >> num) {
        A.push_back(num);
    }
    SelectionSort(A);
    for (int i = 0; i < A.size(); i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}


