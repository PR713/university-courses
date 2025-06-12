package org.example.decorator;

public interface DataSource {
    void writeData(String data);
    String readData();
}
