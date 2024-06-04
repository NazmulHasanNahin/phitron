function calculateGrade(score) {
    if (score >= 0 && score < 40) {
        return "F";
    } else if (score >= 40 && score < 50) {
        return "C";
    } else if (score >= 50 && score < 60) {
        return "B";
    } else if (score >= 60 && score < 70) {
        return "A-";
    } else if (score >= 70 && score < 80) {
        return "A";
    } else if (score >= 80 && score <= 100) {
        return "A+";
    } else {
        return "Invalid score. Please provide a number between 0 and 100.";
    }
}

// example to run
const score = 75;
const grade = calculateGrade(score);
console.log(`The grade for ${score} is ${grade}.`);
