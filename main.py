from aiogram import Dispatcher, types, F, filters, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()

class Card(StatesGroup):
    card_number = State()

main_button = ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Отправить контакт📚", request_contact=True)]
], resize_keyboard=True)

bot = Bot(token="7432926301:AAEqTYXzNfQ22mf4atZYHVagQsp3vgBWAbA")
dp = Dispatcher(bot=bot)

keyboard1 = [
    [KeyboardButton(text="Til tallang🇺🇿, Выберите язык🇷🇺")]
]

keyboard2 = [
    [KeyboardButton(text="Uzbek tili🇺🇿"), KeyboardButton(text="Rus tili🇷🇺")]
]

keyboard3 = [
    [KeyboardButton(text="Menu📖"),KeyboardButton(text="Karzina info🛒")],
    [KeyboardButton(text="Biz haqimizda🍟"),KeyboardButton(text="Siz haqingizda🎫")],
    [KeyboardButton(text="Yordam🆘"),KeyboardButton(text="Tilni ozgartirish🏴")],
    [KeyboardButton(text="Karzina🛒")]
]

keyboard4 = [
    [KeyboardButton(text="Burger🍔"),KeyboardButton(text="Suvlar🥤")],
    [KeyboardButton(text="Orqaga qaytish🔙")]
]

keyboard5 = [
    [KeyboardButton(text="Sirli Burger🍔"),KeyboardButton(text="Katta Burger🍔")],
    [KeyboardButton(text="Kichkina Burger🍔"),KeyboardButton(text="Achchiq Burger🍔")],
    [KeyboardButton(text="Ortacha burger🍔"),KeyboardButton(text="Oddiy Burger🍔")],
    [KeyboardButton(text="Orqaga qaytish🍔")]
]

keyboard6 = [
    [KeyboardButton(text="Coca-Cola🥤"),KeyboardButton(text="Sprite🥤")],
    [KeyboardButton(text="Fanta🥤"),KeyboardButton(text="Pepsi🥤")],
    [KeyboardButton(text="Oddiy Suv🥤"),KeyboardButton(text="Gazli Suv🥤")],
    [KeyboardButton(text="Orqaga qaytish🔙")]
]

keyboard8 = [
    [KeyboardButton(text="Karzinani Sotib Olish🛒"),KeyboardButton(text="Karzinani Sotib Olmaslik🛒")],
    [KeyboardButton(text="Orqaga qaytish🔙")]
]

keyboard9 = [
    [KeyboardButton(text="Humo💳"),KeyboardButton(text="UzCard💳")],
]

keyboard10 = [
    [KeyboardButton(text="Til tallang🇺🇿, Выберите язык🇷🇺")]
]

keyboard11 = [
    [KeyboardButton(text="Uzbek tili🇺🇿"), KeyboardButton(text="Rus tili🇷🇺")]
]


#########################################################33##########33

keyboard12 = [
    [KeyboardButton(text="меню📖"),KeyboardButton(text="Karzina info🛒")],
    [KeyboardButton(text="O нас🍟"),KeyboardButton(text="о вас🎫")],
    [KeyboardButton(text="помочь🆘"),KeyboardButton(text="изменение языка🏴")],
    [KeyboardButton(text="Карзина🛒")]
]

keyboard13 = [
    [KeyboardButton(text="Бургеры🍔"),KeyboardButton(text="напитки🥤")],
    [KeyboardButton(text="возвращаться🔙")]
]

keyboard14 = [
    [KeyboardButton(text="Бургер🍔"),KeyboardButton(text="большой бургер🍔")],
    [KeyboardButton(text="маленький бургер🍔"),KeyboardButton(text="чили бургер🍔")],
    [KeyboardButton(text="средний бургер🍔"),KeyboardButton(text="обычный бургер🍔")],
    [KeyboardButton(text="возвращаться🍔")]
]

keyboard15 = [
    [KeyboardButton(text="Кока-Кола🥤"),KeyboardButton(text="спрайт🥤")],
    [KeyboardButton(text="Фанта🥤"),KeyboardButton(text="пепси🥤")],
    [KeyboardButton(text="обычный чай🥤"),KeyboardButton(text="газированная вода🥤")],
    [KeyboardButton(text="возвращаться🥤")]
]

keyboard16 = [
    [InlineKeyboardButton(text="купить", callback_data="olish1"),
     InlineKeyboardButton(text="не купить", callback_data="olmaslik1")]
]

