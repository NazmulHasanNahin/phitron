#include <bits/stdc++.h> 
string kevinStackProblem(string &s)
{
	// Write your code here.
	stack<char>st;
	for(char c:s)
	{
		st.push(c);
	}
	s.clear();
	while(!st.empty())
	{
		s.push_back(st.top());
		st.pop();
	}
	return s;
}
// https://www.codingninjas.com/studio/problems/kevin-s-stack-problem_1169465?leftPanelTabValue=PROBLEM