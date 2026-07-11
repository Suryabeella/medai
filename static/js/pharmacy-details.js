// =========================================
// MediAI Pharmacy Details JavaScript
// =========================================

// Page Load Animation

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});

// Download Report Placeholder

function downloadReport() {

    alert("PDF download feature will be added in the next version.");

}

// Buy Button Animation

const buyBtn = document.querySelector(".buy-btn");

if (buyBtn) {

    buyBtn.addEventListener("click", () => {

        buyBtn.innerHTML =
            '<i class="fa-solid fa-spinner fa-spin"></i> Opening...';

    });

}
