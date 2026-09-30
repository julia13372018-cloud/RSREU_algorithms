#include <iostream>
#include <vector>
#include <algorithm>

bool check(long long len, const std::vector<long long>& ropes, long long k) {
    if (len == 0) return false;
    long long count = 0;
    for (long long r : ropes) {
        count += r / len;
    }
    return count >= k;
}

int main() {
    long long n, k;
    if (!(std::cin >> n >> k)) return 0;
    std::vector<long long> ropes(n);
    long long max_len = 0;
    for (long long i = 0; i < n; i++) {
        std::cin >> ropes[i];
        max_len = std::max(max_len, ropes[i]);
    }
    long long left = 1, right = max_len, ans = 0;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (check(mid, ropes, k)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    std::cout << ans << std::endl;
    return 0;
}

