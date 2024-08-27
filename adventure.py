######
# TREENODE CLASS
######
class TreeNode:

  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    
      self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while story_node.choices:
      choice = int(input("Enter 1 or 2 to continue the story: ").strip())
      if choice != 1 and choice != 2:
        print("Enter a valid choice...1 or 2...")
      elif choice == 1 or choice == 2:
        chosen_idx = choice - 1
        chosen_child = story_node.choices[chosen_idx]
        print(chosen_child.story_piece)

        story_node = chosen_child
      


######
# VARIABLES FOR TREE
######

# creating tree nodes
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")
choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
# adding children to root
story_root.add_child(choice_a)
story_root.add_child(choice_b)

# adding children nodes to choice a
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

#adding children to choice b
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

# User initial input and greeting
try:
    user_name = input("What is your name? ").strip()
except EOFError:
    print("No input provided.")
else:
    if user_name:
        print(f"Nice to meet you, {user_name}!")
    else:
        print("Hello, mysterious traveler!")

######
# TESTING AREA
######
print("Once upon a time...")
story_root.traverse()
