package org.example;

import org.example.adapter.RoundHole;
import org.example.adapter.RoundPeg;
import org.example.adapter.SquarePeg;
import org.example.adapter.SquarePegAdapter;
import org.example.decorator.CompressionDecorator;
import org.example.decorator.EncryptionDecorator;
import org.example.decorator.FileDataSource;

import java.io.File;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello, World!");
        RoundHole hole = new RoundHole(5);
        RoundPeg rpeg = new RoundPeg(5);

        hole.fits(rpeg); // true

        SquarePeg small_sqpeg = new SquarePeg(5);
        SquarePeg large_sqpeg = new SquarePeg(10);

        //hole.fits(small_sqpeg); // this won ’t compile ( incompatible types )
        SquarePegAdapter small_sqpeg_adapter = new SquarePegAdapter(small_sqpeg);
        SquarePegAdapter large_sqpeg_adapter = new SquarePegAdapter(large_sqpeg);
        if (hole.fits(small_sqpeg_adapter)) System.out.println("true"); // true
        if (!hole.fits(large_sqpeg_adapter)) System.out.println("false"); // false



        //

        File file = new File("./src/main/resources/text");

        FileDataSource fileDataSource = new FileDataSource(file);

        EncryptionDecorator eD = new EncryptionDecorator(fileDataSource);
        System.out.println("\n\n\n");
        String originalData = "tajny tekst";
        System.out.println("Original data: " + originalData);
        eD.writeData(originalData);

        String readData = eD.readData();
        System.out.println("Read data: " + readData);

        System.out.println("Data matches: " + originalData.equals(readData));


        CompressionDecorator cD = new CompressionDecorator(fileDataSource);
        System.out.println("\n\n\n");
        String originalData1 = "tajny tekst";
        System.out.println("Original data: " + originalData1);
        cD.writeData(originalData);

        String readData1 = cD.readData();
        System.out.println("Read data: " + readData1);

        System.out.println("Data matches: " + originalData1.equals(readData1));
    }
}