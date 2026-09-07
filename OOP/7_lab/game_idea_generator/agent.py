from random import choice
from google.adk.agents.llm_agent import Agent
from google.genai.types import GenerateContentConfig


def generate_game_idea(genre: str, platform: str = "PC", players: int = 1) -> dict:
    """
    Генерує базову ідею для гри за жанром, платформою та кількістю гравців.

    Args:
        genre: жанр гри, наприклад RPG, Puzzle, Horror, Strategy, Adventure
        platform: платформа гри, наприклад PC, Mobile, Console
        players: кількість гравців

    Returns:
        dict: структурована ідея гри або повідомлення про помилку
    """

    if not genre or genre.strip() == "":
        return {
            "status": "error",
            "error": "Жанр гри не може бути порожнім",
            "result": None
        }

    if not platform or platform.strip() == "":
        return {
            "status": "error",
            "error": "Платформа гри не може бути порожньою",
            "result": None
        }

    if players < 1:
        return {
            "status": "error",
            "error": "Кількість гравців має бути більшою або дорівнювати 1",
            "result": None
        }

    genre = genre.strip().lower()
    platform = platform.strip()

    settings = [
        "покинуте космічне місто",
        "магічний ліс, який змінюється щоночі",
        "підводна цивілізація",
        "кіберпанковий мегаполіс",
        "середньовічне королівство після катастрофи",
        "школа для винахідників",
        "планета, де час рухається назад"
    ]

    mechanics = [
        "гравець відкриває нові здібності через дослідження світу",
        "кожне рішення змінює сюжет і поведінку персонажів",
        "ігровий світ перебудовується після кожного рівня",
        "ресурси обмежені, тому потрібно планувати кожен крок",
        "персонаж має унікальну силу, але вона має небезпечні наслідки",
        "гравець комбінує предмети для створення нових можливостей"
    ]

    goals = [
        "врятувати світ від поступового зникнення",
        "знайти джерело дивної енергії",
        "розкрити таємницю головного героя",
        "побудувати безпечне поселення",
        "перемогти систему, яка контролює життя людей",
        "повернути втрачені спогади"
    ]

    unique_features = [
        "сюжет змінюється залежно від стилю гри користувача",
        "вороги навчаються на діях гравця",
        "кожен рівень генерується випадково",
        "гравець може змінювати правила світу",
        "персонажі пам’ятають попередні дії гравця",
        "фінал залежить не від перемог, а від моральних рішень"
    ]

    title_words = [
        "Echo", "Shadow", "Nova", "Chrono", "Crystal", "Last", "Hidden", "Broken"
    ]

    title_objects = [
        "Realm", "Signal", "Forest", "Protocol", "Kingdom", "Memory", "Island", "Machine"
    ]

    title = f"{choice(title_words)} {choice(title_objects)}"

    idea = {
        "title": title,
        "genre": genre,
        "platform": platform,
        "players": players,
        "setting": choice(settings),
        "main_mechanic": choice(mechanics),
        "goal": choice(goals),
        "unique_feature": choice(unique_features)
    }

    return {
        "status": "success",
        "error": None,
        "result": idea
    }


