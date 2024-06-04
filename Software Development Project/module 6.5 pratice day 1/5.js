function divisibleBy3And5() {
    let numbers = [];
    for (let i = 1; i <= 50; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            numbers.push(i);
        }
    }

    return numbers;
}


let divisibleNumbers = divisibleBy3And5();
console.log(divisibleNumbers);
