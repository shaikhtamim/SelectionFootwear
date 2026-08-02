document.addEventListener("DOMContentLoaded", function () {

    const popup = document.getElementById("visitorPopup");
    const form = document.getElementById("visitorForm");

    if (!popup || !form) return;

    // Already Verified
    if (localStorage.getItem("visitor_verified") === "true") {
        document.body.classList.remove("popup-open");
        popup.style.display = "none";
        return;
    }

    // Show Popup
    popup.style.display = "flex";
    document.body.classList.add("popup-open");

    // ===========================
    // Scroll Lock
    // ===========================

    function stopScroll(e) {
        e.preventDefault();
    }

    function stopKeys(e) {

        const keys = [
            "ArrowUp",
            "ArrowDown",
            "PageUp",
            "PageDown",
            "Home",
            "End",
            " "
        ];

        if (keys.includes(e.key)) {
            e.preventDefault();
        }

    }

    window.addEventListener("wheel", stopScroll, { passive: false });
    window.addEventListener("touchmove", stopScroll, { passive: false });
    window.addEventListener("keydown", stopKeys);

    // ===========================
    // Form Submit
    // ===========================

    form.addEventListener("submit", function (e) {

        e.preventDefault();

        const submitBtn = document.getElementById("submitBtn");

        submitBtn.disabled = true;
        submitBtn.innerHTML = "Please Wait...";

        const formData = new FormData(form);

        fetch(form.action, {

            method: "POST",

            body: formData,

            headers: {
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            }

        })
        .then(response => response.json())

        .then(data => {

            if (data.status === "success") {

                // Save User
                localStorage.setItem("visitor_verified", "true");

                // Hide Popup
                popup.style.display = "none";

                // Unlock Website
                document.body.classList.remove("popup-open");

                // Enable Scroll
                window.removeEventListener("wheel", stopScroll);
                window.removeEventListener("touchmove", stopScroll);
                window.removeEventListener("keydown", stopKeys);

            } else {

                submitBtn.disabled = false;
                submitBtn.innerHTML = "Continue";

                alert("Something went wrong.");

            }

        })

        .catch(error => {

            console.error(error);

            submitBtn.disabled = false;
            submitBtn.innerHTML = "Continue";

            alert("Server Error");

        });

    });

});