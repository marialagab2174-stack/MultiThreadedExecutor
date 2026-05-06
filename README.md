# Challenge : Multi-Threaded Executor 🧵

Ce package démontre la gestion de la concurrence sous **ROS 2 Jazzy**. L'objectif est d'empêcher un traitement long de bloquer les tâches rapides du robot.

## 🎯 Objectifs
- Créer un nœud avec deux timers : **Lent (500ms)** et **Rapide (50ms)**.
- Configurer un `ReentrantCallbackGroup` pour autoriser le parallélisme.
- Utiliser `MultiThreadedExecutor` pour distribuer les tâches sur plusieurs threads.

## 💡 Pourquoi c'est important ?
Sans ces outils, le callback lent bloquerait l'exécution du callback rapide. Grâce au `MultiThreadedExecutor`, les logs montrent que le message "RAPIDE" continue de s'afficher même pendant que le traitement "LENT" est en cours.

## 🛠 Compilation
```bash
cd ~/ros2_ws
colcon build --packages-select MultiThreadedExecutor
source install/setup.bash
```

## 🚀 Exécution
Lancer via le fichier Launch :
```bash
ros2 launch MultiThreadedExecutor executor_launch.py
```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent
