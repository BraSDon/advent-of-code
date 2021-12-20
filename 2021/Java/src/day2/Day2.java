package day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day2 {

    private static final String FILENAME = "2021\\Java\\src\\day2\\input.txt";

    public static void main(String[] args) {
        System.out.println(calculateTask1(getCommandsFromInput(getInput())));
        System.out.println(calculateTask2(getCommandsFromInput(getInput())));
    }

    private static int calculateTask1(List<Tuple<Command, Integer>> list) {
        int depth = 0;
        int horizontalPos = 0;
        for (Tuple<Command, Integer> tuple : list) {
            switch (tuple.x) {
                case FORWARD -> horizontalPos += tuple.y;
                case UP -> depth -= tuple.y;
                case DOWN -> depth += tuple.y;
            }
        }
        return depth * horizontalPos;
    }

    private static int calculateTask2(List<Tuple<Command, Integer>> list) {
        int depth = 0;
        int horizontalPos = 0;
        int aim = 0;
        for (Tuple<Command, Integer> tuple : list) {
            switch (tuple.x) {
                case FORWARD -> {
                    horizontalPos += tuple.y;
                    depth += aim * tuple.y;
                }
                case UP -> {
                    aim -= tuple.y;
                }
                case DOWN -> {
                    aim += tuple.y;
                }
            }
        }
        return depth * horizontalPos;
    }

    public static List<String> getInput() {
        List<String> input = new ArrayList<String>();
        try {
            File file = new File(FILENAME);
            Scanner sc = new Scanner(file);
            while (sc.hasNextLine()) {
                input.add(sc.nextLine());
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error occured reading file");
        }
        return input;
    }

    public static List<Tuple<Command, Integer>> getCommandsFromInput(List<String> input) {
        List<Tuple<Command, Integer>> list = new ArrayList<Tuple<Command, Integer>>();
        for (String line : input) {
            String[] content = line.split("\s");
            Command command = Command.fromString(content[0]);
            int value = Integer.parseInt(content[1]);
            list.add(new Tuple<Command, Integer>(command, value));
        }
        return list;
    }
}
