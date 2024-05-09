class Solution {
    func maximumHappinessSum(_ happiness: [Int], _ k: Int) -> Int {
        let happyChildren = happiness.sorted(by: >)
        var happyChildrenSum = 0
        for i in 0..<k {
            happyChildrenSum += max(0, happyChildren[i] - i)
        }
        return happyChildrenSum
    }
}