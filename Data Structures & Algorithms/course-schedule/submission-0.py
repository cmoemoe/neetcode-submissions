#array with dependencies, top sort
#only has 1 prereq

#dfs answers: can i reach numCourses as I go down prereqs
#fail condition if branch we are searching repeats a course num/ graph has cycle
#directed graph

#There are a total of numCourses courses you are required to take
#labeled from 0 to numCourses - 1
#does this mean if numCourses = 3, we must take classes 0, 1, and 2? yes

#hash map to maintain freqs
#if hash map freq > 1: exit dfs and reset map

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i:[] for i in range(numCourses) }

        for course, pre in prerequisites:
            adj[pre].append(course)

        visited = set()

        def dfs(neighbor): 
            if neighbor in visited:
                return False
            if adj[neighbor] == []:
                return True #what's this

            visited.add(neighbor)
            for prereq in adj[neighbor]:
                if not dfs(prereq):
                    return False
            visited.remove(neighbor)
            adj[neighbor] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False #do we ever reach numCourses w/o hitting cycle

        return True

        


            
            