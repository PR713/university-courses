package magazyn;

public abstract class CategoryComponent {
    protected String name;

    public CategoryComponent(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public abstract void print(String indent);

    public void add(CategoryComponent component) {
        throw new UnsupportedOperationException();
    }

    public void remove(CategoryComponent component) {
        throw new UnsupportedOperationException();
    }

    public void addTowar(Towar towar) {
        throw new UnsupportedOperationException();
    }
}