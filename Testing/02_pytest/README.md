# Звіт до роботи

## Тема: _Тестування з бібліотекою pytest_

### Мета роботи: _Ознайомитись з бібліотекою pytest, навчитись створювати параметризовані тести, використовувати fixtures і маркери та аналізувати помилки під час тестування._

---

### Виконання роботи

Виконав завдання з позначками :star: та :fire: з [матеріалів лабораторної роботи](https://github.com/BobasB/it_college/tree/main/notes/07_testing/02_pytest).

1. Створив окреме віртуальне середовище та встановив бібліотеку `pytest`:

   ```powershell
   cd C:\Users\Redpaw\Desktop\College-OOP-And-Testing-Repo\Testing\02_pytest
   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install pytest
   ```

   Роботу перевірив з `Python 3.14.7` та `pytest 9.2.0`. Версію бібліотеки записав у файл `requirements-dev.txt`.

2. Створив клас `Figure` у файлі `app.py`. Він підтримує квадрат, прямокутник та трикутник. Властивості повертають тип фігури, довжину її сторони та кількість кутів.

   Доповнив перевірку довжини: вона має бути додатним скінченним числом типу `int` або `float`. Значення `bool` не приймаються, хоча в Python цей тип є підкласом `int`. Для неправильних даних використав `AssertionError`, як у навчальному прикладі.

3. :star: Додав параметризований тест для всіх дозволених фігур:

   ```python
   @pytest.mark.parametrize(
       "figure_type", Figure.FIGURES, ids=["square", "rectangle", "triangle"]
   )
   def test_allowed_figure(figure_type):
       assert Figure(figure_type, 1).type == figure_type
   ```

   Одна функція виконується тричі. Параметр `ids` задає зрозумілі назви випадків у результатах запуску. Окремо перевірив правильні довжини `1`, `10`, `2.5` та `0.1`.

4. :star: Створив fixture `square`, яка повертає квадрат з довжиною `10`:

   ```python
   @pytest.fixture
   def square():
       return Figure("квадрат", 10)
   ```

   У тесті перевірив її властивості:

   ```python
   @pytest.mark.unit
   def test_square_properties(square):
       assert square.type == "квадрат"
       assert square.get_figure_type == "квадрат"
       assert square.get_figure_length == 10
       assert square.get_angles == 4
   ```

   Fixture розмістив у `conftest.py`. Pytest знаходить її самостійно та передає результат через аргумент `square`. За замовчуванням використовується `scope="function"`, тому кожен тест, який її запитує, отримує окремий об'єкт. [Документація fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html).

5. :fire: Додав окремі параметризовані перевірки неправильного типу фігури та неправильної довжини. Кожен набір даних відображається як окремий тестовий випадок.

   Для типу фігури перевірив `"коло"`, `"шестикутник"`, порожній рядок, назву у верхньому регістрі, назву з пробілами, `None`, число, `True`, список та словник. У всіх десяти випадках виникає `AssertionError` з повідомленням `Невідомий тип фігури`.

   Для довжини перевірив такі групи даних:

   | Дані | Очікуване повідомлення |
   | --- | --- |
   | `0`, `-1`, `-2.5` | `Довжина має бути більшою за 0!` |
   | `"10"`, `""`, `None`, `True`, `False`, список, словник, комплексне число | `Довжина має бути числом!` |
   | `NaN`, додатна та від'ємна нескінченність | `Довжина має бути скінченним числом!` |

   Тест перевіряє і клас винятку, і відповідну частину повідомлення:

   ```python
   def test_invalid_length(length, message):
       with pytest.raises(AssertionError, match=message):
           Figure("квадрат", length)
   ```

   Параметри для цієї функції задав через `pytest.mark.parametrize` у файлі `test_app.py`. Під час перевірки неправильного типу фігури довжина завжди правильна, а під час перевірки довжини завжди використовується дозволений тип фігури.

6. :star: Додав маркер `unit` до двох тестів: `test_triangle_type` та `test_square_properties`. Зареєстрував його у `pyproject.toml`:

   ```toml
   [tool.pytest.ini_options]
   testpaths = ["."]
   python_files = ["test_*.py", "*_test.py"]
   addopts = "--strict-markers"
   markers = [
       "unit: швидкі юніт-тести",
   ]
   ```

   Параметр `--strict-markers` допомагає помітити незареєстрований маркер. Запустив лише позначені тести:

   ```powershell
   .\.venv\Scripts\python.exe -m pytest -m unit -v
   ```

   Результат:

   ```text
   collecting ... collected 35 items / 33 deselected / 2 selected

   test_app.py::test_triangle_type PASSED                                   [ 50%]
   test_app.py::test_square_properties PASSED                               [100%]

   ====================== 2 passed, 33 deselected in 0.06s =======================
   ```

   Інші 33 випадки не запускались, тому що не мають маркера `unit`. [Документація маркерів](https://docs.pytest.org/en/stable/how-to/mark.html).

7. :star: Створив fixture зі `scope="module"` та використав її у двох тестах:

   ```python
   @pytest.fixture(scope="module")
   def shared_rectangle():
       return Figure("прямокутник", 10)


   def test_module_fixture_type(shared_rectangle):
       assert shared_rectangle.get_figure_type == "прямокутник"


   def test_module_fixture_length(shared_rectangle):
       assert shared_rectangle.get_figure_length == 10
   ```

   Для перевірки життєвого циклу fixture виконав команду:

   ```powershell
   .\.venv\Scripts\python.exe -m pytest -k module_fixture -v --setup-show
   ```

   Фрагмент результату:

   ```text
   test_app.py::test_module_fixture_type
       SETUP    M shared_rectangle
           test_app.py::test_module_fixture_type (fixtures used: shared_rectangle) PASSED
   test_app.py::test_module_fixture_length
           test_app.py::test_module_fixture_length (fixtures used: shared_rectangle) PASSED
       TEARDOWN M shared_rectangle

   ====================== 2 passed, 33 deselected in 0.05s =======================
   ```

   `SETUP M` з'явився один раз перед першим тестом, а `TEARDOWN M` — один раз після другого. Обидва тести використали один об'єкт прямокутника. Тести лише читають його властивості та не змінюють спільні дані.

8. :fire: Навмисно зламав тест `test_square_properties`: замінив очікувану довжину `10` на `11` та виконав команду:

   ```powershell
   .\.venv\Scripts\python.exe -m pytest -x --tb=short
   ```

   Фрагмент фактичного результату:

   ```text
   collected 35 items

   test_app.py .F

   ___________________________ test_square_properties ____________________________
   test_app.py:15: in test_square_properties
       assert square.get_figure_length == 11
   E   assert 10 == 11
   ```

   ```text
   FAILED test_app.py::test_square_properties - assert 10 == 11
   !!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!
   ========================= 1 failed, 1 passed in 0.17s =========================
   ```

   Перший тест пройшов, а другий завершився помилкою, тому що справжня довжина дорівнює `10`. Параметр `-x` зупинив виконання після першої невдачі, тому решта 33 випадки не запускались. `--tb=short` скоротив traceback, залишивши місце помилки та невдале порівняння. Код завершення цього запуску — `1`.

   Після досліду повернув очікуване значення `10` та повторно запустив усі тести. Повний вивід досліду зберіг у [pytest_intentional_failure.txt](results/pytest_intentional_failure.txt).

---

### Відповіді на питання

1. **Чим відрізняється тест `unittest.TestCase` від функції `pytest`?**

   У `unittest` створюється клас, який наслідується від `unittest.TestCase`, а перевірки записуються методами на зразок `self.assertEqual()`. Для pytest достатньо звичайної функції з назвою `test_` та виразу `assert`:

   ```python
   # unittest
   class TestFigure(unittest.TestCase):
       def test_length(self):
           self.assertEqual(10, Figure("квадрат", 10).get_figure_length)


   # pytest
   def test_length():
       assert Figure("квадрат", 10).get_figure_length == 10
   ```

   Приклад передбачає відповідні імпорти `unittest` та `Figure`. У попередній роботі для підготовки об'єкта використовував `setUp`, а тут використав fixtures. Для кількох наборів даних у `unittest` застосовував `subTest`, а в pytest — `pytest.mark.parametrize`.

2. **Для чого потрібна параметризація?**

   Вона дозволяє виконати одну тестову функцію з різними даними. Кожен набір має власний результат, тому видно, яке саме значення спричинило помилку. У цій роботі так перевірив дозволені фігури, правильні довжини та неправильні дані.

3. **Що робить fixture та чим відрізняються її області дії?**

   Fixture готує дані або ресурси для тестів. `function` створює результат окремо для кожного тесту, `class` — для тестового класу, `module` — для модуля, `package` — для пакета, а `session` — для всього запуску. У роботі використав `function` для квадрата та `module` для спільного прямокутника.

4. **Як запустити лише потрібні тести та знайти помилку?**

   `-m unit` вибирає тести за маркером, `-k module_fixture` — за частиною назви. Конкретний тест можна запустити через `test_app.py::test_triangle_type`. Параметр `--collect-only` показує знайдені тести без виконання, `-v` деталізує результат, `-x` зупиняє запуск після першої невдачі, а `--tb=short` скорочує traceback. [Документація запуску pytest](https://docs.pytest.org/en/stable/how-to/usage.html).

---

### Команди запуску

З кореневої папки репозиторію:

```powershell
cd Testing\02_pytest
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m pytest -m unit -v
.\.venv\Scripts\python.exe -m pytest -k module_fixture -v --setup-show
.\.venv\Scripts\python.exe -m pytest test_app.py::test_triangle_type -v
```

Активація середовища не потрібна, тому що команди прямо викликають його інтерпретатор.

### Результат виконання тестів

Після відновлення навмисно зламаного тесту виконав повний запуск з `-v`:

```text
collecting ... collected 35 items

test_app.py::test_triangle_type PASSED                                   [  2%]
test_app.py::test_square_properties PASSED                               [  5%]
test_app.py::test_allowed_figure[square] PASSED                          [  8%]
test_app.py::test_allowed_figure[rectangle] PASSED                       [ 11%]
test_app.py::test_allowed_figure[triangle] PASSED                        [ 14%]
test_app.py::test_valid_length[1] PASSED                                 [ 17%]
test_app.py::test_valid_length[10] PASSED                                [ 20%]
test_app.py::test_valid_length[2.5] PASSED                               [ 22%]
test_app.py::test_valid_length[0.1] PASSED                               [ 25%]
test_app.py::test_invalid_figure[circle] PASSED                          [ 28%]
test_app.py::test_invalid_figure[hexagon] PASSED                         [ 31%]
test_app.py::test_invalid_figure[empty] PASSED                           [ 34%]
test_app.py::test_invalid_figure[uppercase] PASSED                       [ 37%]
test_app.py::test_invalid_figure[spaces] PASSED                          [ 40%]
test_app.py::test_invalid_figure[none] PASSED                            [ 42%]
test_app.py::test_invalid_figure[integer] PASSED                         [ 45%]
test_app.py::test_invalid_figure[boolean] PASSED                         [ 48%]
test_app.py::test_invalid_figure[list] PASSED                            [ 51%]
test_app.py::test_invalid_figure[dictionary] PASSED                      [ 54%]
test_app.py::test_invalid_length[zero] PASSED                            [ 57%]
test_app.py::test_invalid_length[negative-integer] PASSED                [ 60%]
test_app.py::test_invalid_length[negative-float] PASSED                  [ 62%]
test_app.py::test_invalid_length[string] PASSED                          [ 65%]
test_app.py::test_invalid_length[empty-string] PASSED                    [ 68%]
test_app.py::test_invalid_length[none] PASSED                            [ 71%]
test_app.py::test_invalid_length[true] PASSED                            [ 74%]
test_app.py::test_invalid_length[false] PASSED                           [ 77%]
test_app.py::test_invalid_length[list] PASSED                            [ 80%]
test_app.py::test_invalid_length[dictionary] PASSED                      [ 82%]
test_app.py::test_invalid_length[complex] PASSED                         [ 85%]
test_app.py::test_invalid_length[nan] PASSED                             [ 88%]
test_app.py::test_invalid_length[positive-infinity] PASSED               [ 91%]
test_app.py::test_invalid_length[negative-infinity] PASSED               [ 94%]
test_app.py::test_module_fixture_type PASSED                             [ 97%]
test_app.py::test_module_fixture_length PASSED                           [100%]

============================= 35 passed in 0.07s ==============================
```

Усі 35 тестових випадків пройшли без попереджень. Повний вивід знаходиться у [pytest_verbose.txt](results/pytest_verbose.txt). Результати окремих запусків зберіг у [pytest_unit.txt](results/pytest_unit.txt) та [pytest_module_fixture.txt](results/pytest_module_fixture.txt).

---

### Структура роботи

```text
02_pytest/
├── .gitignore
├── app.py
├── conftest.py
├── test_app.py
├── pyproject.toml
├── requirements-dev.txt
├── README.md
└── results/
    ├── pytest_verbose.txt
    ├── pytest_unit.txt
    ├── pytest_module_fixture.txt
    └── pytest_intentional_failure.txt
```

Результат виконання коду знаходиться у файлах [app.py](app.py), [test_app.py](test_app.py) та [conftest.py](conftest.py). Віртуальне середовище та кеші виключив з відстеження Git через локальний `.gitignore`.

---

### Висновок:

- Ознайомився з бібліотекою `pytest` та навчився створювати тести у вигляді звичайних функцій.
- Попрактикувався у використанні параметризації, fixtures та маркерів.
- Перевірив правильні, граничні та неправильні дані класу `Figure`.
- Дослідив повторне використання fixture зі `scope="module"` у двох тестах.
- Навмисно зламав тест, пояснив результат запуску з `-x --tb=short` та відновив правильну перевірку.
---
