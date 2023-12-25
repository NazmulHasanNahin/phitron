/****************************************************************

    Following is the class structure of the Node class:

        class Node
        {
        public:
            int data;
            Node *next;
            Node()
            {
                this->data = 0;
                next = NULL;
            }
            Node(int data)
            {
                this->data = data;
                this->next = NULL;
            }
            Node(int data, Node* next)
            {
                this->data = data;
                this->next = next;
            }
        };


*****************************************************************/

class Stack
{
public:
    Node *head = NULL;
    int sz;
    Stack()
    {
        int sz=0;
        head=NULL;
    }

    int getSize()
    {
        return sz;
    }

    bool isEmpty()
    {
        return sz==0;
    }

    void push(int data)
    {
        Node* newNode=new Node(data);
        newNode->next=head;
        head=newNode;
        sz++;
    }

    void pop()
    {
        //Write your code here
        
        if(head==NULL)
        {
            return;
        }
        Node* dltNode=head;
        head = head->next;
        delete dltNode;
        sz--;
    }

    int getTop()
    {
        //return head->data;
        if(head==NULL)
        {
            return -1;
        }
        return head->data;
    }
};