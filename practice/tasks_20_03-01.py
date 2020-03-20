"""
Нужно реализовать ORM (объектно-реляционная модель, набор классов, которым
можно описать нужную систему) для интернет-магазина. Функционал магазина:
1. Каталог товаров (товар: название, описание, цена, оценки покупателей, отзывы
покупателей);
2. Зарегистрированные покупатели (пользователь: имя, фамилия, телефон, оценки
товаров, отзывы о товарах, заказы);
3. Заказы (заказ: клиент, товары, дата оформления, статус)

План:
1. Сделать конструкторы для всех основных классов
1.1. Создать тестовые экземпляры основных классов (листы объектов)
2. Сделать конструкторы для всех дополнительных классов
3. Реализовать метод формирования заказа у пользователя
4. Реализовать метод оценки товара
5. Реализовать метод составления отзыва
"""

from datetime import date


class User:
    def __init__(self, name, s_name, phone):
        self.name = name
        self.s_name = s_name
        self.phone = phone
        self.marks = list()
        self.reviews = list()
        self.orders = list()

    def make_order(self, goods):
        new_order = Order(user=self, goods=goods)
        self.orders.append(new_order)

    def make_mark(self, good, mark):
        new_mark = Mark(user=self, good=good, mark=mark)
        self.marks.append(new_mark)

    def make_review(self, good, text):
        new_review = Review(user=self, good=good, text=text)
        self.reviews.append(new_review)


class Good:
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price
        self.marks = list()
        self.reviews = list()

    def __str__(self):
        return f"{self.name} ({self.desc}) - {self.price}"


class Order:
    def __init__(self, user, goods):
        self.user = user
        self.goods = goods
        self.date = date.today()
        self.status = "new"


class Mark:
    def __init__(self, user, good, mark):
        self.author = user
        self.good = good
        self.mark = mark
        good.marks.append(self)


class Review:
    def __init__(self, user, good, text):
        self.author = user
        self.good = good
        self.text = text
        good.reviews.append(self)

    def __str__(self):
        return f"\nReview for {self.good.name}\n{self.text}\nAuthor: {self.author.name}"


u = [
    User("Yehor", "Levchenko", 101),
    User("Guido", "Van Rossum", 102),
]
g = [
    Good("Apple", "an apple", 35),
    Good("Toilet paper", "everyone needs it!", 55)
]

y = u[0]
paper = g[1]
y.make_order([paper])

print(f"{y.name} wants to buy {y.orders[0].goods[0]}")
print(f"{y.name} will pay {y.orders[0].goods[0].price}")

y.make_review(paper, "Nice! 10/10 will buy again!")
print(f"{y.reviews[0]}")
