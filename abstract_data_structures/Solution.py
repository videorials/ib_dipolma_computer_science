from linked_list import *

class Solution(object):

    def add_two_numbers(self, l1, l2):

        l1_cur, l2_cur = l1.head, l2.head
        l3 = LinkedList()
        
        carry = 0
        while l1_cur or l2_cur or carry:
            l1_data = l1_cur.data if l1_cur else 0
            l2_data = l2_cur.data if l2_cur else 0

            tmp_tot = l1_data + l2_data + carry
            l3.add_last(tmp_tot % 10)
            carry = tmp_tot // 10

            if l1_cur: l1_cur = l1_cur.next 
            if l2_cur: l2_cur = l2_cur.next

        return(l3)