keyboard17 = [
    [KeyboardButton(text="купить карзину🛒"),KeyboardButton(text="не купить карзину🛒")],
    [KeyboardButton(text="возвращаться🔙")]
]

keyboard18 = [
    [KeyboardButton(text="HUmo💳"),KeyboardButton(text="UzCarD💳")],
]

keyboard19 = [
    [KeyboardButton(text="Uzbek TilI🇺🇿"),KeyboardButton(text="Rus TilI🇷🇺")],
]

keyboard20 = [
    [KeyboardButton(text="Узбекиский язык🇺🇿"), KeyboardButton(text="Русский язык🇷🇺")]
]
button_1 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="1"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_2 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="2"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_3 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="3"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_4 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="4"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_5 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="5"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_6 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="6"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_7 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="7"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_8 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="8"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_9 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="9"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_10 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="10"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_11 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="11"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_12 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="12"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_13 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="13"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

button_14 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="14"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_15 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="15"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_16 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="16"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_17 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="17"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_18 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="18"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_19 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="19"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_20 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="20"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_21 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="21"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_22 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="22"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_23 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="23"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]
button_24 = [
    [InlineKeyboardButton(text="Sotib Olish", callback_data="24"),
     InlineKeyboardButton(text="Sotib olmaslik", callback_data="olmaslik")]
]

Karzina=[]
main_button1 = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

main_button2 = ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

main_button3 = ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)

main_button4 = ReplyKeyboardMarkup(keyboard=keyboard4, resize_keyboard=True)

main_button5 = ReplyKeyboardMarkup(keyboard=keyboard5, resize_keyboard=True)

main_button6 = ReplyKeyboardMarkup(keyboard=keyboard6, resize_keyboard=True)

main_button8 = ReplyKeyboardMarkup(keyboard=keyboard8, resize_keyboard=True)

main_button9 = ReplyKeyboardMarkup(keyboard=keyboard9, resize_keyboard=True)

main_button10 = ReplyKeyboardMarkup(keyboard=keyboard10, resize_keyboard=True)

main_button11 = ReplyKeyboardMarkup(keyboard=keyboard11, resize_keyboard=True)

main_button12 = ReplyKeyboardMarkup(keyboard=keyboard12, resize_keyboard=True)

main_button13 = ReplyKeyboardMarkup(keyboard=keyboard13, resize_keyboard=True)

main_button14 = ReplyKeyboardMarkup(keyboard=keyboard14, resize_keyboard=True)

main_button15 = ReplyKeyboardMarkup(keyboard=keyboard15, resize_keyboard=True)

main_button17 = ReplyKeyboardMarkup(keyboard=keyboard17, resize_keyboard=True)

main_button18 = ReplyKeyboardMarkup(keyboard=keyboard18, resize_keyboard=True)

main_button19 = ReplyKeyboardMarkup(keyboard=keyboard19, resize_keyboard=True)

main_button20 = ReplyKeyboardMarkup(keyboard=keyboard20, resize_keyboard=True)

button1 = InlineKeyboardMarkup(inline_keyboard=button_1)

button2 = InlineKeyboardMarkup(inline_keyboard=button_2)

button3 = InlineKeyboardMarkup(inline_keyboard=button_3)

button4 = InlineKeyboardMarkup(inline_keyboard=button_4)

button5 = InlineKeyboardMarkup(inline_keyboard=button_5)

button6 = InlineKeyboardMarkup(inline_keyboard=button_6)

button7 = InlineKeyboardMarkup(inline_keyboard=button_7)

button8 = InlineKeyboardMarkup(inline_keyboard=button_8)

button9 = InlineKeyboardMarkup(inline_keyboard=button_9)

button10 = InlineKeyboardMarkup(inline_keyboard=button_10)

button11 = InlineKeyboardMarkup(inline_keyboard=button_11)

button12 = InlineKeyboardMarkup(inline_keyboard=button_12)

button13 = InlineKeyboardMarkup(inline_keyboard=button_13)

button14 = InlineKeyboardMarkup(inline_keyboard=button_14)

button15 = InlineKeyboardMarkup(inline_keyboard=button_15)

button16 = InlineKeyboardMarkup(inline_keyboard=button_16)

button17 = InlineKeyboardMarkup(inline_keyboard=button_17)

