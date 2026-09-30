#include <iostream>
#include <vector>
#include <algorithm>

bool check(int dist, const std::vector<int>& coords, int k) {
    int count = 1;
    int last_pos = coords[0];
    for (size_t i = 1; i < coords.size(); i++) {
        if (coords[i] - last_pos >= dist) {
            count++;
            last_pos = coords[i];
        }
    }
    return count >= k;
}

int main() {
    int n, k;
    if (!(std::cin >> n >> k)) return 0;
    std::vector<int> coords(n);
    for (int i = 0; i < n; i++) {
        std::cin >> coords[i];
    }
    int left = 0, right = coords[n - 1] - coords[0], ans = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (check(mid, coords, k)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    std::cout << ans << std::endl;
    return 0;
}

