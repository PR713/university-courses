package pl.agh.edu.dp.labirynth;

public class BombedRoom extends Room {
    private boolean hasBomb;
    private int timer;
    private boolean isBombActive;

    public BombedRoom(int number) {
        super(number);
        this.hasBomb = true;
        this.timer = 15; // 15 sekund na ucieczkę
    }

    public void activateBomb() {
        if (hasBomb) {
            System.out.println("Bomba aktywowana! Masz " + timer + " sekund na ucieczkę!");
            isBombActive = true;
        }
    }

    @Override
    public void Enter() {
        super.Enter();
        if (hasBomb) {
            System.out.println("UWAGA! W pokoju jest bomba!");
        }
    }

    public void checkBomb() {
        if (hasBomb) {
            timer--;
            System.out.println("Bomba wybuchnie za " + timer + " sekund!");
            if (timer <= 0) {
                System.out.println("BOOM! Zginąłeś!");
                System.exit(0);
            }
        }
    }


    public boolean isBombActive() {
        return isBombActive;
    }
}