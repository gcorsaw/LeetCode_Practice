class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        Rows, Columns = len(isInfected), len(isInfected[0])
        total_walls = 0
        
        while True:
            visited = set()
            regions = []       # Stores the coordinates of infected cells in each region
            frontiers = []     # Stores the unique uninfected cells threatened by each region
            walls_needed = []  # Stores the number of walls needed to isolate each region
            
            # 1. Find all disconnected infected regions using BFS
            for row in range(Rows):
                for column in range(Columns):
                    if isInfected[row][column] == 1 and (row, column) not in visited:
                        # Start a BFS for a new region
                        queue = [(row, column)]
                        region = {(row, column)}
                        visited.add((row, column))
                        frontier = set()
                        walls = 0
                        
                        while queue:
                            current_row, current_column = queue.pop(0)
                            # FIX 1: Use dr and dc consistently
                            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                                neighbor_row, neighbor_column = current_row + dr, current_column + dc
                                if 0 <= neighbor_row < Rows and 0 <= neighbor_column < Columns:
                                    if isInfected[neighbor_row][neighbor_column] == 1 and (neighbor_row, neighbor_column) not in visited:
                                        visited.add((neighbor_row, neighbor_column))
                                        region.add((neighbor_row, neighbor_column))
                                        queue.append((neighbor_row, neighbor_column))
                                    elif isInfected[neighbor_row][neighbor_column] == 0:
                                        frontier.add((neighbor_row, neighbor_column))
                                        walls += 1 # Every adjacent 0 requires a wall segment
                                        
                        regions.append(region)
                        frontiers.append(frontier)
                        walls_needed.append(walls)
            
            # FIX 3: Return if no infected regions are left to process
            if not regions:
                return total_walls
                
            # 2. Identify the most dangerous region (threatens the most uninfected cells)
            max_threat_idx = 0
            for i in range(1, len(frontiers)):
                if len(frontiers[i]) > len(frontiers[max_threat_idx]):
                    max_threat_idx = i
                    
            # If the most dangerous region threatens 0 cells, no more spreading is possible
            if len(frontiers[max_threat_idx]) == 0:
                return total_walls
                
            # 3. Contain the most dangerous region
            total_walls += walls_needed[max_threat_idx]
            for row, column in regions[max_threat_idx]:
                isInfected[row][column] = -1 # Mark as permanently contained / walled off
                
            # 4. Spread the remaining regions into their frontiers
            for i in range(len(regions)):
                if i == max_threat_idx:
                    continue
                for row, column in frontiers[i]:
                    # FIX 2: Fixed 'r' to 'row'
                    isInfected[row][column] = 1 

        return total_walls
