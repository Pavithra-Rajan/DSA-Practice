struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode l3;
    l3.next=NULL;
    l3.val=0;
    struct ListNode *curr=&l3;
    int rem=0,sum;
    while(l1!=NULL|| l2!=NULL || rem!=0)
    {
        sum=rem+(l1!=0?l1->val:0)+(l2!=0?l2->val:0);
        rem=sum/10;
        sum%=10;
        curr->next=malloc(sizeof(struct ListNode));
        curr->next->next=NULL;
        curr->next->val=sum;
        curr=curr->next;
        l1=(l1!=NULL?l1->next:NULL);
        l2=(l2!=NULL?l2->next:NULL);
    }
    return l3.next;

}