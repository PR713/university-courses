use rand::Rng;
//&str static reference to a non-modifiable string in program static memory
//String modifiable string, on heap
fn main() {
    let charsets = vec![ //wektor :) zamiast tabeli o stałym rozmiarze
        "lowercase".to_string(),
        //"uppercase".to_string(),
        //"digits".to_string(),
        "special".to_string(),
    ];

    for _ in 0..5 {
        let password = generate_password(12, &charsets);
        println!("{}", password);
    }

}


fn generate_password(length: u32, charsets: &[String]) -> String {
    let mut rng = rand::rng();

    let lowercase = "abcdefghijklmnopqrstuvwxyz";
    let uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let digits = "0123456789";
    let special = "!@#$%^&*()_+-=[]{}|;:,.<>?";

    let mut selected_chars = String::new();
    let mut has_valid_charset = false;

    if !charsets.is_empty() {
        for charset in charsets {
            match charset.as_str() {
                "lowercase" => {
                    selected_chars.push_str(lowercase);
                    has_valid_charset = true;
                }
                "uppercase" => {
                    selected_chars.push_str(uppercase);
                    has_valid_charset = true;
                }
                "digits" => {
                    selected_chars.push_str(digits);
                    has_valid_charset = true;
                }
                "special" => {
                    selected_chars.push_str(special);
                    has_valid_charset = true;
                }
                _ => continue,
            }
        }
    }

    // if no valid charsets were provided or charsets is empty
    if !has_valid_charset {
        selected_chars = format!("{}{}{}{}", lowercase, uppercase, digits, special);
    }

    let mut output = String::new();

    for _ in 0..length {
        let rand_number = rng.random_range(0..selected_chars.len());
        output.push(selected_chars.chars().nth(rand_number).unwrap());
    }

    output
}





#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_password_with_selected_charsets() {
        let test_cases = vec![
            (vec!["lowercase".to_string()], "abcdefghijklmnopqrstuvwxyz"),
            (vec!["uppercase".to_string()], "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            (vec!["digits".to_string()], "0123456789"),
            (vec!["special".to_string()], "!@#$%^&*()_+-=[]{}|;:,.<>?"),
            (vec!["lowercase".to_string(), "uppercase".to_string()], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        ];

        for (charsets, allowed_chars) in test_cases {
            let password = generate_password(20, &charsets);
            assert!(!password.is_empty(), "Password should not be empty");
            //assert! panic'uje gdy warunek jest false, taki assertTrue
            assert_eq!(password.len(), 20, "Password should have correct length");

            for c in password.chars() {
                assert!(
                    allowed_chars.contains(c),
                    "Password contains invalid character '{}'. Allowed chars: {}",
                    c,
                    allowed_chars
                );
            }
        }
    }



    #[test]
    fn test_generate_password_with_empty_or_invalid_charsets() {

        let password1 = generate_password(10, &[]);
        let password2 = generate_password(10, &["invalid".to_string()]);

        assert!(!password1.is_empty(), "Password should not be empty");
        assert!(!password2.is_empty(), "Password should not be empty");


        let all_chars = format!(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{{}}|;:,.<>?"
        );

        for c in password1.chars() {
            assert!(all_chars.contains(c));
        }

        for c in password2.chars() {
            assert!(all_chars.contains(c));
        }

    }
}