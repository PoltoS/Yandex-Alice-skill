MYSQL_SERVERNAME = 'localhost'
MYSQL_USERNAME = ''
MYSQL_PASSWORD = ''
MYSQL_DBNAME = ''
TABLE_users = 'users'
TABLE_home_devices = 'home_devices'
TABLE_user_homes = 'user_homes'
TABLE_user_requests = 'user_requests'
FIND_SERVER = 'https://find.z-wave.me'

HOME_STATE_NEW = 0
HOME_STATE_REMOTEID = 1
HOME_STATE_REMOTEID_USERNAME = 2
HOME_STATE_REMOTEID_USERNAME_PASSWORD = 3
HOME_STATE_READY = 4

COMMAND_EXECUTION_STATUS_NOT_YET = 0
COMMAND_EXECUTION_STATUS_SUCCESS = 1
COMMAND_EXECUTION_STATUS_FAILURE = 2

TEXT_REGISTER_NEW = 'Контроллер умного дома ещё не подключен. Для подключения мне понадобится знание идентификатора' \
                    ' удалённого доступа, имени пользователя и пароля. Я не рекомендую регистрироваться под учётной ' \
                    'записью администратора, а создать отдельного пользователя. Начнём с идентификатора удалённого ' \
                    'доступа. Он написан над формой логина при входе в личный кабинет контроллера.'

TEXT_REGISTER_NEW_SUPPORTED_CONTROLLERS_BUTTON = 'Список поддерживаемых контроллеров'

TEXT_REGISTER_NEW_SUPPORTED_CONTROLLERS = 'Данный навык Алисы работает с контроллерами на базе Z-Way: Z-Wave.Me RaZberry и Hub, Popp Hub, Z-Way для Western Digital, Z-Way для Dune HD'

TEXT_REGISTER_INVALID_REMOTE_ID = 'Введите идентификатора удалённого доступа. Он имеет числовой формат и написан над формой логина при входе в личный кабинет контроллера.'

TEXT_REGISTER_USERNAME = 'Теперь введи имя пользователя. ' \
                         'Для ввода имени пользователя лучше воспользоваться клавиатурой.'

TEXT_REGISTER_USERNAME_REPEAT = 'Нужно ввести имя пользователя контроллеру.'

TEXT_REGISTER_PASSWORD = 'И пароль. Для ввода пароля тоже лучше воспользоваться клавиатурой.'

TEXT_REGISTER_PASSWORD_REPEAT = 'Нужно ввести пароль контроллеру.'

TEXT_REGISTER_READY = 'Контроллер успешно добавлен.'

TEXT_REGISTER_FAILED = 'Не удалось подключиться. Давай попробуем ещё раз. Идентификатор удалённого доступа.'

TEXT_WELCOME = 'Слушаю тебя, мой господин'

TEXT_UNKNOWN_COMMAND = 'Не понимаю. Если нужна помощь, скажи слово помощь.'

TEXT_UNKNOWN_DEVICE = 'Не могу понять, о каком устройстве идет речь.' \
                      ' Устройства нужно назывть ровно так, как они записаны в контроллере.'

TEXT_UNKNOWN_ERROR = 'Что-то пошло не так.'


class Configuration(object):
    SECRET_KEY = 'so_secret!'
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = False
    TEMPLATES_AUTO_RELOAD = True
