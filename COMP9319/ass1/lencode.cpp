#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <sstream>
#define TWO 16383
#define MAX 4194303

using namespace std;

auto to_bytes(vector<unsigned char> &bytes, const string &p, const unordered_map<string, int> &dict) {
    if (p.length() < 3 ) {
        for (unsigned char i: p) bytes.push_back(i);
        return;
    }

    auto num = dict.at(p);
    if (num > TWO) {
        num |= 0xC00000;
        bytes.push_back(num >> 16 & 0xFF);
    } else num |= 0x8000;

    bytes.push_back(num >> 8 & 0xFF);
    bytes.push_back(num & 0xFF);
}

auto main(const int argc, const char *argv[]) -> int {
    string p;
    ifstream in;
    ofstream out;
    string input;
    int index = 0;
    ostringstream ss;
    string::const_iterator c;
    vector<unsigned char> bytes;
    unordered_map<string, int> dict;

    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <source> <target>" << endl;
        return 1;
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

    while (c != input.cend()) {
        if (dict.find(p + *c) != dict.end()) p += *c;
        else {
            if (index < MAX) dict.insert({p + *c, index++});
            to_bytes(bytes, p, dict);
            p = string(1, *c);
        }
        ++c;
    }

    to_bytes(bytes, p, dict);

    out.write(reinterpret_cast<const ostream::char_type*>(bytes.data()), bytes.size());

    out.close();
    return 0;
}
