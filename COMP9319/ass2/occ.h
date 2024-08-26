#ifndef OCC_H
#define OCC_H
#include <fstream>
#include <list>
#include <vector>

#include "support.h"


using namespace std;

class occ {
    list<tuple<char, int>> cache_list{};
    vector<vector<int>> occ_vector{};
    size_t capacity{0};
    size_t current_size{0};
    custom_set& c_char;
    int start{0};
    ifstream file;
    string idx_path;

public:
    explicit occ(custom_set& c_char, const string& idx_path) : c_char(c_char) {
        this->idx_path = idx_path;
    }

    auto begin() -> void {
        file = ifstream(idx_path, std::ios::binary);
    }

    auto setStart(const int start) -> void {
        this->start = start;
    }

    auto setCapacity(const size_t capacity) -> void {
        this->capacity = capacity;
    }

    auto find(const char& c) -> vector<int>& {
        auto it = find_if(cache_list.begin(), cache_list.end(), [c](const tuple<char, int>& elem) {
            return get<0>(elem) == c;
        });

        if (it != cache_list.end()) {
            cache_list.splice(cache_list.end(), cache_list, it);
            return occ_vector[get<1>(*it)];
        }

        int lru_index = get<1>(cache_list.front());
        cache_list.pop_front();
        cache_list.emplace_back(c, lru_index);

        return insert(c, lru_index);
    }

    auto insert(char c, int lru_index) -> vector<int>& {
        auto pos = c_char[c];
        auto size = occ_vector.front().size() - 1;

        auto startPos = start + pos * sizeof(int) * size;
        file.seekg(startPos);
        if (!file) {
            throw std::runtime_error("Failed to seek to the specified position in the file.");
        }

        vector<int> data(size);
        file.read(reinterpret_cast<char*>(data.data()), size * sizeof(int));
        if (!file) {
            throw std::runtime_error("Failed to read the data from the file.");
        }

        data.insert(data.begin(), 0);

        occ_vector[lru_index] = data;
        return occ_vector[lru_index];
    }

    auto pre_insert(const char c) -> void {
        if (current_size == capacity) return;

        cache_list.emplace_back(c, current_size);
        current_size++;
        occ_vector.emplace_back(vector{0});
    }

    auto insert(const vector<int>& occ) {
        for (size_t i = 0; i < occ.size() && i < capacity; i++) {
            occ_vector[i].push_back(occ[i]);
        }
    }

    auto insert(const vector<int>& occ, char c) {
        cache_list.emplace_back(c, current_size);
        current_size++;
        occ_vector.push_back(occ);
    }

    [[nodiscard]] auto full() const -> bool {
        return current_size == capacity;
    }
};

#endif //OCC_H
