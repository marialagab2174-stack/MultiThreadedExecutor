import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
import time

class MultiThreadedNode(Node):
    def __init__(self):
        super().__init__('multithreaded_executor_node')
        
        # Utilisation d'un ReentrantCallbackGroup pour permettre l'exécution parallèle
        self.group = ReentrantCallbackGroup()

        # Timer Rapide (50ms)
        self.timer_fast = self.create_timer(0.05, self.fast_callback, callback_group=self.group)
        
        # Timer Lent (500ms)
        self.timer_slow = self.create_timer(0.5, self.slow_callback, callback_group=self.group)
        
        self.get_logger().info('Démarrage du MultiThreadedExecutor Node...')
        self.get_logger().info('Les deux callbacks devraient s\'exécuter en parallèle sans se bloquer.')

    def fast_callback(self):
        self.get_logger().info('--- Callback RAPIDE (50ms) ---')

    def slow_callback(self):
        self.get_logger().warn('>>> DEBUT Callback LENT (Simule un traitement de 500ms)')
        time.sleep(0.5)
        self.get_logger().warn('<<< FIN Callback LENT')

def main(args=None):
    rclpy.init(args=args)
    node = MultiThreadedNode()
    
    # Utilisation explicite du MultiThreadedExecutor
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
