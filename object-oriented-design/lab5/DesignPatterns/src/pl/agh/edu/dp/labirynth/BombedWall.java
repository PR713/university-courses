package pl.agh.edu.dp.labirynth;

public class BombedWall extends Wall {
    private boolean exploded;

    public BombedWall() {
        this.exploded = false;
    }

    public void explode() {
        this.exploded = true;
        System.out.println("Ściana wybuchła! Uważaj!");
    }

    @Override
    public void Enter() {
        if (exploded) {
            System.out.println("Przechodzisz przez wybuchniętą ścianę");
        } else {
            System.out.println("Uderzasz w ścianę z bombą. Może wybuchnąć!");
        }
    }
}