#include <vector>
#include <utility>
#include <fstream>
#include <cctype>
#include <regex>
#include <iostream>

using namespace std;

class Coordinate {
public:
    int x;
    int y;

    Coordinate(int x, int y) : x(x), y(y) {}

    bool isAdjacentTo(const Coordinate& other) const {
        return abs(x - other.x) <= 1 && abs(y - other.y) <= 1;
    }
};

class DigitGroup {
public:
    int value;
    vector<Coordinate> positions;

    DigitGroup(int value, vector<Coordinate> positions) : value(value), positions(positions) {}
    
    bool isAdjacentTo(const Coordinate& symbolPosition) const {
        for (const auto& position : positions) {
            if (position.isAdjacentTo(symbolPosition)) {
                return true;
            }
        }
        return false;
    }
};

vector<Coordinate> getCoordinates(int start, int length, int rowIndex) {
    vector<Coordinate> coordinates;
    for (int i = start; i < start + length; i++) {
        coordinates.emplace_back(rowIndex, i);
    }
    return coordinates;
}

int main() {
    vector<DigitGroup> digitGroups;
    vector<Coordinate> symbolPositions;
    int sum = 0;

    ifstream myfile("../inputs/day03.txt");
    string line;
    int rowIndex = 0;

    while (getline(myfile, line)) {

        regex numbersRegex("\\d+");
        regex symbolRegex("[^\\d.]");
        smatch match;

        // find all digit groups
        sregex_iterator digitGroupIter(line.begin(), line.end(), numbersRegex);
        sregex_iterator digitGroupEnd;

        while (digitGroupIter != digitGroupEnd) {
            string matched = digitGroupIter->str();
            int position = digitGroupIter->position();
            DigitGroup digitGroup(stoi(matched), getCoordinates(position, matched.length(), rowIndex));
            digitGroups.push_back(digitGroup);
            digitGroupIter++;
        }

        // find all symbols
        sregex_iterator symbolIter(line.begin(), line.end(), symbolRegex);
        sregex_iterator symbolEnd;

        while (symbolIter != symbolEnd) {
            symbolPositions.emplace_back(rowIndex, symbolIter->position());
            symbolIter++;
        }
        rowIndex++;
    }

    // puzzle 1
    for (const auto& digitGroup : digitGroups) {
        for (const auto& symbolPos : symbolPositions) {
            if (digitGroup.isAdjacentTo(symbolPos)) {
                sum += digitGroup.value;
            }
        }
    }

    // puzzle 2
    int sumGearRatio = 0;
    for (const auto& symbolPos : symbolPositions) {
        vector<DigitGroup> adjacentDigitGroups;
        for (const auto& digitGroup : digitGroups) {
            if (digitGroup.isAdjacentTo(symbolPos)) {
                adjacentDigitGroups.push_back(digitGroup);
            }
        }
        if (adjacentDigitGroups.size() == 2) {
            sumGearRatio += adjacentDigitGroups[0].value * adjacentDigitGroups[1].value;
        }
    }

    cout << "Total sum: " << sum << endl;
    cout << "Total sum of gear ratios: " << sumGearRatio << endl;

    return 0;
}
