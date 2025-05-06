#[derive(Debug)]
enum ChessmanType {
    Pawn,
    Knight,
    Bishop,
    Rook,
    Queen,
    King,
}

#[derive(Debug)]
struct Position {
    x: u8,
    y: u8,
}

impl Position {
    fn is_vaild(&self) -> bool{
        self.x >= 1 && self.x <= 8 && self.y >= 1 && self.y <= 8
    }
}

#[derive(Debug)]
enum Color {
    White,
    Black,
}

#[derive(Debug)]
struct Chessman {
    kind: ChessmanType,
    color: Color,
    position: Position,
}

impl Chessman {
    fn mv(&mut self, new_position: Position) -> bool {
        if !new_position.is_vaild() {
            return false;
        }

        let x_diff = (new_position.x as i8 - self.position.x as i8).abs();
        let y_diff = (new_position.y as i8 - self.position.y as i8).abs();

        let direction = match self.color {
            Color::White => 1,
            Color::Black => -1,
        };

        let valid = match self.kind {
            ChessmanType::Pawn => {
                x_diff == 0 && ((new_position.y as i8 - self.position.y as i8) == direction)
            }
            ChessmanType::Knight => {}
            ChessmanType::Bishop => {}
            ChessmanType::Rook => {}
            ChessmanType::Queen => {}
            ChessmanType::King => {
            }
        }

        false
    }
}

fn main() {}