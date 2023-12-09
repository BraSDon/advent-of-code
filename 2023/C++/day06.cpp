#include <iostream>
#include <vector>
#include <regex>
#include <fstream>

using namespace std;

struct Race {
    int time;
    int record;

    Race(int time, int record) {
        this->time = time;
        this->record = record;
    }
};

vector<int> readNextLine(ifstream* file) {
    string line;
    getline(*file, line);
    regex numbersRegex("\\d+");
    sregex_iterator numberIter(line.begin(), line.end(), numbersRegex);
    sregex_iterator numberEnd;
    vector<int> numbers;

    while (numberIter != numberEnd) {
        int value = stoi(numberIter->str());
        numbers.push_back(value);
        numberIter++;
    }
    return numbers;
}

vector<Race> getRaces(vector<int> times, vector<int> records) {
    vector<Race> out;
    for (int i = 0; i < times.size(); i++) {
        out.emplace_back(times[i], records[i]);
    }
    return out;
}

bool winning(int totalTime, int chargingTime, int record)  {
    return (chargingTime * (totalTime - chargingTime)) > record;
}

int calculateWins(const Race& race) {
    int totalWins = 0;
    for (int waiting = 1; waiting < race.time; waiting++) {
        totalWins += winning(race.time, waiting, race.record);
    }
    return totalWins;
}

int calculateProduct(const vector<int>& wins) {
    int product = 1;
    for (int win : wins) {
        product *= win;
    }
    return product;
}

int main () {
    ifstream file("../inputs/day06.txt");
    vector<int> times = readNextLine(&file);
    vector<int> records = readNextLine(&file);
    vector<Race> races = getRaces(times, records);
    vector<int> wins;
    for (const Race& race : races) {
        wins.push_back(calculateWins(race));
    }
    cout << calculateProduct(wins) << endl;
    return 0;
}