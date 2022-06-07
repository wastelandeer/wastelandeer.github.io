import os
import sys
sys.path.append(os.curdir)
# from settings import EMAIL, LINKEDIN, GITHUB, TELEGRAM
import settings

AUTHOR = 'wastelandeer'
SITENAME = 'Resume project'
CSS_FILE = 'pdf-ready.css'
RELATIVE_URLS = True
PATH = 'content'
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'content/theme'
IGNORE_FILES = ['theme']
# Resume info
NAME = 'Виталий Грищенков'
TAGLINE = 'QA Automation Engineer'
PIC = 'Avatara.jpg'
EMAIL = settings.EMAIL
LINKEDIN = settings.LINKEDIN
GITHUB = settings.GITHUB
TELEGRAM = settings.TELEGRAM
EDUCATIONS = [
    {
        'degree': 'История',
        'meta': 'Волгоградский Государственный Университет',
        'time': '2001-2007'
    },
    {
        'degree': 'Средняя школа',
        'meta': '',
        'time': '2001'
    }
]
LANGUAGES = [
    {
        'name': 'Русский',
        'description': 'Родной язык'
    },
    {
        'name': 'Английский',
        'description': 'Itermediate B1'
    }
]
INTERESTS = ['Игры', 'Чтение', 'Кино']
EXPERIENCES = [
    {
        'job_title': 'QA Automation Engineer',
        'time': 'Февраль 2022 - Июнь 2022',
        'company': 'Playrix',
        'details': 'Продолжил закрывать зону ответственности по ручному тестированию. Разрабатываю автоматизированные UI тесты. Поддерживаю и развиваю тестовый фреймворк на базе Python и RobotFramework.'
    },
    {
        'job_title': 'QA Engineer',
        'time': 'Ноябрь 2019 - Февраль 2022',
        'company': 'Playrix',
        'details': 'Занимался ручным тестированием внутренних веб-сервисов компании. Тестировал и frontend, и backend. Проводил технические интервью при найме новых сотрудников. Участвовал в планировании разработки новых сервисов и новой функциональности существующих сервисов. Был наставником для новых коллег. Разрабатывал и поддерживал тестовую документацию. Занимался нагрузочным тестированием внутренних сервисов.'
    },
    {
        'job_title': 'QA Engineer',
        'time': 'Июнь 2018 - Ноябрь 2019',
        'company': 'Playrix',
        'details': 'Занимался ручным тестированием внутренних утилит. Занимался тестированием "движка" компании. Разрабатывал и поддерживал в актуальном состоянии тестовую документацию.'
    },
    {
        'job_title': 'QA Outsource',
        'time': 'Октябрь 2017 - Июнь 2018',
        'company': 'Playrix',
        'details': 'Занимался ручным тестированием игровых проектов компании. Проверял исправление багов. Проверял функциональность по готовым тест-кейсам. Тестировал корректность локализации.'
    },
    {
        'job_title': 'System Administrator',
        'time': 'Сентябрь 2010 - Ноябрь 2013',
        'company': 'СТК',
        'details': 'Администрировал Linux/Windows сервера. Администрировал сетевое оборудование. Обеспечивал техническую поддержку пользователей.'
    }
]
SKILLS = [
    {
        'title': 'Ручное тестирование',
        'level': '50'
    },
    {
        'title': 'Автоматизированное тестирование',
        'level': '50'
    },
    {
        'title': 'TestRail',
        'level': '50'
    },
    {
        'title': 'TestIT',
        'level': '50'
    },
    {
        'title': 'RobotFramework',
        'level': '50'
    },
    {
        'title': 'REST API',
        'level': '50'
    },
    {
        'title': 'POSTGRESQL',
        'level': '50'
    },
    {
        'title': 'Docker',
        'level': '50'
    },
    {
        'title': 'JavaScript',
        'level': '50'
    },
    {
        'title': 'Python',
        'level': '50'
    },
    {
        'title': 'CI/CD',
        'level': '50'
    },
    {
        'title': 'TeamCity',
        'level': '50'
    },
    {
        'title': 'Artillery (HTTP load testing)',
        'level': '50'
    },
    {
        'title': 'Proxy',
        'level': '50'
    },
    {
        'title': 'pytest',
        'level': '50'
    },
    {
        'title': 'Selenium',
        'level': '50'
    },
    {
        'title': 'Playwright',
        'level': '50'
    },
    {
        'title': 'Puppeteer',
        'level': '50'
    },
    {
        'title': 'Appium',
        'level': '50'
    },
    {
        'title': 'git',
        'level': '50'
    },
    {
        'title': 'Github',
        'level': '50'
    }
]