// =========================================
// MediAI Register Page JavaScript
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
// Password Strength
// =========================================

const strengthFill = document.getElementById("strengthFill");
const strengthText = document.getElementById("strengthText");

if (password) {

    password.addEventListener("keyup", function () {

        let value = password.value;

        let strength = 0;

        if (value.length >= 8)
            strength++;

        if (/[A-Z]/.test(value))
            strength++;

        if (/[0-9]/.test(value))
            strength++;

        if (/[^A-Za-z0-9]/.test(value))
            strength++;

        switch (strength) {

            case 1:

                strengthFill.style.width = "25%";
                strengthFill.style.background = "#ef4444";
                strengthText.innerHTML = "Weak Password";
                break;

            case 2:

                strengthFill.style.width = "50%";
                strengthFill.style.background = "#f59e0b";
                strengthText.innerHTML = "Medium Password";
                break;

            case 3:

                strengthFill.style.width = "75%";
                strengthFill.style.background = "#3b82f6";
                strengthText.innerHTML = "Strong Password";
                break;

            case 4:

                strengthFill.style.width = "100%";
                strengthFill.style.background = "#10b981";
                strengthText.innerHTML = "Very Strong Password";
                break;

            default:

                strengthFill.style.width = "0%";
                strengthText.innerHTML = "Password Strength";

        }

    });

}

// =========================================
// Register Form Validation
// =========================================

const registerForm = document.getElementById("registerForm");

if (registerForm) {

    registerForm.addEventListener("submit", function (e) {

        const name =
            document.getElementById("name").value.trim();

        const email =
            document.getElementById("email").value.trim();

        const pass =
            document.getElementById("password").value.trim();

        const confirm =
            document.getElementById("confirmPassword").value.trim();

        if (name === "") {

            e.preventDefault();

            alert("Please enter your name.");

            return;

        }

        if (!validateEmail(email)) {

            e.preventDefault();

            alert("Please enter a valid email.");

            return;

        }

        if (pass.length < 8) {

            e.preventDefault();

            alert("Password must contain at least 8 characters.");

            return;

        }

        if (pass !== confirm) {

            e.preventDefault();

            alert("Passwords do not match.");

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
// Input Animation
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
// Loading Effect
// =========================================

const button = document.querySelector("button");

if (button && registerForm) {

    registerForm.addEventListener("submit", function () {

        button.innerHTML =
            '<i class="fa-solid fa-spinner fa-spin"></i> Creating Account...';

        button.disabled = true;

    });

}

// =========================================
// Fade Effect
// =========================================

window.onload = function () {

    document.body.style.opacity = "1";

};