def checkBST(root):
    min = -1
    max = 10001
    return checknode(root,max,min)

def checknode(self,max,min):
    if not self:
        return True
    if self.data <= min or self.data >= max:
        return False
    else:
        return checknode(self.left, self.data, min) and checknode(self.right,max,self.data)
