#include <iostream>
#include <algorithm>

int main() {
    long long w, h, n;
    if (!(std::cin >> w >> h >> n)) return 0;
    long long left = 1, right = std::max(w, h) * n, ans = right;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if ((mid / w) * (mid / h) >= n) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    std::cout << ans << std::endl;
    return 0;
}

