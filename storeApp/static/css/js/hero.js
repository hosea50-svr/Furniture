window.addEventListener("load", function () {
    const loader = document.getElementById("preloader");

    loader.style.opacity = "0";

    setTimeout(() => {
        loader.style.display = "none";
    }, 500);
});