// #[derive(Debug)]
// enum ChessmanType {
//     Pawn,
//     Knight,
//     Bishop,
//     Rook,
//     Queen,
//     King,
// }

#[derive(Debug)]
enum Chessman {
    Pawn { position: Position, color: Color },
    Knight { position: Position, color: Color },
    Bishop { position: Position, color: Color },
    Rook { position: Position, color: Color },
    Queen { position: Position, color: Color },
    King { position: Position, color: Color },
}

#[derive(Debug, Clone, Copy, PartialEq)]
struct Position {
    x: u8,
    y: u8,
}

impl Position {
    fn is_valid(&self) -> bool{
        self.x >= 1 && self.x <= 8 && self.y >= 1 && self.y <= 8
    }
}

#[derive(Debug, Clone, Copy, PartialEq)]
enum Color {
    White,
    Black,
}

// #[derive(Debug)]
// struct Chessman {
//     kind: ChessmanType,
//     color: Color,
//     position: Position,
// } //można też tak, wtedy testy należy zmodyfikować

impl Chessman {
    fn mv(&mut self, new_position: Position) -> bool {
        if !new_position.is_valid() {
            return false;
        }
        use Chessman::*;

        let position = match self {
            Pawn { position, .. }
            | Knight { position, .. }
            | Bishop { position, .. }
            | Rook { position, .. }
            | Queen { position, .. }
            | King { position, .. } => *position,
        }; //*position oznacza dereferencję bo działamy na referencji (pożyczce)
        //ale jako że ma Derive(Copy) to możemy przypisać zderefencjonowaną wartość
        //ona się wtedy kopiuje zamiast przenoszenia, shallow copy
        //Clone to deep copy .clone()

        let color = match self {
            Pawn { color, .. }
            | Knight { color, .. }
            | Bishop { color, .. }
            | Rook { color, .. }
            | Queen { color, .. }
            | King { color, .. } => *color,
        };

        let x_diff = (new_position.x as i8 - position.x as i8).abs();
        let y_diff = (new_position.y as i8 - position.y as i8).abs();

        let direction = match color {
            Color::White => 1,
            Color::Black => -1,
        };

        let valid = match self {
            Pawn {..} => {
                x_diff == 0 && ((new_position.y as i8 - position.y as i8) == direction)
            }
            Knight {..} => (x_diff == 2 && y_diff == 1 ) || (x_diff == 1 && y_diff == 2),
            Bishop {..} => x_diff == y_diff,
            Rook {..} => x_diff == 0 || y_diff == 0,
            Queen {..} => x_diff == y_diff || y_diff == 0 || x_diff == 0,
            King {..} => x_diff <= 1 && y_diff <= 1,
        };


        if valid {
            match self {
                Pawn { position, .. }
                | Knight { position, .. }
                | Bishop { position, .. }
                | Rook { position, .. }
                | Queen { position, .. }
                | King { position, .. } => *position = new_position,
            }
            true
        } else {
            false
        }
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pawn_move() {
        let mut pawn = Chessman::Pawn { position: Position { x: 1, y: 2 }, color: Color::White };
        assert_eq!(pawn.mv(Position { x: 1, y: 3 }), true);
        assert_eq!(pawn.mv(Position { x: 1, y: 5 }), false);
    }

    #[test]
    fn test_knight_move() {
        let mut knight = Chessman::Knight {
            position: Position { x: 2, y: 1 },
            color: Color::Black,
        };
        assert_eq!(knight.mv(Position { x: 3, y: 3 }), true);
        assert_eq!(knight.mv(Position { x: 4, y: 4 }), false);
    }

    #[test]
    fn test_bishop_move() {
        let mut bishop = Chessman::Bishop {
            position: Position { x: 4, y: 4 },
            color: Color::White,
        };
        assert_eq!(bishop.mv(Position { x: 6, y: 6 }), true);
        assert_eq!(bishop.mv(Position { x: 5, y: 6 }), false);
    }

    #[test]
    fn test_rook_move() {
        let mut rook = Chessman::Rook {
            position: Position { x: 1, y: 1 },
            color: Color::Black,
        };
        assert_eq!(rook.mv(Position { x: 1, y: 8 }), true);
        assert_eq!(rook.mv(Position { x: 2, y: 7 }), false);
    }

    #[test]
    fn test_queen_move() {
        let mut queen = Chessman::Queen {
            position: Position { x: 4, y: 4 },
            color: Color::White,
        };
        assert_eq!(queen.mv(Position { x: 7, y: 7 }), true); //już od (7,7)
        assert_eq!(queen.mv(Position { x: 4, y: 7 }), true);
        assert_eq!(queen.mv(Position { x: 5, y: 1 }), false);
    }

    #[test]
    fn test_king_move1() {
        let mut king = Chessman::King {
            position: Position { x: 5, y: 1 },
            color: Color::White,
        };
        assert_eq!(king.mv(Position { x: 6, y: 2 }), true);
    }

    #[test]
    fn test_king_move2() {
        let mut king = Chessman::King {
            position: Position { x: 5, y: 1 },
            color: Color::White,
        };
        assert_eq!(king.mv(Position { x: 7, y: 3 }), false);
    }
}