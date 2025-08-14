from dotenv import load_dotenv

import os

load_dotenv()

CHANNEL_ID = os.getenv('CHANNEL_ID')
TOKEN = os.getenv('BOT_TOKEN')
DB_URL = os.getenv('DB_URL')
PAYMENTS_TOKEN = os.getenv('PAYMENTS_TOKEN')
BOT_ID = os.getenv('BOT_ID')
YOO_TOKEN = os.getenv('YOO_TOKEN')
YOO_SECRET = os.getenv('YOO_SECRET')
YOOMONEY_WEBHOOK_PATH=os.getenv('YOOMONEY_WEBHOOK_PATH')
TELEGRAM_WEBHOOK_PATH=os.getenv('TELEGRAM_WEBHOOK_PATH')
STAR_K = 1.6

status_mapping = {
    'SOLD': 'Продан',
    'EXPIRED': 'Истекло время',
    'TRADING': 'Идут торги',
}

blank_status_mapping = {
    'PENDING': "⏳ Ожидает обработки",
    'APPROVED': '✅ Обработана',
    'REJECTED': '❌ Отклонена',
}

blank_bank_mapping = {
    "TINKOFF": "🟡 Тинькофф",
    "SBER": "🟢 Сбербанк",
    "ALFA": "🔴 Альфа-Банк",
    "STAR": "⭐ Звезды"
}

