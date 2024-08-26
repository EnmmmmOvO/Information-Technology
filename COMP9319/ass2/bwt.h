//
// Created by Jinghan Wang on 24/7/2024.
//

#ifndef BWT_H
#define BWT_H

#include <string>
#include <fstream>
#include <tuple>

using namespace std;

class bwt {
    string bwt_string{};
    int range;
    size_t start{0};
    ifstream file;
    size_t size{0};

public:
    bwt (int range,const string& bwt_path) : range(range) {
        file = ifstream(bwt_path);
        if (!file.is_open()) throw std::runtime_error("Could not open file " + bwt_path);
        file.seekg(0, std::ios::end);
        size = file.tellg();
        file.seekg(0, std::ios::beg);
    }

    ~bwt() {
        if (file.is_open()) {
            file.close();
        }
    }

    auto getSize() const -> size_t {
        return size;
    }

    auto reset() -> void {
        start = 0;
    }

    auto forward() -> std::tuple<bool, std::string&> {
        bwt_string.resize(range);

        file.clear();
        file.seekg(start);
        file.read(&bwt_string[0], range);
        size_t read_count = file.gcount();
        bwt_string.resize(read_count);

        start += read_count;

        bool isEnd = (start >= size);
        return {isEnd, bwt_string};
    }

    char charAt(size_t index) {
        if (index >= size) {
            throw std::out_of_range("Index out of range");
        }

        if (index >= start && index < start + bwt_string.size()) {
            return bwt_string[index - start];
        }

        // If not, update the start position and reload the cache
        start = (index / range) * range;
        file.clear();
        file.seekg(start);

        bwt_string.resize(range);
        file.read(&bwt_string[0], range);
        bwt_string.resize(file.gcount());

        return bwt_string[index - start];
    }
};

#endif //BWT_H
