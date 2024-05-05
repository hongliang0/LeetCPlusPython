class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var maxProfit = 0
        var leftIndex = 0

        for i in 1..<prices.count {
            if prices[i] < prices[leftIndex] {
                leftIndex = i
            }
            let currentProfit = prices[i] - prices[leftIndex]
            if currentProfit > maxProfit {
                maxProfit = currentProfit
            }
        }
        return maxProfit
    }
}m