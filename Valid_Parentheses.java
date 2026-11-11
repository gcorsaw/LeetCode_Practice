class Solution {
    public boolean isValid(String s) {
        //The data structure for this particular problem would be the char[] (array data structure)
        char[] stack = new char[s.length()];
        int top = 0;

        for(char c : s.toCharArray()){
            if (c == '('){
                stack[top++] = ')';
            }else if (c == '{'){
                stack[top++] = '}';
            }else if(c == '['){
                stack[top++] = ']';
            }else if (top == 0 || stack[--top] != c){
                return false;
            }
        }
        return top == 0;
    }
}