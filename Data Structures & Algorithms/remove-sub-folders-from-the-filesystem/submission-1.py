class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # check for each folder path and create a nodes in the path
        trie = Trie()
        result = []
        for f in folder:
            node = trie.root
            arr = f[1:].split('/')
            for sub_folder in arr:
                if sub_folder in node.children:
                    node = node.children[sub_folder]
                else:
                    node.children[sub_folder] = TrieNode(sub_folder)
                    node = node.children[sub_folder]
            node.isFolder = True
        
        for f in folder:
            node = trie.root
            is_folder = True
            arr = f[1:].split('/')
            for i in range(len(arr)):
                sub_folder = arr[i]
                if is_folder == False:
                    break
                node = node.children[sub_folder]
                if node.isFolder and i != len(arr)-1:
                    is_folder = False
            if is_folder:
                result.append(f)

        return result
                

class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.isFolder = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")


