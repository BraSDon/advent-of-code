#include <iostream>
#include <vector>
#include <regex>
#include <fstream>

using namespace std;

struct Race {
    long time;
    long record;

    Race(long time, long record) {
        this->time = time;
        this->record = record;
    }
};

vector<long> readNextLine(ifstream& file) {
    string line;
    getline(file, line);
    regex numbersRegex("\\d+");
    sregex_iterator numberIter(line.begin(), line.end(), numbersRegex);
    sregex_iterator numberEnd;
    vector<long> numbers;

    while (numberIter != numberEnd) {
        long value = stol(numberIter->str());
        numbers.push_back(value);
        numberIter++;
    }
    return numbers;
}

vector<long> readNextLinePuzzle2(ifstream& file) {
    string line;
    getline(file, line);
    regex numbersRegex("\\d+");
    sregex_iterator numberIter(line.begin(), line.end(), numbersRegex);
    sregex_iterator numberEnd;
    vector<long> numbers;

    string numberString;
    while (numberIter != numberEnd) {
        numberString += numberIter->str();
        numberIter++;
    }
    if (!numberString.empty()) {
        numbers.push_back(stol(numberString));
    }
    return numbers;
}

vector<Race> getRaces(vector<long> times, vector<long> records) {
    vector<Race> out;
    for (int i = 0; i < times.size(); i++) {
        out.emplace_back(times[i], records[i]);
    }
    return out;
}

bool winning(long chargingTime, const Race& race)  {
    return (chargingTime * (race.time - chargingTime)) > race.record;
}

int calculateWins(const Race& race) {
    long fst = 1;
    long snd = race.time - 1;
    while (true) {
        bool fst_winning = winning(fst, race);
        bool snd_winning = winning(snd, race);
        if (fst_winning && snd_winning) {
            return snd - fst + 1;
        }
        if (!fst_winning) {
            fst++;
        }
        if (!snd_winning) {
            snd--;
        }
    }
}

int calculateProduct(const vector<long>& wins) {
    long product = 1;
    for (long win : wins) {
        product *= win;
    }
    return product;
}

void solution(vector<long> (*readLineFunction)(ifstream&)) {
    ifstream file("../inputs/day06.txt");
    vector<long> times = readLineFunction(file);
    vector<long> records = readLineFunction(file);
    vector<Race> races = getRaces(times, records);
    vector<long> wins;
    for (const Race& race : races) {
        wins.push_back(calculateWins(race));
    }
    cout << calculateProduct(wins) << endl;
}

int main () {
    solution(&readNextLine);
    solution(&readNextLinePuzzle2);
    return 0;
}