#API: Сервис поиска ближайших машин для перевозки грузов.

<aside>
🔥 Необходимо разработать REST API сервиc для поиска ближайших машин к грузам.

</aside>

◼Стек и требования:

- **Python** (Django Rest Framework / FastAPI) на выбор.
- **DB** - Стандартный PostgreSQL.
- Приложение должно запускаться в docker-compose без дополнительных доработок.
- Порт - 8000.
- БД по умолчанию должна быть заполнена 20 машинами.
- Груз обязательно должен содержать следующие характеристики:
    - локация pick-up;
    - локация delivery;
    - вес (1-1000);
    - описание.
- Машина обязательно должна в себя включать следующие характеристики:
    - уникальный номер (цифра от 1000 до 9999 + случайная заглавная буква английского алфавита в конце, пример: "
      1234A", "2534B", "9999Z")
    - текущая локация;
    - грузоподъемность (1-1000).
- Локация должна содержать в себе следующие характеристики:
    - город;
    - штат;
    - почтовый индекс (zip);
    - широта;
    - долгота.

> *Список уникальных локаций представлен в прикрепленном csv файле "uszips.csv".*
>
> *Необходимо осуществить выгрузку списка в базу данных Postgres при запуске приложения.*

- При создании машин по умолчанию локация каждой машины заполняется случайным образом;
- Расчет и отображение расстояния осуществляется в милях;
- Расчет расстояния должен осуществляться с помощью библиотеки geopy. help(geopy.distance). Маршруты не учитывать,
  использовать расстояние от точки до точки.

<aside>
⭐ Задание разделено на 2 уровня сложности. Дедлайн по времени выполнения зависит от того, сколько уровней вы планируете выполнить.
</aside>

### Уровень 1

Сервис должен поддерживать следующие базовые функции:

- [x] Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);
- [x] Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));
- [x] Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин
  с расстоянием до выбранного груза);
- [x] Редактирование машины по ID (локация (определяется по введенному zip-коду));
- [x] Редактирование груза по ID (вес, описание);
- [x] Удаление груза по ID.

### Уровень 2

Все что в уровне 1 + дополнительные функции:

- Фильтр списка грузов (вес, мили ближайших машин до грузов);
- Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную).

### **Критерии оценки:**

- Адекватность архитектуры приложения;
- Оптимизация работы приложения.

----

### Как запустить проект
#### Создать .env в корне проекта
```
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=host.docker.internal
DB_PORT=5432
```
#### Выполнить команду 
```bash
docker compose up --build 
```

### Примеры запросов:

#### - Получить список грузов

```
GET - http://localhost/api/cargos/
```

#### Ответ

```json
{
  "id": 1,
  "pick_up_location": {
    "city": "Coamo",
    "state": "Puerto Rico",
    "zip_code": "00769",
    "latitude": 18.09459,
    "longitude": -66.3607
  },
  "delivery_location": {
    "city": "Las Piedras",
    "state": "Puerto Rico",
    "zip_code": "00771",
    "latitude": 18.18797,
    "longitude": -65.86916
  },
  "weight": 124,
  "description": "Груз 1",
  "nearest_cars_count": 2
}

```

#### - Создание нового груза

```
POST - http://localhost/api/cargos/
```
```json
{
    "pick_up_location": "99705",
    "delivery_location": "01079",
    "weight": 156,
    "description": "Описание"
}
```


#### Ответ

```json
{
    "pick_up_location": "99705",
    "delivery_location": "01079",
    "weight": 156,
    "description": "Описание"
}

```

#### - Получить информацию о грузе по ID

```
GET - http://localhost/api/cargos/<id>/
```

#### Ответ

```json
{
    "id": 1,
    "pick_up_location": {
        "city": "Coamo",
        "state": "Puerto Rico",
        "zip_code": "00769",
        "latitude": 18.09459,
        "longitude": -66.3607
    },
    "delivery_location": {
        "city": "Las Piedras",
        "state": "Puerto Rico",
        "zip_code": "00771",
        "latitude": 18.18797,
        "longitude": -65.86916
    },
    "weight": 124,
    "description": "Описание груза",
    "car_distances": [
        {
            "car_number": "2391N",
            "distance": 1741.7072000898597
        },
        {
            "car_number": "9021L",
            "distance": 3038.160193413027
        }
    ]
}
```
#### - Редактирование груза по id

```
PATCH - http://localhost/api/cargos/<id>/
```
```json
{
    "weight": 500,
    "description": "Новое описание"
}
```


#### Ответ

```json
{
    "weight": 500,
    "description": "Новое описание"
}

```
#### - Удаление груза по id

```
DELETE - http://localhost/api/cargos/<id>/
```
#### - Редактирование машины по id

```
PATCH - http://localhost/api/cars/<id>/
```
```json
{
    "number": "7689N",
    "load_capacity": 124,
    "current_location": 11560
}
```


#### Ответ

```json
{
    "id": 1,
    "number": "7689N",
    "load_capacity": 124,
    "current_location": 11560
}

```
