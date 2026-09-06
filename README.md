
# 🤖 Telegram Auction Bot – готовый аукцион-бот с CryptoPay

<p align="center">
  <img src="https://img.shields.io/badge/version-2.2.0-blue.svg" alt="Version 2.2.0">
  <img src="https://img.shields.io/badge/python-3.9+-green.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey.svg" alt="License">
  <img src="https://img.shields.io/badge/price-%245-brightgreen" alt="Price $5">
</p>

<p align="center">
  <b>Полнофункциональный аукцион-бот для Telegram с интеграцией CryptoPay API, поддержкой тем (topics), автозакреплением и гибкими настройками.</b>
</p>

---

## 🎯 О боте

Этот бот позволяет проводить аукционы прямо в Telegram-группах и супергруппах (включая форумы с темами).  
Он полностью готов к использованию: все зависимости устанавливаются автоматически при первом запуске.

**Для кого подойдёт:**
- Владельцы Telegram-каналов и групп, желающие монетизировать аукционы
- Крипто‑сообщества, принимающие ставки в USDT, TON, BTC, ETH
- Администраторы, которым нужен надёжный инструмент с админ‑панелью и статистикой

---

## ✨ Возможности

### 🏆 Аукционы
- Два типа: **денежный** (победитель получает процент от банка) и **предметный** (победитель получает товар)
- Гибкие параметры: стартовая ставка, минимальный шаг, время на перебив, максимальная длительность (hard deadline)
- Автозакрепление сообщения аукциона при старте и открепление после завершения
- Периодические **напоминания** о незавершённом аукционе (настраиваемый интервал)

### 💳 Криптовалютные платежи (CryptoPay)
- Пополнение баланса через инвойсы (USDT, TON, BTC, ETH)
- Вывод средств через чеки, привязанные к пользователю
- Автоматическая проверка оплаты и зачисление средств

### 👤 Пользовательский функционал
- Внутренний кошелёк с историей операций
- Просмотр активных аукционов
- Удобные inline‑кнопки для ставок (быстрые суммы, своя ставка, баланс, обновление)

### 👑 Админ‑панель
- Статистика (пользователи, аукционы, объёмы)
- Управление активными аукционами (остановить, отменить)
- Настройка комиссии, лимитов депозита/вывода, времени перебива и шага
- Включение/отключение автозакрепления и напоминаний
- Просмотр баланса CryptoPay

### 🧵 Поддержка тем (Topics)
- Работа в супергруппах‑форумах – можно создавать аукцион в конкретной теме

### 📁 Автосохранение групп
- Бот автоматически запоминает все группы, в которые его добавили

---

## 📸 Скриншоты

*(Вставьте сюда ссылки на изображения или удалите этот блок)*

