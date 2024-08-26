#ifndef STRUCTURE_HPP
#define STRUCTURE_HPP
#include <cassert>
#include <vector>

using namespace std;

class custom_set {
    vector<char> data;
public:
    custom_set() = default;

    auto push_back(const char value) -> void {
        data.push_back(value);
    }

    auto operator+=(const char value) -> void {
        data.push_back(value);
    }

    auto operator[](const int index) const -> char {
        return data.at(index);
    }

    [[nodiscard]] auto size() const -> size_t {
        return data.size();
    }

    auto operator[](const char value) const -> int {
        int left = 0;
        int right = static_cast<int>(data.size()) - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (data[mid] == value) {
                return mid;
            }

            if (data[mid] < value) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
};

inline auto transform_char(const char c) -> int {
    if (c >= 32 && c <= 126) return c - 27;
    if (c >= 9 && c <= 13) return c - 9;

    assert(false);
}

inline auto reserve_transform_char(const int i) -> char {
    return static_cast<char>(i + (i >= 5 ? 27 : 9));
}

inline auto occ_find(const int i, const vector<int>& occ) -> int {
    auto left = 0;
    int right = occ.size() - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (occ[mid] < i && i <= occ[mid + 1]) {
            return mid;
        }

        if (occ[mid + 1] < i) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return right;
}

inline auto c_find(const int i, const vector<int>& c, custom_set& c_char) -> char {
    auto left = 0;
    int right = c.size() - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;


        if (c[mid] <= i && i < c[mid + 1]) {
            return c_char[mid];
        }

        if (c[mid + 1]< i) {
            left = mid + 1;
        } else if (c[mid + 1] == i) {
            return c_char[mid + 1];
        } else  {
            right = mid - 1;
        }
    }

    return c_char[right];
}


#endif //STRUCTURE_HPP