button18 = InlineKeyboardMarkup(inline_keyboard=button_18)

button19 = InlineKeyboardMarkup(inline_keyboard=button_19)

button20 = InlineKeyboardMarkup(inline_keyboard=button_20)

button21 = InlineKeyboardMarkup(inline_keyboard=button_21)

button22 = InlineKeyboardMarkup(inline_keyboard=button_22)

button23 = InlineKeyboardMarkup(inline_keyboard=button_23)

button24 = InlineKeyboardMarkup(inline_keyboard=button_24)
# START
@dp.message(filters.Command("start"))
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Salom!\n Bizning Botimizga Xush kelibsiz!\nZakaz qiling!, ismingizni kirting",
                         )

@dp.message(Registration.first_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Familiyaniizni Kirting")

@dp.message(Registration.last_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer("Nomer Kiriting",reply_markup=main_button)

@dp.message(Registration.phone_number)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Имя: {data["first_name"]}\nФамилия: "
                         f"{data["last_name"]}\nНомер телефона: {data["phone_number"]}",
                         reply_markup=main_button1)
    await state.clear()

@dp.message(F.text == "Til tallang🇺🇿, Выберите язык🇷🇺")
async def start_function(message: types.Message):
    await message.answer("Siz Til Tallshingiz kerak!", reply_markup=main_button2)

@dp.message(F.text == "Отправить контакт📚")
async def start_function(message: types.Message):
    await message.answer("siz kontankt tshildingiz", reply_markup=main_button1)

@dp.message(F.text == "Uzbek tili🇺🇿")
async def start_function(message: types.Message):
    await message.answer("Siz Uzbek Tilini talladingiz!", reply_markup=main_button3)


@dp.message(F.text == "Menu📖")
async def start_function(message: types.Message):
    await message.answer("Bu bizning Menu Hohlagan ovqat va ichimliklardan sotib olishingiz mumkin!",
                       reply_markup=main_button4)


@dp.message(F.text == "Orqaga qaytish🔙")
async def start_function(message: types.Message):
    await message.answer("Siz Bosh menu ga qaytingiz", reply_markup=main_button3)


@dp.message(F.text == "Burger🍔")
async def start_function(message: types.Message):
    await message.answer("Siz Burgerlar bolimidasiz!", reply_markup=main_button5)


@dp.message(F.text == "Suvlar🥤")
async def start_function(message: types.Message):
    await message.answer("Siz Suvlar bolimidasiz!", reply_markup=main_button6)


@dp.message(F.text == "Sirli Burger🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic"
                                     ".com/images?q=tbn:ANd9GcTlcy0q-obN86MyKK6fjIyYgOVZ5yiG5RXn0A&s",
                                      caption="Narxi:20.000", reply_markup=button1)

@dp.message(F.text == "Oddiy Burger🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?"
                                     "q=tbn:ANd9GcQbZNHm3_ABKibYIRmTtQn6A-kSvNtS1p-ing&s",
                                      caption="Narxi:20.000", reply_markup=button2)

@dp.message(F.text == "Ortacha burger🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.c"
                                     "om/images?q=tbn:ANd9GcTlcy0q-obN86MyKK6fjIyYgOVZ5yiG5RXn0A&s",
                              caption="Narxi:20.000", reply_markup=button3)

@dp.message(F.text == "Katta Burger🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com"
                                     "/images?q=tbn:ANd9GcTlcy0q-obN86MyKK6fjIyYgOVZ5yiG5RXn0A&s",
                                      caption="Narxi:20.000", reply_markup=button4)

@dp.message(F.text == "Kichkina Burger🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/i"
                                     "mages?q=tbn:ANd9GcRxIh4u49puF49usVAJxLr5qhbPGzKqdzjNYQ&s",
                                      caption="Narxi:20.000", reply_markup=button5)

@dp.message(F.text == "Achchiq Burger🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/ima"
                                     "ges?q=tbn:ANd9GcQbZNHm3_ABKibYIRmTtQn6A-kSvNtS1p-ing&s",
                                      caption="Narxi:20.000", reply_markup=button6)

@dp.message(F.text == "Coca-Cola🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZzYte2ea3j4bt2gEr7aOchK42vnBJh6wRtg&s",
                               caption="Narxi:6.000", reply_markup=button7)

@dp.message(F.text == "Pepsi🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsWdOHglLYYxPSU13kq-AE77z-tjxyPbOCoA&s",
                               caption="Narxi:6.000", reply_markup=button8)

@dp.message(F.text == "Fanta🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3gPdiVGOxzR2mTn1iac4Zr1uUXxuS4SHTUA&s",
                               caption="Narxi:6.000", reply_markup=button9)

@dp.message(F.text == "Sprite🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJNazMWEwceh-msgaEN8jKi_ljZJ2s5cCOpw&s",
                               caption="Narxi:6.000", reply_markup=button10)

@dp.message(F.text == "Oddiy Suv🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqNgV8eFA6NIAs3g-eFRgfzuGV1oAxgTz-cA&s",
                               caption="Narxi:2.000", reply_markup=button11)

@dp.message(F.text == "Gazli Suv🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYLBnbCqz6ULAcev9XyQUOR5KouGh8f5ePmQ&s",
                               caption="Narxi:5.000", reply_markup=button12)

@dp.callback_query(F.data == "1")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Sirli Burger")

@dp.callback_query(F.data == "2")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Oddiy Burger")

@dp.callback_query(F.data == "3")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Ortacha Burger")

@dp.callback_query(F.data == "4")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Katta burger")

@dp.callback_query(F.data == "5")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Kichkina Burger")

@dp.callback_query(F.data == "6")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Achchiq Burger")

@dp.callback_query(F.data == "6")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Achchiq Burger")

@dp.callback_query(F.data == "7")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Coca-Cola")

@dp.callback_query(F.data == "8")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Pepsi")

@dp.callback_query(F.data == "9")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Fanta")

@dp.callback_query(F.data == "10")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Sprite")

@dp.callback_query(F.data == "11")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Oddiy Suv")

@dp.callback_query(F.data == "12")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib oldingiz", reply_markup=main_button3)
    Karzina.append("Gazli Suv")

@dp.callback_query(F.data == "olmaslik")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("Siz Tovarni Sotib olmadingiz", reply_markup=main_button3)

@dp.message(F.text == "Biz haqimizda🍟")
async def super(message: types.Message):
    await  message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkoowwpQvzI0o58ATTxkD8-JFmQj8JHcNM1g&s",
                                caption="OqTepa Lavash работает на быстрорастущем рынке "
                                        "Республики Узбекистан и ориентирована на удовлет"
                                        "ворение растущего спроса рынка.Компания продемонс"
                                        "трировала отличные результаты за последние 10 лет "
                                        "и устойчиво растет за счет основного направления би"
                                        "знеса: Продукты питания и напитки.Более подробно 👇h"
                                        "ttps://oqtepalavash.uz", reply_markup=main_button3)

