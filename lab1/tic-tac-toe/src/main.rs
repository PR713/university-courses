use std::io;

fn main() {
    let mut user_input = String::new();
    let mut player1_sign;
    let player2_sign;
    let mut board = [[' '; 3]; 3];
    let mut winner : char = ' ';

    loop{
        println!("Type your command:");
        user_input.clear();
        let _ = io::stdin().read_line(&mut user_input); // get string from the user input
        player1_sign = user_input.chars().nth(0).unwrap(); // get the first char from the given string

        if player1_sign == 'O' || player1_sign == 'X' {
            break;
        }
    }

    println!("\n");

    if player1_sign == 'X' {
        player2_sign = 'O';
    } else {
        player2_sign = 'X';
    }

    let mut num_of_empty_cells : i32 = 9;

    while winner ==  ' ' && num_of_empty_cells > 0 {
        print_board(&board);

        make_move(1, player1_sign, &mut board);
        winner = check_winner(&board);
        num_of_empty_cells -= 1;

        if winner != ' ' || num_of_empty_cells == 0 {
            end_game(1, winner);
            break;
        }

        print_board(&board);

        make_move(2, player2_sign, &mut board);
        winner = check_winner(&board);
        num_of_empty_cells -= 1;

        if winner != ' ' || num_of_empty_cells == 0 {
            end_game(2, winner);
            break;
        }
    }

    print_board(&board);
}


fn print_board(board: &[[char; 3]; 3]) {

    for i in 0..3 {
        println!("  {}  |  {}  |  {}  ", board[i][0], board[i][1], board[i][2]);
        if i < 2 {
            println!("-----------------");
        }
    }
}


fn check_winner(&board : &[[char; 3]; 3]) -> char {
    for i in  0..3 {
        if board[i][0] != ' ' && board[i][0] == board[i][1] && board[i][1] == board[i][2] {
            return board[i][0];
        }

        if board[0][i] != ' ' && board[0][i] == board[1][i] && board[1][i] == board[2][i] {
            return board[0][i];
        }
    }

    if board[0][0] != ' ' && board[0][0] == board[1][1] && board[1][1] == board[2][2] {
        return board[0][0];
    }
    if board[0][2] != ' ' && board[0][2] == board[1][1] && board[1][1] == board[2][0] {
        return board[0][2];
    }

    ' '
}

fn check_position(n : u32, board : &[[char; 3]; 3]) -> bool {
    let x = ((n - 1) / 3) as usize;
    let y = ((n - 1) % 3) as usize;
    if board[x][y] == ' ' {
        return true;
    }
    false
}


fn make_move(num : i32, sign : char, board : &mut [[char; 3]; 3])  {
    println!("Gracz {} ({}), Twój ruch (wprowadź numer pola od 1 do 9): ", num, sign);
    let mut user_input = String::new();
    let mut cmd : char;
    loop {
        user_input.clear();
        let _ = io::stdin().read_line(&mut user_input);
        cmd = user_input.chars().nth(0).unwrap();
        println!("\n");

        if let Some(cmd) = cmd.to_digit(10) {
            if cmd < 1 || cmd > 9 {
                println!("Zakres to od 1 do 9 !!!\n");
                print_board(&board);
            } else {
                if check_position(cmd, &board) {
                    board[ ((cmd - 1)/ 3) as usize ][((cmd - 1) % 3) as usize] = sign;
                    break;
                } else {
                    println!("Wybierz pole, które jeszcze nie jest zajęte!\n");
                }
            }
        } else {
            println!("Niepoprawny znak! Zakres to cyfra od 1 do 9 !!!\n");
            print_board(&board);
        }

    }
}


fn end_game(num : u32, winner : char) {
    if winner == ' ' {
        println!("Remis!");
    } else {
        println!("Wygrał gracz {} ({})!", num, winner);
    }
}