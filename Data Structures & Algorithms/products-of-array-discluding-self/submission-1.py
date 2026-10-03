class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1st pass left to right cum product
        product = 1
        lr_cum_product = [1]
        for i in range(len(nums)):
            product *= nums[i]
            lr_cum_product.append(product)
        # 2nd pass right to let cum product
        product = 1
        rl_cum_product = [1 for i in range(len(nums) + 1)]
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            rl_cum_product[i] = product
        # 3rd pass left * right at each element
        output = []
        for i in range(len(nums)):
            output.append(lr_cum_product[i]*rl_cum_product[i+1])
        
        return output

        