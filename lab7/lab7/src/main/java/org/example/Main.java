package org.example;

import org.example.adapter.RoundHole;
import org.example.adapter.RoundPeg;
import org.example.adapter.SquarePeg;
import org.example.adapter.SquarePegAdapter;

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




    }
}