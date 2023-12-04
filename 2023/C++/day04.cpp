#include <fstream>
#include <regex>
#include <iostream>
#include <set>
#include <cmath>

using namespace std;

set<int> parseLineToSet(string input) {
    set<int> s;
    regex setRegex("\\d+");
    sregex_iterator numberIter(input.begin(), input.end(), setRegex);
    sregex_iterator numberEnd;

    while (numberIter != numberEnd) {
        int value = stoi(numberIter->str());
        s.insert(value);
        numberIter++;
    }
    return s;
}

int main () {
    ifstream myfile("../inputs/day04.txt");
    string line;

    // 0th group: everything
    // 1st group: card x
    // 2nd group: winning numbers
    // 3rd group: my numbers
    regex card_regex("(Card.*\\d+:) *(\\d+.*) *\\| *(\\d+.*)");
    smatch match;

    int sum = 0;
    int lineIndex = 0;
    while (getline(myfile, line)) {
        if (std::regex_search(line, match, card_regex)) {
            set<int> winningSet = parseLineToSet(match[2].str());
            set<int> mineSet = parseLineToSet(match[3].str());

            vector<int> intersection;
            set_intersection(
                winningSet.begin(), winningSet.end(),
                mineSet.begin(), mineSet.end(), back_inserter(intersection)
             );

            int intersectionSize = intersection.size();
            if (intersectionSize == 0) {
                continue;
            }
            sum += pow(2, intersectionSize - 1);
        }
    }

    cout << "Sum of points: " << sum << endl;
    return 0;
}