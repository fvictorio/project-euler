use num_bigint::BigUint;
use std::collections::BTreeSet;
use std::ops::{Add, Div, Mul};

fn get_sum_of_digits(x: &BigUint) -> BigUint {
    let mut result = BigUint::from(0u32);

    let mut x = x.clone();

    while x > BigUint::from(0u32) {
        result += x.modpow(&BigUint::from(1u32), &BigUint::from(10u32));
        x = x.div(&BigUint::from(10u32));
    }

    return result;
}

fn is_interesting(x: &BigUint) -> bool {
    let sum_of_digits = get_sum_of_digits(&x);

    let mut power = sum_of_digits.clone();

    if power == BigUint::from(1u32) {
        return false;
    }

    while power < *x {
        power = power.mul(&sum_of_digits);
        if power == *x {
            return true;
        }
    }

    return false;
}

fn main() {
    let one: BigUint = BigUint::from(1u32);

    let mut base = one.clone();
    let mut exponent = 1u32;

    let mut interesting_numbers: BTreeSet<BigUint> = BTreeSet::new();

    while base.le(&BigUint::from(400u32)) {
        while exponent <= 200 {
            let x = base.pow(exponent);

            if is_interesting(&x) {
                interesting_numbers.insert(x);
            }

            exponent = exponent.add(1u32);
        }

        base = base.add(1u32);
        exponent = 1;
    }

    for (i, x) in interesting_numbers.iter().enumerate() {
        println!("{}: {}", i + 1, x);
    }
}
