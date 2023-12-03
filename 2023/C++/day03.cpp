#include <vector>
#include <utility>
#include <fstream>
#include <cctype>
#include <regex>
#include <iostream>

using namespace std;

struct point {
    int x;
    int y;

    point(int x, int y) {
        this->x = x;
        this->y = y;
    }

    // adjacent to another coordinate (including diagonals)
    bool isAdjacentTo(point other) {
        return abs(x - other.x) <= 1 && abs(y - other.y) <= 1;
    }
};

class Number {
    public:
        int value;
        vector<point> positions;
        Number(int value, vector<point> positions) {
            this->value = value;
            this->positions = positions;
            // print value and positions
            cout << "Value: " << value << endl;
            for (auto position : positions) {
                cout << "(" << position.x << ", " << position.y << ")" << endl;
            }
        }

        bool isAdjacentTo(point symbol_position) {
            for (auto position : positions) {
                if (position.isAdjacentTo(symbol_position)) {
                    return true;
                }
            }
            return false;
        }
};

vector<point> getPositions(int start, int length, int rowIndex) {
    vector<point> positions;
    for (int i = start; i < start + length; i++) {
        positions.push_back(point(rowIndex, i));
    }
    return positions;
}

int main () {
    vector<vector<char>> matrix;
    vector<Number> numbers;
    vector<point> symbol_positions;
    int sum = 0;

    ifstream myfile ("../inputs/day03.txt");
    string line;
    int rowIndex = 0;

    while (getline(myfile, line)) {

        regex numbers_rgx("\\d+");
        regex symbol_rgx("[^\\d.]");
        smatch match;

        // find all numbers
        sregex_iterator nb_iter(line.begin(), line.end(), numbers_rgx);
        sregex_iterator nb_end;

        while (nb_iter != nb_end) {
            string matched = nb_iter->str();
            int position = nb_iter->position();
            Number number(stoi(matched), getPositions(position, matched.length(), rowIndex));
            numbers.push_back(number);
            nb_iter++;
        }

        // find all symbols
        sregex_iterator symbol_iter(line.begin(), line.end(), symbol_rgx);
        sregex_iterator symbol_end;

        while (symbol_iter != symbol_end) {
            symbol_positions.push_back(point(rowIndex, symbol_iter->position()));
            symbol_iter++;
        }
        rowIndex++;
    }

    // for each number, check if it has an adjacent symbol. If yes, add its value to the sum.
    for (auto number : numbers) {
        for (auto symbol_pos : symbol_positions) {
            if (number.isAdjacentTo(symbol_pos)) {
                sum += number.value;
            }
        }
    }
    
    cout << "Total sum: " << sum;
}