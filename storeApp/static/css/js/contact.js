document.querySelector(".contact-form").addEventListener("submit", function () {
    const btn = document.getElementById("submitBtn");

    btn.innerHTML = "Sending...";
    btn.disabled = true;
});
