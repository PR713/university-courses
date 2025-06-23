package org.example.decorator;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Base64;
import java.util.zip.DeflaterOutputStream;
import java.util.zip.InflaterInputStream;

public class CompressionDecorator extends DataSourceDecorator{
    public CompressionDecorator(DataSource source) {
        super(source);
    }

    @Override
    public void writeData(String data) {
        String compressedData = compress(data);
        System.out.println("Compressing data...");
        super.writeData(compressedData);
    }

    @Override
    public String readData() {
        String compressedData = super.readData();
        System.out.println("Decompressing data...");
        return decompress(compressedData);
    }

    private String compress(String data) {
        try {
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            try (DeflaterOutputStream dos = new DeflaterOutputStream(baos)) {
                dos.write(data.getBytes());
            }
            return Base64.getEncoder().encodeToString(baos.toByteArray());
        } catch (IOException e) {
            return data;
        }
    }

    private String decompress(String compressedData) {
        try {
            byte[] compressed = Base64.getDecoder().decode(compressedData);
            ByteArrayInputStream bais = new ByteArrayInputStream(compressed);
            try (InflaterInputStream iis = new InflaterInputStream(bais)) {
                return new String(iis.readAllBytes());
            }
        } catch (Exception e) {
            return compressedData;
        }
    }
}
