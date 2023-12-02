#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>
#include <map>
#include <regex>

using RGB = std::tuple<int, int, int>;

RGB parseSet(std::string& set_string) {
    std::regex redx("([0-9]+) red");
    std::regex greenx("([0-9]+) green");
    std::regex bluex("([0-9]+) blue");
    std::smatch match;

    int red, green, blue;
    red = green = blue = 0;
    if (std::regex_search(set_string, match, redx)) {
        red = std::stoi(match[1]);
    }
    if (std::regex_search(set_string, match, greenx)) {
        green = std::stoi(match[1]);
    }
    if (std::regex_search(set_string, match, bluex)) {
        blue = std::stoi(match[1]);
    }

    return std::make_tuple(red, green, blue);
}

bool isSetPossible(const RGB& set) {
    int red, green, blue;
    std::tie(red, green, blue) = set;
    return red <= 12 && green <= 13 && blue <= 14;
}

bool isGamePossible(const std::vector<RGB>& sets) {
    // return true if all sets are possible
    for (const auto& set : sets) {
        if (!isSetPossible(set)) {
            return false;
        }
    }
    return true;
}

int main () {
    std::ifstream myfile ("../inputs/day02.txt");

    std::string line;
    int sum_of_possible_ids = 0;
    int i = 0;
    while (std::getline(myfile, line)) {
        std::regex gamex("Game ([0-9]+)");
        std::smatch match;
        std::regex_search(line, match, gamex);
        int game = std::stoi(match[1]);

        // get sets by splitting at ";"
        std::vector<RGB> sets;
        std::string delimiter = ";";
        size_t pos = 0;
        std::string token;
        while ((pos = line.find(delimiter)) != std::string::npos) {
            token = line.substr(0, pos);
            sets.push_back(parseSet(token));
            line.erase(0, pos + delimiter.length());
        }
        sets.push_back(parseSet(line)); // handle last set

        if (isGamePossible(sets)) {
            sum_of_possible_ids += game;
        }
    }

    std::cout << "Sum of possible game IDs: " << sum_of_possible_ids << std::endl;
}
