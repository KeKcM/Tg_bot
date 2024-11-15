const wheel = document.getElementById("wheel");
const spinButton = document.getElementById("spinButton");

spinButton.addEventListener("click", () => {
    const randomDegree = Math.floor(Math.random() * 3600) + 360; // Случайный угол до 3600 градусов (10 оборотов)
    wheel.style.transition = "transform 4s ease-out"; // Анимация вращения
    wheel.style.transform = `rotate(${randomDegree}deg)`; // Применение поворота

    setTimeout(() => {
        // Определяем результат
        const finalDegree = randomDegree % 360;
        let result;
        if (finalDegree < 45) result = "Приз 1";
        else if (finalDegree < 90) result = "Приз 2";
        else if (finalDegree < 135) result = "Приз 3";
        else if (finalDegree < 180) result = "Приз 4";
        else if (finalDegree < 225) result = "Приз 5";
        else if (finalDegree < 270) result = "Приз 6";
        else if (finalDegree < 315) result = "Приз 7";
        else result = "Приз 8";

        // Показываем результат
        alert(`Ваш результат: ${result}`);
        
        // Передача результата в Telegram Web App (если требуется)
        if (window.Telegram.WebApp) {
            Telegram.WebApp.sendData(result); // Отправляем результат обратно в бота
        }
    }, 4000); // Задержка на 4 секунды до определения результата
});
