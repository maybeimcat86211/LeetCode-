class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #回傳的值要是一個ListNode
        dummy = ListNode()
        #指標指向要插入的數值或是節點
        cur = dummy
        #儲存可能會溢出的數值
        carry = 0
        #如果l1跟l2不為空值,以及溢出的值不為null
        while l1 or l2 or carry:
            #v1的值為l1的每一個值
            v1 = l1.val if l1 else 0
            #同上
            v2 = l2.val if l2 else 0
            #計算新數字
            val = v1+v2+carry
            #溢出的值等於 相加的值除10
            carry = val//10
            #如果相加結果大於10,只取單位數
            #例如11 mod 10 = 1 
            #所以新的值會為1
            val = val % 10
            #數值寫入節點
            cur.next = ListNode(val)
            #更新指標
            cur = cur.next
            #更新l1 跟l2的指標,如果不為null
            #舉例,第一輪是 l1[0]跟l2[0]相加
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        #別忘記edge cases
        return dummy.next