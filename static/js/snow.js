document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("snow");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    resize();
    window.addEventListener("resize", resize);

    const snowflakes = [];

    for (let i = 0; i < 120; i++) {
        snowflakes.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 4 + 1,
            d: Math.random() + 1
        });
    }

    function drawSnow() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "white";
        ctx.beginPath();

        snowflakes.forEach(f => {
            ctx.moveTo(f.x, f.y);
            ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2);
        });

        ctx.fill();

        snowflakes.forEach(f => {
            f.y += f.d;
            if (f.y > canvas.height) {
                f.y = 0;
                f.x = Math.random() * canvas.width;
            }
        });
    }

    setInterval(drawSnow, 30);
});
