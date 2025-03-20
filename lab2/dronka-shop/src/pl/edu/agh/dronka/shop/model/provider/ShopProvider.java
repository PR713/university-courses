package pl.edu.agh.dronka.shop.model.provider;

import java.io.IOException;
import java.util.*;

import pl.edu.agh.dronka.shop.model.Category;
import pl.edu.agh.dronka.shop.model.Index;
import pl.edu.agh.dronka.shop.model.Item;
import pl.edu.agh.dronka.shop.model.Shop;
import pl.edu.agh.dronka.shop.model.User;

public class ShopProvider {

    public static Shop getExampleShop() {
        Shop shop = new Shop();

        shop.addUser(getExampleUser());

        Index itemsIndex = new Index();

        for (Item item : getExampleItems()) {
            itemsIndex.addItem(item);
        }

        registerExampleCategories(itemsIndex);
        shop.setItemsIndex(itemsIndex);

        return shop;
    }

    public static User getExampleUser() {
        return new User("Jan", "Rejnor");
    }

    public static List<Item> getExampleItems() {
        List<Item> items = new ArrayList<>();

        CSVReader booksReader = new CSVReader("resources/books.csv");
        items.addAll(readItems(booksReader, Category.BOOKS));

        CSVReader electronicsReader = new CSVReader("resources/electronics.csv");
        items.addAll(readItems(electronicsReader, Category.ELECTRONICS));

        CSVReader foodReader = new CSVReader("resources/food.csv");
        items.addAll(readItems(foodReader, Category.FOOD));

        CSVReader musicReader = new CSVReader("resources/music.csv");
        items.addAll(readItems(musicReader, Category.MUSIC));

        CSVReader sportReader = new CSVReader("resources/sport.csv");
        items.addAll(readItems(sportReader, Category.SPORT));

        return items;
    }

    public static void registerExampleCategories(Index index) {
        for (Category category : Category.values()) {
            index.registerCategory(category);
        }
    }

    private static List<Item> readItems(CSVReader reader, Category category) {
        List<Item> items = new ArrayList<>();

        try {
            reader.parse();
            List<String[]> data = reader.getData();
            Map<Integer, String> header = reader.getHeader();

            for (String[] dataLine : data) {


                String name = dataLine[0];
                int price = Integer.parseInt(dataLine[1]);
                int quantity = Integer.parseInt(dataLine[2]);

                boolean isPolish = Boolean.parseBoolean(dataLine[3]);
                boolean isSecondhand = Boolean.parseBoolean(dataLine[4]);

                Map<String,Object> details = new HashMap<>();
                switch(category) {
                    case BOOKS: {
                        details.put(header.get(5),Integer.parseInt(dataLine[5]));
                        details.put(header.get(6),Boolean.parseBoolean(dataLine[6]));
                    }
                    case ELECTRONICS: {
                        details.put(header.get(5),Boolean.parseBoolean(dataLine[5]));
                        details.put(header.get(6),Boolean.parseBoolean(dataLine[6]));
                    }
                    case MUSIC: {
                        details.put();
                    }
                    case SPORT: {
                        break;
                    }
                    case FOOD: {
                        details.put(header.get(5), Date(dataLine[5]));
                    }

                }


                Item item = new Item(name, category, price, quantity);
                item.setPolish(isPolish);
                item.setSecondhand(isSecondhand);
                item.setDetails(details.toString());
                items.add(item);

            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        return items;
    }

}
