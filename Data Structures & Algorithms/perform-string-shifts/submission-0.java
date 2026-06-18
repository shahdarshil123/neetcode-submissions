class Solution {
    public String stringShift(String s, int[][] shift) {
        int move = 0;
        for(int i=0; i < shift.length;i++){
            if(shift[i][0] == 1){
                move += shift[i][1];
            }
            else{
                move -= shift[i][1];
            }
        }
        String result;
        if(move < 0){
            move = -1*move;
            move = move % s.length();
            result = s.substring(move) + s.substring(0, move);
        }
        else{
            move = move % s.length();
            result = s.substring(s.length()-move) + s.substring(0, s.length()-move);
        }

        return result;
    }
}