@dp.message(F.text == "Yordam🆘")
async def super(message: types.Message):
    await  message.answer("Agar yordam kerak bola Adminga murojat qiling:\n"
                          "998+ 99 999 99 99",
                          reply_markup=main_button3)

@dp.message(F.text == "Siz haqingizda🎫")
async def super(message: types.Message):
    await  message.answer(f"User:{message.from_user.username}\n"
                          f"ID:{message.from_user.id}\n"
                          f"Name:{message.from_user.full_name}")

@dp.message(F.text == "Karzina info🛒")
async def start(message: types.Message):
    await message.answer(f"{Karzina}")

@dp.message(F.text == "Sotib Olish")
async def super(message: types.Message):
    await  message.answer("Siz Tovarni sotib oldingiz! Tovaringiz Karzinada!", reply_markup=main_button3)

@dp.message(F.text == "Sotib Olmaslik")
async def super(message: types.Message):
    await  message.answer("Siz Tovarni Sotib Olmadingiz!", reply_markup=main_button3)

@dp.message(F.text == "Karzina🛒")
async def super(message: types.Message):
    await  message.answer("Siz Karzina Bolimidasiz Bu joyda siz "
                          "tovarlarni sotib olish yoki sotib olishni to"
                          "xtashitingiz mumkin", reply_markup=main_button8)

@dp.message(F.text == "Karzinani Sotib Olish🛒")
async def super(message: types.Message):
    await  message.answer("Siz Bu joyda tovarni kartadan sotib olsihingiz mumkin!", reply_markup=main_button9)


@dp.message(F.text == "Karzinani Sotib Olmaslik🛒")
async def super(message: types.Message):
    await  message.answer("Karzinadagi narsalar ochib ketti", reply_markup=main_button3)
    Karzina.clear()

