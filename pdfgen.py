import os
import sys
sys.path.append(os.curdir)
# from settings import EMAIL, LINKEDIN, GITHUB, TELEGRAM
import settings
from settings import OPEN_TO_WORK, LANG

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
NAME = {
    'ru': 'Виталий Грищенков',
    'en': 'Vitaliy Grishchenkov'
}
TAGLINE = 'QA Automation Engineer'
PIC = 'Avatara.jpg'
EMAIL = settings.EMAIL
LINKEDIN = settings.LINKEDIN
GITHUB = settings.GITHUB
TELEGRAM = settings.TELEGRAM

EDUCATIONS = {
    'ru': [
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
    ],
    'en': [
        {
            'degree': 'History',
            'meta': 'Volgograd State University',
            'time': '2001-2007'
        },
        {
            'degree': 'High school',
            'meta': '',
            'time': '2001'
        }
    ]
}

LANGUAGES = {
    'ru': [
        {
            'name': 'Русский',
            'description': 'Родной язык'
        },
        {
            'name': 'Английский',
            'description': 'Itermediate B1'
        }
    ],
    'en': [
        {
            'name': 'Russian',
            'description': 'Native language'
        },
        {
            'name': 'English',
            'description': 'Itermediate B1'
        }
    ]
}

INTERESTS = {
    'ru': ['Игры', 'Чтение', 'Кино'],
    'en': ['Video games', 'Science fiction', 'Fantasy', 'Great movies']
}
EXPERIENCES = {
    'ru': [
        {
            'job_title': 'Senior QA Engineer',
            'time': 'Август 2022 - Настоящее время',
            'company': 'Тиньков Центр Разработки Минск',
            'details': 'Стартовал интеграционное автоматизированное тестирование в команде разработки. Закрываю задачи по ручному тестированию. Самостоятельно чиню небольшие баги. Пишу при необходимости функционал, облегчающий тестирование систем. Провожу код-ревью разрабатываемых фич. Представляю роль QA в активности "три амиго". Взаимодействую с внешними поставщиками сервисов и добиваюсь починки багов, обнаруженных во время тестирования интеграции с ними.'
        },
        {
            'job_title': 'QA Automation Engineer',
            'time': 'Февраль 2022 - Июнь 2022',
            'company': 'Playrix',
            'details': 'Продолжил закрывать зону ответственности по ручному тестированию. Разрабатывал автоматизированные UI тесты. Поддерживал и развивал тестовый фреймворк на базе Python и RobotFramework.'
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
    ],
    'en': [
        {
            'job_title': 'Senior QA Engineer',
            'time': 'August 2022 - Present time',
            'company': 'Tinkov Development Center',
            'details': 'I have founded integration automated testing within the development team. I am managing tasks for manual testing. I am writing functionality, if necessary, to facilitate system testing. I am conducting code reviews of developed features and representing the QA role in "three amigos" activities. I am interacting with external service providers and ensuring the fixing of bugs identified during integration testing with them.'
        },
        {
            'job_title': 'QA Automation Engineer',
            'time': 'February 2022 - June 2022',
            'company': 'Playrix',
            'details': 'Continued to cover the area of responsibility for manual testing. Developed automated UI tests. Maintained and further developed a testing framework based on Python and RobotFramework.'
        },
        {
            'job_title': 'QA Engineer',
            'time': 'November 2019 - February 2022',
            'company': 'Playrix',
            'details': 'I was involved in manual testing of internal web services of the company both on frontend and backend side. I conducted technical interviews when hiring new employees. Participated in planning the development of new services and new functionality for existing services. Acted as a mentor for new colleagues. Developed and maintained testing documentation. I started load testing of internal services in our team.'
        },
        {
            'job_title': 'QA Engineer',
            'time': 'June 2018 - November 2019',
            'company': 'Playrix',
            'details': 'I was involved in manual testing of internal utilities. Conducted testing of the companys "engine". Developed and maintained up-to-date testing documentation.'
        },
        {
            'job_title': 'QA Outsource',
            'time': 'October 2017 - June 2018',
            'company': 'Playrix',
            'details': 'I was involved in manual testing of the company gaming projects. Verified bug fixes. Checked functionality against prepared test cases. Tested the correctness of localization.'
        },
        {
            'job_title': 'System Administrator',
            'time': 'September 2010 - November 2013',
            'company': 'STK',
            'details': 'Administered Linux/Windows servers. Administered network equipment. Provided technical support to users.'
        }
    ]
}

SKILLS = [
    {
        'title': 'Manual testing',
        'level': '50'
    },
    {
        'title': 'Automated testing',
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
        'title': 'CI/CD pipeline',
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
    },
    {
        'title': 'Java',
        'level': '50'
    },
    {
        'title': 'Kotlin',
        'level': '50'
    },
    {
        'title': 'Gitlab',
        'level': '50'
    },
    {
        'title': 'Grpc API',
        'level': '50'
    },
    {
        'title': 'JUnit',
        'level': '50'
    },
    {
        'title': 'Testcontainers',
        'level': '50'
    },
    {
        'title': 'Allure Test Ops',
        'level': '50'
    }
]