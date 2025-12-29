/* ======================
   DOM Ready Helper
====================== */
document.addEventListener("DOMContentLoaded", () => {
    initPasswordToggle();
    autoHideFlashMessages();
    initFormValidation();
});

/* ======================
   Password Show / Hide
====================== */
function initPasswordToggle() {
    const toggles = document.querySelectorAll("[data-toggle-password]");

    toggles.forEach(toggle => {
        toggle.addEventListener("click", () => {
            const inputId = toggle.getAttribute("data-toggle-password");
            const input = document.getElementById(inputId);

            if (!input) return;

            if (input.type === "password") {
                input.type = "text";
                toggle.textContent = "Hide";
            } else {
                input.type = "password";
                toggle.textContent = "Show";
            }
        });
    });
}

/* ======================
   Auto-hide Flash Messages
====================== */
function autoHideFlashMessages() {
    const flashes = document.querySelectorAll(".flash");

    if (!flashes.length) return;

    setTimeout(() => {
        flashes.forEach(flash => {
            flash.style.opacity = "0";
            flash.style.transition = "opacity 0.5s ease";

            setTimeout(() => flash.remove(), 500);
        });
    }, 3000);
}

/* ======================
   Basic Client-side Validation
====================== */
function initFormValidation() {
    const forms = document.querySelectorAll("form[data-validate]");

    forms.forEach(form => {
        form.addEventListener("submit", event => {
            const requiredFields = form.querySelectorAll("[required]");
            let valid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add("input-error");
                    valid = false;
                } else {
                    field.classList.remove("input-error");
                }
            });

            if (!valid) {
                event.preventDefault();
                alert("Please fill in all required fields.");
            }
        });
    });
}
