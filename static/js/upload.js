// =========================================
// MediAI Upload JavaScript
// =========================================

const uploadInput = document.getElementById("prescription");
const preview = document.getElementById("preview");
const uploadArea = document.querySelector(".upload-area");
const uploadBtn = document.getElementById("uploadBtn");
const uploadForm = document.getElementById("uploadForm");
const analyzeBtn = document.getElementById("analyzeBtn");

// =========================================
// Choose Image Button
// =========================================

if (uploadBtn && uploadInput) {

    uploadBtn.addEventListener("click", function () {

        uploadInput.click();

    });

}

// =========================================
// Image Preview
// =========================================

if (uploadInput && preview) {

    uploadInput.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) return;

        // File Type Validation
        const allowed = ["image/png", "image/jpeg", "image/jpg"];

        if (!allowed.includes(file.type)) {

            alert("Please upload PNG, JPG or JPEG image.");

            this.value = "";

            preview.style.display = "none";

            return;

        }

        // File Size Validation (5MB)

        if (file.size > 5 * 1024 * 1024) {

            alert("Image size should be less than 5 MB.");

            this.value = "";

            preview.style.display = "none";

            return;

        }

        const reader = new FileReader();

        reader.onload = function (e) {

            preview.src = e.target.result;

            preview.style.display = "block";

        };

        reader.readAsDataURL(file);

    });

}

// =========================================
// Drag & Drop Support
// =========================================

if (uploadArea) {

    uploadArea.addEventListener("dragover", function (e) {

        e.preventDefault();

        uploadArea.style.background = "#dcfce7";

        uploadArea.style.borderColor = "#059669";

    });

    uploadArea.addEventListener("dragleave", function () {

        uploadArea.style.background = "#f9fffb";

        uploadArea.style.borderColor = "#10b981";

    });

    uploadArea.addEventListener("drop", function (e) {

        e.preventDefault();

        uploadArea.style.background = "#f9fffb";

        uploadArea.style.borderColor = "#10b981";

        const files = e.dataTransfer.files;

        if (files.length > 0) {

            uploadInput.files = files;

            uploadInput.dispatchEvent(new Event("change"));

        }

    });

}

// =========================================
// Upload Form Submit
// =========================================

if (uploadForm) {

    uploadForm.addEventListener("submit", function (e) {

        if (!uploadInput.files.length) {

            e.preventDefault();

            alert("Please select a prescription image.");

            return;

        }

        analyzeBtn.innerHTML =
            '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

        analyzeBtn.disabled = true;

    });

}

// =========================================
// Page Load Animation
// =========================================

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});