function generateReportFunction() {
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;
    const option = document.querySelector("input[name='option']:checked")?.value;

    if(!startDate || !endDate || !option) {
        alert("Please fill all fields");
        return;
    }

    fetch('/get_report',{
        method: "POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({startDate, endDate, option})
    })
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("tableWrapper");
        const oldTable = document.getElementById("reportTable");

        if(oldTable) 
            oldTable.remove();

        const table = document.createElement("table");
        table.id="reportTable";
        
        let headers = [];
        if(option === "todo"){
            headers = ["ID", "Task", "Date", "Deadline", "Status"];
        }
        else if(option === "expense"){
            headers = ["ID", "Item", "Amount", "Date", "Category"];
        }

        const thead = table.createTHead();
        const headerRow = thead.insertRow();
        headers.forEach(h =>{
            const th = document.createElement("th");
            th.innerText = h;
            headerRow.appendChild(th);
        });

        const tbody = table.createTBody();
        data.forEach(row => {
            const tr = tbody.insertRow();
            row.forEach(cell => {
                const td = tr.insertCell();
                td.innerText = cell;
                tr.appendChild(td);
            });
        });
        container.appendChild(table);
    })
    .catch(error => {
        console.error("Error generating report:", error);
        alert("Failed to generate report. Please try again.");
    });
}