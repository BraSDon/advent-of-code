#include <map>
#include <vector>
#include <regex>
#include <iostream>
#include <fstream>

using namespace std;

struct MapEntry {
    long destStart;
    long sourceStart;
    long length;

    MapEntry(long destStart, long sourceStart, long length) {
        this->destStart = destStart;
        this->sourceStart = sourceStart;
        this->length = length;
    }

    MapEntry(array<long, 3> numbers) {
        this->destStart = numbers[0];
        this->sourceStart = numbers[1];
        this->length = numbers[2];
    }

    bool inRange(long sourceValue) {
        return sourceValue >= sourceStart && sourceValue < sourceStart + length;
    }

    long getDestValue(long sourceValue) {
        if (inRange(sourceValue)) {
            long val = destStart + (sourceValue - sourceStart);
            return val;
        } else {
            return sourceValue;
        }
    }
};

struct Map {
    vector<MapEntry> entries;
    Map(vector<MapEntry> entries) : entries(entries) {}
};

struct Input {
    vector<long> seeds;
    vector<Map> maps;

    Input(vector<long> seeds, vector<Map> maps) {
        this->seeds = seeds;
        this->maps = maps;
    }
    
    vector<long> mapSeedsToLocation() {
        vector<long> locationSeeds;
        for (long seed : seeds) {
            long currVal = seed;
            for (Map map : maps) {
                for (MapEntry entry : map.entries) {
                    if (entry.inRange(currVal)) {
                        currVal = entry.getDestValue(currVal);
                        break;
                    }
                }
            }
            locationSeeds.push_back(currVal);
        }
        return locationSeeds;
    }
};

vector<string> readLines(string filename) {
    vector<string> lines;
    ifstream myfile(filename);
    string line;

    while (getline(myfile, line)) {
        lines.push_back(line);
    }
    return lines;
}

vector<long> getSeeds(string& line) {
    vector<long> seeds;
    regex seedRegex("\\d+");
    sregex_iterator seedIter(line.begin(), line.end(), seedRegex);
    sregex_iterator seedEnd;

    while (seedIter != seedEnd) {
        long seed = stol(seedIter->str());
        seeds.push_back(seed);
        seedIter++;
    }
    return seeds;
}

MapEntry getMapEntry(string& line) {
    regex numbersRegex("\\d+");
    sregex_iterator numberIter(line.begin(), line.end(), numbersRegex);
    sregex_iterator numberEnd;

    array<long, 3> numbers;

    int i = 0;
    while (numberIter != numberEnd) {
        long value = stol(numberIter->str());
        numbers[i++] = value;
        numberIter++;
    }
    return MapEntry(numbers);
}

int main () {
    vector<Map> maps;
    string filename = "../inputs/day05.txt";
    vector<string> lines = readLines(filename);
    vector<long> seeds = getSeeds(lines[0]);

    vector<MapEntry> entries;
    for (int i = 2; i < lines.size(); i++) {
        string line = lines[i];
        if (line == "") {
            Map map(entries);
            maps.push_back(map);
            entries.clear();
        } else if (line.find("map") != string::npos) {
            continue;
        } else {
            entries.emplace_back(getMapEntry(line));
        }
    }
    Map map(entries);
    maps.push_back(map);

    Input input(seeds, maps);
    vector<long> locationSeeds = input.mapSeedsToLocation();
    // find smallest location seed
    long smallestLocationSeed = locationSeeds[0];
    for (int i = 1; i < locationSeeds.size(); i++) {
        if (locationSeeds[i] < smallestLocationSeed) {
            smallestLocationSeed = locationSeeds[i];
        }
    }
    cout << "Smallest location seed: " << smallestLocationSeed << endl;
}