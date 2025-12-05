# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists==None or len(lists)==0:
            return None

        def mergeTwo(list_1,list_2):
            newNode=ListNode()
            temp=newNode

            while list_1 and list_2:
                if list_1.val<list_2.val:
                    temp.next=list_1
                    list_1=list_1.next
                else:
                    temp.next=list_2
                    list_2=list_2.next
                temp=temp.next
            while list_1:
                temp.next=list_1
                list_1=list_1.next
                temp=temp.next
            while list_2:
                temp.next=list_2
                list_2=list_2.next
                temp=temp.next
            return newNode.next

        while len(lists)>1:
            tempList=[]
            for i in range(0,len(lists),2):
                list_1=lists[i]
                if i+1<len(lists):
                    list_2=lists[i+1]
                else:
                    list_2=None
                
                tempList.append(mergeTwo(list_1,list_2))
            lists=tempList

        return lists[0]
        