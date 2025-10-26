package org.example.command;

class Editor {
    public String text;
    private int selectionStart;
    private int selectionEnd;

    public Editor() {
        this.text = "";
        this.selectionStart = 0;
        this.selectionEnd = 0;
    }

    public Editor(String initialText) {
        this.text = initialText;
        this.selectionStart = 0;
        this.selectionEnd = 0;
    }

    public String getSelection() {
        if (selectionStart >= 0 && selectionEnd <= text.length() && selectionStart <= selectionEnd) {
            return text.substring(selectionStart, selectionEnd);
        }
        return "";
    }

    public void deleteSelection() {
        if (selectionStart >= 0 && selectionEnd <= text.length() && selectionStart <= selectionEnd) {
            text = text.substring(0, selectionStart) + text.substring(selectionEnd);
            selectionEnd = selectionStart;
        }
    }

    public void replaceSelection(String newText) {
        if (selectionStart >= 0 && selectionEnd <= text.length() && selectionStart <= selectionEnd) {
            text = text.substring(0, selectionStart) + newText + text.substring(selectionEnd);
            selectionEnd = selectionStart + newText.length();
        }
    }

    public void setSelection(int start, int end) {
        this.selectionStart = Math.max(0, start);
        this.selectionEnd = Math.min(text.length(), end);
    }

    public int getSelectionStart() {
        return selectionStart;
    }

    public void setSelectionStart(int start) {
        this.selectionStart = Math.max(0, Math.min(start, text.length()));
    }

    public int getSelectionEnd() {
        return selectionEnd;
    }

    public void setSelectionEnd(int end) {
        this.selectionEnd = Math.max(selectionStart, Math.min(end, text.length()));
    }
}