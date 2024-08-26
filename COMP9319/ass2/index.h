#ifndef INDEX_HPP
#define INDEX_HPP

#include <fstream>
#include <string>
#include <filesystem>
#include <unordered_map>

#include "bwt.h"
#include "occ.h"
#include "support.h"

#define SPAN 800
#define BWT_LOAD 614400
#define OCC_LOAD 614400

using namespace std;

class Index {
    bwt bwt_;
    occ occ_;
    custom_set c_char;
    vector<int> c;
    int start{};
    char start_char{};
    int now;
    vector<string> matched;
    unordered_map<int, string> result_list;

public:
    auto load_index(const string& idx_path) {
        ifstream file(idx_path, std::ios::binary);

        auto total = 0;
        while (true) {
            char ch;
            int value;

            file.read(&ch, sizeof(ch));

            if (ch == '\0') break;

            file.read(reinterpret_cast<char*>(&value), sizeof(value));

            c_char.push_back(ch);
            c.push_back(total);
            total += value;
        }

        occ_.setStart(file.tellg());
        occ_.setCapacity(OCC_LOAD / ((bwt_.getSize() / SPAN + 1) * sizeof(int)));

        auto idx = 0;
        while (file.peek() != EOF && !occ_.full()) {
            auto record = vector{0};
            for (size_t i = 0; i < (bwt_.getSize() / SPAN); i++) {
                int value;
                file.read(reinterpret_cast<char*>(&value), sizeof(value));
                record.push_back(value);
            }
            occ_.insert(record, c_char[idx]);
            idx++;
        }

        file.close();
    }

    auto load_without_export_index(const string& idx_path) {
        auto record = vector(100, 0);

        while (true) {
            auto tmp = bwt_.forward();
            for (const auto c : get<1>(tmp)) {
                record[transform_char(c)]++;
            }
            if (get<0>(tmp)) break;
        }

        auto num = bwt_.getSize() / SPAN;
        occ_.setCapacity(OCC_LOAD / ((num + 1) * sizeof(int)));

        auto total = 0;
        auto idx = 0;
        for (const auto i: record) {
            if (i != 0) {
                char ch = reserve_transform_char(idx);
                occ_.pre_insert(ch);
                c_char.push_back(ch);
                c.push_back(total);
                total += i;
            }
            idx++;
        }

        record = vector(c_char.size(), 0);

        bwt_.reset();

        while (true) {
            auto tmp = bwt_.forward();
            auto idx = 0;
            for (const auto c : get<1>(tmp)) {
                if (idx != 0 && idx % SPAN == 0) {
                    occ_.insert(record);
                }

                record[c_char[c]]++;
                idx++;
            }
            if (get<0>(tmp)) break;
        }

        ofstream file(idx_path, ios::binary);
        file.close();
    }

    auto export_index(const string& idx_path) {
        auto file = ofstream(idx_path, ios::binary);
        auto record = vector(100, 0);

        while (true) {
            auto tmp = bwt_.forward();
            for (const auto c : get<1>(tmp)) {
                record[transform_char(c)]++;
            }
            if (get<0>(tmp)) break;
        }

        auto num = bwt_.getSize() / SPAN;
        occ_.setCapacity(OCC_LOAD / ((num + 1) * sizeof(int)));

        auto total = 0;
        auto idx = 0;
        for (const auto i: record) {
            if (i != 0) {
                char ch = reserve_transform_char(idx);
                occ_.pre_insert(ch);

                file.write(&ch, sizeof(ch));
                file.write(reinterpret_cast<const char*>(&i), sizeof(i));

                c_char.push_back(ch);
                c.push_back(total);
                total += i;
            }
            idx++;
        }

        file << '\0';

        auto start = static_cast<int>(file.tellp());
        occ_.setStart(start);

        record = vector(c_char.size(), 0);

        bwt_.reset();

        idx = 0;
        while (true) {
            auto tmp = bwt_.forward();
            for (const auto c : get<1>(tmp)) {
                if (idx != 0 && idx % SPAN == 0) {
                    occ_.insert(record);
                    for (auto i = 0; i < static_cast<int>(record.size()); i++) {
                        file.seekp(start + (idx / SPAN - 1 + i * num) * sizeof(int));
                        file.write(reinterpret_cast<const char*>(&record[i]), sizeof(record[i]));
                    }
                }

                record[c_char[c]]++;
                idx++;
            }
            if (get<0>(tmp)) break;
        }

        file.close();
    }


    explicit Index(
        const string& bwt_path,
        const string& idx_path,
        const vector<string>& match
        ) : bwt_(BWT_LOAD, bwt_path), occ_(c_char, idx_path), matched(match) {
        if (bwt_.getSize() <= 2000) {
            load_without_export_index(idx_path);
        } else if (filesystem::exists(idx_path)) {
            load_index(idx_path);
        } else {
            export_index(idx_path);
        }


    }

    auto search(const string& pattern) -> unordered_map<int, string> {
        occ_.begin();
        auto i = static_cast<int>(pattern.size() - 1);
        start_char = pattern[i];

        auto idx = c_char[pattern[i]];

        if (idx == -1) return result_list;

        auto fr = c[idx];
        auto to = c[idx + 1] - 1;

        if (to < 0) to = bwt_.getSize() - 1;

        auto record = vector<int>();

        for (auto x = fr; x <= to; x++) {
            if (pattern[i - 1] == bwt_.charAt(x)) {
                start = x;
                auto result = string(1, pattern[i]);
                bwt_search(i - 1, x, pattern, result);
            }
        }

        return result_list;
    }

    auto bwt_search(const int i, const int x, const string& pattern, string& result) -> void {
        auto x_char = bwt_.charAt(x);
        result = x_char + result;

        const auto front = occ_.find(x_char)[x / 800];

        auto tmp = 0;

        for (auto y = x - 1; y >= x / 800 * 800; y--) {
            if (bwt_.charAt(y) == x_char) {
                tmp++;
            }
        }

        auto temp = c[c_char[x_char]] + front + tmp;

        if (i < 0 && bwt_.charAt(temp) == '[') {
            auto match_index = string();
            for (auto const& i: result) {
                if (i == ']') break;
                match_index += i;
            }

            if (result_list.find(stoi(match_index)) != result_list.end())
                return;

            now = stoi(match_index);

            result = '[' + result;
            bwt_forward(this->start, this->start_char, result);
            return;
        }

        if (i > 0 && bwt_.charAt(temp) != pattern[i - 1]) return;

        bwt_search(i - 1, temp, pattern, result);
    }

    auto bwt_forward(const int x, const char& start, string& result) -> void {
        auto temp = x - c[c_char[start]] + 1;
        auto pos = occ_find(temp, occ_.find(start));

        auto i = pos * 800, j = temp - occ_.find(start)[pos];

        while (true) {
            if (bwt_.charAt(i) == start) {
                j--;
            }
            if (j == 0) {
                break;
            }
            i++;
        }

        auto tmp = c_find(i, c, c_char);
        if (tmp != '[') {
            result += tmp;
            bwt_forward(i, tmp, result);
        } else {
            for (const auto& basic_string : matched) {
                if (result.find(basic_string) == string::npos) return;
            }
            this->result_list.insert({now, result});
        }
    }
};

#endif //INDEX_HPP
