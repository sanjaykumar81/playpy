# public class PerfectSubTree {
#
#     public static void main(String [] args){
#
#     }
# }
#
#
# class Solution {
#     private static int maxHeight = 0;
#     public int solution(Tree T) {
#         int height = findHeight(T);
#         if (maxHeight < height){
#             maxHeight = height;
#         }
#         return (int) (Math.pow(2, maxHeight +1)-1);
#     }
#
#     public int findHeight(Tree T){
#         int tHeight = 0;
#         if (T.l == null || T.r == null){
#             return tHeight;
#         }
#         int ltHeight = findHeight(T.l);
#         int rtHeight = findHeight(T.r);
#         if (ltHeight == rtHeight){
#             tHeight = ltHeight +1;
#         }else if (ltHeight < rtHeight){
#             tHeight = ltHeight+1;
#         }else{
#             tHeight = rtHeight+1;
#         }
#         if (maxHeight < tHeight){
#             maxHeight = tHeight;
#         }
#         return tHeight;
#     }
# }


class Tree:
    def __init__(self, data):
        self.x = data
        self.lelf
        self.right


if __name__ == "__main__":
    T = Tree(2)

    pass
