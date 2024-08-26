#include <iostream>
#include <fstream>
#include <unordered_map>
#include <sstream>
#include <unordered_set>
#define TWO_MASK 127
#define THREE_MASK 63
#define MAX 4194303

using namespace std;

auto to_int(std::string::const_iterator &c) -> std::pair<bool, int> {
    const auto b = static_cast<unsigned char>(*c);

    if (b >> 6 == 2) {
        const auto b1 = static_cast<unsigned char>(*++c);
        return {true, (b & TWO_MASK) << 8 | b1};
    }
    if (b >> 6 == 3) {
        const auto b1 = static_cast<unsigned char>(*++c);
        const auto b2 = static_cast<unsigned char>(*++c);
        return {true, (b & THREE_MASK) << 16 | b1 << 8 | b2};
    }

    return {false, static_cast<int>(b)};
}

auto main(const int argc, const char *argv[]) -> int {
    string p;
    ifstream in;
    ofstream out;
    string input;
    string bytes;
    int index = 0;
    ostringstream ss;
    string::const_iterator c;

    unordered_set<string> list;
    unordered_map<int, string> dict;

    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <source> <target>" << endl;
        exit(1);
    }

    in = ifstream (argv[1], ios::binary);
    if (!in) {
        cerr << "Unable to open source file." << std::endl;
        return 1;
    }
    ss << in.rdbuf();
    in.close();

    out = ofstream(argv[2], ios::binary);
    if (!out) {
        cerr << "Unable to open target file." << std::endl;
        return 1;
    }

    input = ss.str();

    if (input.empty()) {
        out.close();
        return 0;
    }

    c = input.cbegin();
    p = string(1, *c++);
    bytes = p;

    for (; c != input.cend(); ++c) {
        auto [type, value] = to_int(c);
        auto temp = type ? dict.find(value) == dict.end() ? p + p[0] : dict.at(value): string(1, static_cast<char>(value));
        bytes += temp;

        if (index < MAX) {
            if (list.find(p + temp[0]) == list.end()) {
                dict.insert({ index++, p + temp[0] });
                list.insert(p + temp[0]);
            } else {
                p += temp;
                continue;
            }
        }
        p = temp;
    }

    out << bytes;
    out.close();

    return 0;
}
