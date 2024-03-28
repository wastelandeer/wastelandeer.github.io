from envparse import env

env.read_envfile()

EMAIL = env('EMAIL', '')
LINKEDIN = env('LINKEDIN', '')
GITHUB = env('GITHUB', '')
TELEGRAM = env('TELEGRAM', '')

OPEN_TO_WORK = True
LANG = 'en'