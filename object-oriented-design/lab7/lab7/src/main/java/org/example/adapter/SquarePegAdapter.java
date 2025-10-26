package org.example.adapter;

public class SquarePegAdapter extends RoundPeg{
    private SquarePeg squarePeg;

    public SquarePegAdapter(SquarePeg squarePeg){
        super(0);
        this.squarePeg = squarePeg;
    }

    @Override
    public int getRadius() {
        return Math.round((float)(this.squarePeg.getWidth() * Math.sqrt(2) / 2 ));
    }
}
