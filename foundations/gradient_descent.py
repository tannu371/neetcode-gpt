class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for i in range(iterations):
            # Derivative:         f'(x) = 2x
            f_x_der = 2 * x
            # Update rule:        x = x - learning_rate * f'(x)
            x -= learning_rate * f_x_der
        # Round final answer to 5 decimal places
        return round(x, 5)