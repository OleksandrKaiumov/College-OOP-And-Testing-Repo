# Звіт до роботи
## Тема: _Віртуальні середовища_
### Мета роботи: _Ознайомитись з віртуальними сердовищами у Python та навчитися використовувати їх та бібліотеки що працюють з ними._

---
### Виконання роботи
   1. Передивився які дії можна зробити за допомогою `pip`. Перевірив які бібліотеки вже інстальовані на компютері;
   ![alt text](1.png)
   
   2. Виконав команди на скріншоті або стрічки;
   ![alt text](2.png)
   3. Ознайомився які ще методи є в бібліотеці `requests`, та спробував їх використати;
   4. Виконав наступні команди
   ```bash
   pip show requests
   pip install requests==2.1
   pip show requests
   pip uninstall requests
   ```
   ![alt text](3.png)
   5. Для любителів Аніме, можна поекспериментувати з бібліотекою `jikanpy` яка є АПІ для роботи з Аніме сайтом MyAnimeList.net та запустити наступний код який виведе оцінки епізодів Аніме серіалу:
      - спочатку інсталюйте бібліотеку `jikanpy` та `Flask` за допомогою:
        ```bash
        pip install jikanpy-v4 Flask
        ```
      - створіть файл `anime.py` та вставте в нього наступний код: 
        ```python
        from flask import Flask, render_template
        from jikanpy import Jikan

        jikan = Jikan()
        app = Flask(__name__)

        j = jikan.anime(54595, extension='episodes')

        @app.route('/')
        def home():
            a = str()
            for episode in j["data"]: 
                a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
            return a

        @app.route('/about')
        def about():
            return render_template('about.html')

        if __name__ == '__main__':
            app.run(debug=True)
        ```
    - 
   6. Запустив програму вище;
   ![alt text](4.png)
   7. Спробував знайти які аніме серіали виходять у цьому сезоні та вивести їх оцінки за допомогою бібліотеки `jikanpy`;
   8. Команда pip show requests мала такий результат тому що я деактивував віртуальне середовище і опинився в глобальному середовищі python.
      ```bash
      Name: requests
      Version: 2.33.1
      Summary: Python HTTP for Humans.
      Home-page:
      Author:
      Author-email: Kenneth Reitz <me@kennethreitz.org>
      License: Apache-2.0
      Location: C:\Users\kaium\AppData\Local\Programs\Python\Python313\Lib\site-packages
      Requires: certifi, charset_normalizer, idna, urllib3
      Required-by: jikanpy-v4
      ```
   9. Для VENV середовища потрібно ігнорувати кореневі папки середовищ, щоб Git не відстежував встановлені пакети та службові файли.
   10. Спробував створити віртуальне середовище, встановити бібілотеки jikanpy та Flask та запустити програму з попереднього завдання через Visual Studio.
   ![alt text](4.png)
   11. Команди, які можна виконувати за допомогою `pipenv`.
   ![alt text](5.png)
   12. Переконався що створились файли Pipfile та Pipfile.lock. Вони потрібні для керування залежностями Python проєкту. `Pipfile` описує основні залежності проєкту `Pipfile.lock` фіксує точні версії всіх пакетів.
   13. Результат виконання програми у VS Code, cmd та pipenv shell:
   ```html
   b'<!DOCTYPE html>'
b'<html lang="en">'
b''
b'<head>'
b'    <meta charset="UTF-8">'
b'    <title>httpbin.org</title>'
b'    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"'
b'        rel="stylesheet">'
b'    <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">'
b'    <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />'
b'    <style>'
b'        html {'
b'            box-sizing: border-box;'
b'            overflow: -moz-scrollbars-vertical;'
b'            overflow-y: scroll;'
b'        }'
b''
b'        *,'
b'        *:before,'
b'        *:after {'
b'            box-sizing: inherit;'
b'        }'
b''
b'        body {'
b'            margin: 0;'
b'            background: #fafafa;'
b'        }'
b'    </style>'
b'</head>'
b''
b'<body>'
b'    <a href="https://github.com/requests/httpbin" class="github-corner" aria-label="View source on Github">'
b'        <svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;"'
b'            aria-hidden="true">'
b'            <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>'
b'            <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"'
b'                fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>'
b'            <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"'
b'                fill="currentColor" class="octo-body"></path>'
b'        </svg>'
b'    </a>'
b'    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="position:absolute;width:0;height:0">'
b'        <defs>'
b'            <symbol viewBox="0 0 20 20" id="unlocked">'
b'                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V6h2v-.801C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8z"></path>'
b'            </symbol>'
b''
b'            <symbol viewBox="0 0 20 20" id="locked">'
b'                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8zM12 8H8V5.199C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8z"'
b'                />'
b'            </symbol>'
b''
b'            <symbol viewBox="0 0 20 20" id="close">'
b'                <path d="M14.348 14.849c-.469.469-1.229.469-1.697 0L10 11.819l-2.651 3.029c-.469.469-1.229.469-1.697 0-.469-.469-.469-1.229 0-1.697l2.758-3.15-2.759-3.152c-.469-.469-.469-1.228 0-1.697.469-.469 1.228-.469 1.697 0L10 8.183l2.651-3.031c.469-.469 1.228-.469 1.697 0 .469.469.469 1.229 0 1.697l-2.758 3.152 2.758 3.15c.469.469.469 1.229 0 1.698z"'
b'                />'
b'            </symbol>'
b''
b'            <symbol viewBox="0 0 20 20" id="large-arrow">'
b'                <path d="M13.25 10L6.109 2.58c-.268-.27-.268-.707 0-.979.268-.27.701-.27.969 0l7.83 7.908c.268.271.268.709 0 .979l-7.83 7.908c-.268.271-.701.27-.969 0-.268-.269-.268-.707 0-.979L13.25 10z"'
b'                />'
b'            </symbol>'
b''
b'            <symbol viewBox="0 0 20 20" id="large-arrow-down">'
b'                <path d="M17.418 6.109c.272-.268.709-.268.979 0s.271.701 0 .969l-7.908 7.83c-.27.268-.707.268-.979 0l-7.908-7.83c-.27-.268-.27-.701 0-.969.271-.268.709-.268.979 0L10 13.25l7.418-7.141z"'
b'                />'
b'            </symbol>'
b''
b''
b'            <symbol viewBox="0 0 24 24" id="jump-to">'
b'                <path d="M19 7v4H5.83l3.58-3.59L8 6l-6 6 6 6 1.41-1.41L5.83 13H21V7z" />'
b'            </symbol>'
b''
b'            <symbol viewBox="0 0 24 24" id="expand">'
b'                <path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z" />'
b'            </symbol>'
b''
b'        </defs>'
b'    </svg>'
b''
b''
b'    <div id="swagger-ui">'
b'        <div data-reactroot="" class="swagger-ui">'
b'            <div>'
b'                <div class="information-container wrapper">'
b'                    <section class="block col-12">'
b'                        <div class="info">'
b'                            <hgroup class="main">'
b'                                <h2 class="title">httpbin.org'
b'                                    <small>'
b'                                        <pre class="version">0.9.2</pre>'
b'                                    </small>'
b'                                </h2>'
b'                                <pre class="base-url">[ Base URL: httpbin.org/ ]</pre>'
b'                            </hgroup>'
b'                            <div class="description">'
b'                                <div class="markdown">'
b'                                    <p>A simple HTTP Request &amp; Response Service.'
b'                                        <br>'
b'                                        <br>'
b'                                        <b>Run locally: </b>'
b'                                        <code>$ docker run -p 80:80 kennethreitz/httpbin</code>'
b'                                    </p>'
b'                                </div>'
b'                            </div>'
b'                            <div>'
b'                                <div>'
b'                                    <a href="https://kennethreitz.org" target="_blank">the developer - Website</a>'
b'                                </div>'
b'                                <a href="mailto:me@kennethreitz.org">Send email to the developer</a>'
b'                            </div>'
b'                        </div>'
b'                        <!-- ADDS THE LOADER SPINNER -->'
b'                        <div class="loading-container">'
b'                            <div class="loading"></div>'
b'                        </div>'
b''
b'                    </section>'
b'                </div>'
b'            </div>'
b'        </div>'
b'    </div>'
b''
b''
b"    <div class='swagger-ui'>"
b'        <div class="wrapper">'
b'            <section class="clear">'
b'                <span style="float: right;">'
b'                    [Powered by'
b'                    <a target="_blank" href="https://github.com/rochacbruno/flasgger">Flasgger</a>]'
b'                    <br>'
b'                </span>'
b'            </section>'
b'        </div>'
b'    </div>'
b''
b''
b''
b'    <script src="/flasgger_static/swagger-ui-bundle.js"> </script>'
b'    <script src="/flasgger_static/swagger-ui-standalone-preset.js"> </script>'
b"    <script src='/flasgger_static/lib/jquery.min.js' type='text/javascript'></script>"
b'    <script>'
b''
b'        window.onload = function () {'
b'            '
b''
b'            fetch("/spec.json")'
b'                .then(function (response) {'
b'                    response.json()'
b'                        .then(function (json) {'
b'                            var current_protocol = window.location.protocol.slice(0, -1);'
b'                            if (json.schemes[0] != current_protocol) {'
b'                                // Switches scheme to the current in use'
b'                                var other_protocol = json.schemes[0];'
b'                                json.schemes[0] = current_protocol;'
b'                                json.schemes[1] = other_protocol;'
b''
b'                            }'
b'                            json.host = window.location.host;  // sets the current host'
b''
b'                            const ui = SwaggerUIBundle({'
b'                                spec: json,'
b'                                validatorUrl: null,'
b"                                dom_id: '#swagger-ui',"
b'                                deepLinking: true,'
b'                                jsonEditor: true,'
b'                                docExpansion: "none",'
b'                                apisSorter: "alpha",'
b'                                //operationsSorter: "alpha",'
b'                                presets: ['
b'                                    SwaggerUIBundle.presets.apis,'
b'                                    // yay ES6 modules \xe2\x86\x98'
b'                                    Array.isArray(SwaggerUIStandalonePreset) ? SwaggerUIStandalonePreset : SwaggerUIStandalonePreset.default'
b'                                ],'
b'                                plugins: ['
b'                                    SwaggerUIBundle.plugins.DownloadUrl'
b'                                ],'
b'            '
b'            // layout: "StandaloneLayout"  // uncomment to enable the green top header'
b'        })'
b''
b'        window.ui = ui'
b''
b'        // uncomment to rename the top brand if layout is enabled'
b'        // $(".topbar-wrapper .link span").replaceWith("<span>httpbin</span>");'
b'        })'
b'    })'
b'}'
b"    </script>  <div class='swagger-ui'>"
b'    <div class="wrapper">'
b'        <section class="block col-12 block-desktop col-12-desktop">'
b'            <div>'
b''
b'                <h2>Other Utilities</h2>'
b''
b'                <ul>'
b'                    <li>'
b'                        <a href="/forms/post">HTML form</a> that posts to /post /forms/post</li>'
b'                </ul>'
b''
b'                <br />'
b'                <br />'
b'            </div>'
b'        </section>'
b'    </div>'
b'</div>'
b'</body>'
b''
b'</html>'
   ```
   14. Вибрав бібліотеку `Rich` на `Pypi` та інсталював її. Виконав базовий приклад.
   ![alt text](7.png)
   15. Змінив інтерпретатор Python та виконав скрипт через кнопку `Run`.
   ![alt text](8.png)
   16. Результатом виконання flake8 є такі помилки у моєму коді. Виправив ці помилки.
   ```bash
   .\rich_example.py:3:75: W292 no newline at end of file
.\script.py:5:16: W292 no newline at end of file
   ```
   17. Результат виконання команд `pipenv check --scan` та `pipenv audit`. Вразливості не знайдено.
   ![alt text](9.png)
   18. Якщо виконати скрипт без активації віртуального середовища, то отримаємо помилку про те, що значення IT_TEST не існує в поточному середовищі.
   19. Результат виконання `poetry` команд.
   ![alt text](10.png)
   20. Створіив програму для цього проекту та запустив її у віртуальному середовищі створеному а допомогою `poetry`.

---
### Результатом виконання коду:
Результат виконання коду у звіті відповідно до завдань.

---
### Висновок:
- Ознайомитився з віртуальними сердовищами у Python та навчився використовувати їх та бібліотеки що працюють з ними.
---