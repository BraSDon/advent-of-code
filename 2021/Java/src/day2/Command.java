package day2;

public enum Command {
    FORWARD("forward"),
    DOWN("down"),
    UP("up");

    private String name;

    Command(String name) {
        this.name = name;
    }

    public static Command fromString(String text) {
        for (Command cmd : Command.values()) {
            if (cmd.name.equalsIgnoreCase(text)) {
                return cmd;
            }
        }
        return null;
    }
}
