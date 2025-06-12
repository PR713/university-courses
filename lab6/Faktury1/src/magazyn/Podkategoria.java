package magazyn;

import java.util.ArrayList;
import java.util.List;

public class Podkategoria extends CategoryComponent {
    private List<CategoryComponent> children;

    public Podkategoria(String name) {
        super(name);
        this.children = new ArrayList<>();
    }

    @Override
    public void add(CategoryComponent component) {
        children.add(component);
    }

    @Override
    public void remove(CategoryComponent component) {
        children.remove(component);
    }

    @Override
    public void print(String indent) {
        System.out.println(indent + "Podkategoria: " + name);
        for (CategoryComponent component : children) {
            component.print(indent + "  ");
        }
    }
}