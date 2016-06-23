# ToDoApp
Система для управления задачами, которая отображает изменения в реальном времени для всех, кто в данный момент открыл сайт (аналог: trello). Основной экран представляет из себя набор областей, между которыми можно перетаскивать карточки задач. При этом, когда карточка меняет область или порядок в области, это изменение отображается у всех, кто в данный момент открыл основной экран. Аналогично изменение атрибутов карточки (заголовок, комментарии, исполнитель и тд) отображается в реальном времени.

1. Создание проектов и задач. (Сделано)
2. Комментирование задач. (Сделано)
3. Назначение исполнителя и срока сдачи. (Сделано)
4. Изменения отображаются в реальном времени для всех пользователей, просматривающих проект. (Сделано)
5. Проект работает на PostgreSQL. (Сделано)

Чтобы запустить проект нужно

1. Установить PostgreSQL.
2. Пройти все шаги здесь: https://github.com/DjangoGirls/tutorial-extensions/blob/master/optional_postgresql_installation/README.md, название базы данных - todoapp, пользователь - julia. 
Если у Ваc MAC OS, и возникает проблема с невозможностью загрузки какой-то билиотеки из-за картинки, то добавляем эту строчку в ~/.bash_profile
```
export DYLD_FALLBACK_LIBRARY_PATH=$HOME/anaconda/lib/:$DYLD_FALLBACK_LIBRARY_PATH
```

3. В папке ToDoApp
```
python manage.py runserver
```
