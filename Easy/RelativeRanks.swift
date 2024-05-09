class Solution {
    func findRelativeRanks(_ score: [Int]) -> [String] {
        let sortedScores = score.sorted(by: >)
        var ranks = [Int: String]()

        for (index, rank) in sortedScores.enumerated() {
            switch index{
                case 0:
                    ranks[rank] = "Gold Medal"
                case 1:
                    ranks[rank] = "Silver Medal"
                case 2:
                    ranks[rank] = "Bronze Medal"
                default:
                ranks[rank] = String(index + 1)
            }
        }
        return score.map {ranks[$0, default: ""]}
    }
}