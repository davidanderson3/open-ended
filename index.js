async function loadTable() {
    const response = await fetch('table.json');
    const data = await response.json();

    const columns = ["Rank", "Neighborhood", "Location", "New Score (/27)", "Notes"];

    const table = document.getElementById('scores');
    const thead = table.createTHead();
    const headerRow = thead.insertRow();
    columns.forEach(col => {
        const th = document.createElement('th');
        th.textContent = col;
        th.addEventListener('click', () => sortTable(col));
        headerRow.appendChild(th);
    });

    const tbody = table.createTBody();
    data.forEach(row => {
        const tr = tbody.insertRow();
        columns.forEach(col => {
            const cell = tr.insertCell();
            cell.textContent = row[col];
        });
    });
}

function sortTable(column) {
    const table = document.getElementById('scores');
    const rows = Array.from(table.tBodies[0].rows);
    const index = Array.from(table.tHead.rows[0].cells).findIndex(th => th.textContent === column);

    const asc = table.getAttribute('data-sort') !== column;
    rows.sort((a, b) => {
        const aText = a.cells[index].textContent;
        const bText = b.cells[index].textContent;
        if (!isNaN(parseFloat(aText)) && !isNaN(parseFloat(bText))) {
            return asc ? parseFloat(aText) - parseFloat(bText) : parseFloat(bText) - parseFloat(aText);
        }
        return asc ? aText.localeCompare(bText) : bText.localeCompare(aText);
    });

    table.tBodies[0].innerHTML = '';
    rows.forEach(row => table.tBodies[0].appendChild(row));
    table.setAttribute('data-sort', asc ? column : '');
}

window.addEventListener('DOMContentLoaded', loadTable);