@dp.message(F.text == "Humo💳")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz Humo kartangizni nomerini jonating")


@dp.message(F.text == "Tilni ozgartirish🏴")
async def start_function(message: types.Message):
    await message.answer("Siz til ozgartirish bolimidasiz", reply_markup=main_button19)

@dp.message(F.text == "Rus TilI🇷🇺")
async def start_function(message: types.Message):
    await message.answer("Siz Rus tili ni talladingiz!", reply_markup=main_button12)
    Karzina.clear()
@dp.message(F.text == "Uzbek TilI🇺🇿")
async def start_function(message: types.Message):
    await message.answer("Siz Uzbek tilini TAlladingiz!", reply_markup=main_button3)

@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'r", reply_markup=main_button2)
    Karzina.clear()
    await state.clear()


@dp.message(F.text == "UzCard💳")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Siz Uzcard kartangizni nomerini jonating")


@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'r", reply_markup=main_button2)
    Karzina.clear()
    await state.clear()

async def reg_one():
    pass
###################################################################################################################
#######################RUSSIAN$$$$$$$$$$#################

@dp.message(F.text == "Rus tili🇷🇺")
async def start_function(message: types.Message):
    await message.answer("вы выбрали русский язык!", reply_markup=main_button12)

@dp.message(F.text == "меню📖")
async def start_function(message: types.Message):
    await message.answer("эта наш меню!",
                       reply_markup=main_button13)

@dp.message(F.text == "возвращаться🔙")
async def start_function(message: types.Message):
    await message.answer("ты возвращаешься", reply_markup=main_button12)


@dp.message(F.text == "Бургеры🍔")
async def start_function(message: types.Message):
    await message.answer("ты в бургерном отделе!", reply_markup=main_button14)


@dp.message(F.text == "напитки🥤")
async def start_function(message: types.Message):
    await message.answer("вы находитесь в разделе напитков!", reply_markup=main_button15)

@dp.message(F.text == "Бургер🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlcy0q-obN86MyKK6fjIyYgOVZ5yiG5RXn0A&s",
                                      caption="расходы:20.000", reply_markup=button13)

@dp.message(F.text == "обычный бургер🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbZNHm3_ABKibYIRmTtQn6A-kSvNtS1p-ing&s",
                                      caption="расходы:20.000", reply_markup=button14)

@dp.message(F.text == "средний бургер🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlcy0q-obN86MyKK6fjIyYgOVZ5yiG5RXn0A&s",
                              caption="расходы:20.000", reply_markup=button15)

@dp.message(F.text == "большой бургер🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlcy0q-obN86MyKK6fjIyYgOVZ5yiG5RXn0A&s",
                                      caption="расходы:20.000", reply_markup=button16)

@dp.message(F.text == "маленький бургер🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxIh4u49puF49usVAJxLr5qhbPGzKqdzjNYQ&s",
                                      caption="расходы:20.000", reply_markup=button17)

@dp.message(F.text == "чили бургер🍔")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbZNHm3_ABKibYIRmTtQn6A-kSvNtS1p-ing&s",
                                      caption="расходы:20.000", reply_markup=button18)

@dp.message(F.text == "Кока-Кола🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZzYte2ea3j4bt2gEr7aOchK42vnBJh6wRtg&s",
                               caption="расходы:6.000", reply_markup=button19)

@dp.message(F.text == "пепси🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsWdOHglLYYxPSU13kq-AE77z-tjxyPbOCoA&s",
                               caption="расходы:6.000", reply_markup=button20)

@dp.message(F.text == "Фанта🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3gPdiVGOxzR2mTn1iac4Zr1uUXxuS4SHTUA&s",
                               caption="расходы:6.000", reply_markup=button21)

@dp.message(F.text == "спрайт🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJNazMWEwceh-msgaEN8jKi_ljZJ2s5cCOpw&s",
                               caption="расходы:6.000", reply_markup=button22)

@dp.message(F.text == "обычный чай🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqNgV8eFA6NIAs3g-eFRgfzuGV1oAxgTz-cA&s",
                               caption="расходы:2.000", reply_markup=button23)

@dp.message(F.text == "газированная вода🥤")
async def start_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYLBnbCqz6ULAcev9XyQUOR5KouGh8f5ePmQ&s",
                               caption="расходы:5.000", reply_markup=button24)

