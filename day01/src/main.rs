use std::fs::read_to_string;
use regex::Regex;

fn main() {
    let digit: u32 = read_to_string("input").unwrap().lines().map(|line: &str| { find_digits(line) }).map(parse_digits).sum();
    println!("{}", digit)
}

fn find_digits(line: &str) -> (&str, &str) {
    let valid_digits = "[0-9]|one|two|three|four|five|six|seven|eight|nine";
    let re = Regex::new(r"^.*?([0-9]|one|two|three|four|five|six|seven|eight|nine).*([0-9]|one|two|three|four|five|six|seven|eight|nine).*?$").unwrap();
    if re.is_match(line) {
        let caps = re.captures(line).unwrap();
        return (caps.get(1).unwrap().as_str(), caps.get(2).unwrap().as_str())
    } else { // only one valid digit in line
        let re = Regex::new(r"([0-9]|one|two|three|four|five|six|seven|eight|nine)").unwrap();
        let caps = re.captures(line).unwrap();
        return (caps.get(1).unwrap().as_str(), caps.get(1).unwrap().as_str())
    }
}

fn parse_digit(digit: &str) -> u32 {
   match digit {
       "1" | "one" => 1,
       "2" | "two" => 2,
       "3" | "three" => 3,
       "4" | "four" => 4,
       "5" | "five" => 5,
       "6" | "six" => 6,
       "7" | "seven" => 7,
       "8" | "eight" => 8,
       "9" | "nine" => 9,
       &_ => 0,
   }
}

fn parse_digits(digits: (&str, &str)) -> u32 {
    parse_digit(digits.0) * 10 + parse_digit(digits.1)
}

#[test]
fn test_find_digits1() {
    let input1 = "1abc2";
    assert_eq!(find_digits(input1), ("1", "2"));
    let input2 = "pqr3stu8vwx";
    assert_eq!(find_digits(input2), ("3", "8"));
    let input3 = "a1b2c3d4e5f";
    assert_eq!(find_digits(input3), ("1","5"));
    let input4 = "treb7uchet";
    assert_eq!(find_digits(input4), ("7","7"));
}

#[test]
fn test_find_digits2_and_parse() {
    let input5 = "two1nine";
    assert_eq!(parse_digits(find_digits(input5)), 29);
    let input6 = "eightwothree";
    assert_eq!(parse_digits(find_digits(input6)), 83);
    let input7 = "abcone2threexyz";
    assert_eq!(parse_digits(find_digits(input7)), 13);
    let input8 = "xtwone3four";
    assert_eq!(parse_digits(find_digits(input8)), 24);
    let input9 = "4nineeightseven2";
    assert_eq!(parse_digits(find_digits(input9)), 42);
    let input10 = "zoneight234";
    assert_eq!(parse_digits(find_digits(input10)), 14);
    let input11 = "7pqrstsixteen";
    assert_eq!(parse_digits(find_digits(input11)), 76);
}
