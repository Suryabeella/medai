// =========================================
// MediAI Analysis JavaScript
// =========================================

// Hide Loader (if available)

window.addEventListener("load", () => {

    const loader = document.getElementById("loader");

    if (loader) {

        loader.style.display = "none";

    }

});

// =========================================
// Smooth Scroll to AI Cards

const aiCards = document.querySelectorAll(".ai-card");

aiCards.forEach((card, index) => {

    card.style.animationDelay = `${index * 0.2}s`;

});

// =========================================
// Print Report

function printReport() {

    window.print();

}

// =========================================
// Download Report (Placeholder)

function downloadReport() {

    alert("PDF Download feature will be added.");

}