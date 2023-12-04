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

int matchedWinning(string line, smatch match) {
    set<int> winningSet = parseLineToSet(match[2].str());
    set<int> mineSet = parseLineToSet(match[3].str());

    vector<int> intersection;
    set_intersection(
        winningSet.begin(), winningSet.end(),
        mineSet.begin(), mineSet.end(), back_inserter(intersection)
    );

    return intersection.size();
}

int main () {
    ifstream myfile("../inputs/day04.txt");
    string line;

    // 0th group: everything
    // 1st group: card x
    // 2nd group: winning numbers
    // 3rd group: my numbers
    regex card_regex("(Card.*\\d+): *(\\d+.*) *\\| *(\\d+.*)");
    smatch match;

    map<int, pair<int, int>> cardToFrequencyAndIntersectionSize; 
    int sumOfPoints = 0;
    int sumOfFrequencies = 0;

    while (getline(myfile, line)) {
        if (std::regex_search(line, match, card_regex)) {
            int cardNumber = stoi(match[1].str().substr(4));
            int intersectionSize = matchedWinning(line, match);
            cardToFrequencyAndIntersectionSize.insert({cardNumber, {1, intersectionSize}});
            sumOfPoints += pow(2, intersectionSize - 1);
        }
    }

    for (auto& entry : cardToFrequencyAndIntersectionSize) {
        int cardNumber = entry.first;
        int frequency = entry.second.first;
        int intersectionSize = entry.second.second;
        for (int i = 0; i < intersectionSize; i++) {
            int cardIdToBeInserted = cardNumber + i + 1;
            cardToFrequencyAndIntersectionSize[cardIdToBeInserted].first += frequency;
        }   
    }

    for (auto& entry : cardToFrequencyAndIntersectionSize) {
        sumOfFrequencies += entry.second.first;
    }

    std::cout << "Sum of points: " << sumOfPoints << std::endl;
    std::cout << "Sum of frequencies: " << sumOfFrequencies << std::endl;
    return 0;
}