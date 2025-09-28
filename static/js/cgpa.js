const gradePoints = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
    "P": 4,
    "F": 0
};
let sgpa = 0;   // use let instead of const

function generateInputs() {
    const numSubjects = parseInt(document.getElementById("numberOfSubject").value);
    const container = document.getElementById("subjectInputs");
    container.innerHTML = ""; // clear previous inputs

    if (!numSubjects || numSubjects <= 0) {
        document.getElementById('result').innerText = 'Please enter a valid number of subjects (>=1).';
        return;
    }
    for (let i = 1; i <= numSubjects; i++) {
        const div = document.createElement("div");
        div.classList.add("subject");

        div.innerHTML = `
            <label>Subject ${i} Grade:</label>
            <select name="grade" id="grade${i}">
                <option value="O">O</option>
                <option value="A+">A+</option>
                <option value="A">A</option>
                <option value="B+">B+</option>
                <option value="B">B</option>
                <option value="C">C</option>
                <option value="P">P</option>
                <option value="F">F</option>
            </select>

            <label>Credits:</label>
            <input type="number" name="credit" id="credits${i}" required placeholder="eg. 3" min="1">
        `;
        container.appendChild(div);
    }
    document.getElementById("calculateSGPA").style.display = "block";
    document.getElementById("cgpaCalculator").style.display = "none";
    document.getElementById("choose").style.display = "none";
    document.getElementById("resetButton").style.display = "block";
    document.getElementById("cgparesult").innerText = "";
    document.getElementById("result").innerText = "";
}

document.getElementById("sgpaForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const grades = document.getElementsByName("grade");
    const credits = document.getElementsByName("credit");

    let totalCredits = 0;
    let weightedSum = 0;

    for (let i = 0; i < grades.length; i++) {
        const grade = grades[i].value;
        const credit = parseFloat(credits[i].value);

        if (grade && credit) {
            weightedSum += gradePoints[grade] * credit;
            totalCredits += credit;
        }
    }

    if (totalCredits === 0) {
        document.getElementById("result").innerText = "Please enter valid grades and credits!";
        return;
    }

    sgpa = (weightedSum / totalCredits).toFixed(2); // reassign works now
    document.getElementById("result").innerText = "Your SGPA is: " + sgpa;

    document.getElementById("choose").style.display = "block";
});

function calculateCGPA() {

    const currcgpa = parseFloat(document.getElementById("currentCGPA").value);
    if (isNaN(currcgpa) || isNaN(sgpa) || sgpa === 0) {
        document.getElementById("cgparesult").innerText = "Please calculate SGPA first and enter current CGPA.";
        return;
    }
    const cgpa = ((currcgpa + parseFloat(sgpa)) / 2).toFixed(2);
    document.getElementById("cgparesult").innerText = `Your CGPA is: ${cgpa}`;

    document.getElementById("resetButton").style.display = "block";
    
}

document.getElementById("yes").addEventListener("click", function () {
    document.getElementById("cgpaCalculator").style.display = "block";
    document.getElementById("choose").style.display = "none"; // hide choose after Yes
});

document.getElementById("no").addEventListener("click", function () {
    document.getElementById("choose").style.display = "none";
    document.getElementById("cgparesult").innerText += "\nCGPA calculation skipped.";
});



