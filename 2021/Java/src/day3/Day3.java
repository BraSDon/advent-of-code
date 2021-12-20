package day3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Day3 {

    private static final String FILENAME = "2021\\Java\\src\\day3\\input.txt";

    public static void main(String[] args) {
        List<char[]> input;
        try {
            input = getInput();
            int generatorRating = convertCharArrayToInt(filterInput(input, false).get(0));
            int scrubberRating = convertCharArrayToInt(filterInput(input, true).get(0));
            System.out.println(generatorRating * scrubberRating);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static List<char[]> getInput() throws FileNotFoundException {
        List<char[]> input = new ArrayList<>();
        File file = new File(FILENAME);
        Scanner sc = new Scanner(file);
        while (sc.hasNextLine()) {
            input.add(sc.nextLine().toCharArray());
        }
        sc.close();
        return input;
    }

    public static List<char[]> filterInput(List<char[]> input, boolean isScrubber) {
        List<char[]> copy = new ArrayList<>(input);
        for (int i = 0; i < input.get(0).length && copy.size() > 1; i++) {
            char c = getNumber(copy, i, isScrubber);
            int finalI = i;
            copy = copy.stream().filter(x -> x[finalI] == c).collect(Collectors.toList());
        }
        return copy;
    }


    public static char getNumber(List<char[]> input, int position, boolean isScrubber) {
        int amountZeros = 0;
        int amountOnes = 0;
        for (char[] word : input) {
            switch (word[position]) {
                case '0' -> amountZeros++;
                case '1' -> amountOnes++;
            }
        }

        if (isScrubber) {
            return amountZeros <= amountOnes ? '0' : '1';
        } else {
            return amountZeros > amountOnes ? '0' : '1';
        }
    }

    public static int convertCharArrayToInt(char[] word) {
        return Integer.parseInt(new String(word), 2);
    }
}
