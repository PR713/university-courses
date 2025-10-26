package org.example.decorator;

import java.util.Base64;

public class EncryptionDecorator extends DataSourceDecorator {
    public EncryptionDecorator(DataSource source) {
        super(source);
    }


    public void writeData(String data) {
        String encryptedData = encrypt(data);
        System.out.println("Encrypting data...");
        super.writeData(encryptedData);
    }

    public String readData() {
        String encryptedData = super.readData();
        return decrypt(encryptedData);
    }

    private String encrypt(String data) {
        StringBuilder encrypted = new StringBuilder();
        for (char c : data.toCharArray()) {
            encrypted.append((char) (c ^ 42)); // XOR z kluczem 42
        }
        return Base64.getEncoder().encodeToString(encrypted.toString().getBytes());
    }

    private String decrypt(String encryptedData) {
        try {
            String decoded = new String(Base64.getDecoder().decode(encryptedData));
            StringBuilder decrypted = new StringBuilder();
            for (char c : decoded.toCharArray()) {
                decrypted.append((char) (c ^ 42)); // XOR z tym samym kluczem
            }
            return decrypted.toString();
        } catch (Exception e) {
            return encryptedData;
        }
    }
}
