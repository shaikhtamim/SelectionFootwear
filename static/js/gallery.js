document.addEventListener("DOMContentLoaded", function () {

    const images = document.querySelectorAll(".gallery-popup-image");

    const popup = document.getElementById("galleryPopup");
    const popupImage = document.getElementById("popupImage");

    const closeBtn = document.querySelector(".popup-close");
    const nextBtn = document.querySelector(".popup-next");
    const prevBtn = document.querySelector(".popup-prev");

    const thumbsContainer = document.getElementById("popupThumbs");

    let currentIndex = 0;

    // Create thumbnails automatically
    images.forEach((img, index) => {

        const thumb = document.createElement("img");

        thumb.src = img.src;

        thumb.classList.add("thumb-image");

        thumb.addEventListener("click", function () {

            showImage(index);

        });

        thumbsContainer.appendChild(thumb);

    });

    const thumbs = thumbsContainer.querySelectorAll(".thumb-image");

    function updateActiveThumb() {

        thumbs.forEach(t => t.classList.remove("active"));

        thumbs[currentIndex].classList.add("active");

    }

    function showImage(index) {

        currentIndex = index;

        popupImage.src = images[index].src;

        popup.classList.add("active");

        updateActiveThumb();

    }

    // Open popup
    images.forEach((img, index) => {

        img.addEventListener("click", function () {

            showImage(index);

        });

    });

    // Next
    nextBtn.addEventListener("click", function () {

        currentIndex++;

        if (currentIndex >= images.length) {

            currentIndex = 0;

        }

        showImage(currentIndex);

    });

    // Previous
    prevBtn.addEventListener("click", function () {

        currentIndex--;

        if (currentIndex < 0) {

            currentIndex = images.length - 1;

        }

        showImage(currentIndex);

    });

    // Close
    closeBtn.addEventListener("click", function () {

        popup.classList.remove("active");

    });

    // Click outside image
    popup.addEventListener("click", function (e) {

        if (e.target === popup) {

            popup.classList.remove("active");

        }

    });

    // Keyboard controls
    document.addEventListener("keydown", function (e) {

        if (!popup.classList.contains("active")) return;

        if (e.key === "Escape") {

            popup.classList.remove("active");

        }

        if (e.key === "ArrowRight") {

            nextBtn.click();

        }

        if (e.key === "ArrowLeft") {

            prevBtn.click();

        }

    });

});
