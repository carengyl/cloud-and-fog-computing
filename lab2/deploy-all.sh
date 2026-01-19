#!/bin/bash

# Переходим в директорию с манифестами
cd kubernetes

echo "1. Запускаем Redis..."
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml

echo "2. Собираем образ frontend v1..."
cd ../frontend
docker build -t lab1-frontend:v1 .

echo "3. Загружаем образ в Minikube..."
minikube image load lab1-frontend:v1

echo "4. Запускаем frontend v1..."
cd ../kubernetes
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml

echo "5. Проверяем..."
kubectl get pods
kubectl get services

echo "6. Доступ к приложению:"
minikube service frontend-service --url

echo "Готово! Приложение доступно по адресу выше."