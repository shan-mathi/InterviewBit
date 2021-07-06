    def level_order(self):
        if self is None:
            return []
        queue = [root]
        next_queue=[]
        level=[]
        result = []
        while not queue:
            for root in queue:
                level.append(root.data)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            result.append(level)
            level=[]
            queue=next_queue[:]
            next_queue=[]
        return result
