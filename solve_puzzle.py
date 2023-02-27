def solve_puzzle(arr): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    last_index = len(arr) - 1

    visited = set()

    def solve_inner(current_index):
        if current_index == last_index:
            return True
        
        if current_index in visited:
            return False
        
        visited.add(current_index)

        step_size = arr[current_index]

        right_index = (current_index + step_size) % len(arr)
        left_index = (current_index - step_size) % len(arr)
        
        return solve_inner(left_index) or solve_inner(right_index)
    
    return solve_inner(0)
