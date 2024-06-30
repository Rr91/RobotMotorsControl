#  RobotMotorsControl

## Описание проекта

Проекта RobotMotorsControl содержит скрипт для управления простейщим роботом

## Описание работы с Git


- Создаем репозиторий в интерфейсе github.
- Добавляем в настройки github ssh токен созданный командой 
```yaml 
ssh-keygen
```
- Клонируем репозиторий с github на локальный компьютер командой
```yaml 
git clone
```
- После создания/изменения файлов их нужно добавить в промежуточную область командой 
```yaml 
git add
```
- Далее делаем коммит для сохранения изменений
```yaml 
git commit -m 'Comment'
```
- Для отправки изменений в репозиторий github используем команду 
```yaml 
git push
```
- Для добавление улучшений используем новую ветку. Команда для создания и переключения на новую ветку
```yaml 
git checkout -b feature_branch_name
```
- После завершения доработок делаем коммит и сохраняем на github c созданием там соответствубщей ветки
```yaml 
git push --set-upstream origin feature_branch_name
```
- Создаем пул-реквест в интерфейсе github

