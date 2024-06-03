// const num = 20;
// for (let i = 2; i <= num; i++) {
//     if (true) {
//         console.log(i);
//     }
// }

const all_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

const evenFinder = (numbers) => {
    let evens = [];
    let odd=[];
    for (let i = 2; i < numbers.length; i++) {
        if (numbers[i] % 2 == 0) {
            evens.push(numbers[i]);
        }
        else{
            odd.push(numbers[i]);
        }
    }
    return {evens,odd};
    // return odd;
}

const result = evenFinder(all_num)
console.log(result);



// problem statement
// 1 theke 20 prjnto number er theke odd even ber kora