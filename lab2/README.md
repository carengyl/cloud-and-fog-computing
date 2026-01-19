
# Minikube
```
curl -LO https://storage.googleapis.com/minikube/
releases/latest/minikube-linux-amd64
```
```
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

# kubectl
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```
```
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
# Запуск minikube
```
minikube start --driver=docker
```
# Проверка
```
kubectl get nodes
```

# Собрать образ
```
docker build -t lab1-frontend:latest ./frontend
```
# Загрузить в Minikube registry
```
minikube image load lab1-frontend:latest
```

# Ход работы
### Шаг 1: Запуск Minikube
```bash
minikube start --driver=docker
```

### Шаг 2: Сборка и загрузка образов
```bash
# Собрать v1
docker build -t lab1-frontend:v1 ./frontend
minikube image load lab1-frontend:v1

# Собрать v2 (с голубым фоном)
cp frontend/app-v2.py frontend/app.py  # Подменяем файл
docker build -t lab1-frontend:v2 ./frontend
cp frontend/app.py frontend/app-v2.py  # Возвращаем обратно
minikube image load lab1-frontend:v2
```

### Шаг 3: Деплой приложения v1
```bash
kubectl apply -f kubernetes/redis-deployment.yaml
kubectl apply -f kubernetes/redis-service.yaml
kubectl apply -f kubernetes/frontend-deployment.yaml
kubectl apply -f kubernetes/frontend-service.yaml
```

### Шаг 4: Проверка
```bash
kubectl get pods
kubectl get services
minikube service frontend-service --url
```

### Шаг 5: Rolling Update до v2
```bash
kubectl apply -f kubernetes/update-frontend-deployment-v2.yaml
```

### Шаг 6: Наблюдение за обновлением
```bash
# Смотрим, как поды обновляются постепенно
kubectl get pods -w

# Описание деплоймента для проверки стратегии
kubectl describe deployment frontend-deployment
```

### Шаг 7: Проверка работы
```bash
# Получить URL сервиса
minikube service frontend-service --url

# Открыть в браузере
# Обновите страницу несколько раз, увидите как счетчик увеличивается
# И как постепенно меняется цвет фона при обновлении подов
```

---

## Очистка после лабораторной работы №2
```bash
# Удалить все ресурсы
kubectl delete -f kubernetes/

# Остановить Minikube
minikube stop

# Удалить Minikube кластер (опционально)
minikube delete
```
