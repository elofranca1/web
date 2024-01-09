let index = 0; // 当前幻灯片索引

function moveSlide(step) {
    const slides = document.querySelectorAll('.carousel-slide img');
    const totalSlides = slides.length;

    // 更新索引
    index = (index + step + totalSlides) % totalSlides;

    // 移动到下一幻灯片
    const offset = -index * 100;
    for (let slide of slides) {
        slide.style.transform = `translateX(${offset}%)`;
    }
}

function fetchMonsterInfo() {
    fetch('/generate-monster')
        .then(response => response.json())
        .then(data => {
            document.getElementById('monster-name-value').textContent = data.name;
            document.getElementById('monster-personality-value').textContent = data.personality;
            document.getElementById('monster-ability-value').textContent = data.ability;
        })
        .catch(error => {
            console.error('Error fetching monster info:', error);
        });
}

// 页面加载完毕时执行
document.addEventListener('DOMContentLoaded', function () {
    // 初始加载妖兽信息
    fetchMonsterInfo();

    // 为按钮添加点击事件监听器
    document.getElementById('generate-button').addEventListener('click', function () {
        fetchMonsterInfo(); // 点击按钮时重新获取妖兽信息
    });
});
