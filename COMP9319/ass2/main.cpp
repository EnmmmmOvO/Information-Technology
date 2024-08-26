#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>


#include "index.h"

using namespace std;


auto main(const int argc, const char *argv[]) -> int {
    if (argc < 4) {
        cerr << "Usage: " << argv[0] << " <bwt_path> <idx_path> <match_string_1> ..." << endl;
        return 1;
    }

    vector<string> arguments;
    string longest_arg = argv[3];

    for (int i = 4; i < argc; ++i) {
        auto arg = string(argv[i]);
        if (arg.size() > longest_arg.size()) {
            arguments.push_back(longest_arg);
            longest_arg = arg;
        } else {
            arguments.emplace_back(arg);
        }
    }

    auto idx = Index(argv[1], argv[2], arguments);

    auto result = idx.search(longest_arg);

    auto keys = vector<int>();
    for (const auto& [key, _] : result) {
        keys.push_back(key);
    }

    sort(keys.begin(), keys.end());
    for (const auto& key : keys) {
        cout << result[key] << endl;
    }

    return 0;
}