@dp.callback_query(F.data == "13")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("Бургер")

@dp.callback_query(F.data == "14")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("обычный бургер")

@dp.callback_query(F.data == "15")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("средний бургер")

@dp.callback_query(F.data == "16")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("большой бургер")

@dp.callback_query(F.data == "17")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("маленький бургер")

@dp.callback_query(F.data == "18")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("чили бургер")

@dp.callback_query(F.data == "19")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("Кока-Кола")

@dp.callback_query(F.data == "20")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("пепси")

@dp.callback_query(F.data == "21")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("фанта")

@dp.callback_query(F.data == "22")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("спрайт")

@dp.callback_query(F.data == "23")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("обычный вода")

@dp.callback_query(F.data == "24")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы купили этот товар ваш товар в корзине", reply_markup=main_button12)
    Karzina.append("газированная вода")


@dp.callback_query(F.data == "olmaslik1")
async def lavash(call: types.CallbackQuery):
    await call.message.answer("вы не купили этот товар", reply_markup=main_button12)



@dp.message(F.text == "O нас🍟")
async def super(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkoowwpQvzI0o58ATTxkD8-JFmQj8JHcNM1g&s",
                                caption="OqTepa Lavash работает на быстрорастущем рынке "
                                        "Республики Узбекистан и ориентирована на удовлет"
                                        "ворение растущего спроса рынка.Компания продемонс"
                                        "трировала отличные результаты за последние 10 лет "
                                        "и устойчиво растет за счет основного направления би"
                                        "знеса: Продукты питания и напитки.Более подробно 👇h"
                                        "ttps://oqtepalavash.uz", reply_markup=main_button12)

@dp.message(F.text == "помочь🆘")
async def super(message: types.Message):
    await message.answer("если нада помочь то звоните этому номеру:\n"
                          "998+ 99 999 99 99",
                          reply_markup=main_button12)

@dp.message(F.text == "о вас🎫")
async def super(message: types.Message):
    await message.answer(f"User:{message.from_user.username}\n"
                          f"ID:{message.from_user.id}\n"
                          f"Name:{message.from_user.full_name}", reply_markup=main_button12)

@dp.message(F.text == "Karzina info🛒")
async def start(message: types.Message):
    await message.answer(f"{Karzina}")

@dp.message(F.text == "купить")
async def super1(message: types.Message):
    await message.answer("вы купили товар, ваш товар в корзине!", reply_markup=main_button12)

@dp.message(F.text == "не купить")
async def super2(message: types.Message):
    await message.answer("вы не купили товар!", reply_markup=main_button12)

@dp.message(F.text == "Карзина🛒")
async def super3(message: types.Message):
    await message.answer("вы в карцином одделе", reply_markup=main_button17)

@dp.message(F.text == "купить карзину🛒")
async def super5(message: types.Message):
    await message.answer("вы здесь можете купить карзину", reply_markup=main_button18)

@dp.message(F.text == "не купить карзину🛒")
async def super(message: types.Message):
    await  message.answer("вы не купили карзину", reply_markup=main_button12)
    Karzina.clear()

@dp.message(F.text == "HUmo💳")
async def start_function(message: types.Message, state: FSMContext, isdigit):
    await state.set_state(Card.card_number)
    await message.answer("отпавьте номер карты")

@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'r4", reply_markup=main_button2)
    Karzina.clear()
    await state.clear()


@dp.message(F.text == "UzCarD💳")
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("отпавьте номер карты", reply_markup=main_button2)


@dp.message(Card.card_number)
async def card_number(message: types.Message, state: FSMContext):
    await state.update_data(card_number=message.text)
    await message.answer("Zo'r4", reply_markup=main_button12)
    Karzina.clear()
    await state.clear()

@dp.message(F.text == "изменение языка🏴")
async def start_function(message: types.Message):
    await message.answer("ты можешь менять языки", reply_markup=main_button20)

@dp.message(F.text == "Узбекиский язык🇺🇿")
async def start_function(message: types.Message):
    await message.answer("вы выбрали узбекиикий язык!", reply_markup=main_button3)

@dp.message(F.text == "Русский язык🇷🇺")
async def start_function(message: types.Message):
    await message.answer("вы выбрали русский язык!", reply_markup=main_button12)
    Karzina.clear()
async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())