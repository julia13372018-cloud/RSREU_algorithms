#include <iostream>
#include <algorithm>

int main() {
    long long n, x, y;
    if (!(std::cin >> n >> x >> y)) return 0;
    long long first_page = std::min(x, y);
    long long left = 0, right = (n - 1) * first_page, ans = right;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if ((mid / x) + (mid / y) >= n - 1) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    std::cout << ans + first_page << std::endl;
    return 0;
}

