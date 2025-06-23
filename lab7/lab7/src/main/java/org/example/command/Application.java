package org.example.command;

import java.util.ArrayList;
import java.util.List;

class Application {
    public List<Editor> editors;
    public Editor activeEditor;
    public String clipboard;
    public CommandHistory history;

    public Application() {
        this.editors = new ArrayList<>();
        this.clipboard = "";
        this.history = new CommandHistory();
        createUI();
    }

    public void createUI() {
        System.out.println("UI created with menu items: Cut, Copy, Paste, Undo");

        Editor defaultEditor = new Editor("Welcome to the text editor!");
        editors.add(defaultEditor);
        activeEditor = defaultEditor;
    }

    public void executeCommand(Command c) {
        if (c != null) {
            c.execute();
            history.push(c);
        }
    }

    public void undo() {
        Command command = history.pop();
        if (command != null) {
            command.undo();
            System.out.println("Undo executed");
        } else {
            System.out.println("Nothing to undo");
        }
    }

    public void addEditor(Editor editor) {
        editors.add(editor);
    }

    public void setActiveEditor(Editor editor) {
        if (editors.contains(editor)) {
            activeEditor = editor;
        }
    }
}
