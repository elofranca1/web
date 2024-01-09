let currentSlide = 0;
// 获取所有的幻灯片元素
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
    // 隐藏所有的幻灯片
    slides.forEach(slide => {
        slide.style.display = 'none';
    });
    // 显示指定索引的幻灯片
    slides[index].style.display = 'block';
}

function moveSlide(direction) {
    // 计算新的索引
    currentSlide = (currentSlide + direction + slides.length) % slides.length;
    // 显示新的幻灯片
    showSlide(currentSlide);
}

// 初始化显示第一张图片
showSlide(currentSlide);

// 给左右箭头添加点击事件
document.getElementById('left-arrow').addEventListener('click', () => moveSlide(-1));
document.getElementById('right-arrow').addEventListener('click', () => moveSlide(1));
