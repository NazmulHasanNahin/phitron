var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];
var uniqueNumbers = [];

for (var i = 0; i < numbers.length; i++) {
    var isDuplicate = false;
    for (var j = 0; j < uniqueNumbers.length; j++) {
        if (numbers[i] === uniqueNumbers[j]) {
            isDuplicate = true;
            break;
        }
    }
    if (!isDuplicate) {
        uniqueNumbers.push(numbers[i]);
    }
}

console.log(uniqueNumbers);
