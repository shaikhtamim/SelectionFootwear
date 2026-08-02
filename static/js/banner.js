(function () {
    "use strict";

    function animateBanner() {
        var title = document.getElementById("banner-text");
        if (!title) return;

        title.style.visibility = "visible";
        title.style.opacity = "1";

        var originalHTML = title.innerHTML;
        var rawLines = originalHTML.split("<br>");
        title.innerHTML = "";

        var globalIndex = 0;

        rawLines.forEach(function (line) {
            var lineContainer = document.createElement("span");
            lineContainer.classList.add("line");

            var tempDiv = document.createElement("div");
            tempDiv.innerHTML = line.trim();
            var nodes = tempDiv.childNodes;

            nodes.forEach(function (node) {
                if (node.nodeType === 3) {
                    node.textContent.split("").forEach(function (char) {
                        var span = document.createElement("span");
                        span.className = "letter";
                        span.textContent = char;
                        span.style.animation =
                            "slideDown 2.5s cubic-bezier(0.16, 1, 0.3, 1) " +
                            globalIndex * 0.08 +
                            "s forwards";
                        globalIndex++;
                        lineContainer.appendChild(span);
                    });
                } else {
                    var word = document.createElement(node.tagName.toLowerCase());
                    word.className = node.className;

                    Array.prototype.forEach.call(node.textContent, function (char) {
                        var span = document.createElement("span");
                        span.className = "letter";
                        span.textContent = char;
                        span.style.animation =
                            "slideDown 2.5s cubic-bezier(0.16, 1, 0.3, 1) " +
                            globalIndex * 0.08 +
                            "s forwards";
                        globalIndex++;
                        word.appendChild(span);
                    });

                    lineContainer.appendChild(word);
                    lineContainer.appendChild(document.createTextNode(" "));
                }
            });

            title.appendChild(lineContainer);
        });
    }

    function initMobileNav() {
        var toggle = document.querySelector('[data-action="toggle-nav"]');
        var overlay = document.querySelector('[data-action="close-nav"]');
        var titles = document.querySelectorAll(".nav-sections-item-title");

        function openNav() {
            document.body.classList.add("nav-open", "nav-before-open");
            if (overlay) overlay.hidden = false;
        }

        function closeNav() {
            document.body.classList.remove("nav-open", "nav-before-open");
            if (overlay) overlay.hidden = true;
        }

        if (toggle) {
            toggle.addEventListener("click", function () {
                if (document.body.classList.contains("nav-open")) {
                    closeNav();
                } else {
                    openNav();
                }
            });

            toggle.addEventListener("keydown", function (e) {
                if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault();
                    toggle.click();
                }
            });
        }

        if (overlay) {
            overlay.addEventListener("click", closeNav);
        }

        // Only accordion titles — do NOT block real menu link navigation
        titles.forEach(function (title) {
            title.addEventListener("click", function (e) {
                var switchLink = title.querySelector("a");
                if (switchLink && e.target.closest("a") === switchLink) {
                    e.preventDefault();
                }
                titles.forEach(function (t) {
                    t.classList.remove("active");
                });
                title.classList.add("active");
            });
        });

        // Allow menu links to navigate; close drawer for cleaner transition
        var menuLinks = document.querySelectorAll(
            ".nav-sections .navigation a.level-top, .nav-sections .header.links a"
        );
        menuLinks.forEach(function (link) {
            link.addEventListener("click", function () {
                closeNav();
            });
        });

        window.addEventListener("resize", function () {
            if (window.innerWidth > 1024) {
                closeNav();
            }
        });
    }

    function boot() {
        initMobileNav();

        if (document.readyState === "complete") {
            setTimeout(animateBanner, 200);
        } else {
            window.addEventListener("load", function () {
                setTimeout(animateBanner, 200);
            });
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", boot);
    } else {
        boot();
    }
})();
