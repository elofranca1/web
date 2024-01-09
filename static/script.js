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
    document.getElementById('footer-image').addEventListener('click', function () {
        fetchMonsterInfo(); // 点击按钮时重新获取妖兽信息
    });
});

function selectScene(scene,clickedButton) {
    document.getElementById('selected-scene').value = scene;

    // 可以移除下面的行，如果不需要在选择时显示弹窗
    var buttons = document.getElementsByClassName('slide-btn');
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.add('dimmed');
    }

    // 移除被点击按钮的 dimmed 类
    clickedButton.classList.remove('dimmed');
}
function selectTheme(theme) {
    document.getElementById('selected-theme').value = theme;
}

function selectLength(length) {
    document.getElementById('selected-length').value = length;
}


document.getElementById('submit-button').addEventListener('click', function () {
    // 收集需要发送的数据
    var data = {
        monster_name: document.getElementById('monster-name-value').innerText,
        monster_personality: document.getElementById('monster-personality-value').innerText,
        monster_ability: document.getElementById('monster-ability-value').innerText,
        selected_theme: document.getElementById('selected-theme').getAttribute('value'), // 更新主题的值
        selected_length: document.getElementById('selected-length').getAttribute('value'), // 更新页数的值
        story_summary: document.getElementById('story-summary-input').value,
        selected_scene: document.getElementById('selected-scene').getAttribute('value')
    };

    // 发送 AJAX 请求到服务器
    fetch('/submit-data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.text())
        .then(html => {
            // 使用服务器响应的新 HTML 更新页面
            document.documentElement.innerHTML = html;
        })
        .catch(error => console.error('Error:', error));
});