| Создание аукциона | Карточка аукциона | Админ‑панель |
|-------------------|--------------------|---------------|
| ![](https://via.placeholder.com/300x200.png?text=Скриншот+1) | ![](https://via.placeholder.com/300x200.png?text=Скриншот+2) | ![](https://via.placeholder.com/300x200.png?text=Скриншот+3) |

---

## 🤖 Демо‑бот

Хотите посмотреть, как работает бот?  
Напишите мне в Telegram – я предоставлю доступ к тестовой версии или покажу запись работы.

👉 **Контакт: [@KodoDrive](https://t.me/KodoDrive)**

---

## 🚀 Быстрый старт

### 1. Получите код
Приобретите бота у [@KodoDrive](https://t.me/KodoDrive) за **5$**.  
После оплаты вы получите архив с файлом `auction_bot.py` и примером `.env`.

### 2. Установите Python 3.9+
Убедитесь, что Python установлен и добавлен в PATH.

### 3. Запустите бота
```bash
python auction_bot.py


При первом запуске автоматически установятся все необходимые зависимости (aiogram, aiohttp, aiosqlite, python-dotenv).
```
### 4. Настройте окружение

Создайте файл .env в той же папке и укажите свои данные:

```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
ADMIN_IDS=123456789,987654321
CRYPTO_PAY_TOKEN=12345:ABCdefGHIjklMNO
```

### 5. Добавьте бота в группу

Бот должен быть администратором группы (для закрепления сообщений).
После добавления отправьте любое сообщение в группу – она автоматически сохранится.

### 6. Создайте аукцион

Используйте команду /new_auction в группе или личном чате с ботом.

---

### ⚙️ Настройки (переменные окружения)

Параметр Описание По умолчанию
```env
BOT_TOKEN Токен бота от @BotFather –
ADMIN_IDS ID администраторов через запятую –
CRYPTO_PAY_TOKEN Токен CryptoPay –
DEFAULT_MIN_STEP Минимальный шаг ставки 1.0
DEFAULT_START_BID Стартовая ставка 10.0
DEFAULT_BID_TIME Время на перебив (сек) 60
DEFAULT_MIN_DEPOSIT Мин. депозит (USDT) 5.0
DEFAULT_MIN_WITHDRAW Мин. вывод (USDT) 10.0
PLATFORM_FEE Комиссия платформы (0.30 = 30%) 0.30
DEFAULT_MAX_DURATION Макс. длительность (0 – без огранич.) 0
DEFAULT_REMINDER_INTERVAL Интервал напоминаний (сек) 300
DB_PATH Путь к базе данных SQLite auction_bot.db
```
---

### 📋 Команды

## 👤 Для всех пользователей

· /start – приветствие, баланс
· /balance – кошелёк
· /deposit – пополнить
· /withdraw – вывести
· /auctions – список активных аукционов
· /history – последние операции

## 👑 Для администраторов

· /new_auction – создать аукцион (в группе или личном чате)
· /admin – панель управления
· /stats – статистика
· /stop_auction [ID] – принудительно завершить с текущим лидером
· /cancel_auction [ID] – отменить аукцион
· /my_auctions – ваши созданные аукционы
· /scan_chats – пересканировать группы
· /list_chats – список сохранённых групп

---

### 💰 Покупка

Цена: 5$ (единоразово, бессрочная лицензия)

# Что входит:

· Полный исходный код auction_bot.py
· Файл .env.example с пояснениями
· Поддержка при установке (по необходимости)

# Как купить:

1. Напишите в Telegram: @KodoDrive
2. Сообщите, что хотите приобрести бота
3. Оплатите 5$ (USDT, можно через CryptoBot или другой способ)
4. Получите архив с кодом и инструкцию

---

### 📄 Лицензия

Данный продукт распространяется по принципу одна покупка – одна установка. Запрещена перепродажа или публикация кода в открытом доступе.

---

### 🛠 Технические детали

· Язык: Python 3.9+
· Библиотеки: aiogram 3.4.1, aiohttp, python-dotenv, aiosqlite
· База данных: SQLite (встроенная, не требует установки)
· Платежи: CryptoPay API

---

### 📞 Контакты

· Автор и поддержка: @KodoDrive
· Купить бота: напишите в личные сообщения

---

<p align="center">
  <b>Без воды. Только код и результат. 🚀</b>
</p>
```

---

<!-- kododrive-projects-block -->

## Проекты KodoDrive

Другие проекты автора: [профиль @svod011929](https://github.com/svod011929) · [Telegram](https://t.me/KodoDrive)

### VPN и инфраструктура

- [BuryatVPN — VPN-сервис + Telegram](https://github.com/svod011929/buryatvpn)
- [VPN Server Installer — VLESS + TLS](https://github.com/svod011929/vpn-server-installer)
- [3X-UI Auto Installer](https://github.com/svod011929/3x-ui-auto-installer)
- [AWG Bot Installer — AmneziaWG](https://github.com/svod011929/awg-bot-installer)
- [RemnaShop Installer](https://github.com/svod011929/remnashop-installer)
- [VPN Auto Installer — панели](https://github.com/svod011929/vpn-auto-installer)
- [VPNHubBot — Telegram VPN-бот](https://github.com/svod011929/VPNHubBot)

### Telegram и автоматизация

- [KDS Server Panel — SSH из Telegram](https://github.com/svod011929/KDS_Server_Panel)
- [Telegram → VK Poster](https://github.com/svod011929/telegram-to-vk-poster)
- [KDS Parser CryptoBot](https://github.com/svod011929/kds_parser_cryptobot)
- **Auction Bot** ← ты здесь
- [Invest Bot](https://github.com/svod011929/invest-bot)
- [Crypto Check Bot](https://github.com/svod011929/crypto-check-bot)
- [KodoRefStarsBot](https://github.com/svod011929/KodoRefStarsBot)

### Магазины и финансы

- [KodoCashFlow](https://github.com/svod011929/KodoCashFlow)
- [Telegram Crypto Shop](https://github.com/svod011929/telegram-crypto-shop)
- [TalkProfit](https://github.com/svod011929/talkprofit)

### Сайты

- [KodoDrive Portfolio](https://github.com/svod011929/kododrive-portfolio)
- [kododrive.github.io](https://github.com/svod011929/kododrive.github.io)

<!-- /kododrive-projects-block -->
