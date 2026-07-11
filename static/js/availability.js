// =========================================
// MediAI Availability JavaScript
// =========================================

// Search Medicine

const search = document.getElementById("searchMedicine");

if (search) {

    search.addEventListener("keyup", function () {

        const value = this.value.toLowerCase();

        const rows = document.querySelectorAll("tbody tr");

        rows.forEach((row) => {

            row.style.display =
                row.innerText.toLowerCase().includes(value)
                ? ""
                : "none";

        });

    });

}

// =========================================
// Card Animation

const cards = document.querySelectorAll(".summary-card, .pharmacy-card");

cards.forEach((card, index) => {

    card.style.animationDelay = `${index * 0.15}s`;

});

// =========================================
// Page Load

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});

// =========================================
// Highlight Available Status

document.querySelectorAll(".status").forEach((status) => {

    const text = status.innerText.trim().toLowerCase();

    if (text.includes("unavailable")) {
         status.style.background = "#fee2e2";
         status.style.color = "#dc2626";
    } else if (text.includes("available")) {

        status.style.background = "#dcfce7";
        status.style.color = "#047857";
        } 
    }

);