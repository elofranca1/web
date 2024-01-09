let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.style.display = 'none';
        if (i === index) {
            slide.style.display = 'block';
        }
    });
}

function moveSlide(direction) {
    currentSlide = (currentSlide + direction + slides.length) % slides.length;
    showSlide(currentSlide);
}

showSlide(currentSlide); // 初始化显示第一张图片