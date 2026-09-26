# Звіт до роботи
## Тема: _Загальне тестування та юніт-тести_
### Мета роботи: _Ознайомитись з перевіркою даних та модулем unittest, навчитись створювати юніт-тести, перевіряти винятки та використовувати subTest і mock._

---
### Виконання роботи
   1. Створив функцію `validate_positive_number()`, яка перевіряє введене значення. Якщо передати додатне число `8`, функція повертає `8`. Для від'ємного числа `-3` виникає `ValueError` з повідомленням `Число має бути більшим за нуль`. Якщо передати рядок замість числа, виникає `ValueError` з повідомленням `Потрібно ввести число`.

   2. Створив функцію `count_vowels()`, яка рахує англійські та українські голосні літери без врахування регістру:
      ```python
      def count_vowels(text: str) -> int:
          vowels = set("aeiouyаеиіоуяюєї")
          return sum(symbol in vowels for symbol in text.casefold())
      ```
      Написав для неї шість тестів. Перевірив звичайний англійський текст, рядок без голосних, великі літери, порожній рядок, рядок з цифрами та рядок з українськими літерами.

   3. Створив клас `Figure` та перевірив властивості `get_figure_type` і `get_figure_length`. Під час перевірки помилкової реалізації властивість довжини повертала `self.type` замість `self.length`, тому тест не пройшов:
      ```text
      test_figure_length (test.TestFigure.test_figure_length) ... FAIL

      AssertionError: 5 != 'квадрат'

      Ran 1 test in 0.001s
      FAILED (failures=1)
      ```
      Після виправлення властивість повертає правильне значення:
      ```python
      @property
      def get_figure_length(self) -> int | float:
          return self.length
      ```

   4. Додав властивість `get_angles`, яка повертає кількість кутів фігури. Для квадрата і прямокутника вона повертає `4`, а для трикутника — `3`.

   5. Додав тести для нульової довжини, від'ємної довжини та невідомого типу фігури. У кожному випадку перевіряється виникнення `AssertionError` та частина повідомлення помилки.

   6. Додав тест із `subTest` для всіх типів `Figure`:
      ```python
      for figure_type, angles in expected_angles.items():
          with self.subTest(figure_type=figure_type):
              figure = Figure(figure_type, 2)
              self.assertEqual(figure_type, figure.get_figure_type)
              self.assertEqual(angles, figure.get_angles)
      ```

   7. Створив функцію `read_positive_number()` з використанням `input()`. За допомогою `patch` передав значення `7` без ручного введення, перевірив результат функції та те, що `input()` був викликаний один раз. Окремо перевірив неправильне значення `-1`.

---
### Відповіді на питання
   1. `assert` перевіряє твердження. Якщо умова хибна, виникає `AssertionError`. У класі `Figure` він використаний для перевірки довжини й типу фігури.
   2. `raise ValueError` доцільно використовувати, коли функція отримала значення правильного типу операції, але неправильне за змістом. У моєму прикладі так перевіряється число, яке не є додатним.
   3. `setUp` виконується перед кожним тестовим методом, тому кожен тест отримує новий незалежний об'єкт `Figure`. `tearDown` виконується після кожного тесту. `setUpClass` і `tearDownClass` виконуються один раз до та після всіх тестів класу.
   4. `subTest` дозволяє виконати одну перевірку для кількох наборів даних. Якщо один набір не пройде, unittest покаже конкретне значення `figure_type`, а інші набори все одно будуть перевірені.
   5. `mock.patch` тимчасово замінює зовнішню залежність. У цій роботі він замінює `builtins.input`, тому тест не чекає ручного введення та завжди отримує передбачуване значення.
   6. Юніт-тести повинні бути незалежними та повторюваними, щоб результат одного тесту не залежав від порядку запуску або результатів інших тестів.

---
### Команди запуску
```bash
cd Testing/01_general_and_unittest
python test.py
python -m unittest -v
```

### Результат виконання тестів
```text
test_empty_string (test.TestCountVowels.test_empty_string) ... ok
test_english_text (test.TestCountVowels.test_english_text) ... ok
test_string_with_digits (test.TestCountVowels.test_string_with_digits) ... ok
test_text_without_vowels (test.TestCountVowels.test_text_without_vowels) ... ok
test_ukrainian_letters (test.TestCountVowels.test_ukrainian_letters) ... ok
test_uppercase_letters (test.TestCountVowels.test_uppercase_letters) ... ok
test_all_figure_types_with_subtest (test.TestFigure.test_all_figure_types_with_subtest) ... ok
test_figure_length (test.TestFigure.test_figure_length) ... ok
test_figure_type (test.TestFigure.test_figure_type) ... ok
test_negative_length (test.TestFigure.test_negative_length) ... ok
test_unknown_figure (test.TestFigure.test_unknown_figure) ... ok
test_zero_length (test.TestFigure.test_zero_length) ... ok
test_read_incorrect_number (test.TestInputWithMock.test_read_incorrect_number) ... ok
test_read_positive_number (test.TestInputWithMock.test_read_positive_number) ... ok
test_correct_number (test.TestNumberValidation.test_correct_number) ... ok
test_incorrect_number (test.TestNumberValidation.test_incorrect_number) ... ok
test_not_a_number (test.TestNumberValidation.test_not_a_number) ... ok

Ran 17 tests in 0.003s

OK
```

---
### Структура роботи
```text
01_general_and_unittest/
├── app.py
├── test.py
└── README.md
```

Результат виконання коду знаходиться у файлах [app.py](app.py) та [test.py](test.py).

---
### Висновок:
- Ознайомився з перевіркою даних за допомогою `assert` та винятків.
- Навчився створювати й запускати юніт-тести з використанням модуля `unittest`.
- Попрактикувався у перевірці правильних, граничних та неправильних даних.
- Навчився використовувати `subTest` для наборів даних та `patch` для заміни функції `input()`.
---
