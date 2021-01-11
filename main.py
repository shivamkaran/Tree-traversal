class BinaryTreeNode:
  def __init__(self, data):
    self.data = data   #root
    self.left =  None  #left child
    self.right = None  #right child

# Traverse Preorder
  def PreOrder(self):
    print(self.data, end=' ')
    if self.left:
       self.left.PreOrder()
    if self.right:
      self.right.PreOrder()
  
# Traverse Inorder
  def inOrder(self):
    if self.left:
      self.left.inOrder()
    print(self.data, end=' ')
    if self.right:
      self.right.inOrder()


#Traverse Postorder
  def postOrder(self):
    if self.left:
      self.left.postOrder()
    if self.right:
      self.right.postOrder()
    print(self.data, end=' ')


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.righ = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)


print("Pre order Traversal: ", end="")
root.PreOrder()
print("\nIn order Traversal: ", end="")
root.inOrder()
print("\nPost order Traversal: ", end="")
root.postOrder()

       
