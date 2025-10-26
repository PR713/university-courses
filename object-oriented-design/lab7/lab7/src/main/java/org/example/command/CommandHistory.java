package org.example.command;

import java.util.ArrayList;
import java.util.List;

class CommandHistory {
    private List<Command> history;

    public CommandHistory() {
        this.history = new ArrayList<>();
    }

    public void push(Command c) {
        history.add(c);
    }

    public Command pop() {
        if (!history.isEmpty()) {
            return history.remove(history.size() - 1);
        }
        return null;
    }

    public boolean isEmpty() {
        return history.isEmpty();
    }

    public int size() {
        return history.size();
    }
}
