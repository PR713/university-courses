package org.example.command;

class CopyCommand extends Command {

    public CopyCommand(Application app, Editor editor) {
        super(app, editor);
    }

    @Override
    public void execute() {
        app.clipboard = editor.getSelection();
    }
}
