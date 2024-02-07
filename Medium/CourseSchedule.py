class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Number of times a node has been visited
        visited = [0] * numCourses

        # Use dfs to find cycles in directed graph. 0 means unseen,
        # 1 means seen, 2 means completed and ok
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True

            # Otherwise, mark as visited
            visited[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 2
            return True

        # Check each course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