def generate_game_mechanic(game_type: str) -> dict:
    """
    Генерує ігрову механіку для заданого типу гри.

    Args:
        game_type: тип гри, наприклад survival, puzzle, rpg, strategy

    Returns:
        dict: опис ігрової механіки або повідомлення про помилку
    """

    if not game_type or game_type.strip() == "":
        return {
            "status": "error",
            "error": "Тип гри не може бути порожнім",
            "mechanic": None
        }

    game_type = game_type.strip().lower()

    mechanics_by_type = {
        "survival": [
            "гравець має контролювати голод, енергію та температуру",
            "ресурси поступово зникають, тому потрібно досліджувати нові території",
            "кожна ніч стає небезпечнішою за попередню"
        ],
        "puzzle": [
            "гравець змінює напрямок гравітації для проходження рівнів",
            "кожна дія відкриває одну можливість, але блокує іншу",
            "головоломки будуються навколо керування часом"
        ],
        "rpg": [
            "навички персонажа розвиваються залежно від дій, а не від рівнів",
            "репутація змінює ставлення NPC до гравця",
            "предмети мають історію та можуть впливати на сюжет"
        ],
        "strategy": [
            "гравець керує містом з обмеженими ресурсами",
            "вороги адаптують тактику після кожної битви",
            "успіх залежить від дипломатії, економіки та оборони"
        ]
    }

    selected_mechanics = mechanics_by_type.get(
        game_type,
        [
            "гравець поступово відкриває нові правила світу",
            "ігрові рішення мають довготривалі наслідки",
            "основна механіка поєднує дослідження, ризик і винагороду"
        ]
    )

    return {
        "status": "success",
        "game_type": game_type,
        "mechanic": choice(selected_mechanics)
    }


def estimate_game_scope(team_size: int, development_months: int, complexity: str) -> dict:
    """
    Оцінює приблизний масштаб гри за розміром команди, часом розробки та складністю.

    Args:
        team_size: кількість людей у команді
        development_months: кількість місяців на розробку
        complexity: складність гри: low, medium або high

    Returns:
        dict: рекомендація щодо масштабу гри або повідомлення про помилку
    """

    if team_size < 1:
        return {
            "status": "error",
            "error": "Команда має містити хоча б одну людину",
            "recommendation": None
        }

    if development_months < 1:
        return {
            "status": "error",
            "error": "Кількість місяців має бути більшою або дорівнювати 1",
            "recommendation": None
        }

    complexity = complexity.strip().lower()

    if complexity not in ["low", "medium", "high"]:
        return {
            "status": "error",
            "error": "Складність має бути: low, medium або high",
            "recommendation": None
        }

    score = team_size * development_months

    if complexity == "high":
        score -= 6
    elif complexity == "medium":
        score -= 3

    if score <= 3:
        recommendation = "Дуже маленька гра: один рівень, одна основна механіка, мінімум графіки."
    elif score <= 8:
        recommendation = "Невелика інді-гра: кілька рівнів, проста система прогресу, базовий сюжет."
    elif score <= 15:
        recommendation = "Середній проєкт: декілька механік, персонажі, меню, збереження прогресу."
    else:
        recommendation = "Більший проєкт: можна додати сюжетну кампанію, різні режими та складніші системи."

    return {
        "status": "success",
        "team_size": team_size,
        "development_months": development_months,
        "complexity": complexity,
        "recommendation": recommendation
    }


root_agent = Agent(
    model="gemini-3.1-flash-lite-preview",
    name="game_idea_generator",
    description="Агент для генерації ідей комп’ютерних та мобільних ігор.",
    instruction="""
    Ти агент-генератор ідей для ігор.

    Твоє завдання:
    - допомагати створювати концепції нових ігор;
    - пропонувати жанр, сетинг, основну механіку, ціль гри та унікальну особливість;
    - відповідати українською мовою;
    - давати структуровану відповідь;
    - не писати занадто довго, якщо користувач не просить детальний опис.

    Формат відповіді для ідеї гри:
    1. Назва гри
    2. Жанр
    3. Платформа
    4. Короткий опис
    5. Основна механіка
    6. Мета гравця
    7. Унікальна особливість

    Використовуй інструмент generate_game_idea, коли користувач просить придумати ідею гри.
    Використовуй інструмент generate_game_mechanic, коли користувач просить придумати окрему механіку.
    Використовуй інструмент estimate_game_scope, коли користувач питає, наскільки складною може бути гра для певної команди або терміну.
    Якщо користувач дає некоректні дані, поясни помилку простими словами.
    """,
    tools=[
        generate_game_idea,
        generate_game_mechanic,
        estimate_game_scope
    ],
    generate_content_config=GenerateContentConfig(
        temperature=1.2,
        top_k=40,
        top_p=0.95,
    )
)