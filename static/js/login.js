// =========================================
// MediAI Login Page JavaScript
// =========================================

// Show / Hide Password

const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

if (togglePassword && password) {
    togglePassword.addEventListener("click", function () {

        if (password.type === "password") {

            password.type = "text";

            this.classList.remove("fa-eye");
            this.classList.add("fa-eye-slash");

        } else {

            password.type = "password";

            this.classList.remove("fa-eye-slash");
            this.classList.add("fa-eye");

        }

    });
}

// =========================================
// Login Form Validation
// =========================================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", function (e) {

        const email = document
            .getElementById("email")
            .value
            .trim();

        const pass = document
            .getElementById("password")
            .value
            .trim();

        if (email === "") {

            e.preventDefault();

            alert("Please enter your email.");

            return;
        }

        if (pass === "") {

            e.preventDefault();

            alert("Please enter your password.");

            return;
        }

        if (!validateEmail(email)) {

            e.preventDefault();

            alert("Please enter a valid email address.");

            return;
        }

    });

}

// =========================================
// Email Validation
// =========================================

function validateEmail(email) {

    const pattern =
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    return pattern.test(email);

}

// =========================================
// Input Focus Animation
// =========================================

const inputs = document.querySelectorAll(".input-box input");

inputs.forEach((input) => {

    input.addEventListener("focus", function () {

        this.parentElement.classList.add("active");

    });

    input.addEventListener("blur", function () {

        if (this.value === "") {

            this.parentElement.classList.remove("active");

        }

    });

});

// =========================================
// Button Loading Effect
// =========================================

const button = document.querySelector("button");

if (button && loginForm) {

    loginForm.addEventListener("submit", function () {

        button.innerHTML =
            '<i class="fa-solid fa-spinner fa-spin"></i> Logging In...';

        button.disabled = true;

    });

}

// =========================================
// Fade Animation
// =========================================

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});