package org.example.command;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Command Pattern Demo - Full Implementation ===\n");

        Application app = new Application();
        Editor editor = app.activeEditor;

        System.out.println("Initial editor content: '" + editor.text + "'");
        System.out.println("Initial clipboard: '" + app.clipboard + "'\n");

        editor.setSelection(0, 7);
        System.out.println("Selected text: '" + editor.getSelection() + "'");

        Command copyCmd = new CopyCommand(app, editor);
        app.executeCommand(copyCmd);
        System.out.println("After copy - Clipboard: '" + app.clipboard + "'");

        editor.setSelection(8, 10);
        Command cutCmd = new CutCommand(app, editor);
        app.executeCommand(cutCmd);
        System.out.println("After cut - Editor: '" + editor.text + "'");
        System.out.println("After cut - Clipboard: '" + app.clipboard + "'");

        editor.setSelection(editor.text.length(), editor.text.length());
        Command pasteCmd = new PasteCommand(app, editor);
        app.executeCommand(pasteCmd);
        System.out.println("After paste - Editor: '" + editor.text + "'");

        System.out.println("\n=== Testing UndoCommand ===");
        Command undoCmd = new UndoCommand(app, editor);
        app.executeCommand(undoCmd);
        System.out.println("After UndoCommand (undo paste): '" + editor.text + "'");

        System.out.println("\n=== Testing Direct Undo ===");
        app.undo();
        System.out.println("After undo cut: '" + editor.text + "'");
        System.out.println("Clipboard after undo cut: '" + app.clipboard + "'");

        app.undo();
        System.out.println("After undo copy: '" + editor.text + "'");
        System.out.println("Clipboard after undo copy: '" + app.clipboard + "'");

        System.out.println("\n=== Multiple Editors Test ===");
        Editor editor2 = new Editor("Second editor content");
        app.addEditor(editor2);
        app.setActiveEditor(editor2);

        System.out.println("Second editor content: '" + editor2.text + "'");

        editor2.setSelection(0, 6);
        Command cutCmd2 = new CutCommand(app, editor2);
        app.executeCommand(cutCmd2);
        System.out.println("After cut on second editor: '" + editor2.text + "'");
        System.out.println("Clipboard now contains: '" + app.clipboard + "'");

        app.setActiveEditor(editor);
        editor.setSelection(0, 0);
        Command pasteCmd2 = new PasteCommand(app, editor);
        app.executeCommand(pasteCmd2);
        System.out.println("After paste to first editor: '" + editor.text + "'");

        System.out.println("\n=== Final State ===");
        System.out.println("Editor 1: '" + app.editors.get(0).text + "'");
        System.out.println("Editor 2: '" + app.editors.get(1).text + "'");
        System.out.println("Clipboard: '" + app.clipboard + "'");
        System.out.println("Command history size: " + app.history.size());

        System.out.println("\n=== Final UndoCommand Test ===");
        Command finalUndoCmd = new UndoCommand(app, editor);
        app.executeCommand(finalUndoCmd);
        System.out.println("After final UndoCommand: '" + editor.text + "'");
        System.out.println("Final command history size: " + app.history.size());
    }
}