TEXTS = {
    "cmd_start_auction_caption": "📦 Стартовая цена: {starter_price}🌟\n"
                                 "💰 Текущая ставка: {real_price}🌟\n"
                                 "➡️ Мин. следующая ставка: {min_next_price}🌟\n"
                                 "🚀 Цена мгновенного выкупа: {moment_buy_price}🌟\n"
                                 "⏰ Завершение: {expired_at} (МСК)\n"
                                 "👤 Продавец: {name}\n",

    "cmd_start_msg": "👋 Привет, {name}! Добро пожаловать в Lotoro Аукцион 🎁\n\n"
                     "🕒 Мы на связи с 8:00 до 23:00 (МСК). Обычно отвечаем в течение 5–10 минут.\n\n"
                     "🌙 Заявки после 23:00 обрабатываются утром. Спасибо за понимание!",

    "main_menu_msg": "🔍 Выберите действие из меню ниже:",

    "user_profile_msg": "👤 Ваш профиль:\n"
                        "📛 Имя пользователя: {username}\n"
                        "📦 Ваши лоты: {lots}\n"
                        "💰 Баланс: {balance}🌟\n",

    "support_msg": "📩 Нужна помощь? Напишите в поддержку через кнопку ниже ✅",

    "withdraw_stars_msg": "💸 Хотите вывести звёзды? Нажмите на кнопку ниже и следуйте инструкции!",

    "create_lot_1_msg": "📷 Пришлите фото подарка, который хотите продать.\n"
                        "👀 Лицо можно замазать.\n"
                        "❌ Для отмены — нажмите «Отменить».",

    "create_lot_2_msg": "💰 Введите стартовую цену (в звёздах).\n"
                        "📌 1🌟 = 1,65₽",

    "create_lot_3_msg": "🚀 Укажите цену мгновенного выкупа (блиц-цену).\n"
                        "📌 1🌟 = 1,65₽",

    "create_lot_3.2_msg": "⚠️ Цена выкупа должна быть выше стартовой:",

    "create_lot_4_msg": "🕒 Укажите длительность лота (в часах):",

    "create_lot_end_caption": "📦 Стартовая цена: {starter_price}🌟\n"
                              "🚀 Цена мгновенного выкупа: {blitz_price}🌟\n"
                              "⏰ Длительность: {hours} ч.\n"
                              "👤 Продавец: {name}\n",

    "create_lot_end_notif_msg": "📝 Лот отправлен на модерацию. Мы уведомим, как только он появится на аукционе!",

    "deposit_balance_msg": "💳 Введите количество звёзд для пополнения(🌟 = {star_k}руб):\n"
                           "❌ Для отмены — нажмите «Отменить».",

    "deposit_balance_msg_2": "💳 Введите количество звёзд для пополнения:\n"
                             "✅ Сейчас пришлём счёт для оплаты.",

    "send_deposit_balance_msg": "📨 Готовим счёт на пополнение на {stars}🌟({rub}рублей)...",

    "limitations_deposit_balance_msg": "📌 Пополнение доступно от 50 до 10 000 звёзд.",

    "successful_payment": "🎉 Пополнение на {stars}🌟 прошло успешно. Спасибо!",

    "interrupt_work_msg": "🚫 Операция прервана.",

    "lot_sold_msg": "✅ Лот уже выкуплен другим пользователем.",

    "lot_expired_msg": "⌛ Время продажи лота истекло. Он не был выкуплен.",

    "not_enough_stars": "❗ Недостаточно звёзд. Пополните баланс с помощью кнопки ниже ⬇️",

    "you_are_seller_msg": "⚠️ Вы не можете делать ставку на свой собственный лот.",

    "bet_is_already_yours_msg": "⌛ Вы уже сделали ставку. Дождитесь перебития или купите лот сразу.",

    "user_buy_lot_msg": "🎁 Вы выкупили лот #{id} за {moment_buy_price}🌟! @{username} отправит вам подарок в течение часа.",

    "seller_send_gift_msg": "📦 Ваш лот #{id} продан. Победитель — @{username}.\n"
                            "⏳ У вас 1 час на отправку подарка. Иначе возможна блокировка.",

    "seller_expired_lot_msg": "📦 Ваш лот #{id} завершился без ставок.",

    "sold_lot_caption": "🎁 Лот: <b>#{id}</b>\n"
                        "💵 Стартовая цена: <b>{starter_price}</b>🌟\n"
                        "💰 Цена продажи: <b>{moment_buy_price}</b>🌟\n"
                        "👤 Продавец: <b>{seller}</b>\n"
                        "✅ Статус: <b>{status}</b>\n"
                        "🧑 Покупатель: <b>{name}</b>",

    "expired_lot_caption": "📦 Лот: <b>#{id}</b>\n"
                           "💵 Стартовая цена: <b>{starter_price}</b>🌟\n"
                           "👤 Продавец: <b>{name}</b>\n"
                           "⌛ Статус: <b>{status}</b>",

    "bid_exceeded_msg": "📉 Ваша ставка на лот #{id} перебита. Звёзды возвращены на баланс.",

    "successful_bid_msg": "✅ Ставка успешно принята!",

    "update_lot_after_bid_caption": "🎯 Лот: <b>#{id}</b>\n"
                                    "💵 Стартовая цена: <b>{starter_price}</b>🌟\n"
                                    "🔄 Текущая ставка: <b>{real_price}</b>🌟\n"
                                    "➡️ Следующая ставка: <b>{min_next_price}</b>🌟\n"
                                    "🚀 Цена выкупа: <b>{moment_buy_price}</b>🌟\n"
                                    "👤 Продавец: <b>{name}</b>\n"
                                    "⏰ Завершение: <b>{expired_at}</b> (МСК)\n"
                                    "📌 Статус: <b>{status}</b>",

    "username_missing_msg": "⚠️ У вас нет username. Установите его в настройках Telegram и повторите команду.",

    "you_are_banned_msg": "🚫 Вы были забанены. Если это ошибка — напишите в поддержку.",

    "you_win_lot": "🎉 Ваша ставка на лот #{id} победила! @{username} отправит вам подарок в течение часа.",

    "tech_channel_msg": "🔧 Зайдите в тех. канал, чтобы найти ответы на частые вопросы.",

    "banned_list_msg": "🚫 Список забаненных пользователей:",

    "banned_list_msg_empty_msg": "✅ Список пуст.",

    "send_user_username_msg": "✍ Введите username пользователя (без @):",

    "can't_see_admin_account_msg": "❌ Просмотр профиля администратора запрещён.",

    "successful_ban_msg": "✅ Пользователь успешно забанен.",

    "send_ban_msg": "🚫 Вы были забанены. Если это ошибка — обратитесь в поддержку.",

    "successful_unban_msg": "✅ Пользователь успешно разбанен.",

    "send_unban_msg": "⚠️ Вы разбанены. Повторные нарушения приведут к пожизненному бану.",

    "see_new_lots_caption": "🆕 Лот: <b>#{id}</b>\n"
                            "💵 Стартовая цена: <b>{starter_price}</b>🌟\n"
                            "🔄 Текущая ставка: <b>{real_price}</b>🌟\n"
                            "➡️ Следующая ставка: <b>{min_next_price}</b>🌟\n"
                            "🚀 Цена выкупа: <b>{moment_buy_price}</b>🌟\n"
                            "👤 Продавец: <b>{name}</b>\n"
                            "⏰ Завершение: <b>{expired_at}</b> (МСК)",

    "send_new_lot_caption": "📦 Лот: <b>#{id}</b>\n"
                            "💵 Стартовая цена: <b>{starter_price}</b>🌟\n"
                            "➡️ Следующая ставка: <b>{min_next_price}</b>🌟\n"
                            "🚀 Цена выкупа: <b>{moment_buy_price}</b>🌟\n"
                            "👤 Продавец: <b>{name}</b>\n"
                            "⏰ Завершение: <b>{expired_at}</b> (МСК)\n"
                            "📌 Статус: <b>{status}</b>",

    "send_approve_lot_notif": "✅ Ваш лот одобрен и опубликован!\n"
                              "🔗 Ссылка: https://t.me/{CHANNEL_ID}/{message_id}",

    "no_new_lots_msg": "🎉 Все лоты проверены. Новых нет!",

    "send_reject_lot_notif": "❌ Ваш лот #{id} отклонён. Обратитесь в поддержку за деталями.",

    "reviewed_all_lots_before_this_msg": "✅ Все предыдущие лоты просмотрены.",

    "reviewed_all_lots_after_this_msg": "✅ Все последующие лоты просмотрены.",

    "end_moderation_msg": "🛑 Вы завершили модерацию лотов.",

    "end_watching_msg": "🛑 Вы завершили просмотр лотов.",

    "moment_price_men_real_price": "❗ Лот нельзя выкупить: ставка выше блиц-цены.",

    "ref_msg_prev": """<b>🎁 Реферальная программа Lotoro</b>. Приглашай друзей и зарабатывай! 💸

🔗 Получай <b>5%</b> от каждого пополнения, сделанного приглашёнными пользователями.

📲 Поделись своей ссылкой — человек будет закреплён за тобой навсегда.

💰 Бонусы приходят <b>автоматически</b> после каждого пополнения!

<b>Готов начать?</b> Нажми кнопку ниже и получи ссылку 👇""",

    "create_ref_link": "📎 Создать ссылку",

    "u_have_ref_link": "❗ У вас уже есть реферальная ссылка.\n\n"
                       "Если хотите изменить её — обратитесь в поддержку.",

    "your_ref_link": "<b>🎉 Ваша реферальная ссылка готова!</b>\n"
                     "Мы отправим её вам в виде кнопки ниже.\n"
                     "Пересылайте друзьям и зарабатывайте! 💸",

    "earn_with_lotoro": """🎉 Зарабатывай с Lotoro!

Аукционный бот, где можно продавать и покупать уникальные подарки и вещи.

👇 Жми и заходи:""",

    "join_to_lotoro": "🚀 Присоединиться к Lotoro",

    "link_reg": "🎉 Вы зарегистрированы по ссылке от @{inviter}!\n"
                "Он будет получать 5% с каждого вашего пополнения.",

    "u_are_referral": "Вы не можете создать реферальную ссылку, так как сами являетесь рефералом.",

    "ref_stars": "Вам пришло {stars}🌟, от вашего реферала.",

    "successful_yoo_pay": "✅ Счёт успешно оплачен!",

    "user_lot_caption": "🎯 Лот: <b>#{id}</b>\n"
                                    "💵 Стартовая цена: <b>{starter_price}</b>🌟\n"
                                    "🔄 Текущая ставка: <b>{real_price}</b>🌟\n"
                                    "➡️ Следующая ставка: <b>{min_next_price}</b>🌟\n"
                                    "🚀 Цена выкупа: <b>{moment_buy_price}</b>🌟\n"
                                    "🧑 Покупатель: <b>{name}</b>\n"
                                    "⏰ Завершение: <b>{expired_at}</b> (МСК)\n"
                                    "📌 Статус: <b>{status}</b>",

    "user_lot_caption_bid": "🎯 Лот: <b>#{id}</b>\n"
                                    "💵 Стартовая цена: <b>{starter_price}</b>🌟\n"
                                    "🔄 Текущая ставка: <b>{real_price}</b>🌟\n"
                                    "➡️ Следующая ставка: <b>{min_next_price}</b>🌟\n"
                                    "🚀 Цена выкупа: <b>{moment_buy_price}</b>🌟\n"
                                    "👤 Продавец: <b>{name}</b>\n"
                                    "⏰ Завершение: <b>{expired_at}</b> (МСК)\n"
                                    "📌 Статус: <b>{status}</b>",

    "user_not_found": "🚫 Пользователь не найден в базе данных.",

    "write_value_of_stars_msg": "✨ Пожалуйста, укажите количество звёзд, которое вы хотите вывести.",

    "choose_bank_msg": "🏦 Выберите банк, которым вы пользуетесь.",

    "write_correct_value_of_stars": "🔢 Введите числовое значение, не превышающее ваш баланс в профиле.",

    "write_your_account_number": "💳 Укажите номер карты или телефона, на которые будет произведён перевод.",

    "withdraw_from_50_stars": "⚠️ Минимальная сумма для вывода — 50 звёзд.",

    "blank_send_to_administrators": "📨 Ваша заявка отправлена администрации. ⏳ Обработка занимает до 24 часов в будние дни 🗓️ и до 48 часов в выходные и праздничные дни 🎉.",

    "withdraw_request_admin":   "🧾 Заявка на вывод №<b>{id}</b>\n"
                                "👤 Пользователь: <b>@{user_id}</b>\n"
                                "🏦 Вывод: <b>{bank}</b>\n"
                                "💳 Номер карты / Телефон: <b>{account_number}</b>\n"
                                "💰 Сумма к выводу: <b>{star_amount}</b>🌟\n"
                                "🕒 Создана: <b>{created_at}</b> (МСК)\n"
                                "{processed_block}"

}


