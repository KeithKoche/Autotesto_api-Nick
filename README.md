# Autotesto_api-Nick
Репозиторий содержит решение домашнего задания по теме №4 "Тестирование API. REST, restful, SOAP, типы запросов"

Папка "dz_4_1_KNE" содержит набор автотестов к API-сервису https://dog.ceo/dog-api/
Название набора: dz_4_1dog.py
Тесты в наборе: 
                test_status_code -- проверка статус-кода при валидном ответе
                test_list_all_breeds_app_j -- проверка заголовка Content-Type
                test_list_all_breeds_schema -- валидация json-схемы общего метода на возврат всех пород
                test_breed_not_exists -- проверка отсутствия лишних пород
                test_some_subbreed -- проверка фильтра видов по подвидам

Папка "dz_4_2_KNE" содержит набор автотестов к API-сервису https://www.openbrewerydb.org/
Название набора: dz_4_2brew.py
Тесты в наборе:
                test_brew_status_code -- проверка статус-кода при валидном ответе
                test_app_json_brew_utf -- проверка заголовка Content-Type
                test_brew_json_schema -- валидация json-схемы общего метода на возврат всех ЛКЗ
                test_single_brew_by_id -- проверка получения ЛКЗ по id
                test_brew_by_city_names -- проверка вывода ЛКЗ из заданного диапазона по атрибуту names

Папка "dz_4_3_KNE" содержит набор автотестов к API-сервису https://jsonplaceholder.typicode.com/
Название набора: dz_4_3ph.py
Тесты в наборе:
                test_ph_status_code -- проверка статус-кода
                test_ph_json_utf -- проверка заголовка Content-Type
                test_ph_json_schema -- валидация json-схемы метода на возврат поста пользователя
                test_ph_comments -- проверка выборки комментов из диапазона
                test_ph_return_user_by_id --  проверка на возврат пользователя по id

Папка "dz_4_4_KNE" содержит тестовую функцию для проверки статус-кода при отклике адреса https://ya.ru с динамическими 
вариациями, задаваемыми через командную строку
Название тестового файла/функции: dz_4_4sq.py / test_valide_status_code