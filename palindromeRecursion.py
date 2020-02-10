from my_linked_list import LinkedList
EVENLENGTH = 500
ODDLENGTH = 499

def generatePalindrome(typeStr = ""):
    if typeStr == "odd":
        palindromeOdd = LinkedList()
        for i in range(ODDLENGTH):
            if i % 2 == 0:
                palindromeOdd.pushFront(0)
            else:
                palindromeOdd.pushFront(1)
        return palindromeOdd
    else:
        palindromeEven = LinkedList()
        for i in range(EVENLENGTH):
            if i < EVENLENGTH / 2:
                if i == 0:
                    palindromeEven.pushFront(1)
                elif i % 2 == 0:
                    palindromeEven.pushFront(1)
                else:
                    palindromeEven.pushFront(0)
            else:
                if i % 2 == 1:
                    palindromeEven.pushFront(1)
                else:
                    palindromeEven.pushFront(0)
        return palindromeEven

def palindrome(head, firstNode = None, counter = 1, halfwayPoint = 0):
    if counter == 1:
        firstNode = head
    if head.getNextNode() == None:
        halfwayPoint = counter // 2
        if firstNode.data == head.data:
            same = True
            firstNode = firstNode.getNextNode()
            return halfwayPoint, same, firstNode
        return halfwayPoint, False, firstNode

    else:
        halfwayPoint, same, firstNode = palindrome(head.getNextNode(), firstNode, counter+1)
        
        if halfwayPoint >= counter:
            if counter == 1:
                return same
            else:
                return halfwayPoint, same, firstNode

        if same:
            if firstNode.data == head.data:
                firstNode = firstNode.getNextNode()
                return halfwayPoint, same, firstNode
            else:
                return halfwayPoint, False, firstNode
        else:
            return halfwayPoint, False, firstNode
        
        
        
    


def main():

    evenPalindrome = generatePalindrome("even") # Generate even length Palindrome
    oddPalindrome = generatePalindrome("odd") # Generate odd length Palindrome

    evenNotPalindrome = LinkedList()
    oddNotPalindrome = LinkedList()
    for i in range(EVENLENGTH):
        evenNotPalindrome.pushFront(i)

    for i in range(ODDLENGTH):
        oddNotPalindrome.pushFront(i)


    #print(evenPalindrome)
    print(palindrome(evenPalindrome.getNode()))
    
    #print(oddPalindrome)    
    print(palindrome(oddPalindrome.getNode()))

    #print(evenNotPalindrome)    
    print(palindrome(evenNotPalindrome.getNode()))

    #print(oddNotPalindrome)    
    print(palindrome(oddNotPalindrome.getNode()))


main()