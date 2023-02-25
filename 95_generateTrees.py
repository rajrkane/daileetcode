class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateSubTrees(start: int, end: int):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end+1):
                leftTrees = generateSubTrees(start, i-1)
                rightTrees = generateSubTrees(i+1, end)
                for left in leftTrees:
                    for right in rightTrees:
                        curTree = TreeNode(i)
                        curTree.left = left 
                        curTree.right = right 
                        trees.append(curTree)
            return trees 

        return generateSubTrees(1, n)
