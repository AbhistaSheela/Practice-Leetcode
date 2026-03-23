from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        orig = image[sr][sc]
        if orig == color:
            return image

        R, C = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color  # mark visited by recoloring

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image