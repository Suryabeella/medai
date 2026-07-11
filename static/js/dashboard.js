// =====================================
// MediAI Dashboard JavaScript
// =====================================

// Card Hover Animation

const cards = document.querySelectorAll(".card");

cards.forEach((card) => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-10px)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px)";

    });

});

// =====================================
// Welcome Animation

window.addEventListener("load", () => {

    document.querySelector(".welcome-card").style.opacity = "1";

});

// =====================================
// Notification Bell

const bell = document.querySelector(".profile i");

if (bell) {

    bell.addEventListener("click", () => {

        alert("No new notifications.");

    });

}

const profileBtn = document.getElementById("profileBtn");
const profileDropdown = document.getElementById("profileDropdown");

if (profileBtn && profileDropdown) {
    profileBtn.addEventListener("click", function () {
        profileDropdown.classList.toggle("show");
    });

    document.addEventListener("click", function (e) {
        if (!profileBtn.contains(e.target) && !profileDropdown.contains(e.target)) {
            profileDropdown.classList.remove("show");
        }
    });
     profileDropdown.addEventListener("click", function (e) {
        e.stopPropagation();
    });

}
