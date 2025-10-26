package org.example.command;

class CutCommand extends Command {

    public CutCommand(Application app, Editor editor) {
        super(app, editor);
    }

    @Override
    public void execute() {
        saveBackup();
        app.clipboard = editor.getSelection();
        editor.deleteSelection();
    }
}
