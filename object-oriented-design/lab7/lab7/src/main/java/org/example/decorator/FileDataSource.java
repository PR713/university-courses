package org.example.decorator;

import java.io.*;

public class FileDataSource implements DataSource {
    private File filename;


    public FileDataSource(File filename) {
        this.filename = filename;
    }

    @Override
    public void writeData(String data) {
        try (FileWriter writer = new FileWriter(filename)) {
            writer.write(data);
            System.out.println("Writing data to file: " + filename);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }

    @Override
    public String readData() {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            StringBuilder result = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                result.append(line).append("\n");
            }
            System.out.println("Reading data from file: " + filename);
            return result.toString().trim();
        } catch (IOException e) {
            System.err.println("Error reading from file: " + e.getMessage());
            return "";
        }
    }
}
