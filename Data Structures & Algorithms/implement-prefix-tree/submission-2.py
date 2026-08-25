class Node:
    def __init__(self, val):
        self.next = [None for _ in range(26)]
        self.val = val
        self.end = False  # default no word ends here

class PrefixTree:
    def __init__(self):
        self.head = Node("")

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return 
        
        curr = self.head
        for i in range(len(word)):
            pos = ord(word[i].lower()) - ord('a')
            if curr.next[pos] is None:
                curr.next[pos] = Node(word[i].lower())
            curr = curr.next[pos]

        # Mark the end of the word
        curr.end = True

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True

        curr = self.head
        for i in range(len(word)):
            pos = ord(word[i].lower()) - ord('a')
            if curr.next[pos] is None:
                return False
            curr = curr.next[pos]

        return curr.end  # True if word ends here

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        curr = self.head
        for i in range(len(prefix)):
            pos = ord(prefix[i].lower()) - ord('a')
            if curr.next[pos] is None:
                return False
            curr = curr.next[pos]

        return True
